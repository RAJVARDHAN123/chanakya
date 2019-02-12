"""empty message

Revision ID: 0434493ef3bb
Revises: 
Create Date: 2018-07-13 07:41:34.604152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0434493ef3bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enrolment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enrolment_key', sa.String(length=5), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('crm_potential_id', sa.String(length=20), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_enrolment_enrolment_key'), 'enrolment', ['enrolment_key'], unique=True)
    op.create_index(op.f('ix_enrolment_phone_number'), 'enrolment', ['phone_number'], unique=False)
    op.create_table('options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('option_1', sa.String(length=128), nullable=True),
    sa.Column('option_2', sa.String(length=128), nullable=True),
    sa.Column('option_3', sa.String(length=128), nullable=True),
    sa.Column('option_4', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('en_question_text', sa.String(length=1024), nullable=False),
    sa.Column('hi_question_text', sa.String(length=1024), nullable=False),
    sa.Column('difficulty', sa.Enum('easy', 'medium', 'hard', name='difficulty'), nullable=False),
    sa.Column('category', sa.String(length=32), nullable=False),
    sa.Column('question_type', sa.Enum('MCQ', 'short_answer', 'view', name='questiontype'), nullable=False),
    sa.Column('options_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['options_id'], ['options.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('started_on', sa.DateTime(), nullable=False),
    sa.Column('submitted_on', sa.DateTime(), nullable=False),
    sa.Column('received_marks', sa.Integer(), nullable=False),
    sa.Column('max_possible_marks', sa.Integer(), nullable=False),
    sa.Column('set_name', sa.String(length=32), nullable=False),
    sa.Column('enrolment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enrolment_id'], ['enrolment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.Enum('male', 'female', 'others', name='gender'), nullable=False),
    sa.Column('mobile', sa.String(length=10), nullable=True),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('school_medium', sa.Enum('english', 'vernacular', name='schoolinstructionmedium'), nullable=True),
    sa.Column('qualification', sa.Enum('no_reading_writing', 'reading_writing', 'class_5_pass', 'class_8_pass', 'class_10_pass', 'class_12_pass', 'graduate', 'post_graduation', 'prof_degree', name='qualification'), nullable=True),
    sa.Column('class_10_marks', sa.String(length=10), nullable=True),
    sa.Column('class_12_marks', sa.String(length=10), nullable=True),
    sa.Column('class_12_stream', sa.Enum('pcm', 'pcb', 'pcmb', 'commerce_with_maths', 'commerce_without_maths', 'arts', 'others', name='class12stream'), nullable=True),
    sa.Column('pin_code', sa.String(length=6), nullable=True),
    sa.Column('state', sa.Enum('Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'National Capital Territory of Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'), nullable=True),
    sa.Column('district', sa.String(length=100), nullable=True),
    sa.Column('tehsil', sa.String(length=100), nullable=True),
    sa.Column('city_or_village', sa.String(length=100), nullable=True),
    sa.Column('caste_parent_category', sa.Enum('sc', 'st', 'obc', 'general', 'other', name='caste'), nullable=True),
    sa.Column('caste', sa.String(length=100), nullable=True),
    sa.Column('urban_rural', sa.Enum('urban', 'rural', name='urbanorrural'), nullable=True),
    sa.Column('family_head', sa.Enum('father', 'mother', 'other', name='familyhead'), nullable=True),
    sa.Column('family_head_other', sa.String(length=100), nullable=True),
    sa.Column('family_head_qualification', sa.Enum('no_reading_writing', 'reading_writing', 'class_5_pass', 'class_8_pass', 'class_10_pass', 'class_12_pass', 'graduate', 'post_graduation', 'prof_degree', name='qualification'), nullable=True),
    sa.Column('fam_members', sa.Integer(), nullable=True),
    sa.Column('earning_fam_members', sa.Integer(), nullable=True),
    sa.Column('monthly_family_income', sa.Integer(), nullable=True),
    sa.Column('urban_family_head_prof', sa.Enum('unemployed', 'no_training_jobs', 'jobs_with_training', 'high_training', 'read_write_jobs', 'routine_work', 'prof_degree_work', name='urbanprofessions'), nullable=True),
    sa.Column('family_head_income', sa.Integer(), nullable=True),
    sa.Column('rural_family_head_prof', sa.Enum('unemployed', 'labourer', 'caste_related_work', 'business', 'independent_work', 'work_on_own_land', 'service', name='ruralprofessions'), nullable=True),
    sa.Column('family_head_org_membership', sa.Enum('nothing', 'member_1_org', 'member_1plus_org', 'office_holder', 'pub_leader', name='ruralorgmembership'), nullable=True),
    sa.Column('family_type', sa.Enum('single', 'joint', name='familytype'), nullable=True),
    sa.Column('family_land_holding', sa.Integer(), nullable=True),
    sa.Column('family_draught_animals', sa.Integer(), nullable=True),
    sa.Column('housing_type', sa.Enum('hut', 'kacha_house', 'pucca_house', 'kothi', name='housingtype'), nullable=True),
    sa.Column('owned_items', sa.String(length=1000), nullable=True),
    sa.Column('user_agent', sa.String(length=150), nullable=True),
    sa.Column('network_speed', sa.Float(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('enrolment_id', sa.Integer(), nullable=True),
    sa.Column('test_data_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enrolment_id'], ['enrolment.id'], ),
    sa.ForeignKeyConstraint(['test_data_id'], ['test_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('test_data')
    op.drop_table('question')
    op.drop_table('options')
    op.drop_index(op.f('ix_enrolment_phone_number'), table_name='enrolment')
    op.drop_index(op.f('ix_enrolment_enrolment_key'), table_name='enrolment')
    op.drop_table('enrolment')
    # ### end Alembic commands ###
