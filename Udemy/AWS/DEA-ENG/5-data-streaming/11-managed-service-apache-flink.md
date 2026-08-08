# Amazon Managed Service for Apache Flink

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Apache Flink?

**Apache Flink** es un framework de código abierto para el **procesamiento de flujos de datos
(stream processing)** distribuido y con estado (*stateful*). Permite ejecutar cálculos sobre datos
que llegan de forma continua (en lugar de en lotes cerrados), manteniendo baja latencia y alto
throughput incluso a gran escala. Es la tecnología que usan, entre otros, sistemas de analítica en
tiempo real, detección de fraude o monitorización de eventos.

**Amazon Managed Service for Apache Flink** (a veces referido como *MSF*) es la versión
**totalmente gestionada** de este framework en AWS: Amazon se encarga de aprovisionar, escalar y
mantener la infraestructura subyacente, y de integrar el resto de servicios de AWS sin necesidad de
código adicional para esa integración. El usuario se centra únicamente en construir la lógica de la
aplicación de streaming.

## Casos de uso

- **Analítica en tiempo real**: cálculo de métricas o agregaciones sobre flujos de datos, por ejemplo
  para monitorización (ej. tráfico de un sitio web y actividad de usuarios en tiempo real).
- **Streaming ETL**: procesamiento/transformación de datos de streaming como parte de un pipeline ETL.

Para construir la aplicación se puede consultar los datos con **SQL**, o desarrollarla directamente
con **Python**, **Scala** o **Java**.

## Características del servicio gestionado

- **Serverless**: no hay que gestionar la infraestructura subyacente; el servicio escala
  automáticamente según la carga de trabajo real.
- **Alta fiabilidad y rendimiento**, heredados del motor de Flink, sin tener que ocuparse de escalar
  o integrar los distintos componentes manualmente.

## Cómo funciona

### Fuentes (Flink sources)

Los datos se pueden ingerir con una configuración mínima desde:

- **Amazon Kinesis Data Streams** — la integración más habitual (ver [[2-kinesis-overview]]).
- **Amazon MSK (Managed Streaming for Apache Kafka)** — servicio gestionado de AWS para Apache Kafka,
  que igualmente facilita crear y ejecutar aplicaciones de streaming basadas en Kafka.
- **Amazon S3**.
- **Fuentes de datos personalizadas**, accesibles mediante conectores de Apache Flink o APIs.

### Procesamiento

Una vez ingeridos, los datos se pueden **filtrar**, **agregar** o **enriquecer** sobre la marcha,
usando el motor de streaming de Flink, diseñado para operar con **latencia muy baja** (casi en tiempo
real).

Entre las capacidades más destacadas del motor:

- **Cálculos con estado (stateful)**: Flink puede mantener y actualizar un estado interno a medida
  que van llegando los datos, lo cual es clave para casos de uso como la **detección de anomalías**.
- **Checkpoints y snapshots periódicos**: garantizan una solución **tolerante a fallos**, permitiendo
  volver a un estado anterior consistente si ocurre algún problema durante el procesamiento.
- **Detección de anomalías**: implementando algoritmos que identifican patrones extraños o
  desviaciones en el flujo de datos, para disparar alertas o respuestas automatizadas en tiempo real
  (ej. detección de fraude en el sector bancario).
- **Acciones controladas por eventos**: se pueden definir acciones dentro de la aplicación en función
  de los datos procesados en el flujo.
- **Integración con otros servicios de AWS**, como **AWS Lambda**, para ejecutar código personalizado
  adicional como parte del procesamiento.

### Destinos (Flink sinks)

Los datos procesados se entregan a los llamados **sinks**, que pueden incluir:

- Buckets de **Amazon S3**.
- **Amazon Kinesis Data Streams**.
- **Amazon MSK**.
- Otras fuentes de datos personalizadas o herramientas analíticas de visualización.

## Precios

Modelo de precios basado en el **consumo**, sin costes iniciales — solo se paga por los recursos
realmente utilizados.

La unidad de facturación es la **KPU (Kinesis Processing Unit)**:

| KPU | Equivalencia |
| --- | ------------ |
| 1 KPU | 1 vCPU + 4 GB de memoria |

- Cada aplicación creada requiere **1 KPU adicional** dedicada a su orquestación, que también se
  factura.
- Si la aplicación usa almacenamiento de datos, se cobra adicionalmente en función del volumen, medido
  en **GB al mes**.
- El número de KPUs **escala automáticamente** según las necesidades de la aplicación. También se
  puede **aprovisionar manualmente** una cantidad fija de KPUs cuando se prefiere tener más control.
- **Modo interactivo (Studio Notebooks)**: permite desarrollar de forma interactiva usando notebooks.
  Al activarlo se cargan **2 KPUs adicionales**, facturadas con el mismo modelo de coste de
  almacenamiento.

> ⚠️ La transcripción original de esta clase usa "CPU" como unidad de precio, pero la definición dada
> (1 vCPU + 4 GB de memoria) corresponde exactamente a la **KPU (Kinesis Processing Unit)**, que es la
> unidad de facturación real de Amazon Managed Service for Apache Flink — se ha corregido en este
> apunte.
