"""create_todos_table

Revision ID: 03e438a91198
Revises: 03e438a91198
Create Date: 2023-08-25 18:08:10.481487

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03e438a91198'
down_revision: Union[str, None] = '03e438a91198'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("is_done", sa.Boolean, default=False, nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("todos")
