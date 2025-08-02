from typing import Annotated

from fastapi import Depends, Request

from app.utils.types import Database as DatabaseType


def get_database(request: Request):
    return request.app.state.database


Database = Annotated[DatabaseType, Depends(get_database)]
