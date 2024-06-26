"""add extra body to assistants

Revision ID: 8dbb8f38ef77
Revises: e7339aab6549
Create Date: 2024-03-19 15:27:39.793603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8dbb8f38ef77'
down_revision: Union[str, None] = 'e7339aab6549'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assistant', sa.Column('extra_body', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assistant', 'extra_body')
    # ### end Alembic commands ###
