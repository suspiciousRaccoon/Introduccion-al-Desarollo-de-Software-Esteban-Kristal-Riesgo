[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gWx9VeHk)
# TP2 Parte 1- IntroDex

## Temas a evaluar

- Git
- Trabajo en equipo
- Testing
- Desarrollo BackEnd (Framework: FastAPI)

## Glosario

- Equipo Pokemon: Un equipo Pokemon es un grupo de pokemones de entre 1 y 6 integrantes. Puede tener al mismo pokemon repetido muchas veces.
- Generacion: Los juegos de Pokemon llevan mucho tiempo lanzandose y cada nuevo grupo de Pokemones sale en nuevos juegos que conforman una Generacion. Es decir, las entregas de ciertos juegos forman parte de cierta generacion del 1 al 9. Por ejemplo, la Generacion 3 introdujo, entre otros, a los juegos de Pokemon Ruby, Zafiro y Esmeralda, asi como pokemones como Metagross.
- Movimiento: Es la ejecucion de una accion en combate de un Pokemon. Cada Pokemon sabe entre 1 y 4 movimientos, pudiendo olvidar uno para reemplazarlo por otr.
- Grupo de Huevo: Los pokemones para reproducirse ponen huevos. Un grupo de huevos son aquellos pokemones que son "compatibles entre si" para reproducirse.
- EVs: Son especializaciones de estadísticas para un Pokemon. Todos los pokemones tienen un máximo de 510 EVs para mejorar sus estadísticas y pueden asignarsele un máximo de 255 por estadística.
- Naturaleza: Todo Pokemon, además, tiene una Naturaleza que le aumenta una estadística y le reduce otra.

## Organizacion

Este trabajo practico es extenso y **grupal**. Deberán revisar el trabajo de sus compañeros y aplicar buenas prácticas de equipo de desarrollo así como escribir pruebas y mantener el orden.

Los grupos de este trabajo práctico son de **al menos 4 integrantes** con la posibilidad de extenderlo hasta **5 integrantes**. En general, va a ser mas sencillo organizarse con menos personas.

Los equipos conformados por 5 integrantes tendrán la obligacion de completar el punto opcional del enunciado.

## Consigna

El trabajo práctica va a estar desarrollado en tres etapas. Esta consigna corresponde a la primer etapa del Trabajo Práctico 2, o también llamada TP2 parte 1.

Como estudiantes de ingeniería de la renombrada facultad de la UBA, nos piden desarrollar el siguiente proyecto:

