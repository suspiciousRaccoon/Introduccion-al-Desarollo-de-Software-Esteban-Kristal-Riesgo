[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zTSr6e87)

# TP2 Parte 3 - IntroDex

## Temas a evaluar

- Git
- Trabajo en equipo
- Testing
- Bases de Datos Relacionales (SQLite)
- Desarrollo BackEnd (Framework: FastAPI)
- Desarrollo FrontEnd (Framework: Svelte)

## Consigna

Ya terminado el segundo "sprint" de trabajo debemos proceder con el siguiente: crear el frontend desde el cual nuestros usuarios van a poder usar nuestro sistema. Para ello podemos mergear nuestra parte_2 a main si nuestro corrector nos da el Approve necesario.

Debemos crear un frontend que utilice el mismo backend que programamos en las partes anteriores. Las definiciones de los endpoints del BE ya dadas son suficientes para resolver este FE. Pero pueden retocar alguno de los endpoints ya creados si así lo desean, por ejemplo, la información que devuelven si en alguna de las páginas del FE quieren mostrar aún más información.

Para desarrollar este FE vamos a necesitar un repositorio completamente nuevo y vacío, ya que es un sistema distinto que se integra al backend que ya tenemos sólo a través de requests para que toda la aplicación cobre vida.

En cuanto a lo que va a componer a nuestro frontend, vamos a requerir de varias páginas que compongan al sitio completo, **dejando el diseño totalmente libre** para ustedes decidirlo.
No sólo con libertad de UI (User Interface - la interfaz visual con el usuario) como de UX (User Experience - cómo se comporta la página en interacción con el usuario).
Les vamos a hablar de cosas que deben ser posible hacer/ver en su sitio, pero ustedes van a decidir si para resolver esas cuestiones usan 1 página o 5 páginas o 10 páginas.
No se va a evaluar la "calidad gráfica o visual", pero sí la _navegabilidad_ y facilidad de uso para el usuario. También se va a evaluar la reusabilidad de código: incentivamos fuertemente la creación de componentes reusables a usar en muchas páginas, qeu eviten la repetición de código y el retrabajo futuro.

Para poder hacer todo esto, nuestras páginas van a necesitar hacer varias requests a nuestro backend, incluso puede haber varias requests hechas para una sola página. Tengan en cuenta que si bien podemos retocar un poco los endpoints de backend, la idea NO es adaptar todo el backend para tener endpoints que devuelvan exactamente lo que cada una de las páginas necesita. Sino que el backend es su propio sistema que trabaja con las **entidades** que ya estuvimos trabajando, y el frontend es un nuevo sistema que debe utilizar esas entidades y endpoints de la forma necesaria para cumplir sus propios objetivos. No vamos a pedir eficiencia para esta materia, en el futuro de su carrera van a ir perfeccionando estas habilidades.

Durante todo este proceso se debe pensar en un usuario que sabe sobre el mundo de pokemon, por lo que conoce sus entidades y glosario, pero no sabe nada de desarrollo de sistemas ni tampoco es tan experto como para nunca cometer un error. Por lo que, por ejemplo, el usuario no va a ser capaz de pedir un pokemon por su id en nuestra base de datos, sino que puede conocer su nombre. También por ejemplo puede no saber todas las limitaciones de un equipo pókemon por lo que hay que evitar que cometa errores o validarlos para informarle cuando comete uno y que pueda arreglarlo. Con lo cual **los IDs serán información "invisible"** para el usuario y no debe ser mostrada.

## Requerimientos

### Página de inicio

La página de inicio, bienvenida o presentación es la página inicial que debe presentarle nuestra aplicación al usuario para transmitirle qué es capaz de hacer en ella y atraparlo para quedarse.

### Navegación

El usuario debe de poder entender simplemente cómo navegar la página y todas sus secciones/features. Se recomienda tener una barra de navegación o algún tipo de menú para esto.

Por otro lado, siempre que en una página se mencione una entidad o concepto relevante de Pokemon, debo poder ver más información sobre él o existir la posibilidad de navegar a él. Por ejemplo, puede que esté en la página de detalle del pokemon Pikachu, pero si me nombra un Movimiento, debo poder navegar a más detalles sobre ese movimiento que me está comentando, si no es que ya están todos allí mismo.

