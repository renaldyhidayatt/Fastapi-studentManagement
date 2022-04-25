"""staff-migrations

Revision ID: d2138eca5d9e
Revises: bdaba9cffeb0
Create Date: 2022-04-25 14:05:59.793315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2138eca5d9e"
down_revision = "bdaba9cffeb0"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "staff",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("course.id")),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("staff")
