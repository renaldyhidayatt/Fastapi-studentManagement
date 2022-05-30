"""attendance-migrations

Revision ID: 15159264774b
Revises: 89da88360cf5
Create Date: 2022-04-25 14:06:28.909871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "15159264774b"
down_revision = "89da88360cf5"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "attendance",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("student_id", sa.Integer, sa.ForeignKey("student.id")),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("course.id")),
        sa.Column("date", sa.DateTime, default=sa.func.now()),
        sa.Column("status", sa.String(length=255)),
    )


def downgrade():
    op.drop_table("attendance")
