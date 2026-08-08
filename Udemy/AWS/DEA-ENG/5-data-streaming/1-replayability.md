# Replayability en el Streaming de Datos

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es replayability?

**Replayability** (rejugabilidad/repetibilidad) es la capacidad de **reprocesar o reintroducir datos que
ya se habían tratado**, cuando por alguna razón necesitan volver a manejarse.

Es como tener una **segunda oportunidad** de procesar los datos correctamente, sobre todo cuando el
primer intento no salió como estaba previsto.

## ¿Por qué es importante?

| Motivo                              | Explicación                                                                                                                                                                             |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gestión de errores**              | Algo no funcionó como se esperaba (ej. un SMS no se envía por mala señal) y se necesita reintentar hasta que el proceso tenga éxito.                                                    |
| **Consistencia de los datos**       | Ayuda a sincronizar y corregir datos para que todo el flujo sea uniforme y preciso, incluso cuando el flujo de datos es complejo.                                                       |
| **Adaptación a cambios de esquema** | Si un tipo de dato cambia, la replayability permite reajustarse a ese cambio de forma eficiente, haciendo la solución más duradera.                                                     |
| **Testing y desarrollo**            | Los desarrolladores pueden probar nuevas funciones o corregir errores usando datos reales (reproduciéndolos y reprocesándolos) sin arriesgar la integridad de los datos en tiempo real. |

## Estrategias de implementación

### Operaciones idempotentes

Hacer la misma operación varias veces debe producir **el mismo resultado** que hacerla una sola vez.

- Ejemplo: pulsar varias veces "Me gusta" en una publicación debe resultar en un solo "like", no en
  varios.
- Ejemplo: enviar varias veces un formulario/review no debe duplicar esa review.

### Logging y auditoría

Llevar un registro (log) de **qué ocurrió y cuándo**, para poder rastrear quién hizo qué sobre los
datos. Esto permite identificar con precisión el momento en que algo empezó a desviarse del plan y
corregirlo.

### Checkpointing (puntos de control)

Marcar **puntos específicos** dentro del recorrido de procesamiento de datos, de forma similar a marcar
una página de un libro.

- Si ocurre un problema, se puede volver a ese punto de control en lugar de reprocesar desde el
  principio.

### Backfilling (relleno)

Mecanismo para **actualizar datos antiguos** con información nueva o corregida, garantizando que los
datos históricos se mantengan **correctos y completos**.

## Replayability en AWS

- **Amazon Kinesis** ofrece esta capacidad de replayability de forma nativa, ya que es un requisito
  muy importante específicamente en el flujo (streaming) de datos.

> ⚠️ La replayability actúa como una **red de seguridad**: cuando algo sale mal en el procesamiento de
> datos, permite repetir el proceso y manejarlo de forma eficiente, en lugar de perder datos o dejar el
> sistema en un estado inconsistente.
