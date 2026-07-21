# Programación (Schedules) de ETL Jobs y Crawlers

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

Continuando con el **ETL Job** configurado en la clase anterior (ejecutado hasta ahora solo **on
demand**), en esta práctica se muestra cómo programar su ejecución de forma recurrente, y cómo hacer lo
mismo para un **Glue Crawler**.

> Nota: en esta demostración se crea un schedule y después se elimina, para no incurrir en coste por
> ejecuciones programadas innecesarias en una cuenta de práctica.

## Programar un ETL Job

1. Entrar en los **detalles del job** (Job details).
2. Ir a la pestaña/sección **Schedules**.
3. **Create schedule**, indicando:
   - **Nombre** del schedule (ej. `horario-mensual`).
   - **Frecuencia**: por ejemplo diaria, semanal o mensual.
     - Si es **diaria**: se especifica la hora y el minuto de inicio (ej. 03:30).
     - Si es **mensual**: además de la hora, se especifica el **día del mes** (ej. día 1, a las 03:30).
   - **Descripción** (opcional).
4. **Create schedule** para activarlo.

### Múltiples schedules

Es posible añadir **más de un schedule** al mismo job (ej. uno semanal y otro mensual en paralelo). No
es un escenario muy habitual — normalmente un job usa un único schedule —, pero está disponible para
casos con necesidades de programación muy personalizadas.

### Eliminar un schedule

Para eliminarlo: seleccionar el schedule → **Action → Delete** → confirmar. La eliminación tarda solo
unos segundos en reflejarse.

## Programar un Glue Crawler

El mismo concepto aplica a los **Crawlers**:

1. Ir al **crawler** ya configurado (creado previamente como on demand).
2. Editar sus propiedades y navegar al **paso 4 (Schedule)**.
3. Cambiar la frecuencia (ej. a **diaria**) con las mismas opciones vistas para el ETL Job (hora,
   minuto, día del mes según corresponda).

> En esta práctica no se llega a guardar la programación del crawler — el objetivo es solo mostrar que
> **tanto los ETL Jobs como los Crawlers admiten programación** con las mismas opciones de frecuencia.
