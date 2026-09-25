# Building Agents with Claude

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: de la teoría a la práctica

Hasta aquí hemos venido aprendiendo qué son los agents y cómo se comportan — el loop, el
context, el manager pattern y los subagents. Esta lección se vuelve práctica: cómo
construirlos de verdad con Claude.

## 1. Tres decisiones antes de construir

Todo lo que sigue se reduce a tres decisiones:

1. **Qué usar**: el Claude Agent SDK, o escribir el loop tú mismo.
2. **Dónde corre**: tu propio proceso, o la infraestructura de Anthropic.
3. **Cómo mantenerte seguro**: hooks que **enforcean** (obligan), no prompts que piden.

> 📌 Fíjate en esa última palabra — *enforce* versus *ask* — porque marca hacia dónde va
> toda la lección. Son dos cosas muy distintas, y las tres decisiones son examinables.

## 2. Qué usar: el Claude Agent SDK

**Claude Code empaquetado como librería.**

La analogía es una cocina ya equipada, con los electrodomésticos instalados. Y la
explicación clave: **no es una librería genérica de agents**. Es Claude Code en sí mismo,
empaquetado para que tu código lo maneje en vez de una persona en una terminal. Viene en
Python y TypeScript, y corre el mismo agent loop y el mismo manejo de context que le dan
poder a Claude Code.

Trae herramientas ya construidas — no hay que implementar la ejecución de tools:

`Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `WebSearch`, `WebFetch` (ocho en total).
El resultado: el agent arranca a trabajar de inmediato, en vez de tener que escribir y
probar cada una de esas tools antes de que el agent pueda hacer algo.

> ⚠️ **Punto examinable donde los principiantes se equivocan**: el Agent SDK no es un
> framework genérico de agents. El nombre suena genérico — "agent SDK" suena a un kit
> para construir cualquier tipo de agent, de cualquier estilo. No lo es. Es una cosa
> específica: Claude Code, envuelto para que tu código lo maneje.

## 3. Escribir el loop tú mismo (custom harness)

### ¿Qué es un harness?

*Harness* se traduce al español como **arnés**, el mismo término que se usa en testing para
un *test harness* ("arnés de pruebas"). En el contexto de agents, el harness es **todo el
código que envuelve al modelo y lo conecta con el mundo real**.

La analogía es el arnés de un caballo: el caballo pone la fuerza, pero es el arnés el que
la canaliza hacia la carreta y permite dirigirla. Aquí pasa lo mismo: Claude razona y
decide qué tool quiere usar, pero **por sí solo no ejecuta nada**, solo devuelve texto o
una solicitud de `tool_use`. El harness es el que:

1. **Llama** a la API con el historial de mensajes y las tools disponibles.
2. **Revisa** si Claude pidió usar una tool (`stop_reason == "tool_use"`).
3. **Ejecuta** esa tool de verdad (leer un archivo, consultar una base de datos, llamar a
   una API...).
4. **Devuelve** el resultado a Claude como un bloque `tool_result`.
5. **Repite** hasta que Claude termina o se cumple alguna condición de corte (ej. un
   máximo de iteraciones).

Todo agent tiene un harness: Claude Code tiene el suyo, y el Agent SDK te entrega ese
mismo harness ya construido. Un **custom harness** (o "harness propio") es simplemente
cuando ese código lo escribes tú.

> 💡 En español se puede decir "arnés", pero en la documentación, en la industria y en el
> examen se usa el término en inglés, *harness*. Piénsalo como "el código orquestador que
> rodea al modelo".

### El loop en código

**Llamar, revisar si hay tool use, ejecutar, y volver a llamar.**

```python
while not done:
    response = client.messages.create(...)
    if response.stop_reason == "tool_use":
        result = run_my_tool(response)
        # se envía el resultado de vuelta y se llama de nuevo
    else:
        done = True