Debemos implementar un sitio web para obtener información sobre Pokemones, sus movimientos y habilidades así como también la posibilidad de creación de equipos de combate (similar a https://pokemondb.net/). El sitio web va constar de una parte de desarrollo backend, una base de datos para persistir la información, y una parte de desarrollo frontend. Esta primer etapa corresponde al desarrollo backend de la aplicación.

Tenemos la suerte de que nuestro asesores ya hablaron con el cliente del proyecto y saben suficiente de software como para darnos las especificaciones de la API que vamos a necesitar para la realizacion del proyecto completo.

Vamos a necesitar varios endpoints definidos a continuación.

### Generaciones

#### Listar Generaciones existentes
```
GET /api/generaciones/
```
que devolverá su ID y nombre y estarán ordenadas de menor a mayor.
```
[
    {
        "id": 1,
        "nombre": "Generación I",
    },
    ...
]
```

### Pokemon


#### Obtener un pokemon específico a partir de su ID

```
GET /api/pokemon/30
```
que devolverá su ID, nombre, imagen, altura, peso, generaciones, tipos, habilidades, stats, evoluciones y movimientos según su método de aprendizaje (huevo, máquina de tiempo, nivel).

Las debilidades de un tipo se identifican por cuán efectivo es un tipo en hacerle daño a otro. Un ataque de un pokemon a otro genera cierto daño, pero el tipo tiene un efecto sobre esa cantidad de daño. Los efectos son:
- si el tipo A le hace el doble de daño de lo normal (200%) al tipo B, significa que el tipo A es súper efectivo ante B y que B es débil ante el A.
- si el tipo A le hace el daño normal (100%) al tipo B, significa que A es efectivo ante B.
- si A le hace la mitad del daño normal (50%) a B, A no es tan efectivo ante B y/o B es resistente a A.
- si A no le hace daño (0%) a B, significa que A no es efectivo ante B y/o B es inmune a A.
Las relaciones no son simétricas: no porque A sea super efectivo ante B significa que A sea inmune a B.

```
{
    "id": 30,
    "nombre": "nidorina",
    "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
    "altura": 0.8,
    "peso": 20.0,
    "generaciones": [
        {
            "id": 1,
            "nombre": "Generación I"
        },
		...,
        {
            "id": 8,
            "nombre": "Generación VIII"
        }
    ],
    "tipos": [
        {
            "id": 4,
            "nombre": "Veneno",
            "debilidades": [
                {
                    "id": 5,
                    "nombre": "Tierra"
                },
                {
                    "id": 14,
                    "nombre": "Psíquico"
                }
            ]
        }
    ],
    "habilidades": [
        {
            "id": 38,
            "nombre": "Punto Tóxico"
        },
		...,
        {
            "id": 55,
            "nombre": "Entusiasmo"
        }
    ],
    "estadisticas": {
        "ataque": 62,
        "defensa": 67,
        "ataque_especial": 55,
        "defensa_especial": 55,
        "puntos_de_golpe": 70,
        "velocidad": 56
    },
    "evoluciones": [
        {
            "id": 31,
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/31.png",
            "nombre": "nidoqueen"
        }
    ],
    "movimientos_huevo": [],
    "movimientos_maquina": [
        {
            "id": 32,
            "nombre": "Perforador",
            "generacion": {
                "id": 1,
                "nombre": "Generación I"
            },
            "tipo": {
                "id": 1,
                "nombre": "Normal"
            },
            "categoria": "físico",
            "potencia": 0,
            "precision": 30,
            "puntos de poder": 5,
            "efecto": "Causes a one-hit KO."
        },
		...,
    ],
    "movimientos_nivel": [
        {
            "id": 10,
            "nombre": "Arañazo",
            "generacion": {
                "id": 1,
                "nombre": "Generación I"
            },
            "tipo": {
                "id": 1,
                "nombre": "Normal"
            },
            "categoria": "físico",
            "potencia": 40,
            "precision": 100,
            "puntos_de_poder": 35,
            "efecto": "Inflicts regular damage with no additional effect."
        },
		...,
    ]
}
```
o el status code correspondiente con su error:
```
{ "detalle": "Pokemon no encontrado" }
```

#### Listar todos los pokemon

```
GET /api/pokemon
```
que devolverá de cada pokemon su ID, nombre, imagen, generaciones y tipos:
```
[
	{
        "id": 30,
        "nombre": "nidorina",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
        "generaciones": [
            {
                "id": 1,
                "nombre": "Generación I"
            },
            ...,
        ],
        "tipos": [
            {
                "id": 4,
                "nombre": "Veneno",
            }
        ],
	},
	{
		...
	},
	...
]
```

#### Filtrar pokemon

El endpoint recién nombrado deberá además poder filtrar la lista de pokemones:

```
GET /api/pokemon?tipo=4
GET /api/pokemon?nombre_parcial=ido
```

La respuesta mostrará una lista que sólo va a contener pokemones que tengan ese `tipo` y/o que contengan el `nombre_parcial` dentro de su nombre.


### Movimientos

#### Obtener la información de un movimiento a partir de su ID

```
GET /api/movimientos/<id>
```
que devolverá su ID, nombre, su tipo (Roca, Planta, etc), categoría (Fisico, Estado, Especial, etc), potencia (power), precision (accuracy), puntos de poder (pp), generación en la que fue introducido, efecto en texto, Pokemon que lo pueden aprenden (separado según si es por huevo, máquina, o nivel)
```
{
    "id": 32,
    "nombre": "Perforador",
    "generacion": {
        "id": 1,
        "nombre": "Generación I"
    },
    "tipo": {
        "id": 1,
        "nombre": "Normal"
    },
    "categoria": "físico",
    "potencia": 0,
    "precision": 30,
    "puntos_de_poder": 5,
    "efecto": "Causes a one-hit KO.",
    "pokemon_por_huevo": [
        {
            "id": 32,
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/32.png",
            "nombre": "nidoran-m",
            "altura": 0.5,
            "peso": 9.0
        },
        ...
    ],
    "pokemon_por_nivel": [
        {
            "id": 33,
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/33.png",
            "nombre": "nidorino",
            "altura": 0.9,
            "peso": 19.5
        },
        ...
    ],
    "pokemon_por_maquina": [
        {
            "id": 30,
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
            "nombre": "nidorina",
            "altura": 0.8,
            "peso": 20.0
        },
        ...
    ]
}
```
o el status code correspondiente con su error:
```
{ "detalle": "Movimiento no encontrado" }
```

#### Listar movimientos

```
GET /api/movimientos
```
que devolverá cada movimiento con su ID, nombre, tipo (Roca, Planta, etc), categoría (Fisico, Estado, Especial, etc), potencia (power), precision (accuracy), puntos de poder (pp), generación en la que fue introducido y efecto en texto.


### Equipos

La escena competitiva del juego requiere que se puedan crear Equipos, pero también limita contenido hasta ciertas generaciones y cantidades.

Condiciones de un equipo:
  - se le asocia una generación que es la "máxima" generación que se permite: lo que implica que sus pokemones, movimientos y etc deben existir en esa generación o una anterior.
  - se permiten como máximo 6 integrantes, pero puede existir un equipo con 0 integrantes.
  - cada integrante debe referenciar a un Pokemon existente según la generación elegida.
  - cada integrante debe tener no más de 4 movimientos, pero puede tener 0 movimientos.
  - los movimientos elegidos para cada integrante deben ser válidos para ese Pokemon y esa generación.


#### Obtener la información de un equipo a partir de su ID:
```
GET /api/equipos/<id>
```
que devolverá su ID, nombre, generación y la lista de integrantes con su información:
```
{
    "id": 1,
    "nombre": "Equipo Rocket",
    "generacion": {
        "id": 1,
        "nombre": "Generación I"
    },
    "integrantes": [
        {
            "id": 2,
            "apodo": "Viborita",
            "pokemon": {
                "id": 23,
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
                "nombre": "ekans",
                "estadisticas": {
                    "ataque": 62,
                    "defensa": 67,
                    "ataque_especial": 55,
                    "defensa_especial": 55,
                    "puntos_de_golpe": 70,
                    "velocidad": 56
                },
                "generaciones": [...],
                "tipos": [...],
            },
            "movimientos": [
                {
                    "id": 228,
                    "nombre": "Persecución",
                    "generacion": {
                        "id": 2,
                        "nombre": "Generación II"
                    },
                    "tipo": {
                        "id": 17,
                        "nombre": "Siniestro"
                    },
                    "categoria": "físico",
                    "potencia": 40,
                    "precision": 100,
                    "puntos_de_poder": 20,
                    "efecto": "Has double power against, and can hit, Pokémon attempting to switch out."
                }
            ]
        }
    ]
},
```
o el status code correspondiente con su error:
```
{ "detalle": "Equipo no encontrado" }
```

#### Listar equipos
```
GET /api/equipos
```
que devolverá para una lista de equipos, donde para cada equipo detallará su ID, nombre, cantidad de integrantes y generación.
```
[
    {
        "id": 1,
        "nombre": "Equipo Rocket",
        "generacion": {
            "id": 4,
            "nombre": "Generación IV"
        },
        "cant_integrantes": 3
    },
    ...
]
```


#### Crear un equipo
```
POST /api/equipos

Body:
{
    "nombre": "Equipo Rocket",
    "id_generacion": 4
}
```
que recibirá la información del equipo a crear (nombre único y ID de su generación)
y devolverá la información del equipo creado:
```
{
    "id": 1,
    "nombre": "Equipo Rocket",
    "generacion": {
        "id": 1,
        "nombre": "Generación I"
    },
    "integrantes": []
}
```
o el status code correspondiente con su error.

Nota: Recalcamos la importancia de que no puede haber dos equipos con el mismo nombre.


#### Actualizar un equipo
```
PUT /api/equipos/<id_equipo>

Body:
{
    "nombre": "Team Rocket",
    "id_generacion": 4
}
```
que permite cambiar el nombre o generación del equipo (si el equipo ya cuenta con integrantes, no se puede asignar una generación inválida con los mismos).
Devolverá la misma información que en el endpoint de crear equipo
```
{
    "id": 1,
    "nombre": "Team Rocket",
    "generacion": {
        "id": 4,
        "nombre": "Generación IV"
    },
    "integrantes": []
}
```
o el status code correspondiente con su error.


#### Eliminar equipo
```
DELETE /api/equipos/<id_equipo>
```
que permite eliminar un equipo creado. Todos los integrantes deben ser eliminados también.
Devolverá la información completa del equipo eliminado
```
{
    "id": 1,
    "nombre": "Team Rocket",
    "generacion": {
        "id": 4,
        "nombre": "Generación IV"
    },
    "integrantes": []
}
```

#### Agregar un Integrante a un equipo
```
POST /api/equipos/<id_equipo>/integrantes

Body:
{
    "id_pokemon": 23,
    "apodo": "Champion",
}
```
donde un Integrante de un equipo debe referenciar a un Pokemon existente (por su ID)
y el endpoint devolverá la información del integrante creado:
```
{
    "id": 2,
    "apodo": "Champion",
    "pokemon": {
        "id": 23,
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
        "nombre": "ekans",
        "generaciones": [...],
        "tipos": [...],
    },
    "movimientos": []
}
```
o el status code correspondiente con su error.


#### Agregar un Movimiento a un Integrante
```
POST /api/equipos/<id_equipo>/integrantes/<id_integrante>/movimientos

Body:
{
    "id_movimiento": 228
}
```
donde se debe referenciar a un Movimiento existente (por su ID)
y el endpoint devolverá la información del movimiento agregado:
```
{
    "id": 228,
    "nombre": "Persecución",
    "generacion": {
        "id": 2,
        "nombre": "Generación II"
    },
    "tipo": {
        "id": 17,
        "nombre": "Siniestro"
    },
    "categoria": "físico",
    "potencia": 40,
    "precision": 100,
    "puntos_de_poder": 20,
    "efecto": "Has double power against, and can hit, Pokémon attempting to switch out."
}
```
o el status code correspondiente con su error.


#### Editar un Integrante de un equipo
```
PUT /api/equipos/<id_equipo>/integrantes/<id_integrante>

Body:
{
    "apodo": "Campeón",
    "movimientos": [228]
}
```
donde un Integrante de un equipo debe referenciar a un Pokemon existente (por su ID)
y el endpoint devolverá la información del integrante creado:
```
{
    "id": 2,
    "apodo": "Campeón",
    "pokemon": {
        "id": 23,
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
        "nombre": "ekans",
        "generaciones": [...],
        "tipos": [...],
    },
    "movimientos": [
        {
            "id": 228,
            "nombre": "Persecución",
            "generacion": {
                "id": 2,
                "nombre": "Generación II"
            },
            "tipo": {
                "id": 17,
                "nombre": "Siniestro"
            },
            "categoria": "físico",
            "potencia": 40,
            "precision": 100,
            "puntos_de_poder": 20,
            "efecto": "Has double power against, and can hit, Pokémon attempting to switch out."
        }
    ]
}
```
o el status code correspondiente con su error.

Este endpoint permite agregar múltiples movimientos en una sola interacción a un mismo integrante (además de editar su apodo). Si hay error en alguno de los movimientos (por ejemplo, algún movimiento inválido), debe fallar toda la operación sin haber cambiado nada.
Notar que el id_pokemon no se permite editar. Si se quiere cambiar el Pokemon elegido se debe eliminar el integrante y agregar uno nuevo.


#### Eliminar un Integrante de un equipo
```
DELETE /api/equipos/<id_equipo>/integrantes/<id_integrante>
```
y el endpoint devolverá la información del integrante eliminado:
```
{
    "id": 2,
    "apodo": "Campeón",
    "pokemon": {
        "id": 23,
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
        "nombre": "ekans",
        "generaciones": [...],
        "tipos": [...],
    },
    "movimientos": [
        {
            "id": 228,
            "nombre": "Persecución",
            "generacion": {
                "id": 2,
                "nombre": "Generación II"
            },
            "tipo": {
                "id": 17,
                "nombre": "Siniestro"
            },
            "categoria": "físico",
            "potencia": 40,
            "precision": 100,
            "puntos_de_poder": 20,
            "efecto": "Has double power against, and can hit, Pokémon attempting to switch out."
        }
    ]
}
```

Deben eliminarse los datos de tablas intermedias relacionadas al Integrante si las hubiese.

### OPCIONAL: Página de creación de Pokemones

El organizador del proyecto mostró su deseo de también crear sus propios Pokemon, similar a lo que ofrece [esta página](https://pokemon.alexonsager.net/). Ésto implicaría que, para crear un Pokemon, necesitamos de otros 2 para usarlos como "padres".
```
POST /api/pokemon
```
La request debe poder recibir todos los detalles de Pokemon, incluyendo: nombre, altura, peso, generaciones, tipos, habilidades, stats y movimientos según su tipo (huevo, máquina, nivel).

El nombre estará dado de combinar las primeras 3 letras del primer pokemon y las últimas 3 del segundo:
```
{
    "altura": 0.8,
    "peso": 20.0,
    "generaciones": [5,6,7,8],
    "tipos": [4],
    "habilidades": [38,55],
    "estadisticas": {
        "ataque": 62,
        "defensa": 67,
        "ataque_especial": 55,
        "defensa_especial": 55,
        "puntos_de_golpe": 70,
        "velocidad": 56
    },
    "movimientos_huevo": [32],
    "movimientos_maquina": [],
    "movimientos_nivel": [10, 21],
    "primer_padre": [30],
    "segundo_padre": [86]
}
```

la respuesta debe ser igual al endpoint de mostrar un pokemon según su ID.

IMPORTANTE: notar que todos los campos que referencian a movimientos, tipos, generaciones, habilidades y otros pokemon lo hacen a a través de sus IDs y solo incluyen eso, no los objetos completos.

El Pokemon creado debe cumplir ciertas condiciones en base a sus padres:

- Debe compartir al menos un tipo con AMBOS padres.
- Debe tener una cantidad de estadística total exactamente igual al promedio de sus padres
- Debe compartir al menos una habilidad con AMBOS padres
- Puede aprender cualquier movimiento que sus padres puedan
- No tiene evoluciones
- Comparte el resto de sus features con alguno de sus padres (altura, peso, etc)
- Tiene una imagen customizada que combine las caracteristicas de ambos Pokemones, por ejemplo [este pokemon](https://pokemon.alexonsager.net/25/11) que es la combinacion de `Pikachu` y `Metapod`

Estas condiciones y validaciones deben ser realizadas por el sevidor BE. En caso de que no se cumpla alguno de ellos se debe devolver un error correspondiente indicándolo.

Este requisito, de formar grupos de 5 personas, pasa a ser **obligatorio**.

Nota: Notar que en este caso, la imagen del nuevo pokemon que estamos inventando no está en el mismo dominio de URL que los pokemon normales. Este caso especial deberá ser manejado correctamente.


## Archivos Disponibles

Como se mencionó, el directorio /data cuenta con todos los archivos .csv necesarios para el sistema. Los mismos deben ser cargados al comienzo de la ejecución del programa y mantener su estado en memoria RAM.

**IMPORTANTE**: el archivo `pokemon.csv` contiene la información básica de todos los Pokemon, pero no su imagen. Para ello vamos a usar imágenes ya subidas a la Internet. De manera que el endpoint que muestra información de un Pokemon, en el campo de la imagen debe mostrar una URL con este formato

`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<id>.png`

reemplazar `<id>` por el ID del pokemon que se quiere mostrar.

Además, el repositorio base cuenta con un directorio bruno/ con una coleccion con los endpoints a implementar definidos anteriormente. La misma se puede utilizar para verificar que los endpoints estén funcionando correctamente luego de implementarlos.

## Requisitos adicionales

El proyecto debe estar desarrollado usando en Python usando el framework FastAPI siguiendo los lineamientos de estructuración de proyecto vistos en clase.

Se debe usar pipenv para setear el virtual environment. Las dependencias deben estar listadas en un archivo Pipfile para poder ser instaladas con `pipenv`. Luego de tenerlo seteado, el proyecto debe poder ser corrido con el comando ```pipenv run fastapi dev main.py```.

Además de contar con los endpoints especificados, el proyecto deberá cargar la información al iniciar desde los archivos CSV provistos en el directorio /data.

Sin embargo, no es necesario que las modificaciones hechas en una corrida del sistema afecten a otras instancias (no es necesario persistir la información más que en memoria RAM).

El repositorio debe contar un con archivo .gitignore que incluya los contenidos comunes de Python y demás que no se necesiten subir (archivos generador por la ejecución del script, venv setup, etc.)

Se debe contar con tests unitarios realizados con pytest, con mocks para las dependencias (como vimos en clase) que obtengan un coverage de al menos **75%**.

El proyecto debe seguir las guias de estilo establecidas por la herramienta `black` y no deben presentar warnings ni errores con ella.

En caso de usar alguna librería que no sea de la libería standard de Python (es decir, si hay que usar `pip` o algún otro manejador de paquetes para usarla) no vista en clase consultar con su corrector antes de utilizarla.

Este proyecto va a ser la base del sistema, las siguientes partes del TP van a trabajar sobre este mismo código, por lo que mantener buena calidad de código e implementar buenas prácticas les va a servir mucho.


## Flujo de trabajo en equipo

El flujo de trabajo esperado es el siguiente:

- Alumno 1 decide resolver el endpoint `GET pokemon/<id>`
- Alumno 1 crea su rama de trabajo y realiza su trabajo, una vez listo pushea y realiza un PR.
- Alumno X revisa el PR de su compañero, dejando comentarios de ser necesario. En caso de que no haya comentarios, aprobar el PR.
- Alumno 1 revisa los comentarios de haberlos, los resuelve y realiza el paso anterior nuevamente. Y así hasta que el PR esté aprobado, momento en el cual el Alumno 1 lo mergea.

Es requisito para la aprobación del trabajo práctico que cada integrante haya **creado al menos un PR** y que haya revisado y **aprobado al menos un PR** de algún compañero. En caso de que un integrante no cumpla el requisito tendrá el trabajo desaprobado.

## Entrega

El trabajo se entregará a través de GH Classroom y del repositorio provisto. Se deberá crear una rama `parte1` y hacer un Pull Request a la rama `main`.

`main` **no debe tener ningún contenido más allá del proviste por el repositorio base**. Todo el código debe ser escrito en la rama `parte1`. Con lo cual, todo su trabajo interno va a partir de `parte1`.