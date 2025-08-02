from app.pokemon.models.schema.base import Schema


class EstadisticaPublic(Schema):
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    puntos_de_golpe: int
    velocidad: int
