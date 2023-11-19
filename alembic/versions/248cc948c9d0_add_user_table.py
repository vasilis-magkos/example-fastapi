"""add user table

Revision ID: 248cc948c9d0
Revises: 73518d4b31d6
Create Date: 2023-11-18 14:41:33.974544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "248cc948c9d0"
down_revision = "73518d4b31d6"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
