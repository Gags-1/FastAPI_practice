"""create posts table

Revision ID: 421fc9f3bca5
Revises: 
Create Date: 2024-05-26 10:51:58.100350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '421fc9f3bca5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                     sa.Column('title', sa.String, nullable=False ))
    pass


def downgrade():
    op.drop_table('posts')
    pass
