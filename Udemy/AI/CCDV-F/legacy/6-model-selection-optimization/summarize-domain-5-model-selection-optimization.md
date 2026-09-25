# Domain 5: Model Selection and Optimization

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 5: Model Selection and Optimization** (40 diapositivas).
Cubre cinco lecciones: cómo funcionan realmente los LLMs por dentro, los modos de thinking y
las bases del prompting, la ingeniería debajo del SDK y la REST API, cómo elegir entre
Opus/Sonnet/Haiku, y cómo gestionar tokens y coste.

## 1. How LLMs Actually Work

### Tokens — las piezas que el modelo lee

Un modelo no lee palabras, lee **tokens**: fragmentos de palabras. `"Claude is helpful"` se
divide en 4 tokens: `Claude`, `is`, `help`, `ful` — "helpful" por sí sola ya son dos tokens.

> 💰 Importa porque **pagas por token**, y el context window se mide en tokens, no en
> palabras.
>
> 📏 Regla aproximada: **1 token ≈ 4 caracteres** de inglés.

### El context window — el escritorio del modelo

El context window es **todo lo que el modelo puede ver a la vez**: el escritorio, de tamaño
fijo y medido en tokens.

- 📋 System prompt — tus instrucciones.
- 💬 Conversación hasta el momento.
- 📄 Cualquier documento que hayas añadido.
- 📐 Fijo y finito: los modelos de Claude actuales tienen ventanas muy grandes, pero siguen
  siendo finitas.

> 🔗 Es la misma idea de la "pizarra" del Domain 1 — ahora con nombre y número: el context
> window = todo lo que el modelo puede ver en una sola request.

### Next-token generation — una pieza a la vez

El modelo predice el siguiente token, una y otra vez, realimentando cada resultado:

```text
"The sky is ___"        → predice "blue"
"The sky is blue ___"    → predice "and"
"The sky is blue and ___" → predice "clear"
```

> 🔁 Un párrafo entero no es más que este loop repetido. No hay un plan escrito de
> antemano — la respuesta emerge token a token.

### Sampling — eligiendo el siguiente token

El modelo no siempre elige la opción con más probabilidad. Cada paso genera una lista
ranqueada de candidatos:

| Candidato | Probabilidad |
| --- | --- |
| blue | 62% |
| grey | 21% |
| clear | 11% |
| dark | 6% |

**Temperature**: controla cuánto se aleja el modelo del candidato top.

- **Baja** → casi siempre el candidato top (predecible).
- **Alta** → más variedad (creativo).

> 🎯 El sampling es el mecanismo que elige uno de esa lista ranqueada.

### Non-determinism — por qué las respuestas varían

Un mismo prompt puede producir respuestas ligeramente distintas cada vez, por el sampling.

> ✅ Esto es normal, **no es un bug**.
>
> 🧪 Por eso testear una app de Claude es distinto a testear código tradicional. Una
> temperature más baja da más consistencia — pero rara vez una salida perfectamente
> idéntica.

### Key Takeaways — How LLMs Actually Work

1. Los tokens son fragmentos de texto — pagas y mides en tokens, no en palabras.
2. El context window es todo lo que el modelo ve a la vez, de tamaño fijo.
3. Los modelos escriben un token a la vez; el sampling hace que el mismo prompt varíe.

## 2. Thinking Modes and Prompting Basics

### Fast mode — responder directamente

El modo por defecto: sin paso de razonamiento extra, respuesta directa (`PROMPT` → `ANSWER`).

> 🏃 Correcto para la mayoría de tareas cotidianas — un resumen, una reescritura, una
> pregunta simple.
>
> ⚡ Sin paso de razonamiento extra = menor latency y menor coste. Recurre a más solo
> cuando la tarea es genuinamente difícil.

### Extended thinking — mostrar el trabajo

Razona primero, responde después: `HARD PROMPT` → `SCRATCHPAD` (razona paso a paso) →
`BETTER ANSWER`.

