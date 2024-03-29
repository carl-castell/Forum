"""added reply feature

Revision ID: 4930063922de
Revises: 201b32a403b4
Create Date: 2023-04-19 18:50:41.944811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4930063922de'
down_revision = '201b32a403b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reply_content', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    # ### end Alembic commands ###
