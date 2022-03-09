"""models without image columns

Revision ID: d999e7fa4ed9
Revises: 
Create Date: 2022-03-02 19:18:16.787207

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd999e7fa4ed9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('general_information', sa.Text(), nullable=True),
    sa.Column('disclaimer', sa.Boolean(), nullable=True),
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password_hash'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('events',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('finished', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('validity', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tattooists',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('general_information', sa.Text(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password_hash')
    )
    op.create_table('tattoos',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('colors', sa.Boolean(), nullable=True),
    sa.Column('body_parts', sa.Text(), nullable=True),
    sa.Column('id_client', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_tattooist', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_event', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['id_event'], ['events.id'], ),
    sa.ForeignKeyConstraint(['id_tattooist'], ['tattooists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('id_tattoo', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_tattoo'], ['tattoos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materials',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('id_order', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_product', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_order'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materials')
    op.drop_table('orders')
    op.drop_table('tattoos')
    op.drop_table('tattooists')
    op.drop_table('products')
    op.drop_table('events')
    op.drop_table('clients')
    # ### end Alembic commands ###