"""backfill first_name and last_name from full_name

Revision ID: 9c6157790a7f
Revises: c0afe465a324
Create Date: 2026-05-24 03:32:50.944465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c6157790a7f'
down_revision: Union[str, Sequence[str], None] = 'c0afe465a324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text("""
        UPDATE users
        SET
            first_name = split_part(full_name, ' ', 1),
            last_name  = NULLIF(split_part(full_name, ' ', 2), '')
        WHERE full_name IS NOT NULL
    """))

def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text("""
        UPDATE users
        SET full_name = CONCAT(first_name, ' ', last_name)
        WHERE first_name IS NOT NULL
    """))
