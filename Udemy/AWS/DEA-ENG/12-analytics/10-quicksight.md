# Amazon QuickSight

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon QuickSight** es el servicio de **inteligencia de negocios (BI)** de AWS, usado para
visualizar datos y crear informes/dashboards — por ejemplo, a partir de resultados de consultas de
[Amazon Athena](../2-query-athena/1-athena-intro.md).

## Qué permite hacer con los datos empresariales

- **Crear visualizaciones** e informes/dashboards.
- Realizar **análisis ad hoc**.
- **Recibir alertas sobre anomalías** detectadas en los datos.
- Obtener rápidamente **conocimientos (insights) empresariales** a partir de los datos.

## SPICE

**SPICE** (Super-fast, Parallel, In-memory Calculation Engine) es el **motor de cálculo** de
QuickSight:

- Almacena y procesa los datos **en memoria**.
- Es **paralelo**: distribuye el cálculo para acelerar el procesamiento.
- Está diseñado para ser **súper rápido**, permitiendo consultas interactivas sobre los datos sin
  tener que volver a consultar la fuente de datos original cada vez.
- Ofrece **10 GB de almacenamiento por usuario**, y es **altamente disponible y duradero**.

## Integración con Redshift

> ⚠️ Para que QuickSight pueda consultar un clúster de **Redshift**, ambos deben estar en la
> **misma región** — igual que ocurre entre Redshift y los buckets de S3 que consulta con
> [Redshift Spectrum](../9-redshift-data-warehouse/13-redshift-spectrum.md).

## Ediciones y roles de usuario

QuickSight tiene distintos **roles de usuario**, cuyo alcance depende de la edición contratada.
En la edición **Enterprise**, por ejemplo, los usuarios con rol de **lector (reader)**:

- Solo pueden **ver, exportar e imprimir** un dashboard.
- **No pueden guardarlo como un análisis** — no tienen permiso para modificarlo ni crear
  visualizaciones nuevas a partir de él.
