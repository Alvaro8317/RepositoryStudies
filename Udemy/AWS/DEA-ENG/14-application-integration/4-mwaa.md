# Amazon MWAA (Managed Workflows for Apache Airflow)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon MWAA** es, como su nombre indica, **Apache Airflow gestionado** en la nube: un servicio de
**orquestación totalmente gestionado** que utiliza Apache Airflow por debajo.

- Los flujos de trabajo se configuran con código **Python** — útil si ya se está familiarizado con
  Python y/o con Apache Airflow.
- Al estar alojado (managed), no hay que preocuparse de la configuración de la infraestructura
  subyacente: basta con centrarse en crear los flujos de trabajo mediante scripts de Python.

## Características clave

- **Escalado automático** de la capacidad de ejecución del flujo de trabajo según la demanda — útil
  para canalizaciones de datos más complejas o ETLs pesados.
- Integración con **IAM** y con **CloudWatch** (métricas y monitorización).

## Casos de uso

- Flujos de trabajo complejos: **transformaciones de datos** avanzadas, orquestación de
  **pipelines de Machine Learning**, o ETLs con **dependencias complejas**.
- **Automatización basada en eventos**: por ejemplo, la carga de un archivo a S3 o una actualización
  en una tabla de DynamoDB puede desencadenar un flujo de trabajo en respuesta a ese evento.

## DAGs (Directed Acyclic Graphs)

Airflow organiza los flujos de trabajo en tareas mediante **DAGs** (grafos acíclicos dirigidos),
lo que garantiza un orden claro y lógico (una secuencia) y evita dependencias cíclicas.

- Los DAGs se escriben en **Python** y se alojan en un **bucket S3**.
- En el script se definen las **tareas** que forman el flujo de trabajo, su **orden** y qué hace
  cada una.
- Un DAG representa el flujo de trabajo completo: una colección de tareas con dependencias
  específicas entre ellas.
  - Cada **nodo** del grafo es una **tarea**.
  - Cada **arista dirigida** representa el orden/dependencia entre tareas.

> No es necesario saber escribir DAGs en detalle para el examen — basta con entender el concepto:
> MWAA es Apache Airflow gestionado, los flujos de trabajo se definen en Python como DAGs, y
> simplifica la gestión integral de procesos y pipelines de datos.
