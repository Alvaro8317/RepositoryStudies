# Probar la carga Delta y unificar el ETL

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con el `Job` de `Core` funcionando para la carga completa inicial (ver
[[8-assembling-the-core-job]]), toca probar que la **`Delta Load`** también funciona correctamente, y
unificar todo el flujo `ETL` en un único `Job` padre.

## 1. Añadir datos nuevos al sistema fuente

Para poder probar la carga incremental, primero hace falta tener datos nuevos en el origen que aún no
se hayan cargado:

1. En `pgAdmin`, sobre la tabla `sales` del esquema `public`, clic derecho → `Import` con el archivo
   de datos adicionales correspondiente.
2. Marcar cabecera (`Header`) y delimitador coma, igual que en la carga inicial.

> ⚠️ Si la importación falla porque ya hay columnas configuradas de una importación previa, hay que
> revisar y volver a mapear manualmente las columnas del archivo (en este caso: `quantity` y `price`)
> antes de reintentar.

Al consultar la tabla de origen ordenando por las filas más recientes, se confirma que ahora hay datos
nuevos (de mayo de 2022) que **todavía no están** en la capa `Core`.

## 2. Activar la lógica real de Delta Load

En la transformación `SetLastLoad Sales` (ver [[4-staging-sales-delta-load]]), se había fijado
manualmente un valor "dummy" (`1970-01-01`) para forzar la carga completa inicial. Ahora se activa la
consulta real, comentada hasta ahora, que obtiene el **valor máximo** real de la columna delta ya
cargada en `Core`.

Se verifica con `Preview` que el valor obtenido es el esperado, se guarda la transformación, y se
vuelve a ejecutar todo el flujo: primero `Staging_job`, y después `core_job`.

## 3. Unificar el ETL en un Job padre

Se crea un nuevo `Job` que actúa como orquestador (`Job` padre), incluyendo:

1. Un paso `Job` que ejecuta `Staging_job`.
2. Un paso `Job` que ejecuta `core_job`.

Se guarda como `CompleteETLprocess`.

## 4. Verificar el resultado

Al ejecutar `CompleteETLprocess`, no aparecen errores. Al consultar `core.sales` ordenando por
`transaction_id` en orden **descendente** (para ver primero las filas más recientes), se confirma que
los nuevos datos de mayo de 2022 ya están cargados correctamente en `Core`.

> ⚠️ Si al revisar los datos nuevos parecen no estar ahí, puede ser solo un problema de **orden** en
> la consulta (los datos más recientes quedan al final si no se ordena explícitamente) — no
> necesariamente un fallo real del `ETL`.

Con esto, el flujo `ETL` completo del caso práctico queda probado de punta a punta: extracción desde
el sistema fuente, modelado dimensional, y carga incremental en el `Data Warehouse`.
