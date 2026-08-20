# Redshift: Federated Queries

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## El problema: datos aislados en distintos sistemas

Tradicionalmente, en los data warehouses, los datos suelen estar **aislados en distintos
sistemas** (una base de datos PostgreSQL, alguna base de datos operativa, alguna base de datos
NoSQL, etc.). Analizarlos juntos es complicado.

El enfoque tradicional para resolverlo es ejecutar **trabajos ETL**:

1. **Extraer** los datos de todas esas fuentes.
2. **Transformar** los datos a un formato uniforme.
3. **Cargar** los datos en el data warehouse.

Este enfoque tiene inconvenientes:

- Consume **muchos recursos**.
- Requiere **tiempo y planificación**.
- Introduce **latencia**: el ETL se ejecuta de forma **periódica/por lotes**, así que los datos no
  están disponibles **en tiempo real**.

## ¿Qué son las Federated Queries?

Las **Federated Queries** permiten **consultar datos que están fuera de Redshift**, sin necesidad
de copiarlos primero al data warehouse.

- Permiten **combinar y analizar datos de distintas fuentes** directamente.
- **No es necesario copiar los datos** a Redshift para poder consultarlos.
- Reduce la **transferencia de datos** y **elimina la necesidad de pipelines ETL** para esas
  fuentes — no hay que duplicar los datos, se consultan directamente donde están.

> ⚠️ Las Federated Queries son específicas para **bases de datos relacionales**. Para consultar
> datos en **S3** sin copiarlos, la funcionalidad equivalente es **Redshift Spectrum** (tratado en
> otra parte del curso).

## Fuentes soportadas

Redshift está diseñado para federar consultas contra bases de datos **compatibles con
PostgreSQL**, incluyendo:

- **Amazon RDS para PostgreSQL**.
- **Amazon Aurora** (con compatibilidad PostgreSQL).
- Bases de datos **PostgreSQL autogestionadas en EC2**.
- Bases de datos **PostgreSQL on-premises** (en el propio centro de datos del usuario, conectadas
  vía red).

## Cómo funciona

1. Se crean **definiciones de esquema externo (external schema)** que apuntan a la fuente de datos
   externa.
2. A partir de ahí, se pueden consultar las **tablas externas** junto con las tablas normales de
   Redshift usando **SQL estándar** — desde el punto de vista de la consulta, se comportan como
   una tabla más.
3. Estos datos externos también se pueden usar directamente en **herramientas de BI** (ej. Power
   BI conectado a Redshift, incluyendo tablas externas que apuntan a otra fuente).

## Optimización del cómputo

- Redshift intenta **trasladar el máximo cómputo posible a la fuente de datos externa**, para
  minimizar la transferencia de datos por la red y maximizar el rendimiento.
- Parte del cálculo de las Federated Queries se **distribuye directamente en la base de datos
  operativa remota**.
- Redshift también usa su propio **procesamiento paralelo** para dar soporte a estas consultas
  cuando es necesario.

> ⚠️ Las Federated Queries amplían las capacidades de análisis de Redshift más allá de sus propios
> datos: mediante esquemas externos, se pueden usar tablas de bases de datos externas como si
> estuvieran dentro de Redshift.
