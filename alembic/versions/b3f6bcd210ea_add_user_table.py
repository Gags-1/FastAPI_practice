"""add user table

Revision ID: b3f6bcd210ea
Revises: 070f5162380d
Create Date: 2024-05-26 13:29:33.314607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3f6bcd210ea'
down_revision: Union[str, None] = '070f5162380d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                
                                server_default=sa.text('now()'), nullable=False),
                                sa.PrimaryKeyConstraint('id'),
                                sa.UniqueConstraint('email')

    )
    pass


def downgrade():
    op.drop_table('users')
    pass
