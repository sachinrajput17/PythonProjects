"""empty message

Revision ID: da70944e7305
Revises: 66f9bb6abef7
Create Date: 2020-07-17 16:42:49.396099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da70944e7305'
down_revision = '66f9bb6abef7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('role', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('role', 'password')
    # ### end Alembic commands ###
