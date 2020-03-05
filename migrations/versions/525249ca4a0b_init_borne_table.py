"""Init borne table

Revision ID: 525249ca4a0b
Revises: 
Create Date: 2020-03-04 12:42:13.842102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '525249ca4a0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borne',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cycle_datetime', sa.DateTime(), nullable=False),
    sa.Column('cycle_time', sa.Integer(), nullable=False),
    sa.Column('cycle_dist', sa.Float(), nullable=False),
    sa.Column('cycle_type', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borne')
    # ### end Alembic commands ###