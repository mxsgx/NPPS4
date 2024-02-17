"""empty message

Revision ID: eb7aa83ce83e
Revises: 
Create Date: 2024-02-08 14:34:04.268398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "eb7aa83ce83e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("key", sa.Text(), nullable=True),
        sa.Column("passwd", sa.Text(), nullable=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("bio", sa.Text(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("exp", sa.Integer(), nullable=False),
        sa.Column("previous_exp", sa.Integer(), nullable=False),
        sa.Column("next_exp", sa.Integer(), nullable=False),
        sa.Column("game_coin", sa.Integer(), nullable=False),
        sa.Column("free_sns_coin", sa.Integer(), nullable=False),
        sa.Column("paid_sns_coin", sa.Integer(), nullable=False),
        sa.Column("social_point", sa.Integer(), nullable=False),
        sa.Column("unit_max", sa.Integer(), nullable=False),
        sa.Column("waiting_unit_max", sa.Integer(), nullable=False),
        sa.Column("energy_max", sa.Integer(), nullable=False),
        sa.Column("energy_full_time", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("license_live_energy_recoverly_time", sa.Integer(), nullable=False),
        sa.Column("energy_full_need_time", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("over_max_energy", sa.Integer(), nullable=False),
        sa.Column("training_energy", sa.Integer(), nullable=False),
        sa.Column("training_energy_max", sa.Integer(), nullable=False),
        sa.Column("friend_max", sa.Integer(), nullable=False),
        sa.Column("invite_code", sa.Integer(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("update_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("tutorial_state", sa.Integer(), nullable=False),
        sa.Column("active_deck_index", sa.Integer(), nullable=False),
        sa.Column("active_background", sa.Integer(), nullable=False),
        sa.Column("active_award", sa.Integer(), nullable=False),
        sa.Column("center_unit_owning_user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_user_invite_code"), ["invite_code"], unique=False)
        batch_op.create_index(batch_op.f("ix_user_key"), ["key"], unique=False)

    op.create_table(
        "achievement",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("achievement_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("achievement_type", sa.Integer(), nullable=False),
        sa.Column("achievement_filter_category_id", sa.Integer(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("is_accomplished", sa.Boolean(), nullable=False),
        sa.Column("is_reward_claimed", sa.Boolean(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("end_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("is_new", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("achievement_id", "user_id"),
    )
    with op.batch_alter_table("achievement", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_achievement_achievement_filter_category_id"),
            ["achievement_filter_category_id"],
            unique=False,
        )
        batch_op.create_index(batch_op.f("ix_achievement_achievement_id"), ["achievement_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_achievement_type"), ["achievement_type"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_end_date"), ["end_date"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_insert_date"), ["insert_date"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_is_accomplished"), ["is_accomplished"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_is_new"), ["is_new"], unique=False)
        batch_op.create_index(batch_op.f("ix_achievement_user_id"), ["user_id"], unique=False)

    op.create_table(
        "album",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("rank_max_flag", sa.Boolean(), nullable=False),
        sa.Column("love_max_flag", sa.Boolean(), nullable=False),
        sa.Column("rank_level_max_flag", sa.Boolean(), nullable=False),
        sa.Column("highest_love_per_unit", sa.Integer(), nullable=False),
        sa.Column("favorite_point", sa.Integer(), nullable=False),
        sa.Column("sign_flag", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("album", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_album_love_max_flag"), ["love_max_flag"], unique=False)
        batch_op.create_index(batch_op.f("ix_album_rank_level_max_flag"), ["rank_level_max_flag"], unique=False)
        batch_op.create_index(batch_op.f("ix_album_rank_max_flag"), ["rank_max_flag"], unique=False)
        batch_op.create_index(batch_op.f("ix_album_unit_id"), ["unit_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_album_user_id"), ["user_id"], unique=False)

    op.create_table(
        "award",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("award_id", sa.Integer(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("award", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_award_award_id"), ["award_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_award_user_id"), ["user_id"], unique=False)

    op.create_table(
        "background",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("background_id", sa.Integer(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("background", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_background_background_id"), ["background_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_background_user_id"), ["user_id"], unique=False)

    op.create_table(
        "incentive",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("add_type", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("expire_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("claimed", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("incentive", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_incentive_add_type"), ["add_type"], unique=False)
        batch_op.create_index(batch_op.f("ix_incentive_expire_date"), ["expire_date"], unique=False)
        batch_op.create_index(batch_op.f("ix_incentive_insert_date"), ["insert_date"], unique=False)
        batch_op.create_index(batch_op.f("ix_incentive_item_id"), ["item_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_incentive_user_id"), ["user_id"], unique=False)

    op.create_table(
        "live_clear",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("live_difficulty_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("hi_score", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("hi_combo_cnt", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("clear_cnt", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "live_difficulty_id"),
    )
    with op.batch_alter_table("live_clear", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_live_clear_live_difficulty_id"), ["live_difficulty_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_live_clear_user_id"), ["user_id"], unique=False)

    op.create_table(
        "live_effort",
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("live_effort_point_box_spec_id", sa.Integer(), nullable=False),
        sa.Column("current_point", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "login_bonus",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("month", sa.Integer(), nullable=False),
        sa.Column("day", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "year", "month", "day"),
    )
    with op.batch_alter_table("login_bonus", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_login_bonus_day"), ["day"], unique=False)
        batch_op.create_index(batch_op.f("ix_login_bonus_month"), ["month"], unique=False)
        batch_op.create_index(batch_op.f("ix_login_bonus_user_id"), ["user_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_login_bonus_year"), ["year"], unique=False)

    op.create_table(
        "museum_unlock",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("museum_contents_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "museum_contents_id"),
    )
    with op.batch_alter_table("museum_unlock", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_museum_unlock_museum_contents_id"), ["museum_contents_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_museum_unlock_user_id"), ["user_id"], unique=False)

    op.create_table(
        "removable_skill_info",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_removable_skill_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "unit_removable_skill_id"),
    )
    with op.batch_alter_table("removable_skill_info", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_removable_skill_info_unit_removable_skill_id"), ["unit_removable_skill_id"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_removable_skill_info_user_id"), ["user_id"], unique=False)

    op.create_table(
        "scenario",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("scenario_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("scenario", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_scenario_completed"), ["completed"], unique=False)
        batch_op.create_index(batch_op.f("ix_scenario_scenario_id"), ["scenario_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_scenario_user_id"), ["user_id"], unique=False)

    op.create_table(
        "sub_scenario",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("subscenario_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("sub_scenario", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_sub_scenario_completed"), ["completed"], unique=False)
        batch_op.create_index(batch_op.f("ix_sub_scenario_subscenario_id"), ["subscenario_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_sub_scenario_user_id"), ["user_id"], unique=False)

    op.create_table(
        "tos_agree",
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "unit",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_id", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("favorite_flag", sa.Boolean(), nullable=False),
        sa.Column("is_signed", sa.Boolean(), nullable=False),
        sa.Column("insert_date", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("exp", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("skill_exp", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("max_level", sa.Integer(), nullable=False),
        sa.Column("love", sa.Integer(), nullable=False),
        sa.Column("rank", sa.Integer(), nullable=False),
        sa.Column("display_rank", sa.Integer(), nullable=False),
        sa.Column("level_limit_id", sa.Integer(), nullable=False),
        sa.Column("unit_removable_skill_capacity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("unit", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_unit_active"), ["active"], unique=False)
        batch_op.create_index(batch_op.f("ix_unit_user_id"), ["user_id"], unique=False)

    op.create_table(
        "unit_deck",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("deck_number", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "deck_number"),
    )
    with op.batch_alter_table("unit_deck", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_unit_deck_deck_number"), ["deck_number"], unique=False)
        batch_op.create_index(batch_op.f("ix_unit_deck_user_id"), ["user_id"], unique=False)

    op.create_table(
        "unit_supporter",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("amount", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "unit_id"),
    )
    with op.batch_alter_table("unit_supporter", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_unit_supporter_unit_id"), ["unit_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_unit_supporter_user_id"), ["user_id"], unique=False)

    op.create_table(
        "incentive_unit_option",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_id", sa.Integer(), nullable=False),
        sa.Column("is_signed", sa.Boolean(), nullable=False),
        sa.Column("exp", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("skill_exp", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("max_level", sa.Integer(), nullable=False),
        sa.Column("love", sa.Integer(), nullable=False),
        sa.Column("rank", sa.Integer(), nullable=False),
        sa.Column("display_rank", sa.Integer(), nullable=False),
        sa.Column("level_limit_id", sa.Integer(), nullable=False),
        sa.Column("unit_removable_skill_capacity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["incentive.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "unit_deck_position",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("deck_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("unit_owning_user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["deck_id"],
            ["unit_deck.id"],
        ),
        sa.ForeignKeyConstraint(
            ["unit_owning_user_id"],
            ["unit.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("deck_id", "unit_owning_user_id"),
    )
    with op.batch_alter_table("unit_deck_position", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_unit_deck_position_deck_id"), ["deck_id"], unique=False)
        batch_op.create_index(
            batch_op.f("ix_unit_deck_position_unit_owning_user_id"), ["unit_owning_user_id"], unique=False
        )

    op.create_table(
        "unit_removable_skill",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_owning_user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("unit_removable_skill_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["unit_owning_user_id"],
            ["unit.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("unit_owning_user_id", "unit_removable_skill_id"),
    )
    with op.batch_alter_table("unit_removable_skill", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_unit_removable_skill_unit_owning_user_id"), ["unit_owning_user_id"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_unit_removable_skill_user_id"), ["user_id"], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("unit_removable_skill", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_unit_removable_skill_user_id"))
        batch_op.drop_index(batch_op.f("ix_unit_removable_skill_unit_owning_user_id"))

    op.drop_table("unit_removable_skill")
    with op.batch_alter_table("unit_deck_position", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_unit_deck_position_unit_owning_user_id"))
        batch_op.drop_index(batch_op.f("ix_unit_deck_position_deck_id"))

    op.drop_table("unit_deck_position")
    op.drop_table("incentive_unit_option")
    with op.batch_alter_table("unit_supporter", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_unit_supporter_user_id"))
        batch_op.drop_index(batch_op.f("ix_unit_supporter_unit_id"))

    op.drop_table("unit_supporter")
    with op.batch_alter_table("unit_deck", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_unit_deck_user_id"))
        batch_op.drop_index(batch_op.f("ix_unit_deck_deck_number"))

    op.drop_table("unit_deck")
    with op.batch_alter_table("unit", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_unit_user_id"))
        batch_op.drop_index(batch_op.f("ix_unit_active"))

    op.drop_table("unit")
    op.drop_table("tos_agree")
    with op.batch_alter_table("sub_scenario", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_sub_scenario_user_id"))
        batch_op.drop_index(batch_op.f("ix_sub_scenario_subscenario_id"))
        batch_op.drop_index(batch_op.f("ix_sub_scenario_completed"))

    op.drop_table("sub_scenario")
    with op.batch_alter_table("scenario", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_scenario_user_id"))
        batch_op.drop_index(batch_op.f("ix_scenario_scenario_id"))
        batch_op.drop_index(batch_op.f("ix_scenario_completed"))

    op.drop_table("scenario")
    with op.batch_alter_table("removable_skill_info", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_removable_skill_info_user_id"))
        batch_op.drop_index(batch_op.f("ix_removable_skill_info_unit_removable_skill_id"))

    op.drop_table("removable_skill_info")
    with op.batch_alter_table("museum_unlock", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_museum_unlock_user_id"))
        batch_op.drop_index(batch_op.f("ix_museum_unlock_museum_contents_id"))

    op.drop_table("museum_unlock")
    with op.batch_alter_table("login_bonus", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_login_bonus_year"))
        batch_op.drop_index(batch_op.f("ix_login_bonus_user_id"))
        batch_op.drop_index(batch_op.f("ix_login_bonus_month"))
        batch_op.drop_index(batch_op.f("ix_login_bonus_day"))

    op.drop_table("login_bonus")
    op.drop_table("live_effort")
    with op.batch_alter_table("live_clear", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_live_clear_user_id"))
        batch_op.drop_index(batch_op.f("ix_live_clear_live_difficulty_id"))

    op.drop_table("live_clear")
    with op.batch_alter_table("incentive", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_incentive_user_id"))
        batch_op.drop_index(batch_op.f("ix_incentive_item_id"))
        batch_op.drop_index(batch_op.f("ix_incentive_insert_date"))
        batch_op.drop_index(batch_op.f("ix_incentive_expire_date"))
        batch_op.drop_index(batch_op.f("ix_incentive_add_type"))

    op.drop_table("incentive")
    with op.batch_alter_table("background", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_background_user_id"))
        batch_op.drop_index(batch_op.f("ix_background_background_id"))

    op.drop_table("background")
    with op.batch_alter_table("award", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_award_user_id"))
        batch_op.drop_index(batch_op.f("ix_award_award_id"))

    op.drop_table("award")
    with op.batch_alter_table("album", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_album_user_id"))
        batch_op.drop_index(batch_op.f("ix_album_unit_id"))
        batch_op.drop_index(batch_op.f("ix_album_rank_max_flag"))
        batch_op.drop_index(batch_op.f("ix_album_rank_level_max_flag"))
        batch_op.drop_index(batch_op.f("ix_album_love_max_flag"))

    op.drop_table("album")
    with op.batch_alter_table("achievement", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_achievement_user_id"))
        batch_op.drop_index(batch_op.f("ix_achievement_is_new"))
        batch_op.drop_index(batch_op.f("ix_achievement_is_accomplished"))
        batch_op.drop_index(batch_op.f("ix_achievement_insert_date"))
        batch_op.drop_index(batch_op.f("ix_achievement_end_date"))
        batch_op.drop_index(batch_op.f("ix_achievement_achievement_type"))
        batch_op.drop_index(batch_op.f("ix_achievement_achievement_id"))
        batch_op.drop_index(batch_op.f("ix_achievement_achievement_filter_category_id"))

    op.drop_table("achievement")
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_key"))
        batch_op.drop_index(batch_op.f("ix_user_invite_code"))

    op.drop_table("user")
    # ### end Alembic commands ###