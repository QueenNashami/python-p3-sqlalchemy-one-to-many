"""create db

Revision ID: faebd12f9523
Revises: 
Create Date: 2023-07-21 12:50:33.994080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faebd12f9523'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create games table
    op.create_table(
        'games',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('genre', sa.String(), nullable=False),
        sa.Column('platform', sa.String(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
    )

    # Create reviews table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.Column('comment', sa.String(), nullable=False),
        sa.Column('game_id', sa.Integer(), sa.ForeignKey('games.id')),
    )


def downgrade():
    op.drop_table('reviews')
    op.drop_table('games')
