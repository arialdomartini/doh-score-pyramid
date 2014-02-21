"""a tip has a title image

Revision ID: 518ab3d37e4
Revises: 545de35c0815
Create Date: 2014-02-14 09:03:59.772871

"""

# revision identifiers, used by Alembic.
revision = '518ab3d37e4'
down_revision = '545de35c0815'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('tips',
            sa.Column('title_image', sa.Unicode(100)),
    )

def downgrade():
    pass
