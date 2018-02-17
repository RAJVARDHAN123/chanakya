"""empty message

Revision ID: 8a8974528c5f
Revises: 34aa1e0aac8a
Create Date: 2018-02-17 14:25:38.127050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a8974528c5f'
down_revision = '34aa1e0aac8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('college_type', sa.Enum('Normal', 'Distant', name='collegetype'), nullable=False))
    op.add_column('student', sa.Column('college_which', sa.String(length=256), nullable=False))
    op.add_column('student', sa.Column('father_prof', sa.String(length=64), nullable=False))
    op.add_column('student', sa.Column('is_10_pass', sa.Enum('yes', 'no', name='boolean'), nullable=False))
    op.add_column('student', sa.Column('is_12_pass', sa.Enum('yes', 'no', name='boolean'), nullable=False))
    op.add_column('student', sa.Column('is_college_enrolled', sa.Enum('yes', 'no', name='boolean'), nullable=False))
    op.add_column('student', sa.Column('is_works', sa.Enum('yes', 'no', name='boolean'), nullable=False))
    op.add_column('student', sa.Column('last_class_passed', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('monthly_fam_income', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('mother_prof', sa.String(length=64), nullable=False))
    op.add_column('student', sa.Column('num_earning_fam_members', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('num_fam_members', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('owns_computer', sa.Enum('yes', 'no', name='boolean'), nullable=False))
    op.add_column('student', sa.Column('percentage_10', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('percentage_12', sa.Integer(), nullable=False))
    op.add_column('student', sa.Column('stream_11_12', sa.Enum('medical', 'non_medical', 'commerce_maths', 'commerce_no_maths', name='stream_11_12'), nullable=False))
    op.add_column('student', sa.Column('works_where', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'works_where')
    op.drop_column('student', 'stream_11_12')
    op.drop_column('student', 'percentage_12')
    op.drop_column('student', 'percentage_10')
    op.drop_column('student', 'owns_computer')
    op.drop_column('student', 'num_fam_members')
    op.drop_column('student', 'num_earning_fam_members')
    op.drop_column('student', 'mother_prof')
    op.drop_column('student', 'monthly_fam_income')
    op.drop_column('student', 'last_class_passed')
    op.drop_column('student', 'is_works')
    op.drop_column('student', 'is_college_enrolled')
    op.drop_column('student', 'is_12_pass')
    op.drop_column('student', 'is_10_pass')
    op.drop_column('student', 'father_prof')
    op.drop_column('student', 'college_which')
    op.drop_column('student', 'college_type')
    # ### end Alembic commands ###
