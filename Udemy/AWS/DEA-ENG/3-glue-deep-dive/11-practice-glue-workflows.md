# Práctica: Glue Workflows

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En esta práctica se crea y configura un **Glue Workflow** desde la interfaz gráfica de Glue, para
orquestar **Crawlers** y **Jobs** usando **Triggers**, incluyendo tanto un disparador bajo demanda como
un disparador programado.

## Crear un workflow en blanco

1. En **Glue → Workflows**, añadir un nuevo workflow **en blanco** (blank workflow).
2. Darle un nombre sencillo (ej. `workflow`).
3. Opcionalmente se pueden configurar propiedades adicionales:
   - **Max concurrency**: número máximo de ejecuciones concurrentes.
   - **Tags**, etc.
4. Crear el workflow y abrirlo para configurarlo mediante la **interfaz gráfica** (el editor visual de
   nodos).

## Añadir el primer trigger

> ⚠️ Todo workflow debe empezar siempre con un **Trigger**: no se puede añadir un Job o Crawler como
> primer nodo directamente.

Al añadir el primer trigger se puede elegir uno existente o crear uno nuevo. En esta práctica se crea
uno nuevo de tipo **On-demand** (ej. nombrado `trigger-on-demand`).

Recordatorio de los tipos de trigger disponibles en este punto:

- **Schedule**: ejecución diaria, semanal, o con una frecuencia personalizada mediante **expresión
  cron**.
- **Event**: se activa a partir de la salida de un componente anterior (un Job o Crawler) — se ve más
  adelante en esta misma práctica.
- **On-demand**: ejecución manual desde la consola de Glue. Se puede combinar con otros servicios, por
  ejemplo una regla de **EventBridge** o una función **Lambda** que invoque el workflow.

Con el trigger on-demand añadido, ya se podría ejecutar el workflow manualmente desde este punto.

## Añadir un Job al workflow

- Se añade un nuevo nodo de tipo **Job** (o Crawler), eligiendo el primer ETL Job ya creado en
  prácticas anteriores.
- Este nodo queda conectado al trigger inicial.

## Encadenar un trigger basado en eventos

Para añadir un componente que dependa del resultado del Job, hay que añadir un **nuevo trigger** de
tipo **Event**, seleccionando el nodo del Job como origen del evento:

- **Trigger logic** (lógica de disparo): con **múltiples** eventos conectados a un mismo trigger, se
  puede configurar para que se dispare después de **cualquier** evento observado (`any`) o después de
  **todos** los eventos observados (`all`) — por ejemplo, si hay 5 Jobs distintos y se quiere esperar a
  que todos terminen con éxito antes de continuar.
- Con un único evento conectado, esta lógica es indiferente (`any` = `all`).
- Se le da nombre al trigger (ej. `segundo-disparador`).

### Configurar el evento observado (watched event)

Al seleccionar el trigger se puede ver y editar el **watched event**: la condición exacta que dispara
el trigger, referida a un nodo anterior concreto:

- **Succeeded**: se dispara cuando el Job/Crawler anterior termina con **éxito**.
- **Failed**: se dispara cuando el Job/Crawler anterior **falla**.

Esta condición se puede cambiar en cualquier momento seleccionando el trigger y editando el "watched
event" (por ejemplo, cambiar de `Failed` a `Succeeded` o viceversa), y el nodo se actualiza en el
editor visual reflejando la nueva condición.

## Añadir un Crawler tras el segundo trigger

- Tras el segundo trigger (basado en el evento del Job), se añade un nodo de tipo **Crawler**: se
  ejecutará cuando se cumpla la condición configurada en ese trigger (en este caso, tras el éxito del
  Job).
- Se pueden seguir añadiendo componentes adicionales de dos formas:
  - Añadiendo **Jobs o Crawlers adicionales para disparar** desde el propio trigger.
  - Añadiendo **Jobs o Crawlers adicionales a vigilar** desde el propio trigger (para que también
    formen parte de la condición de disparo).
  - O simplemente usando el editor visual para conectar nuevos nodos directamente.

> El editor visual puede resultar algo confuso al principio (hay varias formas de llegar al mismo
> resultado), pero el concepto de fondo es sencillo: triggers que conectan Jobs y Crawlers entre sí.

## Cambiar el trigger inicial a uno programado

Como alternativa al trigger on-demand, se puede:

1. Eliminar el trigger on-demand inicial.
2. Añadir un nuevo trigger de tipo **Schedule** (ej. `trigger-de-prueba`), configurado para ejecutarse
   de forma **diaria**.
3. Conectar el Job al nuevo trigger seleccionándolo y usando **Actions → Add jobs to trigger**, eligiendo
   el Job correspondiente para asociarlo al workflow.

## Limpieza

> ⚠️ Al haber configurado un trigger de tipo **Schedule** (ejecución diaria), y para evitar incurrir en
> costes por ejecuciones automáticas no deseadas, se elimina el workflow completo al finalizar la
> práctica.

## Conclusión

Se ha creado y configurado un Glue Workflow combinando triggers de tipo **on-demand**, **event** y
**schedule** con Jobs y Crawlers, demostrando cómo orquestar distintos componentes de Glue entre sí
usando condiciones de éxito/fallo.
