"""add init column

Revision ID: 45ce77a8d6e8
Revises: 205f8327c68c
Create Date: 2023-01-11 17:30:52.879336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ce77a8d6e8'
down_revision = '205f8327c68c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user", sa.Column("password", sa.String))


def downgrade() -> None:
    op.drop_column("user", "password")
