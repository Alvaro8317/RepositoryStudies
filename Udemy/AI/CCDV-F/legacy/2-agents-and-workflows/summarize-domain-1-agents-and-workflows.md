# Domain 1: Agents and Workflows

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 1: Agents and Workflows**. Cubre seis lecciones:
Workflow o Agent, el agent loop por dentro, context y memory, el patrón manager/subagents,
cómo construir agentes con Claude, y los agentic frameworks del mercado.

## 1. ¿Workflow o Agent?

La pregunta central del dominio: **¿quién decide el siguiente paso — el desarrollador o el
modelo?**

- **Workflow**: el desarrollador escribe los pasos; Claude solo rellena el contenido de
  cada paso (ej. un mostrador de venta de billetes de tren con 4 ventanillas fijas en un
  orden que nunca cambia). Claude puede escribir el resumen del paso 3, pero nunca puede
  saltarse el paso 2 ni inventar un paso 5.
- **Agent**: el desarrollador da el objetivo y las tools; Claude decide el siguiente paso
  en tiempo de ejecución (como un conductor de auto-rickshaw que solo necesita el
  destino, no una ruta prescrita).

> ⚠️ La diferencia NO es "cuál es más inteligente" ni "cuál usa tools" — ambos usan tools.
> La única línea que importa es **dónde está el control**.

### Cuatro patrones de workflow

| Patrón           | Descripción                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| **Chaining**     | La salida de un paso alimenta el siguiente (Step 1 → Step 2 → Step 3). |
| **Routing**      | Se clasifica primero, luego se envía al handler correcto.              |
| **Parallel**     | Se ejecutan pasos independientes a la vez y luego se combinan.         |
| **Orchestrator** | Un paso planifica el trabajo y reúne los resultados de varios workers. |

### Workflow vs Agent, lado a lado

|                     | Workflow                     | Agent                          |
| ------------------- | ---------------------------- | ------------------------------ |
| Pasos decididos por | Tú, de antemano              | Claude, en tiempo de ejecución |
| Predecible          | Sí                           | No                             |
| Coste               | Conocido                     | Variable                       |
| Debugging           | Fácil                        | Más difícil                    |
| Mejor para          | Tareas repetidas y conocidas | Tareas abiertas (open-ended)   |

> ⚠️ Un agent puede necesitar 3 tool calls o 30 — esa imprevisibilidad de coste es una
> preocupación real de producción, no una nota al pie.

**Regla de examen: cuando ambos podrían funcionar, elige el workflow.** Antes de elegir,
pregúntate: ¿los pasos cambian según la petición?, ¿conoces todos los pasos de antemano?,
¿es aceptable un coste impredecible?

## 2. Dentro del Agent Loop

Un agent no es una caja mágica: es un **loop** que repite cuatro pasos hasta cumplir una
condición de parada.

```text
1. Claude piensa → 2. Llama a una tool → 3. El resultado vuelve → 4. El loop se repite
```

- **Paso 1 — Claude piensa**: razona sobre el goal, las tools disponibles y el historial,
  pero solo sobre **una cosa**: la siguiente acción inmediata, no el plan completo.
- **Paso 2 — Claude llama a una tool**: Claude solo *pide* ejecutar una tool; es tu código
  quien decide si se ejecuta. Ese hueco entre la petición y la ejecución (el
  **request-execute gap**) es donde viven las aprobaciones y los checks de seguridad.
- **Pasos 3 y 4 — el resultado vuelve y el loop se repite**: el resultado se añade al
  historial de mensajes, que crece en cada ciclo. Claude vuelve al paso 1 con más
  información, pero también con más contexto ocupado (tema de la siguiente lección).

> ⚠️ Un loop sin condición de salida corre — y factura — para siempre. Los agentes de
> producción **siempre** fijan un límite de iteraciones.

Un loop puede parar por tres motivos: se cumplió el goal, se alcanzó el límite de
iteraciones, o ocurrió un error irrecuperable.

### Tres formas de loop

| Forma                 | Cómo corre                | Cuándo usarla                       |
| --------------------- | ------------------------- | ----------------------------------- |
| **Single call**       | Sin loop                  | Una tool, una respuesta             |
| **Tool-use loop**     | Se repite hasta terminar  | Los pasos no se conocen de antemano |
| **Subagent dispatch** | Un loop lanza otros loops | Subtareas separables                |

> 📝 La mayoría de escenarios de examen piden elegir entre estas tres formas.

## 3. Context y Memory

El context window es como una **pizarra de tamaño fijo**: system prompt, historial de
conversación y tool outputs compiten por el mismo espacio, y cuando se llena, algo tiene
que ceder. La calidad se degrada **silenciosamente antes** de que algo falle de forma
visible.

### Dos fallos distintos: bloat y drift

