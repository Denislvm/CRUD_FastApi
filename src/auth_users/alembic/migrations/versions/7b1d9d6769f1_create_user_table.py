from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b1d9d6769f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('email', sa.String(200)),
        sa.Column('password', sa.String(200)),
        sa.Column('date', sa.Date),
    )


def downgrade():
    pass
