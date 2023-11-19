"""add content column to posts table

Revision ID: 73518d4b31d6
Revises: 4e3d35666c28
Create Date: 2023-11-18 14:36:19.574712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "73518d4b31d6"
down_revision = "4e3d35666c28"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content"),
    pass
