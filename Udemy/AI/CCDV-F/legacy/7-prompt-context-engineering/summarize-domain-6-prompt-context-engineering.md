# Domain 6: Prompt and Context Engineering

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 6: Prompt and Context Engineering**. Cubre cuatro
lecciones: cómo escribir un buen prompt, el uso de examples/templates/refinamiento
iterativo, context engineering (context rot, attention budget, RAG, just-in-time
context), y cómo hacer confiable el output del modelo.

## 1. Writing a Good Prompt

### ¿Qué es prompt engineering?

**Prompt engineering** es, en esencia, redactar la instrucción de forma que el modelo la
entienda bien a la primera.

| | Prompt vago | Prompt claro |
| --- | --- | --- |
| Ejemplo | `"Tell me about this."` | `"Summarise this in 3 bullets."` |
| Resultado | Respuesta genérica y pobre | Respuesta precisa y útil |

> 💡 Es la palanca más barata y más rápida que tienes: no requiere cambio de código ni
> cambio de modelo, solo palabras más claras.

### Las partes de un prompt

No todo prompt necesita las cuatro partes, pero conocerlas ayuda a diagnosticar qué falta
cuando una respuesta decepciona.

| Parte | Qué es |
| --- | --- |
| 📌 **Instruction** | Qué quieres que se haga |
| 📚 **Context** | El trasfondo que el modelo necesita |
| 💡 **Examples** | Mostrar el patrón (se profundiza en la Lección 2) |
| 📐 **Output format** | Cómo debe darse forma a la respuesta |

### Instrucciones claras y específicas

```text
❌ Vague:    "Write about dogs."
✅ Specific: "Write a 3-sentence beginner intro: why dogs make good pets."
```

La versión específica combina **tarea + longitud + audiencia + tono**; la vaga podría
significar cualquier cosa y obliga al modelo a adivinar.

> ⚠️ Vague in, vague out — el modelo rellena los huecos con su mejor suposición, que puede
> no coincidir con la tuya.

### Roles y system prompts

El **system prompt** fija el comportamiento estándar a lo largo de **toda** la
conversación, no solo para una pregunta puntual.

```text
system prompt: "You are a patient maths tutor for ten-year-olds."
→ palabras más simples, tono alentador, en cada respuesta
```

> 🔗 El rol de sistema ya apareció en Domain 2. La receta es: **rol primero, luego la
> tarea**.

### Formatear el output

```text
📄 Como párrafo:
"Dogs make good pets because they are loyal, and they also help
with exercise, plus…"

✅ "Answer in 3 bullet points":
• Loyal companions
• Encourage exercise
• Great for families
```

> 👤 Esta es la forma que lee una **persona**. La Lección 4 lleva esto un paso más allá,
> hacia la forma que parsea tu **código** (structured outputs).

## 2. Examples, Templates, and Refinement

### Los examples enseñan el patrón

```text
"Thanks so much!"   → friendly reply ✓
"This is broken."   → friendly reply ✓
Now: this new ticket → ?
```

> 💡 **Show, don't tell** — los examples enseñan el patrón más rápido que cualquier
> descripción.
>
> 🎯 Usa los mínimos examples que logren el resultado correcto.
>
> 🔗 Domain 5 ya cubrió zero-shot, single-shot y multi-shot prompting — esta lección es su
> uso práctico.

### Prompt templates — prompts reutilizables

Un **template** es un prompt con espacios en blanco que se rellenan en cada llamada,
reutilizando la misma estructura cuidadosamente diseñada.

```text
template (escrito una sola vez):
"Reply to {customer_name} about their {issue} in our friendly tone."

Rellenar los blanks con datos:
→ "Priya" + "late delivery"
→ "Sam" + "wrong item"
→ "Ana" + "refund"
```

### Por qué importan los templates

| Beneficio | Qué logra |
| --- | --- |
| 🎯 **Consistencia** | Cada request se formula de la misma forma probada, así las respuestas se mantienen uniformes |
| 🔧 **Un solo lugar para mejorar** | Arreglas el template una vez y todas las peticiones futuras se benefician |

> 🔗 Conecta con el prompt versioning de Domain 2 — el template es lo que versionas y
> puedes revertir (rollback).

### Refinamiento iterativo

Los prompts **no** son de "un solo intento": se escriben, se prueban, se revisan y se
ajustan, repitiendo el ciclo.

```text
✍️ Write → ▶️ Run → 👀 Check output → 🔧 Adjust → ↻ repeat
```

- ¿Demasiado largo? Añade `"keep it under 50 words."`
- ¿Demasiado formal? Añade `"casual tone."`

> 🎯 Trata el prompting como un proceso de afinamiento (tuning), no como una suposición de
> un solo disparo.

## 3. Context Engineering — Feeding the Model Right

### Prompt engineering vs context engineering

| | Prompt engineering | Context engineering |
| --- | --- | --- |
| Alcance | Redactar bien **una** instrucción | Decidir **todo** lo que el modelo ve en una llamada |
| Escala | Una frase (sentence) | Todo el pipeline |
| Incluye | — | `system prompt`, documentos recuperados, historial de conversación, definiciones de tools, memory almacenada |

> 📈 A medida que las apps crecen hacia agents, context engineering se vuelve la
> habilidad más importante.

### Context rot — más no es mejor

A medida que se llena la ventana de contexto, la precisión de recall **empeora**, y
empieza a degradarse **antes** de llegar al límite físico.

> 🤔 **Contraintuitivo**: se asumiría que más contexto siempre ayuda. No es así. A medida
> que crecen los tokens, la capacidad del modelo para recordar cualquier hecho concreto
> baja — y ese declive empieza antes de tocar el límite de tamaño.

