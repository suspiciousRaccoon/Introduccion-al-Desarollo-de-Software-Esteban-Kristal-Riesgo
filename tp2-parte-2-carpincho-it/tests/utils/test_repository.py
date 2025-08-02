import pytest
from pydantic import BaseModel, ConfigDict, PydanticDeprecatedSince211
from sqlalchemy import create_engine
from sqlalchemy.exc import SAWarning
from sqlmodel import Field, Relationship, Session, SQLModel

from app.utils.repository import BaseRepository, Filter

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)


class GrupoAlumno(SQLModel, table=True):
    nota: int | None = Field(default=None, ge=1, le=10)

    grupo_id: int = Field(nullable=False, foreign_key="grupo.id", primary_key=True)
    # grupo: "Grupo" = Relationship(back_populates="integrantes")

    alumno_padron: int = Field(
        nullable=False, foreign_key="alumno.id", primary_key=True
    )
    # alumno: "Alumno" = Relationship()


class Grupo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str

    alumnos: list["Alumno"] | None = Relationship(
        back_populates="grupos", link_model=GrupoAlumno
    )


class Alumno(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

    grupos: list[Grupo] | None = Relationship(
        back_populates="alumnos", link_model=GrupoAlumno
    )


class AlumnoPydantic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

    grupos: list["GrupoPydantic"] | None = None


class GrupoPydantic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    nombre: str | None = None

    alumnos: list["AlumnoPydantic"] | None = None


@pytest.fixture(autouse=True)
def setup_database():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)

    yield
    with engine.begin() as conn:
        SQLModel.metadata.drop_all(conn)
    engine.dispose()


@pytest.fixture
def session(
    setup_database: None,
) -> Session:
    with Session(engine) as session:
        yield session


class AlumnoRepository(BaseRepository[Alumno]):
    entity = Alumno


class IntegranteRepository(BaseRepository[GrupoAlumno]):
    entity = GrupoAlumno


class GrupoRepository(BaseRepository[Grupo]):
    entity = Grupo


