"""studentmigrations

Revision ID: 5c62fb365e5d
Revises: a66a0e14dac9
Create Date: 2022-04-25 14:05:09.660228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5c62fb365e5d"
down_revision = "a66a0e14dac9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "student",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("student_id", sa.Integer, sa.ForeignKey("student.id")),
        sa.Column("course_id", sa.Integer, sa.ForeignKey("course.id")),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("student")
