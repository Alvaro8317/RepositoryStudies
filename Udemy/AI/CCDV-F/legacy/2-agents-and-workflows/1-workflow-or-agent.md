# Workflow or Agent

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: la pregunta central del dominio

Domain 1 (Agents and Workflows) arranca con la pregunta más importante de todo el dominio:
**¿workflow o agent?** Todo lo demás en el dominio — el agent loop, context/memory,
subagents, frameworks — se apoya en esta distinción.

## 1. ¿Qué es un workflow?

**Tú escribes los pasos y Claude rellena los huecos.**

Analogía: un mostrador de venta de billetes de tren con cuatro ventanillas fijas, en un
orden que nunca cambia:

1. Rellenar el formulario
2. Verificar el ID
3. Pago
4. Imprimir el billete

Cada paso está fijo en su lugar y en su orden — el camino se decidió antes de que nadie
llegara al mostrador. Claude puede escribir el resumen en el paso 3, pero nunca puede
saltarse el paso 2 ni inventar un paso 5.

> 📌 **Tú controlas el camino. Claude maneja el lenguaje** dentro de cada paso — hace
> trabajo real, pero no elige qué pasos existen ni en qué orden vienen.
> ⚠️ La mayoría de sistemas en producción son workflows. No es la opción simple que se usa
> antes de aprender la "inteligente" — es lo que realmente son la mayoría de sistemas
> reales.

## 2. Cuatro patrones de workflow

| Patrón           | Qué hace                                                               | Por qué                                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chaining**     | La salida de un paso alimenta el siguiente (Paso 1 → Paso 2 → Paso 3). | El paso 2 no puede empezar hasta que el paso 1 produzca algo — es su input.                                                                  |
| **Parallel**     | Se ejecutan pasos independientes a la vez y luego se combinan.         | Solo pueden correr juntos porque ninguno espera al otro.                                                                                     |
| **Routing**      | Se clasifica primero y luego se envía al handler correcto.             | No todos los caminos se ejecutan — solo se usa un handler, decidido por el paso de clasificación.                                            |
| **Orchestrator** | Un paso planifica el trabajo y reúne los resultados de varios workers. | A diferencia de parallel (donde ya sabes que hay N pasos fijos), aquí el orchestrator decide qué trabajo hace falta, lo reparte y lo recoge. |

## 3. ¿Qué es un agent?

**Tú das el objetivo; Claude elige los pasos.**

Analogía inversa a la anterior: un auto-rickshaw que sale de un punto A hacia un destino
B. En el camino, la ruta 1 tiene una carretera cerrada, la ruta 2 tiene tráfico pesado y
la ruta 3 está libre. El conductor va decidiendo sobre la marcha, según lo que encuentra.

- Nadie escribió ese giro de antemano — el cierre de carretera no se conocía por
  adelantado.
- El conductor solo necesita el destino, no una ruta prescrita.
- Claude decide **un paso a la vez**, no planifica todo el viaje de antemano: decide el
  siguiente movimiento, y luego el siguiente, según lo que va descubriendo.

## 4. La diferencia real

La pregunta que separa ambos: **¿quién decide el siguiente paso — tú o el modelo?**

|                     | Workflow                     | Agent                          |
| ------------------- | ---------------------------- | ------------------------------ |
| Pasos decididos por | Tú, de antemano              | Claude, en tiempo de ejecución |
| Predecible          | Sí                           | No                             |
| Coste               | Conocido                     | Variable                       |
| Debugging           | Fácil                        | Más difícil                    |
| Mejor para          | Tareas repetidas y conocidas | Tareas abiertas (open-ended)   |

**El test práctico**: ¿podrías sentarte ahora mismo, antes de ejecutar nada, y dibujar el
flowchart completo?

- Si **sí** → es un **workflow**.
- Si **no** (porque el camino depende de lo que se descubre sobre la marcha) → es un
  **agent**.

> ⚠️ La diferencia NO es "cuál es más inteligente" ni "cuál usa tools" — ambos usan
> tools. Un agent no es "el listo" y un workflow no es "el básico". La única línea que
> importa es **dónde está el control**.
> ⚠️ Un agent puede necesitar 3 tool calls o 30 — esa imprevisibilidad de coste es una
> preocupación real de producción, no una nota al pie. Si un sistema corre 100,000 veces
> al mes y cada corrida cuesta entre 3 y 30 unidades, el negocio no puede pronosticar su
> factura.

## 5. Cómo elegir

**Regla: si puedes dibujar el flowchart, usa un workflow.**

Antes de elegir, pregúntate:

1. ¿Los pasos cambian según la petición?
2. ¿Conoces todos los pasos de antemano?
3. ¿Es aceptable un coste impredecible?

Ejemplo workflow: cada factura pasa por los mismos 3 checks, siempre.
Ejemplo agent: el proceso varía según lo que se va encontrando.

> 🎯 **Regla de examen — memorizar textualmente: cuando ambos podrían funcionar, elige el
> workflow.** El instinto es elegir el agent porque suena más avanzado, pero en un empate
> real la respuesta correcta es el workflow: da predictibilidad, coste conocido y
> debugging fácil, sin renunciar a nada que la tarea realmente necesitara.

## Puntos clave

- **Workflow** = tú decides los pasos, de antemano.
- **Agent** = Claude decide los pasos, en tiempo de ejecución.
- Cuando ambos encajan, elige el workflow.
- Todo (predictibilidad, coste, debugging) se deriva de una sola decisión: quién tiene el
  control.
