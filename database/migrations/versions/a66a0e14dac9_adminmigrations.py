"""adminmigrations

Revision ID: a66a0e14dac9
Revises: 
Create Date: 2022-04-25 14:04:47.349950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a66a0e14dac9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "admin",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("admin")
