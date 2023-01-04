"""Add CommonMixin

Revision ID: 7ab4d082ce9b
Revises: 60b43c4a8bed
Create Date: 2023-01-04 17:42:51.611260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab4d082ce9b'
down_revision = '60b43c4a8bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('referers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('referer_value', sa.String(length=4096), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('redirect', sa.String(), nullable=False),
    sa.Column('expiration_date', sa.DateTime(), nullable=True),
    sa.Column('stats_is_public', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_agents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_agent_value', sa.String(length=4096), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('url_views',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=15), nullable=False),
    sa.Column('user_agent_id', sa.Integer(), nullable=False),
    sa.Column('referer_id', sa.Integer(), nullable=True),
    sa.Column('view_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['referer_id'], ['referers.id'], ),
    sa.ForeignKeyConstraint(['url_id'], ['urls.id'], ),
    sa.ForeignKeyConstraint(['user_agent_id'], ['user_agents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_views')
    op.drop_table('user_agents')
    op.drop_table('urls')
    op.drop_table('referers')
    # ### end Alembic commands ###
