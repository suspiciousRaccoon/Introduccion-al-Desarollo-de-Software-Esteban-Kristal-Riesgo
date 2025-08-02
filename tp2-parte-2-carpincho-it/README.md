[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Hg0ouXFc)
# TP2 Parte 2- IntroDex

# Instalación
```bash
pipenv install --dev
```
El servidor de FastAPI necesita una base de datos con migraciones aplicadas para correr
Las migraciones se pueden aplicar con:
```bash
alembic upgrade head
```
Lo que va a crear un base de datos sqlite `database.db` en el root del proyecto
Si la base de datos está presente, el servidor va a encargarse de seedearla con la información necesaria para su funcionamiento.

```bash
fastapi dev
```

## Temas a evaluar

- Git
- Trabajo en equipo
- Testing
- Bases de Datos Relacionales (Sqlite)
- Desarrollo BackEnd (Framework: FastAPI)


## Consigna

Ya terminado el primer "sprint" de trabajo debemos proceder con la siguiente: persistir la información que tenemos en bases de datos. Para ello podemos mergear el PR de parte_1 a main si nuestro corrector nos da el Approve necesario.

## Parte 2

Vamos a utilizar el mismo backend que programamos en la parte anterior.
Por lo que en este nuevo repositorio, nuestro primer commit directo a main debe ser uno que copie todos los archivos del repo anterior.
Aclaración: Esto no es algo que se haga en el mundo real, pero para poder utilizar el Google Classroom como queremos es lo mejor que podemos hacer por ahora. En el mundo real, siempre se trabaja sobre el mismo repositorio agregando nuevos commits y nuevas ramas.

En esta parte 2, debemos refactorizar el código que tenemos para usar datos persistidos en una base de datos en lugar de obtenerlos/guardarlos en memoría como veníamos haciendo.

Para ello vamos a necesitar hacer todo lo siguiente:

- Crear la base de datos necesaria en SQLite
- Crear las migraciones pertinentes y las tablas necesarias para estructurar nuestros datos (al realizar los endpoints, vimos algunas posibles entidades a implementar)
- Los datos de los CSVs deberán ser cargados en la base de datos de SQLite en vez de en memoria usando seeds.
- Adaptar la(s) clase(s) Database(s) usada(s) para que haga(n) consultas a la base de datos
- Adaptar y agregar tests
- Corregir errores de la parte anterior
- Definir nuevos endpoints de ser necesarios

Las entidades **mínimas** que esperamos que existan en la base de datos son:

- Pokemon
- Movimiento
- Equipo
- Integrante

Sin embargo podrían ser útiles tener otras entidades como por ejemplo `MetodoDeAprendizaje`, `Tipo`, `Generacion`.

## Endpoints

En esta parte 2 vamos a modificar todos los endpoints existentes que devuelvan listas de tamaño "desconocido" para agregarles Paginación siguiendo los lineamientos vistos en clase.
Es decir, los endpoints de listado de pokemon, de movimientos y de equipos ahora deben poder ser paginados.


### Filtrar movimientos

Al igual que a los pokemons, deberemos poder filtrar movimientos de la siguiente manera:
```
GET /api/movimiento?tipo=4
GET /api/movimiento?nombre_parcial=ido
```

La respuesta mostrará una lista que sólo va a contener movimientos que sean de ese `tipo` y/o que contengan el `nombre_parcial` dentro de su nombre.


## Requisitos adicionales

Existen los mismos requisitos que en la parte 1:

El proyecto debe estar desarrollado usando en Python usando el framework FastAPI siguiendo los lineamientos de estructuración de proyecto vistos en clase.

Se debe usar pipenv para setear el virtual environment. Las dependencias deben estar listadas en un archivo Pipfile para poder ser instaladas con pipenv. Luego de tenerlo seteado, el proyecto debe poder ser corrido con el comando pipenv run fastapi dev main.py.

Además de contar con los endpoints especificados, el proyecto deberá cargar la información al iniciar desde los archivos CSV provistos en el directorio /data. Con la diferencia de que en esta instancia sí es necesario persistir la data y que sobreviva a distintas corridas del sistema.

El repositorio debe contar un con archivo .gitignore que incluya los contenidos comunes de Python y demás que no se necesiten subir (archivos generador por la ejecución del script, venv setup, etc.)

Se debe contar con tests unitarios realizados con pytest, con mocks para las dependencias (como vimos en clase) que obtengan un coverage de al menos 75%.

El proyecto debe seguir las guias de estilo establecidas por la herramienta black y no deben presentar warnings ni errores con ella.

En caso de usar alguna librería que no sea de la libería standard de Python (es decir, si hay que usar pip o algún otro manejador de paquetes para usarla) no vista en clase consultar con su corrector antes de utilizarla.

Además se deberá desarrollar con la base de datos SQLite y el framework de Python correspondiente, SQLModel.
Y también deberá utilizarse Alembic para manejar las migraciones.

Nuevamente recomendamos mantener buena calidad de código e implementar buenas prácticas.


## Flujo de trabajo en equipo

El flujo de trabajo esperado es el siguiente:

- Alumno 1 decide resolver el endpoint `Actualizar list_pokemons`
- Alumno 1 crea su rama de trabajo y realiza su trabajo, una vez listo pushea y realiza un PR.
- Alumno X revisa el PR de su compañero, dejando comentarios de ser necesario. En caso de que no haya comentarios, aprobar el PR.
- Alumno 1 revisa los comentarios de haberlos, los resuelve y realiza el paso anterior nuevamente. Y así hasta que el PR esté aprobado, momento en el cual el Alumno 1 lo mergea.

Sigue siendo requisito para la aprobación del trabajo práctico que cada integrante haya creado al menos un PR y que haya revisado y aprobado al menos un PR de algún compañero. En caso de que un integrante no cumpla el requisito tendrá el trabajo desaprobado.


## Entrega

El trabajo se entregará a través de GH Classroom y del repositorio provisto. Se deberá crear una rama `parte2` y hacer un Pull Request a la rama `main`.

`main` **no debe tener ningún contenido más allá del provisto por el repositorio base y sus archivos exactos de la parte 1**. Todo el código debe ser escrito en la rama `parte2`. Con lo cual, todo su trabajo interno va a partir de `parte2`.

