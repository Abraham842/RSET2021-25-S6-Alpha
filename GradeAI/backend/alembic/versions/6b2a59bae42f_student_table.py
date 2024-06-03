"""student_table

Revision ID: 6b2a59bae42f
Revises: a7667508ebe1
Create Date: 2024-05-20 12:05:30.905454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b2a59bae42f'
down_revision: Union[str, None] = 'a7667508ebe1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('institution', sa.String(), nullable=False),
    sa.Column('exams_attended', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
