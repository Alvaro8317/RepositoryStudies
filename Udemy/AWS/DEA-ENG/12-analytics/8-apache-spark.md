# Apache Spark

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Apache Spark** es un motor de procesamiento de datos **muy rápido** y de **código abierto**, que
proporciona APIs para varios lenguajes: **Java**, **Scala**, **Python** y **R**. Ofrece un
procesamiento **unificado** para ETLs, análisis interactivo, machine learning y procesamiento de
grafos.

- Realiza procesamiento **en memoria**, lo que puede acelerar tareas hasta **100 veces más** que
  Hadoop MapReduce.
- Es **integrable** con Hadoop, con bases de datos NoSQL y con muchos servicios en la nube (por
  ejemplo, [Amazon EMR](3-emr.md) lo soporta como uno de sus frameworks).

## Características principales

- **Big Data**: diseñado para manejar grandes volúmenes de datos.
- **Caché en memoria**: permite cachear datos en memoria y ejecutar consultas optimizadas de forma
  encadenada.
- **Multilenguaje**: soporta Python, Java, Scala y R.
- **Reutilización de código**: el mismo código se puede reutilizar entre distintos tipos de tarea
  (procesamiento por lotes, consultas interactivas, machine learning, etc.).

> ⚠️ Apache Spark **no** está pensado para procesos **OLTP** (transaccionales). Su función
> principal es el procesamiento de datos **en lotes (batch)** y **en tiempo real (streaming)**.

- **Spark Streaming**: permite procesamiento de datos en tiempo real, integrándose fácilmente con
  herramientas como **Amazon Kinesis** y **Apache Kafka**.

## Arquitectura interna

El flujo de ejecución de una aplicación Spark se compone de las siguientes piezas:

| Componente          | Función                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Driver Program**  | Donde se declaran las transformaciones y acciones de la aplicación. Crea el **Spark Context**.                                                                |
| **Spark Context**   | Coordina la ejecución de toda la aplicación y solicita recursos al **Cluster Manager** cuando se requieren.                                                   |
| **Cluster Manager** | Gestiona las solicitudes de recursos para los nodos trabajadores: asigna recursos e instruye a los **Worker Nodes** para que ejecuten un trabajo determinado. |
| **Worker Nodes**    | Ejecutan las tareas, almacenan los resultados y gestionan la caché en memoria.                                                                                |

> No es necesario dominar al detalle esta arquitectura — basta con reconocer las piezas que
> intervienen: **Driver Program → Spark Context → Cluster Manager → Worker Nodes**.

## Componentes de Apache Spark

| Componente          | Función                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Spark SQL**       | Permite ejecutar consultas SQL sobre datos almacenados en **DataFrames** y **Datasets**.                                                                      |
| **Spark Streaming** | Procesamiento de flujos de datos en tiempo real; se integra con **Kinesis**, **Kafka** y servicios similares.                                                 |
| **Spark MLlib**     | Implementaciones de algoritmos de **Machine Learning**: clasificación, regresión, clustering, filtrado, minería de patrones, etc.                             |
| **SparkR**          | Permite aprovechar las características de **R** junto con el procesamiento de Apache Spark.                                                                   |
| **GraphX**          | Permite realizar cálculos iterativos y consultas sobre grafos grandes.                                                                                        |
| **Spark Core API**  | Acceso programático (R, SQL, Python, Scala, Java) con funcionalidades básicas: gestión de memoria, recuperación ante fallos, monitorización de trabajos, etc. |

## Integraciones con servicios de AWS

### Apache Spark + Kinesis

Flujo típico para aplicaciones en tiempo real:

1. Distintos dispositivos capturan información y la envían a **Kinesis Data Streams**.
2. **Data Streams** ingiere y almacena esos flujos de datos.
3. Los datos se envían a **Apache Spark** (desplegado, por ejemplo, en [Amazon EMR](3-emr.md)),
   donde se construyen aplicaciones personalizadas en tiempo real.
4. Los datos finales se envían a un **dashboard** (herramientas de Business Intelligence) para su
   análisis visual.

### Apache Spark + Redshift

Flujo típico para procesamiento batch de datos crudos:

1. Los datos crudos (sin tratar) se almacenan en un **bucket S3**, que actúa como repositorio.
2. Un clúster de **Amazon EMR** ejecuta **Apache Spark**, que lee esos datos desde S3.
3. Spark realiza **transformaciones**: limpieza, agregación y análisis de los datos.
4. Los datos procesados se envían de vuelta a **S3**, o se cargan directamente en **Redshift** para
   poder ejecutar consultas SQL más complejas.

### Apache Spark + Athena

**Athena** permite seleccionar **Apache Spark** como motor de análisis alternativo, frente a la
opción por defecto de **Athena SQL**.

- Acceso programático mediante **API** o **CLI**.
- Se pueden ajustar las **DPU** (Data Processing Units) tanto para el **coordinador** como para el
  tamaño de los **ejecutores** (worker nodes).
- El precio se basa en el **uso de cómputo**, según las **DPU por hora** consumidas.

> Basta con saber que estas integraciones existen: Apache Spark se puede combinar con otros
> servicios del cloud de AWS sin mayor complicación.
