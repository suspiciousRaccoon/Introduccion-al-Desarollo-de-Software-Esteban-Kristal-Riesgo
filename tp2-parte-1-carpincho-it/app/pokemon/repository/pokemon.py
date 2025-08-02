from app.pokemon.models.pokemon import Pokemon


from app.utils.types import Database


class PokemonRepository:
    def __init__(self, database: Database):
        self.database = database

    def get(self, pokemon_id: int) -> Pokemon | None:
        for pokemon in self.database["pokemons"]:
            if pokemon.id == pokemon_id:
                return pokemon
        return None

    def get_all(
        self, tipo: int | None = None, nombre_parcial: str | None = None
    ) -> list[Pokemon]:
        resultados = self.database["pokemons"]

        if tipo is not None:
            filtrados_por_tipo = []
            for pokemon in resultados:
                if pokemon.tipos:
                    for type in pokemon.tipos:
                        if type.id == tipo:
                            filtrados_por_tipo.append(pokemon)
                            break
            resultados = filtrados_por_tipo

        if nombre_parcial is not None:
            filtrados_por_nombre = []
            for pokemon in resultados:
                if nombre_parcial.lower() in pokemon.nombre.lower():
                    filtrados_por_nombre.append(pokemon)
            resultados = filtrados_por_nombre

        return resultados
