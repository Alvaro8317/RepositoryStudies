# Domain 4: Eval, Testing, and Debugging

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 4: Eval, Testing, and Debugging**. Este dominio es el
más pequeño del curso (una sola clase, de unos 8 minutos) y cubre una única lección:
**cómo depurar (debug) una app construida sobre Claude cuando algo falla**.

## 1. When Things Go Wrong — Debugging Claude Apps

*In this lecture: identificar el tipo de error, averiguar de dónde viene el problema,
leer el trace, y elegir cómo recuperarse.*

### El instinto correcto: clasificar antes de arreglar

> 💥 **Instinto de principiante**: empezar a cambiar cosas al azar.
> 🔧 **Instinto profesional**: parar y clasificar primero.

El proceso de debugging tiene cuatro pasos, siempre en este orden: **Type → Origin →
Trace → Recover**.

### Paso 1 — Identificar el tipo de error

No todos los errores significan lo mismo, aunque en un log se vean parecidos ("la
request no pasó"):

| Código  | Nombre      | Significado                                               |
| ------- | ----------- | --------------------------------------------------------- |
| **429** | Rate limit  | TU cuenta envió demasiadas requests                       |
| **529** | Overloaded  | El servicio está saturado — no tiene nada que ver contigo |
| **400** | Bad request | Tu propia request estaba mal formada                      |

> 🔍 Leer el tipo exacto de error es donde empieza el debugging de verdad.

### Paso 2 — ¿De dónde vino el problema?

La pregunta clave: ¿es tu código alrededor de Claude, o es lo que Claude produjo?

|         | Integration layer (la plumbing)                     | Model output (la respuesta)     |
| ------- | --------------------------------------------------- | ------------------------------- |
| Qué es  | Tu código · la red · una llamada mal hecha a la API | Lo que Claude realmente produjo |
| Ejemplo | `429` → tu código envió demasiadas requests         | JSON con un campo faltante      |

> 🎯 La idea más importante de la lección: siempre pregúntate — ¿es mi plumbing, o es la
> respuesta? Arreglar la capa equivocada malgasta horas.

Para saber en qué capa está el fallo, hay que leer el trace — el siguiente paso.

### Paso 3 — Leer el trace

Hay que seguir el registro paso a paso para encontrar exactamente dónde falló:

```text
Request → Tool call → Tool result → Response
                          ❌ (ejemplo: se rompió aquí)
```

Preguntas guía al recorrer el trace: ¿la tool nunca se llamó?, ¿la tool devolvió datos
malos?, ¿Claude interpretó mal un resultado que en realidad era correcto?

> 🔍 Ese paso exacto donde se rompió es el **failure mode** — la forma específica en que
> este sistema falla. Nombrarlo apunta directamente a la solución.

### Paso 4 — Elegir cómo recuperarse

La solución debe ajustarse al tipo de error diagnosticado, no ser siempre la misma:

| Estrategia          | Cuándo aplica                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Retry**           | `529` overloaded → exponential backoff (es temporal, no es culpa tuya). `429` rate limit → esperar exactamente el tiempo indicado en `retry-after`. |
| **Fix the request** | Un `400` o un schema mal formado — reintentar no sirve de nada; hay que arreglar la request misma.                                                  |

> 🎯 La habilidad central es hacer coincidir la recuperación con el diagnóstico — no
> reintentar a ciegas.

## Puntos clave del dominio

- Clasifica antes de arreglar: **type → origin → trace → recover**, siempre en ese orden.
- Distingue **integration layer** (tu código) de **model output** (la respuesta de
  Claude) — aislar en qué capa está el problema evita perder horas arreglando lo que no es.
- Ajusta la recuperación al error: reintenta las sobrecargas temporales (`529`, `429`),
  pero arregla directamente las requests malformadas (`400`) — reintentarlas no soluciona nada.
