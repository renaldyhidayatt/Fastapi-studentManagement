"""course-migrations

Revision ID: 5746ccd51ae6
Revises: 5c62fb365e5d
Create Date: 2022-04-25 14:05:25.127554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5746ccd51ae6"
down_revision = "5c62fb365e5d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "course",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("course")
