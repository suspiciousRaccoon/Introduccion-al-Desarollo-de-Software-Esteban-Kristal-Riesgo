from pydantic import ConfigDict
from sqlmodel import SQLModel


class Schema(SQLModel):
    model_config = ConfigDict(from_attributes=True)
