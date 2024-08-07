"""Added about, publisher, age_rating, developer and tags columns to Game model, also changed image_url to ARRAY type. Lastly added date_added to reviews model

Revision ID: 8aaf2fea4fff
Revises: 96cc751bedbb
Create Date: 2024-08-01 23:24:14.120302

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8aaf2fea4fff"
down_revision = "96cc751bedbb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.add_column(sa.Column("about", sa.String(length=1000), nullable=False))
        batch_op.add_column(
            sa.Column("publisher", sa.String(length=250), nullable=False)
        )
        batch_op.add_column(sa.Column("age_rating", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("developer", sa.String(), nullable=False))
        batch_op.add_column(
            sa.Column("tags", postgresql.ARRAY(sa.String()), nullable=True)
        )

    with op.batch_alter_table("reviews", schema=None) as batch_op:
        batch_op.add_column(sa.Column("date_added", sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("reviews", schema=None) as batch_op:
        batch_op.drop_column("date_added")

    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.drop_column("tags")
        batch_op.drop_column("developer")
        batch_op.drop_column("age_rating")
        batch_op.drop_column("publisher")
        batch_op.drop_column("about")

    # ### end Alembic commands ###
