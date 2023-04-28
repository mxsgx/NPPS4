import base64
import time

from .. import idol
from .. import util
from ..idol import user
from ..idol import error

import fastapi
import pydantic


class UserInfoDataResponse(pydantic.BaseModel):
    user_id: int
    name: str
    level: int
    exp: int
    previous_exp: int
    next_exp: int
    game_coin: int
    sns_coin: int
    free_sns_coin: int
    paid_sns_coin: int
    social_point: int
    unit_max: int
    waiting_unit_max: int
    energy_max: int
    energy_full_time: str
    license_live_energy_recoverly_time: int
    energy_full_need_time: int
    over_max_energy: int
    training_energy: int
    training_energy_max: int
    friend_max: int
    invite_code: str
    insert_date: str
    update_date: str
    tutorial_state: int
    # TODO
    lp_recovery_item: list = []


class BirthdayUserInfoResponse(pydantic.BaseModel):
    birth_month: int
    birth_day: int


class UserInfoResponse(pydantic.BaseModel):
    user: UserInfoDataResponse
    birth: BirthdayUserInfoResponse | None = None
    ad_status: bool | None = None
    server_timestamp: int


@idol.register("/user/userInfo")
def userinfo(context: idol.SchoolIdolUserParams) -> UserInfoResponse:
    u = user.get(context)
    if u is None:
        raise error.IdolError(error.ERROR_CODE_LIB_ERROR, 500, "User is not known", http_code=500)
    return UserInfoResponse(
        user=UserInfoDataResponse(
            user_id=u.id,
            name=u.name,
            level=u.level,
            exp=u.exp,
            previous_exp=u.previous_exp,
            next_exp=u.next_exp,
            game_coin=u.game_coin,
            sns_coin=u.free_sns_coin + u.paid_sns_coin,
            free_sns_coin=u.free_sns_coin,
            paid_sns_coin=u.paid_sns_coin,
            social_point=u.social_point,
            unit_max=u.unit_max,
            waiting_unit_max=u.waiting_unit_max,
            energy_max=u.energy_max,
            energy_full_time=util.timestamp_to_datetime(u.energy_full_time),
            license_live_energy_recoverly_time=u.license_live_energy_recoverly_time,
            energy_full_need_time=u.energy_full_need_time,
            over_max_energy=u.over_max_energy,
            training_energy=u.training_energy,
            training_energy_max=u.training_energy_max,
            friend_max=u.friend_max,
            invite_code=u.friend_id,
            insert_date=util.timestamp_to_datetime(u.insert_date),
            update_date=util.timestamp_to_datetime(u.update_date),
            tutorial_state=u.tutorial_state,
        ),
        server_timestamp=int(time.time()),
    )