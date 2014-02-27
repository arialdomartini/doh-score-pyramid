"""visits table

Revision ID: 17e895070c93
Revises: 343c8f5c04fa
Create Date: 2014-02-21 18:56:25.929416

"""

# revision identifiers, used by Alembic.
revision = '17e895070c93'
down_revision = '343c8f5c04fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'visits',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('session', sa.Unicode(36), nullable=False),
        sa.Column('tip_id', sa.Integer, nullable=False),
    )


def downgrade():
    pass
