"""create table product

Revision ID: f655f2081a32
Revises: bcb7ca4a9b2d
Create Date: 2024-01-22 10:28:54.110766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f655f2081a32'
down_revision = 'bcb7ca4a9b2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('set', sa.String(length=20), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
