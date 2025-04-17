"""add new column to user

Revision ID: 18259414b385
Revises: ae7e8d34d152
Create Date: 2025-04-17 23:36:17.295874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18259414b385'
down_revision: Union[str, None] = 'ae7e8d34d152'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lots', sa.Column('current_rate_user_id', sa.BigInteger(), nullable=True,default=None))
    op.create_foreign_key(None, 'lots', 'users', ['current_rate_user_id'], ['telegram_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lots', type_='foreignkey')
    op.drop_column('lots', 'current_rate_user_id')
    # ### end Alembic commands ###
