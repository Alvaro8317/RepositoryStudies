# Inside the Agent Loop

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: un agent es un loop, no una caja mágica

La lección anterior estableció que un agent es el sistema donde Claude decide los pasos.
Esta lección abre esa caja: un agent es, literalmente, un **loop** de cuatro pasos que se
repite hasta que se cumple una condición de parada:

```text
1. Claude piensa → 2. Llama a una tool → 3. El resultado vuelve → 4. El loop se repite
```

> 📌 Cuatro pasos, una y otra vez. Eso es genuinamente todo lo que hay — una vez que ves
> el loop, los agents dejan de sonar misteriosos.

## 1. Paso 1 — Claude piensa

La pregunta que Claude se hace en este paso es: *dado el goal y el historial, ¿qué debo
hacer a continuación?*

Trabaja con tres cosas:

- **El goal** — lo que pediste.
- **Las tools** — lo que tiene permitido usar.
- **El historial** — todo lo que ha pasado hasta ahora.

En la primera pasada, ese historial está casi vacío. En la décima pasada, contiene todo
lo que ya ocurrió.

> ⚠️ Claude razona sobre **una sola cosa**: la acción inmediata siguiente, no el plan
> completo. La idea intuitiva de que el agent se sienta al principio, diseña un plan de
> 12 pasos y luego lo ejecuta es **incorrecta**. Decide un movimiento, observa lo que
> vuelve, decide el siguiente movimiento — y así es exactamente por qué no puedes dibujar
> el flowchart de antemano (el test de la lección anterior).

## 2. Paso 2 — Claude llama a una tool (el request-execute gap)

**Claude pide, tu código ejecuta.** Este paso tiene tres partes:

1. **Claude**: "llama a esta tool con estos inputs".
2. **El gap**: tu código decide si de verdad la ejecuta.
3. **La tool**: solo corre si tu código lo permite.

> ⚠️ Claude **nunca** ejecuta nada por sí mismo. La petición de Claude no va directo a la
> tool — pasa primero por tu código. Ese hueco entre la petición y la ejecución (el
> **request-execute gap**) es donde viven las aprobaciones y los checks de seguridad
> (se retoma en la Lección 5).

Ese gap no es una limitación técnica incómoda: es el único punto de todo el loop donde tú
puedes decir que no. Tu código puede mirar la petición y ejecutarla, rechazarla, o pedirle
confirmación a un humano primero. Sin ese gap, un agent simplemente actuaría, sin nadie
en medio.

## 3. Pasos 3 y 4 — el resultado vuelve y el loop se repite

Lo que realmente importa aquí: **cada pasada empieza con más que la anterior.**

El historial de mensajes crece en cada ciclo — el resultado se añade al historial, así
que Claude ahora sabe algo que no sabía un momento antes, y vuelve al paso 1 con **el
mismo razonamiento, pero mejor información**. Nada cambia en *cómo* piensa Claude entre
pasadas; lo que cambia es *sobre qué* está pensando — cada vuelta tiene una pieza más del
rompecabezas.

> ⚠️ Ese historial crece en cada pasada sin límite natural, y crecer para siempre no es
> gratis — es exactamente el tema de la próxima lección (context y memory).

## 4. El stopping problem

Los loops necesitan que se les diga cuándo parar. **Un loop sin salida corre para
siempre — y te factura para siempre.** La primera mitad es un problema técnico; la
segunda es un problema de negocio, y suele ser la que de verdad llama la atención.

Un loop puede parar por tres motivos:

| Motivo               | Qué significa                                                  |
| -------------------- | -------------------------------------------------------------- |
| **Goal cumplido**    | Claude determina que la tarea está terminada (el final feliz). |
| **Límite alcanzado** | Se llegó al número máximo de iteraciones (red de seguridad).   |
| **Error**            | Ocurrió un fallo irrecuperable (red de seguridad).             |

> 🎯 **Regla de examen**: los agents de producción **siempre** fijan un límite de
> iteraciones. Esa palabra, *siempre*, es la diferencia entre una demo (donde tú estás
> mirando cada corrida) y un sistema real (donde nadie vigila cada ejecución, y si una se
> descontrola, solo ese límite la detiene).

## 5. Tres formas de loop

La forma se elige según **cuánto se sabe de antemano** — no según qué tan "avanzado"
suene el patrón.

| Forma                 | Cómo corre                 | Cuándo usarla                                                  |
| --------------------- | -------------------------- | -------------------------------------------------------------- |
| **Single call**       | Sin loop.                  | Una tool, una respuesta — ya sabes exactamente qué hace falta. |
| **Tool-use loop**     | Se repite hasta terminar.  | Los pasos no se conocen de antemano.                           |
| **Subagent dispatch** | Un loop lanza otros loops. | El trabajo se divide en subtareas separables.                  |

> 📝 La mayoría de escenarios de examen piden elegir entre estas tres formas — no es
> información de fondo, es el formato de respuesta real de muchas preguntas.
> 📌 *Subagent dispatch* todavía se ve "delgado" en este punto — a propósito. Hace falta
> el trabajo de las próximas dos lecciones (context/memory y manager/subagents) antes de
> que tenga sentido completo.

## Puntos clave

- Un agent es un loop de cuatro pasos: piensa, llama a una tool, observa, repite.
- Claude **pide**; tu código **ejecuta** — el request-execute gap es donde vive el
  control de seguridad.
- El historial crece en cada pasada — mismo razonamiento, mejor información, pero también
  más contexto ocupado.
- Los agents de producción **siempre** fijan un límite de iteraciones.
- La elección entre single call, tool-use loop y subagent dispatch depende de cuánto
  sabes de antemano sobre los pasos necesarios.
