# Amazon Kinesis Data Firehose

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es?

**Kinesis Data Firehose (KDF)** es un servicio **totalmente gestionado (fully managed)** que captura,
transforma y carga flujos de datos en **casi tiempo real** hacia distintos almacenes de datos.

A diferencia de los sistemas de procesamiento tradicionales, no requiere configuración extensa,
código personalizado ni gestión manual de infraestructura (por ejemplo, no hay que gestionar shards
como en Kinesis Data Streams). El enfoque práctico es: se definen la(s) fuente(s), el destino y,
opcionalmente, las transformaciones — y el servicio se encarga del resto, incluyendo el
**escalado automático** ante aumentos de volumen.

## Flujo de datos

### Productores (fuentes)

No requieren código personalizado ni configuración compleja. KDF puede recibir datos directamente
desde:

- **Kinesis Data Streams** — probablemente la integración más habitual.
- **AWS CloudWatch Logs** — para enviar logs a procesar y analizar posteriormente.
- **AWS IoT** — dispositivos que publican datos directamente en KDF para agregación o análisis.
- **CloudWatch Events** — eventos más detallados para análisis en (casi) tiempo real.

### Destinos (consumidores)

- **Amazon S3** — uno de los destinos principales.
- **Amazon Redshift** — de forma indirecta: los datos se cargan primero en un bucket S3 y luego se
  mueven a Redshift mediante el comando `COPY`.
- **OpenSearch**.
- Servicios de terceros como **Splunk** o **MongoDB**.

## Mecanismo de buffering (almacenamiento en búfer)

Antes de entregar los datos a su destino, KDF los acumula en un **búfer**. Es la razón por la que se
habla de "casi tiempo real" y no de tiempo real puro (a diferencia de Kinesis Data Streams).

Los datos se agrupan por lotes hasta alcanzar uno de estos dos límites (lo que ocurra primero):

| Límite de buffer | Valor |
| ----------------- | ----- |
| **Tamaño de archivo** | Configurable hasta **128 MB** |
| **Intervalo de tiempo** | Configurable |

Una vez alcanzado el límite, el lote se envía al destino. Este enfoque por lotes es más **eficiente**
y **rentable**: reduce el número de llamadas a la API y el uso de recursos, algo aceptable cuando no
se necesita procesamiento estrictamente en tiempo real.

## Transformación de datos

KDF permite reformatear, filtrar o modificar los datos **sobre la marcha**, antes de entregarlos:

- Integración directa con **AWS Lambda** para aplicar transformaciones personalizadas casi en tiempo
  real.
- Soporte de formatos estructurados como **Apache Parquet** y **Apache ORC**.
- **Compresión** y **cifrado** de datos disponibles de forma nativa ("out of the box").

> ⚠️ Si el procesamiento de un registro falla, KDF puede enrutar esos datos a un **bucket S3 de
> reserva**, lo que permite reintentar el procesamiento más adelante sin perder la integridad ni la
> fiabilidad de los datos. Ese mismo bucket también sirve para archivar los registros originales.

## Casos de uso típicos

- Análisis en (casi) tiempo real.
- Captura de datos de eventos y logs en grandes volúmenes.
- Escenarios donde el "casi tiempo real" es suficiente y se prioriza la simplicidad, el bajo
  mantenimiento y el escalado automático.

## Precios

El modelo de precios se basa en el **consumo**: se cobra directamente en función del **volumen de
datos procesados**.

## Kinesis Data Streams (KDS) vs. Kinesis Data Firehose (KDF)

| Aspecto | Kinesis Data Streams | Kinesis Data Firehose |
| ------- | --------------------- | ----------------------- |
| Gestión | Requiere configuración manual y exhaustiva (ej. shards) | Totalmente gestionado, sin intervención manual |
| Latencia | Tiempo real: **~200 ms** (consumidor estándar) o **~70 ms** (Enhanced Fan-Out) | Casi tiempo real (según los límites de buffer configurados) |
| Almacenamiento de datos | **Sí** — periodo de retención configurable de **24 horas** (por defecto) hasta **365 días** | **No** — los datos se entregan directamente a los destinatarios, sin retención |
| Escalado | Manual (provisioned) o automático (on-demand) | Automático, siempre |
| Código personalizado | Sí, para productores/consumidores | No, normalmente |
| Uso de recursos | Depende de la configuración | Muy eficiente gracias al buffering y la agrupación por lotes |

La fuerza de Kinesis Data Firehose está en su **simplicidad** y en ser un servicio **totalmente
gestionado**: permite configurar de forma rápida y sencilla el procesamiento y carga de datos casi
en tiempo real (incluyendo transformaciones, compresión y cifrado) sin necesidad de gestionar
infraestructura.
