"""users-migrations

Revision ID: 89da88360cf5
Revises: 533af0b0e974
Create Date: 2022-04-25 14:06:17.375422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "89da88360cf5"
down_revision = "533af0b0e974"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("email", sa.String(length=255), unique=True),
        sa.Column("password", sa.String(length=255)),
        sa.Column("image", sa.String(length=255), default="default.jpg"),
        sa.Column("created_at", sa.DateTime(timezone=True), default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
    )


def downgrade():
    op.create_table("user")
