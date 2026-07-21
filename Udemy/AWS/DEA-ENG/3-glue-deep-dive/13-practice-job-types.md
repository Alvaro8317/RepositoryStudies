# Práctica: Tipos de Job en la consola de Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

Demostración rápida en la consola de cómo se reflejan los conceptos de [[12-glue-job-types|tipos de
Job y motores]] al configurar el ETL Job ya creado en prácticas anteriores.

## Revisar el tipo de motor configurado

En **Job details** del ETL Job existente se puede ver el campo **Type**: se configura automáticamente
según las fuentes de datos y tareas usadas al crear el job en el editor visual.

Desde ahí también se pueden ajustar otros parámetros:

- El **lenguaje** usado por el job.
- El **worker type**.
- **Autoscaling** de workers.
- El **número de workers**, que corresponde directamente al número de **DPUs** — la base sobre la que
  se factura (DPU-horas).

## Límite mínimo de DPUs para Spark

Al intentar reducir el número de workers a **1** y guardar el job, aparece un error indicando que el
**valor mínimo permitido de número de workers es 2** para este tipo de job (Spark).

- Para usar menos de 2 DPUs, es necesario cambiar a un **tipo de job distinto**, por ejemplo un
  **Python Shell Job**.

## Reducir costes con Flex execution

También se puede marcar la opción de ejecución **Flex** directamente en los detalles del job, para
ahorrar costes en trabajos **menos sensibles al tiempo** — el job podría ejecutarse algo más tarde de
lo programado, a cambio de reducir el coste.

## Elegir el motor manualmente con el Script editor

Si se crea el job de forma visual, Glue genera automáticamente el script equivalente por debajo. Como
alternativa, se puede usar el **Script editor** para:

- Elegir manualmente el motor (por ejemplo, crear un job de tipo **Ray**).
- Escribir el script desde cero, con control total sobre el código.
