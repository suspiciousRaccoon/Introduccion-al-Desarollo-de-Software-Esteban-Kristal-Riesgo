from pydantic import BaseModel


class Generacion(BaseModel):
    id: int
    nombre: str
