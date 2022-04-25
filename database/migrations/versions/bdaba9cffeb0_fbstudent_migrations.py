"""fbstudent-migrations

Revision ID: bdaba9cffeb0
Revises: 7f39b15ec875
Create Date: 2022-04-25 14:05:47.808390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bdaba9cffeb0"
down_revision = "7f39b15ec875"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "feedback_student",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("student_id", sa.Integer, sa.ForeignKey("student.id")),
        sa.Column("feedback", sa.Text),
        sa.Column("reply", sa.Text),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("feedback_student")
