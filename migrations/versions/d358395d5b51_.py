"""empty message

Revision ID: d358395d5b51
Revises: e625a84b325b
Create Date: 2022-03-10 14:37:55.239492

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd358395d5b51'
down_revision = 'e625a84b325b'
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
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('image_name', sa.String(), nullable=True),
    sa.Column('image_bin', sa.LargeBinary(), nullable=True),
    sa.Column('image_mimetype', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('sessions',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('finished', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('storage',
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
    sa.Column('image_name', sa.String(), nullable=True),
    sa.Column('image_bin', sa.LargeBinary(), nullable=True),
    sa.Column('image_mimetype', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('token_blocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tattoos',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('colors', sa.Boolean(), nullable=False),
    sa.Column('body_parts', sa.Text(), nullable=True),
    sa.Column('id_client', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_tattooist', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_session', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['id_session'], ['sessions.id'], ),
    sa.ForeignKeyConstraint(['id_tattooist'], ['tattooists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materials',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('id_item', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_tattoo', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_item'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['id_tattoo'], ['tattoos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tattoo_images',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('image_bin', sa.LargeBinary(), nullable=False),
    sa.Column('image_name', sa.String(), nullable=False),
    sa.Column('image_mimetype', sa.String(), nullable=False),
    sa.Column('id_tattoo', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_tattoo'], ['tattoos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tattoo_images')
    op.drop_table('materials')
    op.drop_table('tattoos')
    op.drop_table('token_blocklist')
    op.drop_table('tattooists')
    op.drop_table('storage')
    op.drop_table('sessions')
    op.drop_table('clients')
    # ### end Alembic commands ###
