# Staging de la Fact Table de ventas: carga Delta

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con las tablas ya creadas (ver [[3-setting-up-tables-in-pgadmin]]), toca configurar en `Spoon` (`PDI` /
`Pentaho Data Integration`) la puesta en escena (`Staging`) de la `Fact Table` de ventas.

> ⚠️ Al igual que ya se hizo para la dimensión de producto, se necesita un `Job` separado para
> `Staging` y otro distinto para `Core`: el flujo que ya lee desde `Staging` corresponde en realidad a
> la lógica de `Core`, así que aquí solo se construye la extracción hacia `Staging`.

## Transformación 1 — SetLastLoad

Para la `Delta Load` (ver [[../7-etl-process/4-delta-load]]), primero hace falta extraer el **valor
máximo** de la columna delta (`transactional_date`) que ya está cargado en la capa `Core`, y guardarlo
en una variable.

Se parte de la transformación equivalente ya creada para la dimensión de producto, y se adapta:

- En vez de `product_id`, se usa `transactional_date`.
- La fuente ya no es la dimensión de producto, sino la tabla `sales` de `Core`.
- Se renombra el alias del valor extraído de `max` a algo más descriptivo, ej. `last_load_date`.

> ⚠️ Al no haber datos todavía en `Core` la primera vez, hay que forzar manualmente un valor "dummy"
> muy antiguo para poder disparar una **carga completa inicial**. La consulta real de `Delta Load`
> (el `max` sobre `Core`) se deja comentada, para activarla más adelante una vez que ya haya datos
> cargados.

Se guarda la transformación como `SetLastLoad Sales`.

## Transformación 2 — GetLastLoad

1. **Get Variable**: se recupera la variable con `${last_load_date}`, con nombre de campo
   `last_load_date` y tipo `Timestamp` (importante configurarlo correctamente).
2. **Table Input**: se seleccionan los datos de origen (`public.sales`) con la condición:

   ```sql
   WHERE transactional_date > '${last_load_date}'
   ```

   > ⚠️ Al usar una variable dentro del SQL, hay que marcar la opción **"Replace variables in
   > script"** en el paso `Table Input`, o la variable no se sustituirá.

Se guarda como `GetLastLoad Sales`.

> ⚠️ En este punto, a esta transformación **todavía le falta el paso de salida** (`Table Output`) que
> escriba los datos en `Staging` — se añade en la siguiente clase, al integrarlo en el `Job`.

## Próximas clases

Integrar ambas transformaciones en el `Job` de `Staging` y probar el flujo completo.
