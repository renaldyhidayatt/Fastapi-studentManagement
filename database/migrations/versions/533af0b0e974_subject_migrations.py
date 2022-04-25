"""subject-migrations

Revision ID: 533af0b0e974
Revises: d2138eca5d9e
Create Date: 2022-04-25 14:06:10.119384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "533af0b0e974"
down_revision = "d2138eca5d9e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "subject",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("staff", sa.Integer, sa.ForeignKey("staff.id")),
        sa.Column("course", sa.Integer, sa.ForeignKey("course.id")),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("subject")
