# AWS Lambda

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Lambda?

**AWS Lambda** es un servicio de **computación sin servidor (serverless)** que permite ejecutar código
sin tener que administrar servidores ni infraestructura.

- Nos centramos únicamente en escribir el código; toda la infraestructura subyacente la gestiona AWS.
- **Escala automáticamente** en función de la demanda: si la carga de trabajo aumenta, Lambda escala sin
  que tengamos que configurar ni gestionar nada.
- Soporta **varios lenguajes de programación** (Python, Node.js, Java, entre otros), lo que lo hace muy
  flexible.

## Papel en la ingesta y procesamiento de datos

Lambda es muy útil para configurar **ingesta basada en eventos**: el código se ejecuta automáticamente
como respuesta a que ocurra algo (un evento), por ejemplo la carga de un archivo en un bucket S3.

Casos de uso típicos:

- **Procesar archivos al llegar a S3**: perfilar datos, limpiarlos, transformarlos o transferirlos a otro
  bucket.
- **Procesar streams de datos en tiempo real** (por ejemplo, Kinesis Data Streams), útil cuando hay
  dispositivos IoT u otras fuentes generando datos de forma continua.
- **Automatizar flujos de trabajo** en general: no se limita al procesamiento de datos, sirve para
  ejecutar código en respuesta a cualquier tipo de evento.

## Ventajas

| Ventaja                | Detalle                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------- |
| **Escalable**          | Escala automáticamente según la demanda; no hay que gestionar capacidad de cómputo. |
| **Rentable**           | Se paga solo por la potencia de cómputo utilizada durante la ejecución.             |
| **Sin servidor**       | No hay que configurar ni administrar infraestructura en segundo plano.              |
| **Ingesta sin estado** | Cada invocación es independiente y no almacena información de ejecuciones previas.  |

> ⚠️ Por defecto, cada ejecución (invocación) de una función Lambda es **stateless**: no recuerda nada de
> invocaciones anteriores. Es posible conectarla a otros servicios para darle estado, pero lo habitual es
> que cada ejecución sea independiente.

## Ejemplos prácticos de disparadores (triggers)

### 1. Notificación de S3

Un archivo se carga en un bucket S3 → el bucket envía una **notificación S3** → esto dispara la ejecución
de la función Lambda → el código procesa el archivo (por ejemplo, lo transfiere a otro bucket o lo
transforma).

### 2. Kinesis Data Streams

Se configura **Kinesis** como fuente de eventos (event source) de la función Lambda:

- Los registros van llegando de forma continua al stream (por ejemplo, desde dispositivos IoT).
- Lambda procesa los registros en **lotes (batches)**; por defecto, el tamaño de lote es de **100
  registros**.
- Si el volumen de datos entrante fluctúa mucho o aumenta, Lambda escala automáticamente para mantener el
  ritmo de procesamiento.