@pytest.mark.filterwarnings("ignore", category=SAWarning)
@pytest.mark.filterwarnings("ignore", category=PydanticDeprecatedSince211)
class TestAbstractRepository:
    def test_create(self, session: Session):
        repo = AlumnoRepository(session)
        alumno = repo.create(Alumno(padron=1, nombre="A", apellido="B", edad=20))
        assert alumno is not None
        assert alumno.id == 1

    def test_get(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        alumno = repo.get(1)
        assert alumno is not None
        assert alumno.id == 1

    def test_get_all(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        alumnos = repo.get_all()
        assert alumnos[0].id == 1
        assert alumnos[1].id == 2

    def test_limit_filter(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        alumnos = repo.get_all_with_filter(Filter(limit=1))
        assert len(alumnos) == 1
        assert alumnos[0].id == 1

    def test_offset_filter(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        alumnos = repo.get_all_with_filter(Filter(offset=1))
        assert len(alumnos) == 1
        assert alumnos[0].id == 2

    def test_custom_filter(self, session: Session):
        class AlumnoFilter(Filter):
            nombre: str

        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        alumno = repo.get_with_filter(1, AlumnoFilter(nombre="A"))
        assert alumno.id == 1
        assert alumno.nombre == "A"

        alumno = repo.get_with_filter(2, AlumnoFilter(nombre="B"))
        assert alumno is None

        alumno = repo.get_with_filter(2, AlumnoFilter(nombre="C"))
        assert alumno.id == 2
        assert alumno.nombre == "C"

        alumnos = repo.get_all_with_filter(AlumnoFilter(nombre="A"))
        assert len(alumnos) == 1
        assert alumnos[0].id == 1
        assert alumnos[0].nombre == "A"

    def test_update(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        alumno = repo.update(1, Alumno(nombre="UPDATE"))
        assert alumno.id == 1
        assert alumno.nombre == "UPDATE"

    def test_update_and_get(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        repo.update(2, Alumno(nombre="UPDATE"))
        alumno = repo.get(2)
        assert alumno.id == 2
        assert alumno.nombre == "UPDATE"

    def test_update_instance(self, session: Session):
        repo = AlumnoRepository(session)
        alumno = repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.create(Alumno(id=2, nombre="C", apellido="D", edad=21))
        repo.update_instance(alumno, Alumno(nombre="UPDATE"))
        alumno_updated = repo.get(1)
        assert alumno_updated.id == 1
        assert alumno_updated.nombre == "UPDATE"

    def test_update_entity_does_not_exist(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))

        with pytest.raises(ValueError):
            repo.update(999, Alumno(nombre="UPDATE"))

    def test_delete(self, session: Session):
        repo = AlumnoRepository(session)
        repo.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        repo.delete(1)
        alumno = repo.get(1)
        assert alumno is None

    # relationships

    def test_update_relationships(self, session: Session):
        repo_alumno = AlumnoRepository(session)
        repo_grupo = GrupoRepository(session)
        alumno1 = repo_alumno.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        alumno2 = repo_alumno.create(Alumno(id=2, nombre="C", apellido="D", edad=20))
        group = repo_grupo.create(Grupo(nombre="A & C"))

        assert group.alumnos == []

        # assert m2m relationship is set from Grupo
        repo_grupo.update(
            1,
            Grupo(nombre="A & C club", alumnos=[alumno1, alumno2]),
        )

        group = repo_grupo.get(1)
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)
        assert group.alumnos == [alumno1, alumno2]
        assert group.nombre == "A & C club"
        assert alumno1.grupos == [group]
        assert alumno2.grupos == [group]

        # assert m2m relationship is updated from Alumno
        only_1_group = repo_grupo.create(Grupo(nombre="only A"))
        repo_alumno.update(1, Alumno(grupos=[only_1_group]))
        groups = repo_grupo.get_all()
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)

        assert len(groups) == 2
        assert alumno1.grupos == [groups[1]]
        assert alumno2.grupos == [groups[0]]
        assert groups[0].alumnos == [alumno2]
        assert groups[1].alumnos == [alumno1]

    def test_update_instance_relationships_sqlmodel(self, session: Session):
        repo_alumno = AlumnoRepository(session)
        repo_grupo = GrupoRepository(session)
        alumno1 = repo_alumno.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        alumno2 = repo_alumno.create(Alumno(id=2, nombre="C", apellido="D", edad=20))
        group = repo_grupo.create(Grupo(nombre="A & C"))

        assert group.alumnos == []

        # assert m2m relationship is set from Grupo
        repo_grupo.update_instance(
            group,
            Grupo(nombre="A & C club", alumnos=[alumno1, alumno2]),
        )

        group = repo_grupo.get(1)
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)
        assert group.alumnos == [alumno1, alumno2]
        assert group.nombre == "A & C club"
        assert alumno1.grupos == [group]
        assert alumno2.grupos == [group]

        # assert m2m relationship is updated from Alumno
        only_1_group = repo_grupo.create(Grupo(nombre="only A"))
        repo_alumno.update_instance(alumno1, Alumno(grupos=[only_1_group]))
        groups = repo_grupo.get_all()
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)

        assert len(groups) == 2
        assert alumno1.grupos == [groups[1]]
        assert alumno2.grupos == [groups[0]]
        assert groups[0].alumnos == [alumno2]
        assert groups[1].alumnos == [alumno1]

    def test_update_instance_relationships_dictionary(self, session: Session):
        repo_alumno = AlumnoRepository(session)
        repo_grupo = GrupoRepository(session)
        alumno1 = repo_alumno.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        alumno2 = repo_alumno.create(Alumno(id=2, nombre="C", apellido="D", edad=20))
        group = repo_grupo.create(Grupo(nombre="A & C"))

        assert group.alumnos == []

        # assert m2m relationship is set from Grupo
        repo_grupo.update_instance(
            group,
            {"nombre": "A & C club", "alumnos": [alumno1, alumno2]},
        )

        group = repo_grupo.get(1)
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)
        assert group.alumnos == [alumno1, alumno2]
        assert group.nombre == "A & C club"
        assert alumno1.grupos == [group]
        assert alumno2.grupos == [group]

        # assert m2m relationship is updated from Alumno
        only_1_group = repo_grupo.create(Grupo(nombre="only A"))
        repo_alumno.update_instance(alumno1, {"grupos": [only_1_group]})
        groups = repo_grupo.get_all()
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)

        assert len(groups) == 2
        assert alumno1.grupos == [groups[1]]
        assert alumno2.grupos == [groups[0]]
        assert groups[0].alumnos == [alumno2]
        assert groups[1].alumnos == [alumno1]

    def test_update_instance_relationships_manual(self, session: Session):
        repo_alumno = AlumnoRepository(session)
        repo_grupo = GrupoRepository(session)
        alumno1 = repo_alumno.create(Alumno(id=1, nombre="A", apellido="B", edad=20))
        alumno2 = repo_alumno.create(Alumno(id=2, nombre="C", apellido="D", edad=20))
        group = repo_grupo.create(Grupo(nombre="A & C"))

        assert group.alumnos == []

        # assert m2m relationship is set from Grupo
        group.alumnos = [alumno1]
        group.alumnos.append(alumno2)
        group.nombre = "A & C club"
        repo_grupo.update_instance(group)

        group = repo_grupo.get(1)
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)
        assert group.alumnos == [alumno1, alumno2]
        assert group.nombre == "A & C club"
        assert alumno1.grupos == [group]
        assert alumno2.grupos == [group]

        # assert m2m relationship is updated from Alumno
        only_1_group = repo_grupo.create(Grupo(nombre="only A"))
        alumno1.grupos = [only_1_group]
        repo_alumno.update_instance(alumno1)
        groups = repo_grupo.get_all()
        alumno1 = repo_alumno.get(1)
        alumno2 = repo_alumno.get(2)

        assert len(groups) == 2
        assert alumno1.grupos == [groups[1]]
        assert alumno2.grupos == [groups[0]]
        assert groups[0].alumnos == [alumno2]
        assert groups[1].alumnos == [alumno1]
