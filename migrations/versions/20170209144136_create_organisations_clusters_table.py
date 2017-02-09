# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db02d759783f'
down_revision = u'f35805a0a00f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('organisation_clusters',

        sa.Column('canonical', sa.Text),
        sa.Column('variations', sa.ARRAY(sa.Text)),

    )


def downgrade():
    op.drop_table('organisation_clusters')
