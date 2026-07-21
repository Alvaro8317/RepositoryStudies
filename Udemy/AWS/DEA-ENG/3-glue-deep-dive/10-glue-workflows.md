# Orquestación con Glue Workflows

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son los Glue Workflows?

**Glue Workflows** es la opción de **orquestación** de AWS Glue: permite gestionar la ejecución de
**Crawlers** y **Jobs**, combinándolos entre sí, todo desde dentro del propio servicio de Glue.

Un workflow se compone de:

- **Crawlers**: rastrean una fuente de datos para poblar el Data Catalog.
- **Jobs**: los trabajos ETL (pueden ser varios dentro de un mismo workflow).
- **Triggers**: los desencadenantes que definen las condiciones entre los distintos componentes (por
  ejemplo, entre un Job y un Crawler, o entre Jobs sucesivos).

Por ejemplo, se puede configurar un Trigger que active un Crawler únicamente cuando un Job termine con
**éxito**, o un Trigger que active otro Job cuando el paso anterior termine con **error**.

> ⚠️ Glue Workflows es ideal para orquestar componentes **dentro de Glue** (Crawlers y Jobs). Si se
> necesita una orquestación más compleja que involucre además otros servicios de AWS de forma más
> amplia, la mejor opción es **AWS Step Functions** en lugar de Glue Workflows.

## Formas de crear un workflow

- De forma **visual**, usando la interfaz de Glue: permite ver el flujo de las distintas tareas,
  configurar los componentes y los triggers intermedios, y supervisar la ejecución de todo el workflow.
- A partir de un **Glue Blueprint**.
- Manualmente, usando la consola de Glue o la **API de Glue**.

## Triggers (desencadenantes)

Los triggers pueden iniciar tanto **Jobs** como **Crawlers** indistintamente — no hay diferencia en ese
sentido. Se activan típicamente cuando finaliza un Job o un Crawler anterior, y se pueden configurar
condiciones como:

- Activarse cuando el paso anterior se **completa con éxito**.
- Activarse cuando el paso anterior **falla**.

### Trigger de inicio (start trigger)

Cada workflow se inicia mediante un **trigger primario** (start trigger), del cual existen varios tipos:

| Tipo de trigger | Descripción |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schedule** | Inicia el workflow a intervalos regulares: programaciones predefinidas (diaria, semanal, mensual) o un periodo personalizado usando **expresiones cron**. |
| **On-demand** | Inicia el workflow manualmente desde la consola de Glue. También se puede combinar con una invocación externa, por ejemplo desde una función **Lambda**. |
| **EventBridge event** | Inicia el workflow en respuesta a eventos específicos capturados por **Amazon EventBridge** (arquitectura dirigida por eventos), por ejemplo al subir un archivo a un bucket S3. |

> El trigger **on-demand** es el más flexible para combinarlo con otros servicios: por ejemplo, una
> función Lambda puede invocar el workflow, o una regla de **EventBridge** puede gestionar el disparo
> desde fuera de Glue, permitiendo así construir arquitecturas dirigidas por eventos en tiempo real.

## Próximos pasos

En la siguiente clase se verá de forma práctica cómo crear y configurar un **Glue Workflow**.
