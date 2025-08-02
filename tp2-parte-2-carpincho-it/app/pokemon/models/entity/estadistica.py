from sqlmodel import SQLModel, Field


class Estadistica(SQLModel, table=True):
    id: int = Field(primary_key=True)
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    puntos_de_golpe: int
    velocidad: int
