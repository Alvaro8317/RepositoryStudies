# Tipos de Job y motores en AWS Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Formas de crear un Job en Glue

Al crear un Job en Glue existen distintas formas de trabajar:

- **Visual ETL**: arrastrar y soltar componentes en el editor visual. El **motor subyacente** se
  selecciona automáticamente según los tipos de fuente de datos elegidos (por lo general **Spark**), y
  no se puede cambiar manualmente.
- **Notebook**: permite hacer procesamiento de datos de forma **interactiva**, útil para experimentar.
  Existen distintos tipos de notebook disponibles.
- **Script authoring**: escribir el script del Job completamente desde cero. Al crear un Job de forma
  visual, Glue también genera un script equivalente por debajo, pero aquí se puede escribir el propio
  código directamente. Esta opción da **más control**, incluyendo la posibilidad de elegir un motor
  distinto (por ejemplo, **Python Shell** para tareas ligeras, como método de ahorro de costes).

## Motores / tipos de Job

### Spark

- Es el motor **por defecto**, usado habitualmente para flujos de procesamiento de datos a **gran
  escala**.
- Usa **Apache Spark** por debajo, aprovechando su capacidad de **computación distribuida** — muy
  adecuado para cargas de trabajo de big data.
- **DPU (Data Processing Unit)**: unidad de capacidad de procesamiento. Cada DPU incluye **4 vCPU** y
  **16 GB de memoria**. La facturación es por **DPU-hora**.
- Rango configurable: de **2 a 100 DPUs**, con un valor por defecto de **10 DPUs**. El mínimo es 2 DPUs
  (no se puede reducir por debajo de eso).

### Spark Streaming ETL

- Se usa para analizar y procesar datos **en tiempo real**, reaccionando a eventos en el momento en que
  se producen.
- Trabaja con fuentes de datos en streaming como **Kinesis Data Streams** o **Kafka**.
- Mismo rango de DPUs que los Jobs de Spark estándar (2 a 100, valor por defecto 10).

### Python Shell

- Pensado para tareas de procesamiento de datos **más sencillas o a pequeña escala**, cuando no se
  necesita la capacidad de computación distribuida de Spark.
- Ejecuta Python en un **entorno gestionado** para tareas ligeras, usando muchos menos recursos que un
  Job de Spark.
- Opciones de DPU: **0.0625 DPU** (1/16) o **1 DPU** — incluso el máximo aquí es menor que el mínimo de
  un Job de Spark, lo que permite ahorrar bastante coste en tareas ligeras.

### Ray

- Añadido **recientemente** a Glue. **Ray** es un framework de **código abierto**, nativo de **Python**,
  que ejecuta cargas de trabajo en un clúster distribuido con un entorno **multi-nodo**.
- Al ser nativo de Python, permite llevar a Glue frameworks y librerías ya familiares (por ejemplo, de
  **Machine Learning** o ciencia de datos) y escalarlos a datasets grandes sin necesidad de modificar
  demasiado el código.
- Casos de uso típicos:
  - Paralelizar múltiples transformaciones.
  - Ejecutar la misma carga de trabajo Python sobre cientos de fuentes de datos.
  - Tareas de Machine Learning a gran escala: ingestión, inferencia por lotes en paralelo, etc.
- Los Jobs de Ray se ejecutan sobre los nuevos tipos de **worker EC2 basados en Graviton**, disponibles
  **únicamente** para este tipo de Job (no para Spark).

## Tipos de ejecución (Execution types)

| Tipo         | Descripción                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Standard** | Tipo de ejecución por defecto.                                                                                                                                   |
| **Flex**     | Alternativa más económica para ETL **no sensible al tiempo**. Los Jobs se ponen en cola y se ejecutan cuando hay recursos disponibles, por lo que pueden empezar con cierto retraso, a cambio de un ahorro de coste. |

> Ejemplo de uso de **Flex**: un job de transformación de datos que se ejecuta semanalmente y no
> requiere un horario exacto de inicio — en ese caso, Flex permite ahorrar costes sin impacto real en el
> negocio.
