"""agency1

Revision ID: 94418658de66
Revises: aa2c782bab23
Create Date: 2023-08-21 09:34:40.495659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94418658de66'
down_revision = 'aa2c782bab23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('branch', sa.String(length=255), nullable=True),
    sa.Column('address_1', sa.String(length=255), nullable=True),
    sa.Column('address_2', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('district', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('pin', sa.String(length=255), nullable=True),
    sa.Column('gstin', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name', 'branch', name='uq_name_branch')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency')
    # ### end Alembic commands ###
