# Métodos de Ingestión de Datos

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Dos grandes patrones de ingestión

Antes de profundizar en servicios concretos, es importante distinguir entre dos patrones principales de ingestión de datos:

| Patrón                                         | Descripción                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Ingesta de streaming (Streaming ingestion)** | Ingesta en **tiempo real**, por ejemplo hacia buckets de S3.                                                  |
| **Ingesta por lotes (Batch ingestion)**        | Los datos **no** se transmiten en tiempo real, sino en **lotes** (batches), normalmente de **mayor volumen**. |

## Ingesta por lotes (Batch)

- Se ingieren **grandes volúmenes** de datos de forma **periódica**.
- Puede ser:
  - Una **carga única** (one-time load).
  - Una carga programada según un **horario específico** (ej. cada hora, cada día, cada semana).
- Los datos que se han ido recogiendo/generando hasta ese momento se ingieren juntos en el lote.
- Es el **método por defecto**: siempre que se manejen volúmenes grandes y los datos **no sean sensibles al factor tiempo**, se recomienda usar batch.
- **Ventajas:** más sencillo de implementar y **más rentable (económico)**.

## Ingesta de streaming

- Se usa cuando los datos son **muy sensibles al tiempo** y necesitan procesarse **inmediatamente**.
- Ejemplo típico: **detección de fraude**, donde se necesita procesar y actuar en tiempo real.
- Es el método a elegir **solo cuando el caso de uso lo exige** (tiempo crítico), no por defecto.
- **Desventaja:** es más **complicado de implementar** y **más costoso**, ya que los datos deben estar disponibles de forma inmediata.

## Comparativa rápida

| Aspecto                    | Streaming                                   | Batch                                       |
| -------------------------- | ------------------------------------------- | ------------------------------------------- |
| Latencia                   | Tiempo real                                 | Periódica (horas/días/semanas)              |
| Volumen típico             | Menor por evento                            | Grandes volúmenes acumulados                |
| Complejidad                | Mayor                                       | Menor                                       |
| Coste                      | Más elevado                                 | Más económico                               |
| Caso de uso típico         | Detección de fraude, alertas en tiempo real | Procesamiento periódico de grandes datasets |
| ¿Es el método por defecto? | No (solo cuando se necesita)                | Sí                                          |

## Servicios de AWS asociados

### Para ingesta de streaming

- **Amazon Kinesis** (se profundizará más adelante en esta sección)

### Para ingesta por lotes

- **AWS Glue** — la herramienta más utilizada para este propósito.
- **AWS Lambda** — también puede apoyar en procesos de ingesta por lotes.
