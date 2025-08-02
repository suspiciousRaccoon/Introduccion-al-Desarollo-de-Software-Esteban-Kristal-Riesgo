from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session as SQLModelSession

from app.utils.database import ENGINE


def get_session() -> Generator[SQLModelSession, None, None]:
    with SQLModelSession(ENGINE) as session:
        yield session


Session = Annotated[SQLModelSession, Depends(get_session)]
