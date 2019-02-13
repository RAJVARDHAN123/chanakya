'use strict';
const Joi = require('joi');
const Boom = require('boom');
const EnrolmentKey = require('../models/enrolmentKey');
const CONSTANTS = require('../constants');
const Student = require('../models/student');
const _ = require("underscore");

const internals = {}

// helper methods
internals.validateEnrolmentKey = async function(assessmentService, key) {
    let enrolmentKey = await assessmentService.validateEnrolmentKey(key);
    if (!enrolmentKey) {
        throw Boom.badRequest("The Enrolment Key specified is wrong. Please check and try again.");
    }
    return enrolmentKey;
}
internals.ensureEnrolmentKeyStatus = function(assessmentService, key) {
    let keyStatus = assessmentService.getEnrolmentKeyStatus(key);
    if (keyStatus == 'testAnswered') {
        throw Boom.conflict("This enrolment key has already been used to answer a test.");
    }
    return keyStatus;
}

module.exports = [
    {
        method: 'GET',
        path: '/on_assessment/validate_enrolment_key/{enrolmentKey}',
        options: {
            description: "Validates the given enrolment key.",
            tags: ['api'],
            validate: {
                params: {
                    enrolmentKey: EnrolmentKey.field("key")
                }
            },
            handler: async (request, h) => {
                const { assessmentService } = request.services();

                let enrolmentKey = await assessmentService.validateEnrolmentKey(request.params.enrolmentKey);
                let keyStatus = assessmentService.getEnrolmentKeyStatus(enrolmentKey);
                if (enrolmentKey) {
                    return { valid: true, keyStatus: keyStatus }
                } else {
                    return { valid: false, keyStatus: keyStatus }
                }
            }
        }
    },
    {
        method: 'POST',
        path: '/on_assessment/details/{enrolmentKey}',
        options: {
            description: "Save the details of student answering the test. Can be used in stages according to frontend.",
            tags: ['api'],
            validate: {
                params: {
                    enrolmentKey: EnrolmentKey.field("key")
                },
                payload: {
                    name: Student.field("name"),
                    gender: Joi.string().valid( ..._.keys(CONSTANTS.studentDetails.gender) ),
                    dob: Student.field("dob"),
                    whatsapp: Student.field("whatsapp"),
                    email: Student.field("email"),
                    state: Student.field("state"),
                    city: Student.field("city"),
                    gps: Student.field("gps"),
                    qualification: Joi.string().valid( ..._.keys(CONSTANTS.studentDetails.qualification) ),
                    currentStatus: Joi.string().valid( ..._.keys(CONSTANTS.studentDetails.currentStatus) ),
                    caste: Joi.string().valid( ..._.keys(CONSTANTS.studentDetails.caste) ),
                    religon: Joi.string().valid( ..._.keys(CONSTANTS.studentDetails.religon) )
                }
            },
            handler: async (request, h) => {
                const { assessmentService } = request.services();

                let enrolmentKey = await internals.validateEnrolmentKey(assessmentService, request.params.enrolmentKey);
                internals.ensureEnrolmentKeyStatus(assessmentService, enrolmentKey);

                // some fields are ints on model but string on API for more usability
                // do the required massaging as per the model using mappings in constants
                let payload = request.payload;
                let specialFields = ['gender', 'qualification', 'currentStatus', 'caste', 'religon'];
                _.each(specialFields, (field) => {
                    if (payload[field]) {
                        payload[field] = CONSTANTS.studentDetails[field][ payload[field] ]
                    }
                });

                // patch the student row
                await assessmentService.pathStudentDetails(enrolmentKey, payload);

                return {'sucess': true}
            }
        }
    },
    {
        method: 'POST',
        path: '/on_assessment/questions/{enrolmentKey}',
        options: {
            description: "Get the questions associated with the given enrolment key. Starts the timer of the alloted time for the test.",
            tags: ['api'],
            validate: {
                params: {
                    enrolmentKey: EnrolmentKey.field("key")
                }
            },
            handler: async (request, h) => {
                const { assessmentService } = request.services();

                let enrolmentKey = await internals.validateEnrolmentKey(assessmentService, request.params.enrolmentKey);
                internals.ensureEnrolmentKeyStatus(assessmentService, enrolmentKey);

                let questions = await assessmentService.getQuestionSetForEnrolmentKey(enrolmentKey);
                return {
                    'data': questions,
                    'availableTime': CONSTANTS.questions.timeAllowed
                }
            }
        }
    },
    {
        method: 'POST',
        path: '/on_assessment/questions/{enrolmentKey}/answers',
        options: {
            description: "Saves the answers given by the student. Saves the end time of the test.",
            tags: ['api'],
            validate: {
                params: {
                    enrolmentKey: EnrolmentKey.field("key")
                },
                payload: {
                    answers: Joi.any().default({
                        '398': 504,
                        '400': 524,
                        '401': 512,
                        '405': 532,
                        '409': '-21'
                    })
                }
            },
            handler: async (request, h) => {
                const { assessmentService } = request.services();

                let enrolmentKey = await internals.validateEnrolmentKey(assessmentService, request.params.enrolmentKey);
                internals.ensureEnrolmentKeyStatus(assessmentService, enrolmentKey);

                await assessmentService.recordStudentAnswers(enrolmentKey, request.payload.answers);
                return { success: true };
            }
        }
    }
];
