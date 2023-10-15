from .. import idol
from .. import util
from ..idol import error
from ..idol.system import user

import pydantic


class TutorialProgressRequest(pydantic.BaseModel):
    tutorial_state: int


@idol.register("/tutorial/progress", batchable=False)
async def tutorial_progress(
    context: idol.SchoolIdolUserParams, request: TutorialProgressRequest
) -> idol.core.DummyModel:
    current_user = await user.get_current(context)
    if current_user.tutorial_state == -1:
        raise error.IdolError(detail="Tutorial already finished")
    if current_user.tutorial_state == 0 and request.tutorial_state == 1:
        current_user.tutorial_state = 1
        return idol.core.DummyModel()
    elif current_user.tutorial_state == 1 and request.tutorial_state == 2:
        current_user.tutorial_state = 2
        return idol.core.DummyModel()

    msg = f"STUB /tutorial/progress, user {current_user.tutorial_state} request {request.tutorial_state}"
    util.log(msg, request, severity=util.logging.WARNING)
    raise error.IdolError(detail=msg)
