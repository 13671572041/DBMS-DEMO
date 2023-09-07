"""add_user_id_in_todo_table

Revision ID: ec5d7ccb07c8
Revises: b1c9907db843
Create Date: 2023-09-01 10:45:13.575530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec5d7ccb07c8'
down_revision: Union[str, None] = 'b1c9907db843'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('todos', sa.Column('user_id', sa.Integer))
    op.create_foreign_key(
        "user_todo",
        "todos",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint("user_todo", "todos", type_="foreignkey")
    op.drop_column("todos", "user_id")
