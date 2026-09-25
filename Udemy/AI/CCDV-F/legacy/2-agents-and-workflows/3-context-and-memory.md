# Context and Memory

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: la advertencia de la lección anterior

La lección anterior terminó con una advertencia: el historial de mensajes crece en cada
pasada del loop. Esta lección se ocupa exactamente de eso — qué significa esa
acumulación y qué hacer con ella.

## 1. El context window es una pizarra

El context window es una **pizarra de tamaño fijo**. El system prompt, el historial de
conversación y los tool outputs compiten todos por el mismo espacio — ninguno tiene su
propia pizarra separada. Otra forma de verlo: un cuaderno de páginas limitadas — cuando
se llena, algo tiene que ceder.

> ⚠️ La calidad se degrada **silenciosamente**. No hay un error obvio que avise "se acabó
> el espacio" — las respuestas simplemente empeoran poco a poco mientras todo sigue
> pareciendo que funciona.

Esta pizarra es exactamente donde termina todo lo que vimos en la lección anterior: cada
vuelta del loop escribe más sobre ella, y nunca se limpia sola.

## 2. Dos fallos distintos: bloat y drift

|                  | Bloat                                                                                                | Drift                                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Tipo de problema | Volumen                                                                                              | Atención                                                                                                                                |
| Qué pasa         | El tool output basura desplaza lo que realmente importa (sigue en la pizarra, pero rodeado de ruido) | El goal original queda enterrado bajo turnos posteriores — hacia el turno 40 el agente resuelve, sin darse cuenta, un problema distinto |
| Cómo se arregla  | Reduciendo lo que entra                                                                              | Re-anclando el goal (restableciéndolo explícitamente)                                                                                   |

> ⚠️ Son problemas distintos con arreglos distintos — no tratarlos como uno solo. Si
> tienes drift y lo intentas arreglar recortando el tool output, no soluciona nada: el
> goal sigue enterrado. Bloat es cuánto hay en la pizarra; drift es a dónde se fue la
> atención.

## 3. Primer fix: prune tool output

La idea: **devolver la respuesta, no la respuesta entera.** Un filtro en tu código se
sienta entre lo que la tool devuelve y lo que Claude realmente necesita — por ejemplo, de
500 líneas de JSON a solo tres campos (`order_id`, `status`, `total_amount`), suficientes
para que Claude haga el trabajo perfectamente bien.

> 📌 Es el fix más barato disponible y **el que más se salta**. Barato porque es un
> filtro sencillo, no algo ingenioso o difícil de escribir. Saltado porque es tentador
> pasar la respuesta completa de la tool y dejar que Claude la resuelva — pero cada una
> de esas 500 líneas ocupa espacio en la pizarra. La palabra clave es el momento: se
> filtra **antes** de que llegue a la pizarra, no después.

## 4. Segundo fix: compaction

La idea: **resumir los turnos antiguos y mantener intactos los recientes.**

```text
Antes:   [turnos 1-16 (antiguos)] + [turnos 17-20 (recientes)]  = 20 turnos
Después: [1 bloque de resumen]     + [turnos 17-20 (recientes)]  = espacio recuperado
```

Los 4 turnos recientes se mantienen completos porque son los que más importan ahora
mismo; son los 16 antiguos los que se comprimen en un solo bloque.

> ⚠️ **El trade es detalle por espacio** — no es una operación gratuita de orden. La
> compaction es *lossy* (con pérdida): puede perder un detalle que sí importaba. La
> mayoría de las veces esa información no era importante, pero a veces sí lo era, y no lo
> sabrás hasta que el agente la necesite y no la encuentre.

## 5. ¿Qué es la agent memory?

Si el context window es la pizarra, la memory es **un archivador al lado de la
pizarra**.

|              | Pizarra (context window)         | Archivador (memory)               |
| ------------ | -------------------------------- | --------------------------------- |
| Persistencia | Se borra al final de cada sesión | Sobrevive tras terminar la sesión |
| Coste        | Cuesta tokens en cada llamada    | Solo cuesta al recuperar          |
| Contenido    | Lo que Claude tiene AHORA MISMO  | Lo que Claude puede ir a buscar   |

> 📌 La memory vive **fuera del modelo** — en un archivo o una base de datos en otro
> lugar por completo. Esa es toda la idea, y es justo por eso que sobrevive cuando la
> sesión termina y no cuesta nada hasta que se abre.

## 6. Cómo los agents usan la memory

Solo dos acciones:

- **Escribir al salir**: anotar lo que vale la pena recordar — una decisión, una
  preferencia del usuario, un resultado. Solo lo que importa, no todo.
- **Leer al entrar**: traer de vuelta solo las notas relevantes, no todo el archivador.

> ⚠️ Si lees todo el archivador de vuelta a la pizarra, reconstruyes exactamente el
> mismo bloat que intentabas evitar. El archivador solo ayuda si sacas las dos o tres
> cosas que realmente necesitas.

## Puntos clave

- **Context es ahora, y es costoso** — se paga en cada llamada.
- **Memory es después, y es barata** — se paga solo al recuperar.
- **Poda el tool output antes de que llegue** a la pizarra — es el fix más barato y el
  más saltado.
- Bloat y drift son fallos distintos con arreglos distintos; compaction gana espacio pero
  pierde detalle.
- Memory tiene exactamente dos operaciones: escribir al salir, leer al entrar — nada más.