### Pokemones

Se debe poder ver todos los pokemones existentes y su información correspondientes (toda la que nuestro BE provee, debería poder ser visible de alguna forma).
También se debe poder buscar enter ellos para encontrar un pokemon específico o filtrarlos por alguna condición relevante como su tipo.
Se debe poder seguir la cadena evolutiva de un pokemon. OPCIONAL: se puede también permitir poder seguir la cadena "involutive" de un pokemon, es decir no sólo poder acceder sus evoluciones, sino también sus antecesores.

#### Creación de un pokemón

Si quisieron o debieron realizar la parte opcional, se debe poder crear un nuevo pokemón con toda la información necesario. Y luego, por transitividad, poder buscarlo y ver su información detallada.

### Movimientos

De misma forma, se debe poder ver todos los movimientos existentes y su información correspondiente (toda la proveída por nuestro BE), pudiendo buscar entre ellos y filtrarlos.

### Equipos

Como los Pokemones y los Movimientos, se debe poder ver los equipos existentes y su información correspondiente, incluyendo sus integrantes. OPCIONAL: estaría bueno poder buscar entre ellos y/o filtrarlos.

Más allá de esto, se debe poder crear un equipo y declarar sus integrantes, pudiendo modificar tanto la información del equipo como las particularidades de sus integrantes, incluyendo esto el hecho de eliminar por completo un integrante o agregar uno al equipo.

### Generaciones y Tipos

Estas entidades son menos "relevantes" o complejas, por lo que no vamos a pedir mucha funcionalidad a su alrededor. No vamos a pedir que se puedan ver o buscar entre ellos. Sino que simplemente su información puede ser mostrada en alguna de las páginas ya existentes. De todas maneras, pueden si lo desean crearles sus propias páginas para mostrar su información.

## Requisitos adicionales

El proyecto debe estar desarrollado usando JS a través del framework Svelte siguiendo los lineamientos de estructuración de proyecto vistos en clase.
Al crear el proyecto se debe usar SvelteKit minimal y las dependencias deben manejarse con npm. No es necesario usar ningún Type checking ni linter o formatter. De ustedes quererlo, son libres de elegirlos.

El repositorio debe contar un con archivo .gitignore que incluya los contenidos comunes de Svelte y demás que no se necesiten subir (archivos generador por las dependencias, etc.)

En caso de usar alguna librería que no sea estándar de JavaScript (además de Svelte) no vista en clase, consultar con su corrector antes de utilizarla.

Nuevamente recomendamos mantener buena calidad de código e implementar buenas prácticas.

## Flujo de trabajo en equipo

El flujo de trabajo esperado es el siguiente:

- Alumno 1 decide resolver la página `Lista de pokemones`
- Alumno 1 crea su rama de trabajo y realiza su trabajo, una vez listo pushea y realiza un PR.
- Alumno X revisa el PR de su compañero, dejando comentarios de ser necesario. En caso de que no haya comentarios, aprobar el PR.
- Alumno 1 revisa los comentarios de haberlos, los resuelve y realiza el paso anterior nuevamente. Y así hasta que el PR esté aprobado, momento en el cual el Alumno 1 lo mergea.

Sigue siendo requisito para la aprobación del trabajo práctico que cada integrante haya resuelto **al menos una de las tareas** y que haya revisado y aprobado **al menos un PR** de algun compañero. En caso de que un integrante no cumpla el requisito tendrá el trabajo desaprobado.

## Entrega

El trabajo se entregará a través de GH Classroom y del repositorio provisto. Se deberá crear una rama `parte3` y hacer un Pull Request a la rama `main`.

`main` **no debe tener ningún contenido más allá del proviste por el repositorio base y sus archivos exactos de la parte 1**. Todo el código debe ser escrito en la rama `parte3`. Con lo cual, todo su trabajo interno va a partir de `parte3`.

De necesitar adaptar algo del BE, van a crear una nueva rama `parte3` en el repostorio ya creado para la parte 2 del TP, siguiendo los mismos lineamientos.

Es así como la entrega se compone de un PR final del repositorio creado en el nuevo GH Classroom de la parte 3 + un nuevo PR opcional del repositorio usado en el Assignment de la parte 2 del GH Classroom.
