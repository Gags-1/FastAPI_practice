"""add content column

Revision ID: 070f5162380d
Revises: 421fc9f3bca5
Create Date: 2024-05-26 13:19:34.532397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '070f5162380d'
down_revision: Union[str, None] = '421fc9f3bca5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_column('posts','content')
    pass
