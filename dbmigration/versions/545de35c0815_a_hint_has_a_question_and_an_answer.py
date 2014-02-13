"""a hint has a question and an answer

Revision ID: 545de35c0815
Revises: None
Create Date: 2014-02-13 09:15:31.248430

"""

# revision identifiers, used by Alembic.
revision = '545de35c0815'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'hints',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.Unicode(1000), nullable=False),
        sa.Column('answer', sa.Unicode(2000), nullable=False),
    )

def downgrade():
    pass