> 🧠 Para matemáticas complicadas, lógica multi-paso, planificación cuidadosa — el modelo
> razona antes de responder.
>
> ⚖️ Mejora la calidad en tareas difíciles — pero usa más tokens y tarda más. Es una
> decisión deliberada, no algo que se deja siempre activado.

### Adaptive thinking y effort levels

El modelo decide por sí mismo cuánto pensar; tú fijas el **effort**:

```text
low → medium → high → xhigh → max
más rápido/barato  ←————————————→  más razonamiento, trabajo más difícil
```

> 🤖 Adaptive thinking = el modelo decide por su cuenta cuándo una pregunta necesita
> pensamiento profundo y cuándo basta una respuesta rápida. Ya no fijas un thinking
> budget manual en tokens — solo diriges con el effort, de low a max.
>
> 📌 Esto reemplazó al antiguo thinking budget manual — importa conocer ambos, porque el
> examen nombra los dos.

### Zero-shot prompting — solo preguntar

El prompt completo es la instrucción, sin ejemplos:

```text
"Classify this review as positive or negative."
```

> 🧠 Cero ejemplos — el modelo se apoya solo en lo que ya sabe.
>
> 🎯 El enfoque más simple, y a menudo suficiente — pruébalo siempre primero.

### Single-shot y multi-shot — mostrar ejemplos

| Técnica | Cómo funciona | Trade-off |
| --- | --- | --- |
| **Single-shot** | Un ejemplo resuelto antes de la tarea real (`"Great!" → positive`, luego `"Terrible." → ?`) | Fija el patrón con un solo caso |
| **Multi-shot** | Varios ejemplos (`"Great!" → positive`, `"Awful." → negative`, `"Okay." → neutral`) | Más consistente, pero más tokens |

> 🎯 La habilidad está en usar el **menor número de ejemplos** que logre el resultado.

### Key Takeaways — Thinking Modes and Prompting

1. Fast mode para la mayoría de tareas; extended thinking para las genuinamente difíciles.
2. Adaptive thinking deja que el modelo decida la profundidad — tú diriges con effort
   (low → max).
3. Zero-shot primero; añade ejemplos (single/multi-shot) solo cuando necesites fijar el
   patrón.

## 3. The Engineering Underneath

### El SDK — un wrapper amigable

Un SDK es un toolkit para no escribir HTTP a mano:

```text
😰 REST puro:
POST /v1/messages
headers: { x-api-key, anthropic-version… }
body: JSON.stringify({ model, messages… })

😌 SDK:
client.messages.create(model, messages)
```

Disponible en 🐍 Python y 🟦 TypeScript.

> 🧰 Un SDK envuelve la REST API del Domain 2 — llamas a una función limpia en vez de
> construir requests a mano.

### Qué resuelve el SDK por ti

| Función | Qué hace |
| --- | --- |
| 🔑 **Authentication** | Adjunta tu API key |
| 🔁 **Retries with backoff** | Reintenta automáticamente las requests fallidas |
| 📖 **Error parsing** | Convierte errores en mensajes legibles |
| 🌊 **Streaming** | Gestiona el flujo de tokens en vivo |

> 🔗 ¿Recuerdas los códigos 429 y 529 del Domain 4? El retry incorporado del SDK maneja
> muchos de esos casos sin que escribas una sola línea.
>
> ✅ Esa es la razón para usar un SDK en vez de REST puro.

### Debajo, sigue siendo REST

`client.messages.create()` se convierte en la misma request REST: `POST /v1/messages`.

> ⚠️ Error común de principiante: el SDK está **encima** de la REST API — toda llamada se
> convierte en una request REST por debajo.
>
> 🔗 Todo lo que aprendiste sobre messages, tools y JSON sigue aplicando. Si el SDK no
> puede hacer algo, baja a REST puro.

### Websockets — mantener la línea abierta

| | REST (vía SDK) | Websocket |
| --- | --- | --- |
| Forma | ✉️ Carta: preguntas, recibes respuesta, la conexión se cierra. Se repite por cada mensaje | 📞 Llamada telefónica: una línea continua bidireccional que permanece abierta |
| Mejor para | Casi todo | Interacción en tiempo real, bidireccional |
| Latency | Adecuada para la mayoría de casos | La más baja, persistente |
| Úsalo cuando | Quieres una respuesta | Necesitas un stream en vivo |

