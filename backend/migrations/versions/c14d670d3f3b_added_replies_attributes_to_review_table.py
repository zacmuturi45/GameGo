"""Added replies attributes to Review table

Revision ID: c14d670d3f3b
Revises: b276a4361099
Create Date: 2024-08-06 22:30:22.105828

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c14d670d3f3b"
down_revision = "b276a4361099"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("reviews", schema=None) as batch_op:
        batch_op.add_column(sa.Column("parent_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f("fk_reviews_parent_id_reviews"), "reviews", ["parent_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("reviews", schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f("fk_reviews_parent_id_reviews"), type_="foreignkey"
        )
        batch_op.drop_column("parent_id")

    # ### end Alembic commands ###