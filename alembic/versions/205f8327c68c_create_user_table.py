"""create user table

Revision ID: 205f8327c68c
Revises: 
Create Date: 2023-01-11 17:25:06.116000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '205f8327c68c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("user")