> 🎯 La mayor parte del tiempo es REST. Recurre a un websocket solo cuando construyes algo
> genuinamente en vivo (voz en tiempo real, streaming continuo).

### Key Takeaways — The Engineering Underneath

1. Un SDK envuelve la REST API para que llames a una función limpia, no HTTP puro.
2. Gestiona auth, retries, errores y streaming — pero sigue siendo REST por debajo.
3. Los websockets mantienen una línea abierta para trabajo en tiempo real; REST cubre casi
   todo lo demás.

## 4. Choosing Your Model — Opus, Sonnet, Haiku

### Tres tiers, una misma familia

| Modelo | Perfil | Uso típico |
| --- | --- | --- |
| ⚡ **Haiku** | El más rápido y barato | Construido para alto volumen |
| ⚖️ **Sonnet** | El equilibrio intermedio | Fuerte en la mayoría de tareas, precio moderado |
| 🧠 **Opus** | El más capaz | Para los problemas genuinamente difíciles |

> 👨‍👩‍👧 Misma familia, mismo formato de mensajes. Se diferencian en cuán capaces, cuán
> rápidos y cuán costosos son (Haiku → Sonnet → Opus: más capacidad, menos velocidad y
> menor coste marginal en sentido inverso).

### El triángulo de trade-off

Tres vértices en tensión: ⭐ **Quality**, ⚡ **Latency (speed)**, 💰 **Cost**.

- 🧠 **Opus**: calidad top, más lento, más caro.
- ⚖️ **Sonnet**: el punto medio.
- ⚡ **Haiku**: el más rápido y barato, el menos capaz.

> 🎯 No existe el "mejor" modelo — solo el que mejor encaja con lo que tu tarea realmente
> necesita.

### ¿Qué modelos pueden pensar en profundidad?

| Modelo | Extended / adaptive thinking |
| --- | --- |
| Opus | ✔ Sí |
| Sonnet | ✔ Sí |
| Haiku | ✘ No thinking profundo |

> ⚠️ Si tu tarea necesita razonamiento multi-paso cuidadoso, Haiku no es la opción, sin
> importar lo barato que sea. Es una diferencia de **capacidad**, no solo de precio — y el
> examen lo señala específicamente.

### Cómo elegir — una regla simple

```text
DEFAULT: SONNET → maneja la mayoría del trabajo
  ↓ baja a HAIKU si: tarea de alto volumen y simple (tagging, routing, clasificación)
  ↑ escala a OPUS si: Sonnet genuinamente falla en el razonamiento
```

> 🎯 No pagues por Opus por defecto — y no le pongas una tarea difícil a Haiku.

### Breaking changes entre releases

Un modelo nuevo puede comportarse distinto — hay que re-evaluar: `Model v1 (ya testeado)`
→ `re-evaluate` → `Model v2 (puede diferir)`.

> 🔄 Cuando sale un modelo nuevo, re-evalúa: ¿una tarea que necesitaba Opus ahora corre en
> Sonnet? (Incluso la tokenización puede cambiar, moviendo el coste.)
>
> 🔗 Por esto PINEAS la versión del modelo (Domain 2) — para que un release no cambie el
> comportamiento sin que tú lo decidas.

### Key Takeaways — Choosing Your Model

1. Haiku = rápido/barato, Sonnet = default equilibrado, Opus = tareas más difíciles.
2. Elegir es un balance de quality/latency/cost — y Haiku no puede hacer thinking profundo.
3. Sonnet por defecto; re-testea cuando salen modelos nuevos; pinea tu versión.

## 5. Managing Tokens and Cost

### De dónde viene el coste

Pagas por token, tanto en entrada como en salida:

