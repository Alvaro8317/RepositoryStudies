# Amazon Timestream

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Amazon Timestream** es una base de datos de **series temporales** serverless.

Una serie temporal es básicamente una secuencia de puntos de datos con **marca de tiempo**,
registrados a lo largo del tiempo — usada para medir eventos que cambian con el tiempo. Timestream
está diseñada y optimizada para el **análisis de alto rendimiento en tiempo real** sobre este tipo de
datos.

## Casos de uso

- Logs de aplicaciones y dispositivos **IoT**.
- Monitorización de **DevOps** — por ejemplo, almacenar métricas de CPU, memoria, latencia o
  throughput de red de servidores y contenedores, para detectar anomalías o cuellos de botella en
  tiempo real.
- Datos de mercados financieros.
- En general, cualquier fuente que genere métricas o registros con marca de tiempo.

## Características

- **Serverless**: se adapta automáticamente a la demanda sin gestionar infraestructura, dejando el
  foco en analizar los datos.
- Optimizada para series temporales, con **funciones incorporadas específicas** (ej. suavizado,
  interpolación de datos).
- Alto rendimiento y tiempos de respuesta rápidos incluso con grandes volúmenes de datos.
- Solución de almacenamiento **rentable** para este tipo de datos.
- Soporta **ingestión en tiempo real**, adecuada para aplicaciones sensibles al tiempo.

## Integración con fuentes de datos

Timestream puede recibir datos desde distintos orígenes:

- **Lambda**, para procesar y transformar datos (por ejemplo, provenientes de APIs, webhooks u otros
  triggers) antes de ingerirlos.
- **Kafka** (topics), para streaming de datos hacia análisis en tiempo real.
- **Amazon Managed Service for Apache Flink**, para procesar y agregar datos de streaming antes de
  ingerirlos.
- **Kinesis Data Streams**, para transmitir datos en tiempo real.
- **AWS IoT Core**, para conectar directamente con dispositivos IoT y reenviar sus datos a Timestream.

## Visualización

Timestream almacena y gestiona eficientemente los datos, pero normalmente se combina con una
herramienta de visualización/análisis:

- **Grafana** (gestionado) — es la combinación más habitual. Grafana está construido específicamente
  para representar datos con marca de tiempo como series temporales — incluso puede construir esas
  series a partir de simples logs, sin necesitar una base de datos de series temporales dedicada.
  Por eso encaja de forma tan natural con Timestream: donde Timestream aporta el almacenamiento y
  las consultas optimizadas para series temporales a gran escala, Grafana aporta la capa de
  visualización pensada exactamente para ese mismo tipo de dato.
- **QuickSight**, **SageMaker**, u otras aplicaciones de terceros vía **drivers JDBC**.

## Caso de uso: monitorización IoT en tiempo real

Arquitectura serverless típica para transmitir, procesar y visualizar eventos de series temporales
generados por dispositivos IoT:

1. Los dispositivos IoT envían datos (en distintos formatos) a través de **Kinesis Data Streams**,
   que transporta los eventos de streaming.
2. **Amazon Managed Service for Apache Flink** transforma y agrega los datos casi en tiempo real,
   detectando y limpiando errores antes de la ingesta, dejándolos en un formato optimizado para
   Timestream.
3. Los datos procesados se ingieren en **Timestream**, la base de datos de series temporales
   escalable y serverless.
4. Los datos se visualizan directamente desde Timestream con un dashboard de **Grafana**.

Opcionalmente, el flujo de **Kinesis Data Streams** también se puede ampliar con **Kinesis Data
Firehose** para almacenar los datos en **S3** (por ejemplo, como parte de un data lake), o seguir
procesándolos con funciones **Lambda**.
