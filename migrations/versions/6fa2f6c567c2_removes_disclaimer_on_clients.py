"""removes disclaimer on clients

Revision ID: 6fa2f6c567c2
Revises: a7882a87de99
Create Date: 2022-03-03 22:15:19.343936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fa2f6c567c2'
down_revision = 'a7882a87de99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'disclaimer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('disclaimer', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
