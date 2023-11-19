"""create post table

Revision ID: 4e3d35666c28
Revises: 
Create Date: 2023-11-18 14:25:18.213309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4e3d35666c28"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
