"""empty message

Revision ID: 0a5db1c03ed0
Revises: a005ea560d9c
Create Date: 2024-04-17 15:53:31.649498

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0a5db1c03ed0"
down_revision: Union[str, None] = "a005ea560d9c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("transfer_sha1", sa.Text(), nullable=True, server_default=sa.null()))
        batch_op.create_index(batch_op.f("ix_user_transfer_sha1"), ["transfer_sha1"], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_transfer_sha1"))
        batch_op.drop_column("transfer_sha1")

    # ### end Alembic commands ###
