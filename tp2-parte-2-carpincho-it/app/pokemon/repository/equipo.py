from sqlmodel import select

from app.pokemon.models.entity.equipo import (
    Equipo,
    Integrante,
)
from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.models.entity.movimiento import Movimiento
from app.pokemon.models.schema.equipo import (
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoUpsert,
)
from app.utils.repository import BaseRepository


class EquipoRepository(BaseRepository[Equipo]):
    entity = Equipo

    def get_por_nombre(self, nombre=str) -> Equipo:
        query = select(Equipo).where(Equipo.nombre.ilike(nombre.lower()))
        return self.session.exec(query).first()

    def create(self, data: EquipoUpsert) -> Equipo:
        equipo_existente = self.session.exec(
            select(Equipo).where(
                Equipo.nombre == data.nombre, Equipo.generacion_id == data.id_generacion
            )
        ).first()

        if equipo_existente:
            raise ValueError("Ya existe un equipo con ese nombre")
        nuevo_equipo = Equipo(
            nombre=data.nombre, generacion_id=data.id_generacion, integrantes=[]
        )
        return super().create(nuevo_equipo)

    def update(self, equipo_id: int, data: EquipoUpsert) -> Equipo:
        equipo = self.get(equipo_id)

        if not equipo:
            raise ValueError("Equipo no encontrado")

        return super().update_instance(
            equipo,
            {
                "nombre": data.nombre,
                "generacion": self.session.get(Generacion, data.id_generacion),
            },
        )


class IntegranteRepository(BaseRepository[Integrante]):
    entity = Integrante

    def get(self, equipo_id: int, integrante_id: int) -> Integrante | None:
        return self.session.exec(
            select(Integrante).where(
                Integrante.id == integrante_id, Integrante.equipo_id == equipo_id
            )
        ).first()

    def get_integrante_por_apodo(self, equipo_id: int, apodo: str):
        return self.session.exec(
            select(Integrante).where(
                Integrante.apodo == apodo, Integrante.equipo_id == equipo_id
            )
        ).first()

    def create(self, id_equipo: int, data: EquipoIntegranteAdd) -> Integrante:
        nuevo_integrante = Integrante(
            apodo=data.apodo, pokemon_id=data.id_pokemon, equipo_id=id_equipo
        )
        return super().create(nuevo_integrante)

    def update(
        self, equipo_id: int, integrante_id: int, data: EquipoIntegranteUpdate
    ) -> Integrante:
        if len(data.movimientos) > 4:
            raise ValueError("Un integrante no puede tener mas de 4 movimientos")

        integrante = self.get(equipo_id, integrante_id)
        if not integrante:
            raise ValueError("Integrante no encontrado")

        query = select(Movimiento).where(Movimiento.id.in_(data.movimientos))
        movimientos = self.session.exec(query).all()

        integrante.apodo = data.apodo
        integrante.movimientos = movimientos

        return super().update_instance(integrante)

    def delete(self, equipo_id: int, integrante_id: int) -> Integrante:
        integrante = self.get(equipo_id, integrante_id)
        self.session.delete(integrante)
        self.session.commit()
        return integrante
