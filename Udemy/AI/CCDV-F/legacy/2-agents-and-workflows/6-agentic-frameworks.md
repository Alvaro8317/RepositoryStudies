# Agentic Frameworks

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: última clase del domain 1

La lección anterior mostró cómo construir un agent con el Claude Agent SDK o escribiendo
el loop a mano (custom harness). Esta lección, la última del domain 1, amplía la
imagen: por encima de esas dos opciones están los frameworks agénticos.

## 1. Por qué existen los frameworks

**Todos terminan reconstruyendo el mismo loop, y los frameworks frenan eso.**

Tres equipos distintos, cada uno por su cuenta, escriben el mismo código: el loop, los
retries y el manejo de state. Es código idéntico, escrito tres veces — ninguno de esos
equipos está resolviendo un problema diferente, y ese trabajo repetido nunca fue la parte
interesante de su proyecto real. Un framework es, simplemente, que alguien ya escribió
eso una vez, bien, para que nadie más tenga que hacerlo.

> 📌 Es la misma pieza de código que viste en la lección anterior: el `while not done`,
> el chequeo de tool use, la ejecución de la tool y la llamada de nuevo. Ese era tu
> harness. Cada equipo que construye un agent tiene que escribir algo parecido — el
> framework empaqueta ese trabajo repetido para que no lo vuelvas a escribir.

## 2. Los tres frameworks que hay que conocer: Strands, LangGraph y Pydantic AI

| Framework | Filosofía | Qué te da |
| --- | --- | --- |
| **Strands** | *Model-driven*: le das tools y un goal al modelo, y te haces a un lado | Un agent rápido donde decide el modelo; optimizado para AWS Bedrock |
| **LangGraph** | *Graph-driven*: el agent es una state machine con pasos de LLM | Un camino con ramificaciones que tú controlas — soporta pausa, resume, checkpoints y aprobación humana |
| **Pydantic AI** | *Type-driven*: outputs tipados y dependency injection, con mucho menos código | Contratos de datos estrictos — la validación **es** el punto, no una feature secundaria |

En Strands confías en que el modelo resuelva el camino — no lo estás trazando tú, le
entregas las tools y el destino. En LangGraph tú dibujas la estructura, y por eso puedes
parar en un punto, retomarlo después, o meter un paso de aprobación humana justo en el
medio. En Pydantic AI, si lo que más te importa es que el dato que vuelve tenga
exactamente la forma correcta, siempre, este es el framework construido alrededor de eso.

> 📌 Dos puntos que los conectan: los tres hablan **MCP** (domain 8) — sea cual sea el
> que elijas, todos se conectan a las tools de la misma manera estándar. Y los tres
> construyen tanto *workflows* como *agents* — no son herramientas solo para agents,
> también sirven para los workflows de pasos fijos de la lección 1.

## 3. El espectro completo

**Es un solo espectro, no cuatro mundos separados.**

| | Framework | Agent SDK | Managed Agents | Custom harness |
| --- | --- | --- | --- | --- |
| Código que escribes | Mínimo | Algo | Mínimo | Máximo |
| Dónde corre el loop | Tu proceso | Tu proceso | Anthropic | Tu proceso |
| Control | El modelo del framework | Estándar | Configurado | Total |
| Mejor para | Flujos estándar | Patrones comunes | Trabajo async de larga duración | Necesidades poco usuales |

La flecha corre en las dos direcciones: hacia un lado ganas velocidad y patrones ya
probados, hacia el otro ganas control, pero a costa de más trabajo. Es el mismo
trade-off que aparece una y otra vez en este curso — cada paso hacia más control se paga
en esfuerzo.

> ⚠️ Mira la fila "dónde corre el loop" con cuidado — es la que los separa de verdad.
> **Solo Managed Agents mueve el loop fuera de tu infraestructura.** Framework, Agent SDK
> y custom harness corren los tres en tus propias máquinas; Managed Agents es la única
> opción genuinamente distinta, y es la que responde a la pregunta "¿dónde corre?" de la
> lección anterior.

## 4. Cómo elegir

La regla no es "cuál framework es mejor", es **hacer encajar la forma del framework con
el problema**:

- Si el modelo debe decidir y tú quieres hacerte a un lado → **Strands**.
- Si necesitas un camino ramificado y controlado, con pausas y aprobación humana →
  **LangGraph**.
- Si lo que más importa son contratos de datos estrictos y validados → **Pydantic AI**.

Y si ninguna de esas formas encaja con lo que necesitas, existe una salida de emergencia:
bajar un nivel, al Agent SDK o al custom harness de la lección anterior. Un framework es
un buen default porque alguien ya resolvió el trabajo repetido — pero si la forma
genuinamente no encaja, ya sabes qué hay un nivel más abajo.

## Cierre del domain 1

Con esta lección se completa el domain 1. El recorrido: la pregunta de si tú decides
los pasos o los decide Claude ([[1-workflow-or-agent]]), el agent loop
*think → call tool → observe → repeat* ([[2-inside-the-agent-loop]]), la pizarra que se
llena y cómo manejarla con pruning, compaction y memory ([[3-context-and-memory]]), la
división del trabajo entre una manager y sus subagents
([[4-manager-pattern-and-subagents]]), la construcción con el Agent SDK, un harness
propio, o Managed Agents protegidos por hooks ([[5-building-agents-with-claude]]), y
ahora los frameworks que se sientan por encima de todo eso.

## Puntos clave

1. Los frameworks cambian control por velocidad.
2. Haz encajar la forma del framework con el problema, no busques "el mejor".
3. Baja al SDK (o al custom harness) cuando ninguna forma encaja.
