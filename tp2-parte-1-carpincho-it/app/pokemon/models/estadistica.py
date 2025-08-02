from pydantic import BaseModel


class Estadistica(BaseModel):
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    puntos_de_golpe: int
    velocidad: int
