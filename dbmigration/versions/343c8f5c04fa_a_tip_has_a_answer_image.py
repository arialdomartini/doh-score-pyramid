"""a tip has a answer image

Revision ID: 343c8f5c04fa
Revises: 518ab3d37e4
Create Date: 2014-02-17 08:19:18.923613

"""

# revision identifiers, used by Alembic.
revision = '343c8f5c04fa'
down_revision = '518ab3d37e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('tips',
            sa.Column('answer_image', sa.Unicode(100)),
    )



def downgrade():
    pass