|                  | Bloat                                                   | Drift                                                                                                                     |
| ---------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Tipo de problema | Volumen                                                 | Atención                                                                                                                  |
| Qué pasa         | El tool output basura desplaza lo que realmente importa | El objetivo original queda enterrado bajo turnos posteriores y el agente resuelve, sin darse cuenta, un problema distinto |
| Cómo se arregla  | Reduciendo lo que entra                                 | Re-anclando el goal                                                                                                       |

> ⚠️ Son problemas distintos con arreglos distintos — no tratarlos como uno solo.

### Dos arreglos

- **Prune tool output** (fix más barato y el más saltado): filtrar en tu código *antes*
  de que la respuesta llegue a la pizarra — de 500 líneas de JSON a los 3 campos que
  Claude realmente necesita.
- **Compaction**: resumir los turnos antiguos y mantener intactos los recientes (ej. 20
  turnos → 1 bloque de resumen que reemplaza 16 turnos + 4 turnos recientes completos).

> ⚠️ La compaction es *lossy* (con pérdida) — puede perder un detalle que sí importaba. Es
> un trade-off de detalle por espacio, no una operación gratuita.

### Context window vs Memory

|              | Context window (la pizarra)      | Memory (el archivador)            |
| ------------ | -------------------------------- | --------------------------------- |
| Persistencia | Se borra al final de cada sesión | Sobrevive tras terminar la sesión |
| Coste        | Cuesta tokens en cada llamada    | Solo cuesta al recuperar          |
| Contenido    | Lo que Claude tiene AHORA MISMO  | Lo que Claude puede ir a buscar   |

> 📌 La memory vive **fuera** del modelo — en un archivo o una base de datos. Esa es toda
> la idea.

El uso de memory tiene solo dos acciones: **escribir al salir** (guardar lo que vale la
pena recordar — una decisión, una preferencia, un resultado) y **leer al entrar** (traer
de vuelta solo las notas relevantes, no todo el archivador).

> ⚠️ Si lees todo el archivador de vuelta, reconstruyes el bloat que intentabas evitar.

## 4. Manager, Workers, Subagents

El **manager pattern**: un agente posee el plan (como una wedding planner), y otros
agentes ejecutan tareas concretas (caterer, decorator, photographer) sin ver el plan
completo.

Un **subagent** es un agente fresco, con su propia pizarra vacía y un trabajo estrecho.
Corre su propio agent loop, hace un solo trabajo y devuelve solo su respuesta — el
photographer nunca ve el menú del catering.

### Por qué los subagents mejoran los resultados

| Razón           | Qué logra                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| **Isolation**   | Un documento de 200 páginas se lee dentro del subagent; solo vuelve un párrafo — el manager se mantiene limpio |
| **Containment** | Un fallo se queda dentro de un subagent en lugar de contaminar toda la ejecución                               |
| **Speed**       | Subagents independientes corren en paralelo                                                                    |

> 📌 Tú defines la capacidad de paralelizar, pero es **Claude** quien decide cuándo
> paralelizar de verdad — no estás escribiendo el calendario de ejecución.

### Single agent vs Manager + subagents

|                     | Single agent               | Manager + subagents          |
| ------------------- | -------------------------- | ---------------------------- |
| Contexto por unidad | Todo                       | Solo lo necesario            |
| Trabajo en paralelo | No                         | Sí                           |
| Coste en tokens     | Menor                      | Mayor                        |
| Complejidad         | Baja                       | Mayor                        |
| Mejor para          | Tareas simples y estrechas | Tareas amplias y multi-parte |

> ⚠️ Los subagents no son gratis: pagas los tokens del manager **más** los de cada
> subagent. Nunca presentes este patrón como automáticamente mejor.

**Cuándo añadir un manager**: solo cuando las subtareas son genuinamente independientes,
el contexto de un solo agente se desborda, o la velocidad en paralelo importa de verdad.
No lo añadas para una tarea simple de tres pasos, con pasos dependientes entre sí, o
cuando el coste en tokens es la preocupación principal.

## 5. Building Agents with Claude

Antes de construir, hay tres decisiones que aparecen en el examen:

1. **Con qué construir**: Claude Agent SDK, o escribir el loop tú mismo.
2. **Dónde corre**: tu propio proceso, o la infraestructura de Anthropic.
3. **Cómo mantenerlo seguro**: hooks que *imponen*, en vez de prompts que *piden*.

### Claude Agent SDK

> ⚠️ Error común de principiante: el Agent SDK **no** es un framework de agentes
> genérico. Es **Claude Code empaquetado como librería** (disponible en Python y
> TypeScript), con el mismo agent loop y gestión de contexto que usa Claude Code, y con
> tools ya integradas (Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch) sin
> necesidad de implementar la ejecución de tools tú mismo.

### Escribir el loop tú mismo

Un harness propio implementa el mismo while-loop de la Lección 2, a mano:

```python
while not done:
    response = client.messages.create(...)
    if response.stop_reason == "tool_use":
        result = run_my_tool(response)
        # enviar el resultado de vuelta y volver a llamar
    else:
        done = True
```

