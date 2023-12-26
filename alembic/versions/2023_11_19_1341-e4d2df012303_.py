"""empty message

Revision ID: e4d2df012303
Revises: 47fdce35337e
Create Date: 2023-11-19 13:41:53.322265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e4d2df012303"
down_revision: Union[str, None] = "47fdce35337e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    conn = op.get_bind()
    res = conn.execute(sa.text("select user_id, background_id from background where is_set = 1"))
    user_backgrounds: dict[int, int] = {a[0]: a[1] for a in res}

    with op.batch_alter_table("background", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_background_background_id"), ["background_id"], unique=False)
        batch_op.drop_column("is_set")

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("active_background", sa.Integer(), nullable=False, server_default="1"))
        batch_op.add_column(sa.Column("active_award", sa.Integer(), nullable=False, server_default="1"))

    for user_id, background_id in user_backgrounds.items():
        conn.execute(sa.text(f"update user set active_background = {background_id} where id = {user_id}"))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("active_award")
        batch_op.drop_column("active_background")

    with op.batch_alter_table("background", schema=None) as batch_op:
        batch_op.add_column(sa.Column("is_set", sa.BOOLEAN(), nullable=False))
        batch_op.drop_index(batch_op.f("ix_background_background_id"))

    # ### end Alembic commands ###