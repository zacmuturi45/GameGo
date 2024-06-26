"""Initial migration

Revision ID: d33ee121f2ad
Revises: 
Create Date: 2024-06-19 20:21:45.942728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd33ee121f2ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('platform', sa.String(length=255), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('video_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('purchased_games',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_purchased_games_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_purchased_games_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'game_id')
    )
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payment_method', sa.String(length=255), nullable=True),
    sa.Column('transaction_date', sa.DateTime(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_purchases_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_purchases_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1000), nullable=False),
    sa.Column('game_rating', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_reviews_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlist_games',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_wishlist_games_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_wishlist_games_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'game_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlist_games')
    op.drop_table('reviews')
    op.drop_table('purchases')
    op.drop_table('purchased_games')
    op.drop_table('users')
    op.drop_table('games')
    # ### end Alembic commands ###