| Tipo | Qué incluye |
| --- | --- |
| 📥 **Input tokens** | Tu prompt, documentos y el historial de conversación |
| 📤 **Output tokens** | Lo que Claude escribe — normalmente cuesta **más** por token que el input |

> 💰 Tu factura = cuánto envías + cuánto escribe Claude + qué modelo elegiste. Entender
> esto es la base de todo control de coste.

### Rastrea tu uso

Cada respuesta reporta su conteo de tokens:

```json
"usage": {
  "input_tokens": 1240,
  "output_tokens": 385
}
```

> 📝 Registrar (loggear) estos números muestra qué requests son caras y dónde optimizar.
>
> ✅ No tienes que adivinar cuánto estás gastando.
>
> 🎯 No puedes gestionar un coste que no estás midiendo.

### Modela tu coste antes de construir

```text
tokens por request × requests por día × precio del modelo = coste mensual
```

> 📐 Hazlo **ANTES** de escalar, no después de la factura. Te dice si tu diseño es
> asequible.
>
> 💡 También muestra si un modelo más barato o prompts más cortos te mantendrían dentro
> del presupuesto. Un modelo aproximado vence a una factura sorpresa.

### Prompt caching — reutiliza la parte cara

Un system prompt grande / documento de referencia se guarda una vez → se mantiene listo en
la **CACHE** → se reutiliza. Las lecturas posteriores cuestan una **fracción** del input
fresco.

> 🔗 Conociste el caching en el Domain 2 — aquí está el porqué: es la **primera** palanca
> de coste a la que recurrir.
>
> ⭐ Si tu app reenvía el mismo contexto a menudo, esta es la optimización de mayor
> impacto que tienes disponible.

### El orden de optimización de costes

| Orden | Palanca | Qué hace |
| --- | --- | --- |
| 1 | **Cache** | Reutiliza contexto repetido |
| 2 | **Batch** | Agrupa trabajo no urgente (~50% de descuento) |
| 3 | **Shorten prompts** | Recorta lo que envías |
| 4 | **Downgrade model** | Solo como último recurso |

> 📌 Corta el desperdicio antes de cortar inteligencia.
>
> 📌 Refinamiento de caching: **cache checkpointing** marca puntos en un prompt largo y
> creciente para que las partes estables anteriores sigan en cache mientras la
> conversación se extiende.

### Key Takeaways — Managing Tokens and Cost

1. Pagas por token, input y output — el output normalmente cuesta más.
2. Rastrea el uso desde la respuesta; modela tu coste antes de escalar.
3. Cachea y batchea primero, acorta prompts después, degrada el modelo al final.

## Puntos clave del dominio

- Un LLM piensa en **tokens**, no en palabras; el context window es un escritorio finito
  medido en tokens, y la generación es token a token con sampling — por eso el mismo
  prompt puede variar (temperature baja = más predecible, alta = más variedad).
- Hay tres formas de pensamiento: **fast mode** por defecto, **extended thinking** para
  tareas genuinamente difíciles, y **adaptive thinking** donde tú fijas el effort
  (low → max) y el modelo decide cuánto razonar.
- En prompting, empieza siempre con **zero-shot**; añade ejemplos (**single-shot** /
  **multi-shot**) solo cuando necesites fijar el patrón, usando el menor número posible.
- El **SDK** envuelve la REST API (auth, retries, error parsing, streaming) pero sigue
  siendo REST por debajo; usa **websockets** solo para trabajo genuinamente en tiempo
  real — REST cubre casi todo lo demás.
- Elige entre **Haiku, Sonnet y Opus** según el triángulo quality/latency/cost: Sonnet por
  defecto, Haiku para alto volumen simple, Opus solo cuando Sonnet falla en el
  razonamiento — y recuerda que Haiku no soporta thinking profundo.
- Pinea la versión del modelo y re-evalúa al salir releases nuevos, porque pueden traer
  breaking changes de comportamiento o de tokenización.
- Gestiona el coste midiendo `usage` en cada respuesta y modelando el coste mensual antes
  de escalar; el orden de optimización es **cache → batch → shorten prompts → downgrade
  model**, nunca al revés.
