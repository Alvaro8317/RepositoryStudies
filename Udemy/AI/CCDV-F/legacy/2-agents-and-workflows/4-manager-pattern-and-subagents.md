# Manager Pattern y Subagents

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: de una pizarra a varias

La lección anterior planteó el problema de la pizarra: un context window de tamaño fijo
donde todo compite por el mismo espacio. Esta lección ofrece una respuesta distinta al
mismo problema — en vez de gestionar una pizarra saturada, ¿por qué no tener varias? Esa
es la idea detrás de managers, workers y subagents.

## 1. El manager pattern

Un agente planea y otros ejecutan.

Ejemplo: una wedding planner es la manager y posee el plan. Debajo de ella hay tres
subagents, cada uno con un trabajo estrecho:

- El **caterer**, que solo hace comida.
- El **decorator**, que solo hace el venue.
- El **photographer**, que solo hace fotos.

Ninguno de ellos hace un poco de todo. Y el detalle clave: la planner no cocina la
comida. Un agente posee el plan, y otros poseen la ejecución.

> 📌 Esto conecta directo con la pizarra de la lección anterior: el caterer no necesita
> saber nada de fotografía, el photographer no necesita el menú, y la planner no necesita
> conocer cada ingrediente. En vez de una pizarra enorme con todo, hay cuatro pizarras
> pequeñas, y cada una tiene solo lo que esa persona necesita.

## 2. ¿Qué es un subagent?

**Un agente fresco, un trabajo, y su propia pizarra.**

La manager agent está arriba, y debajo hay varios subagents. Cada uno arranca con una
pizarra completamente vacía (*empty*) y un trabajo estrecho.

La palabra clave es **fresh** (fresco). Un subagent:

1. Corre su propio loop (el mismo ciclo *think → call tool → observe → repeat* de la
   lección sobre el agent loop) — no es un mecanismo nuevo.
2. Hace un solo trabajo — no se le pide manejar varias cosas a la vez.
3. Devuelve solo su respuesta — esta es la parte que más importa para la manager.

> ⚠️ El photographer nunca ve el menú del catering. Cualquier desorden que haya en la
> pizarra del caterer nunca llega al photographer.

## 3. Por qué los subagents mejoran los resultados

**Context enfocado le gana a context saturado** (*crowded*).

Un detalle importante y fácil de pasar por alto: el usuario define la capacidad de cada
subagent, pero es Claude quien decide en tiempo de ejecución cuándo paralelizar. No es el
usuario quien arma el cronograma — se configuran los subagents y se dice qué puede hacer
cada uno, pero la decisión de qué corre en paralelo y qué espera se toma en runtime.

Hay tres razones por las que esto funciona:

| Razón | Qué significa | Ejemplo |
| --- | --- | --- |
| **Isolation** | El trabajo sucio queda en la pizarra del subagent, no en la del manager | Un documento de 200 páginas se lee dentro del subagent, y solo vuelve un párrafo |
| **Containment** | Un fallo queda contenido en un solo subagent, no contamina todo el run | Si un subagent se confunde o llena su pizarra de basura, el manager y los demás subagents siguen sin verse afectados |
| **Speed** | Los subagents independientes corren en paralelo | Corren juntos precisamente porque ninguno espera al otro |

> ⚠️ El examen evalúa las **tres** razones, no solo una. Una pregunta puede describir
> cualquiera de estas tres situaciones y esperar que se reconozca como argumento a favor
> de usar subagents.

## 4. Single agent vs. manager pattern

**Más poder no es automáticamente mejor.**

| | Single agent | Manager + subagents |
| --- | --- | --- |
| Context por unidad | Todo | Solo lo necesario |
| Trabajo en paralelo | No | Sí |
| Costo en tokens | Menor | Mayor |
| Complejidad | Baja | Mayor |
| Mejor para | Tareas simples y acotadas | Tareas amplias y con varias partes |

> ⚠️ **Los subagents no son gratis.** Se paga el token cost de la manager más el de cada
> subagent. No es dividir el trabajo pagando lo mismo: se paga a la manager por planear y
> coordinar, y por separado se paga el loop completo de cada subagent. Tres subagents
> significan cuatro sets de tokens, no uno — por eso la fila de costo dice "mayor".

## 5. Cuándo agregar un manager

Solo se divide el trabajo cuando es genuinamente separable.

**Cuándo sí divide bien:**

- Las subtareas son independientes.
- El context de un solo agente se está desbordando.
- La velocidad en paralelo realmente importa.

Estas tres razones coinciden casi exactamente con los tres beneficios de la sección
anterior: independencia da pie a la división, context desbordado es el problema que
resuelve isolation, y velocidad es el beneficio de speed.

**Cuándo no dividir:**

- Una tarea simple de 3 pasos.
- Pasos que dependen unos de otros (si el paso 2 necesita el resultado del paso 1,
  dividirlos en subagents no gana nada — el segundo igual tiene que esperar).
- Cuando el costo en tokens es la preocupación principal (agregar una manager va en la
  dirección contraria).

> ⚠️ No agregar una manager para una tarea de 3 pasos — se paga coordinación que no hacía
> falta.

## Puntos clave

1. La manager planea, los subagents ejecutan.
2. Cada subagent arranca con el context limpio (fresh).
3. Dividir solo el trabajo que sea genuinamente separable — los subagents no son gratis.