|                       | Agent SDK               | Custom harness       |
| --------------------- | ----------------------- | -------------------- |
| Quién escribe el loop | Anthropic               | Tú                   |
| Tools integradas      | Incluidas               | Las construyes tú    |
| Tiempo de desarrollo  | Rápido                  | Lento                |
| Control               | Comportamiento estándar | Total                |
| Mejor para            | Patrones comunes        | Requisitos inusuales |

> 🎯 Muévete a un custom harness solo cuando puedas **nombrar** lo específico que el SDK
> no te deja hacer (retries a medida, tus propios approval gates, tu propio logging).
> "Quiero más control" no es una respuesta que el examen premia.

### Dónde corre el agente: Agent SDK vs Managed Agents

|                     | Agent SDK                            | Managed Agents                            |
| ------------------- | ------------------------------------ | ----------------------------------------- |
| Quién corre el loop | Tu proceso                           | Anthropic                                 |
| Interfaz            | Librería Python / TypeScript         | REST API                                  |
| Dónde corre         | Tu infraestructura                   | Sandbox en la nube, o sandbox self-hosted |
| Estado de la sesión | Tu filesystem                        | Event log alojado por Anthropic           |
| Mejor para          | Trabajo local, tus propios servicios | Producción async de larga duración        |

> ⚠️ **Matiz clave de examen**: self-hosted es una opción **dentro** de Managed Agents,
> no lo opuesto a él. Los escenarios de residencia de datos apuntan a ese ajuste de
> sandbox.
>
> Managed Agents está en **beta**. Como las sesiones son stateful por diseño, actualmente
> **no** es elegible para Zero Data Retention ni cobertura HIPAA.

### Hooks — seguridad determinista

Un hook es código que **siempre** se ejecuta, sin juicio del modelo de por medio (como la
válvula de una olla a presión: no "piensa" si liberar vapor, simplemente lo hace, cada
vez). El evento `PreToolUse` se dispara **antes** de que la tool corra y puede
bloquearla.

Eventos de hook nombrados: `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`,
`SessionEnd`, `UserPromptSubmit`.

> 🔑 Un prompt le **pide** a Claude amablemente. Un hook **impone**. La palabra
> "deterministic" es la señal de examen.

## 6. Agentic Frameworks

Los frameworks existen porque distintos equipos, sin ellos, reconstruyen el mismo loop,
los mismos retries y el mismo manejo de estado una y otra vez. Un framework escribe ese
trabajo una sola vez, para todos.

### Los tres que hay que conocer

| Framework      | Enfoque      | Rasgo distintivo                                                                                              |
| -------------- | ------------ | ------------------------------------------------------------------------------------------------------------- |
| **Strands**    | Model-driven | Le das tools y un goal, y te apartas; el modelo decide. Optimizado para AWS Bedrock.                          |
| **LangGraph**  | Graph-driven | Tu agente es una máquina de estados con pasos de LLM; permite pause, resume, checkpoints y aprobación humana. |
| **PydanticAI** | Type-driven  | Salidas tipadas e inyección de dependencias, con mucho menos código; la validación es el punto central.       |

> 🔌 Los tres hablan **MCP** (Model Context Protocol, ver Domain 8). Y ojo con el
> wording del blueprint: estos frameworks construyen tanto workflows como agents.

### El espectro completo

|                     | Framework        | Agent SDK        | Managed Agents          | Custom harness        |
| ------------------- | ---------------- | ---------------- | ----------------------- | --------------------- |
| Código que escribes | Menos            | Algo             | Menos                   | Más                   |
| Dónde corre el loop | Tu proceso       | Tu proceso       | El de Anthropic         | Tu proceso            |
| Control             | El del framework | Estándar         | Configurado             | Total                 |
| Mejor para          | Flujos estándar  | Patrones comunes | Async de larga duración | Necesidades inusuales |

> 🔍 Solo **Managed Agents** mueve el loop fuera de tu infraestructura — esa es la fila
> que realmente separa a los cuatro.

## Puntos clave del dominio

- Workflow = tú decides los pasos; Agent = Claude decide en runtime. Ante la duda, elige
  workflow.
- Un agent es un loop: pensar, llamar a una tool, observar, repetir — con un límite de
  iteraciones siempre fijado.
- El context window es caro y es "ahora"; la memory es barata y es "después" — poda el
  tool output antes de que llegue a la pizarra.
- El manager planea, los subagents ejecutan con contexto fresco — pero solo divide el
  trabajo cuando es genuinamente separable.
- El Agent SDK corre en tu proceso; Managed Agents corre en el de Anthropic; los hooks
  imponen seguridad de forma determinista, no negociable por el modelo.
- Los frameworks (Strands, LangGraph, PydanticAI) cambian control por velocidad — elige
  según la forma del problema, y cae al SDK cuando ninguno encaja.
