"""Modified max characters for about game attribute-modified to 10000 characters

Revision ID: c6ab90766372
Revises: c14d670d3f3b
Create Date: 2024-08-12 15:59:03.369029

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c6ab90766372"
down_revision = "c14d670d3f3b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "about",
            existing_type=sa.VARCHAR(length=1000),
            type_=sa.String(length=10000),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "about",
            existing_type=sa.String(length=10000),
            type_=sa.VARCHAR(length=1000),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