> 📌 Meter todo hace que las respuestas empeoren, no que mejoren.

### El attention budget (presupuesto de atención)

Cada token que añades gasta un poco de un recurso limitado, como una **memoria de
trabajo** con capacidad finita.

> 🎯 El contexto es un recurso finito con retornos decrecientes — el objetivo es el
> conjunto **más pequeño** de tokens de alto valor, no el montón más grande. Recorta el
> contenido de bajo valor **antes** de que entre, no después.
>
> ✂️ Cómo **organizas** el contexto también importa: pon las instrucciones clave al
> principio y etiqueta con claridad cada documento, para que el modelo encuentre lo que
> necesita.

### Retrieval y RAG — traer solo lo necesario

```text
📚 500-page document store → 🔍 retriever → 📄 3 relevant chunks → ✅ into the prompt
```

> 📖 **RAG = Retrieval-Augmented Generation**: primero se busca, se extraen solo los pocos
> chunks relevantes, y solo esos se meten en el prompt.
>
> 🎯 Trae los 2 párrafos que responden la pregunta, no el manual entero. Es la respuesta
> directa al context rot.

### Just-in-time context

En vez de cargar todo por adelantado, se mantienen **referencias ligeras** y el
contenido real se carga solo en el momento en que se necesita.

| Referencias ligeras (lo que se guarda) | No se guarda |
| --- | --- |
| 📁 file paths | El contenido completo del archivo |
| 🔍 stored queries | El resultado completo de la query |
| 🔗 web links | La página web completa |

> 💻 **Claude Code funciona así**: ejecuta una query dirigida cuando se necesita, en vez de
> traer la base de datos entera al contexto.
>
> 🎯 Es la recomendación de Anthropic para agents de larga duración: cargar tarde, mantener
> la ventana ligera (lean).

## 4. Making Output Reliable

### Structured outputs — una forma predecible

| | Free text | Structured (JSON) |
| --- | --- | --- |
| Ejemplo | `"The customer Priya spent about 1,240 rupees on the 25th, I think…"` | `{"name": "Priya", "amount": 1240, "date": "2026-07-25"}` |
| Problema/ventaja | Tu código tiene que adivinar | Forma predecible que el programa puede parsear con confianza |

> 🔗 La Lección 1 cubrió la forma que lee una **persona**; aquí es la forma que parsea tu
> **código**. Los schemas se vieron en Domain 2.

### Validar lo que vuelve

Nunca confíes en el output a ciegas — revísalo mediante una **validation gate**.

```text
📨 Claude's response → 🚦 VALIDATION GATE (¿campos correctos? ¿tipos correctos? ¿todo presente?)
    → ✅ app usa la respuesta con seguridad
    → ❌ se captura la respuesta mala
```

> 🔗 El modelo es no determinista (Domain 5) — por eso validas en vez de asumir. Atrapa la
> respuesta mala antes de que la atrapen tus usuarios.

### Manejar refusals y errores con gracia

| | Qué es | Ejemplo |
| --- | --- | --- |
| 🚫 **Refusal** | El modelo declina la petición | `"I can't help with that."` |
| ⚠️ **Error** | Algo falló en la request | `429 / 529` (ver Domain 4) |

Hay que planear para ambos casos: capturarlo, mostrar un mensaje útil, reintentar si tiene
sentido, o recurrir a un valor por defecto seguro.

> 🎯 Frágil vs sólido = cómo se comporta tu app cuando las cosas **no** salen
> perfectamente.

### Técnicas de consistencia

| Técnica | Qué logra |
| --- | --- |
| Lower temperature | El modelo elige opciones más "seguras" |
| 📋 Strict schema | La forma no puede desviarse (drift) |
| 💡 Add examples | El estilo se mantiene uniforme (ya visto en la Lección 2) |
| 📐 One clear format | Sin ambigüedad |

> ⚖️ Ninguna técnica por sí sola lo hace perfectamente idéntico — pero juntas empujan el
> output hacia lo confiable y repetible.
>
> 🔗 El output varía de forma natural porque el modelo es no determinista — estas técnicas
> lo estabilizan.

## Puntos clave del dominio

- Prompt engineering es redactar bien **una** instrucción; context engineering decide
  **todo** lo que el modelo ve en la llamada (system prompt, documentos, historial, tools,
  memory) — a medida que las apps se vuelven agents, gana peso el segundo.
- Un prompt tiene partes (instruction, context, examples, output format) — no todas son
  siempre necesarias, pero conocerlas ayuda a diagnosticar respuestas pobres. Sé
  específico, dale un rol al modelo con el system prompt, y pide la forma de salida que
  quieres.
- Los examples enseñan el patrón más rápido que cualquier descripción (usa los mínimos que
  funcionen); los templates dan consistencia y un solo lugar para mejorar; el prompting es
  iterativo — escribir, correr, revisar, ajustar, repetir.
- **Context rot**: más tokens en la ventana degradan el recall, y esa degradación empieza
  antes del límite físico — el objetivo es el conjunto más pequeño de tokens de alto valor
  (attention budget), no el más grande, y organizarlo bien (instrucciones clave al
  principio, documentos etiquetados) también importa.
- **RAG** recupera solo los chunks relevantes de un corpus grande; **just-in-time context**
  guarda referencias ligeras (paths, queries, links) y carga el contenido real solo cuando
  se necesita — así trabaja Claude Code, y es la recomendación de Anthropic para agents de
  larga duración.
- Para un output confiable: usa structured outputs (JSON con schema) en vez de free text,
  valida siempre la respuesta antes de actuar sobre ella, planea para refusals y errores
  (429/529), y combina temperature baja, schema estricto, examples y un formato claro para
  empujar la consistencia — sin llegar nunca a ser perfectamente idéntica.
