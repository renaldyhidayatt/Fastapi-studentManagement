"""fbstaff-migrations

Revision ID: 7f39b15ec875
Revises: 5746ccd51ae6
Create Date: 2022-04-25 14:05:42.961664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7f39b15ec875"
down_revision = "5746ccd51ae6"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "feedback_staff",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("staff_id", sa.Integer, sa.ForeignKey("staff.id")),
        sa.Column("feedback", sa.Text),
        sa.Column("reply", sa.Text),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("feedback_staff")