```

Ese `while` es el harness. Es el mismo loop de la lección 2 — *call tool, observe,
repeat* — pero aquí está escrito como código real, no es un mecanismo nuevo.

Con un harness propio, **tú** implementas el tool loop. Con el Agent SDK, el SDK lo
maneja por ti.

¿Cuándo escribir el harness? Cuando necesitas retries a medida, tus propios approval
gates, o tu propio logging. Las tres son necesidades puntuales que el comportamiento
estándar no te da — no es insatisfacción general.

> 📌 Ese `if response.stop_reason == "tool_use":` es literalmente el gap de la lección
> 2 hecho código: el momento donde tu código se para entre la solicitud de Claude y la
> ejecución real de la tool. En la lección 2 era una caja en un diagrama; aquí es una
> línea de tu programa.

## 4. Agent SDK vs. custom harness: cómo elegir

**Por defecto, el Agent SDK — cambiar solo por una razón nombrable.**

|                        | Agent SDK               | Custom harness              |
| ---------------------- | ----------------------- | --------------------------- |
| Quién escribe el loop  | Anthropic               | Tú                          |
| Tools incorporadas     | Incluidas               | Las construyes tú           |
| Tiempo de construcción | Rápido                  | Lento                       |
| Control                | Comportamiento estándar | Control total               |
| Mejor para             | Patrones comunes        | Requerimientos poco usuales |

> ⚠️ La regla es precisa: **moverse a un custom harness solo cuando puedes nombrar lo
> específico que el SDK no te deja hacer.** "Quiero más control" no es una respuesta — el
> examen premia poder señalar algo concreto (retries a medida, tus propios approval
> gates, tu propio logging), no control en general.

## 5. Dónde corre tu agente: Agent SDK vs. Managed Agents

|                     | Agent SDK                             | Managed Agents                     |
| ------------------- | ------------------------------------- | ---------------------------------- |
| Quién corre el loop | Tu proceso                            | Anthropic                          |
| Interfaz            | Librería Python o TypeScript          | REST API                           |
| Dónde corre         | Tu infraestructura                    | Sandbox en la nube, o self-hosted  |
| Estado de la sesión | Tu file system                        | Event log hosteado por Anthropic   |
| Mejor para          | Trabajo local y tus propios servicios | Producción async de larga duración |

> ⚠️ **Trampa examinable**: self-hosted es una opción *dentro* del producto managed, no
> lo opuesto a él. Un escenario de residencia de datos ("los datos deben quedarse en tal
> país") apunta a ese setting del sandbox, no a abandonar Managed Agents por completo.

Dos datos más:

- Managed Agents está en **beta**.
- Como las sesiones son *stateful* por diseño, **no es elegible** para zero data
  retention ni para cobertura HIPAA — la limitación se sigue directamente del diseño: lo
  que hace útil a Managed Agents (mantener el estado de la sesión) es justo lo que
  restringen esos dos regímenes de compliance.

## 6. Hooks: seguridad determinística

**Código de seguridad determinístico que siempre corre, sin juicio del modelo de por
medio.**

La analogía: la válvula de una olla a presión no piensa si liberar vapor o no. Lo hace,
siempre, por encima de cierta presión.

Este es el gap de la lección 2, ahora con un hook adentro: Claude pide una tool → un
`PreToolUse` hook intercepta → bloquea el `delete file`. El hook corre **antes** de que
la tool se ejecute, y puede bloquearla.

Los hook events son seis, y cubren toda la vida de una sesión:

- `PreToolUse`
- `PostToolUse`
- `Stop`
- `SessionStart`
- `SessionEnd`
- `UserPromptSubmit`

> ⚠️ **La señal del examen**: pedirle algo a Claude "amablemente" en el prompt es un
> *request* — Claude casi seguro lo va a seguir, pero no está garantizado. Un
> `PreToolUse` hook es código, y corre siempre, exactamente como ese `while`. Cuando una
> pregunta usa la palabra **deterministic** o dice que algo "debe estar garantizado",
> está apuntando a un hook.

## Puntos clave

1. El **Agent SDK** corre en tu propio proceso.
2. **Managed Agents** corre en la infraestructura de Anthropic.
3. Hookea **cada** acción destructiva — no la mayoría, no solo las que parecen riesgosas,
   todas.
