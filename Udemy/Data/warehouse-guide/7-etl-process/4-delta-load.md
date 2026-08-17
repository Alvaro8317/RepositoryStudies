# Carga Delta (Delta Load)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Una vez cargados todos los datos con la `Initial Load`, la `Delta Load` es el proceso que carga los
datos **de forma incremental** y con regularidad (por ejemplo, una frecuencia diaria o cada noche):
solo los datos nuevos del sistema fuente que aún no se han cargado, primero hacia `Staging` y luego
hacia `Core`.

> ⚠️ El workflow de `ETL` no cambia entre la `Initial Load` y la `Delta Load` — es el mismo proceso,
> con las mismas transformaciones. La diferencia es que ahora se ejecuta periódicamente y se aplica un
> filtro sobre una columna delta, de forma que no se cargan siempre todos los datos, sino solo los que
> no se han cargado antes.

## La columna Delta

Para poder configurar una `Delta Load` se necesita una **columna Delta** disponible en cada tabla del
`Data Warehouse`. Normalmente es una `timestamp` de la transacción o algún tipo de fecha de creación
— idealmente una `timestamp` (una fecha por sí sola es menos precisa). Esta columna suele estar ya
disponible en los sistemas fuente, y con ella se pueden identificar los datos nuevos que aún no se han
cargado.

### Cómo funciona en la práctica

1. En cada ejecución del `ETL` se recuerda (normalmente en una variable) el **valor máximo** de la
   columna delta que se cargó — por ejemplo, si la última ejecución cargó hasta la fila con clave de
   venta `4`, se guarda `x = 4`.
2. En la siguiente ejecución, al leer los datos del sistema fuente, se aplica un filtro con ese valor
   (ej. `clave_venta > 4`), de modo que solo se carguen las filas nuevas (ej. la fila `5`).

## Alternativas cuando no hay columna Delta

Lo habitual es contar con una columna delta (normalmente una `timestamp`), pero cuando los datos no
están en buena forma y no hay una disponible, existen alternativas:

- **Clave incremental**: se puede usar una clave primaria en lugar de una `timestamp`, pero solo si
  es un número realmente incremental — no sirve si es una `Natural Key` con un conjunto de números
  arbitrario.
- **Captura automática vía metadatos**: algunas herramientas `ETL` pueden identificar automáticamente,
  a partir de metadatos, qué datos son nuevos o se han modificado — en ese caso no hace falta
  preocuparse por definir una columna delta manualmente. No suele ser la situación más común.
- **Full Load** (carga completa) en cada ejecución: se cargan todos los datos de nuevo y se comparan
  con los ya cargados para detectar cambios o columnas nuevas. Esto ocurre típicamente en tablas de
  **dimensiones** (que normalmente no tienen `timestamp`), y no tanto en tablas de hechos (que sí
  suelen tenerla).

> ⚠️ Si se opta por un `Full Load`, hay que tener cuidado con el **rendimiento**: cuánta carga se pone
> sobre el sistema fuente y en qué momentos se puede ejecutar. Como normalmente se trata de tablas de
> dimensiones, que no suelen ser enormes, el impacto suele ser manejable — o se puede programar por la
> noche, cuando hay margen para poner algo de carga sobre los sistemas fuente.

## Impacto en el tiempo de ejecución del ETL

> ⚠️ Cuantos más datos se cargan, más tiempo toma el proceso `ETL` — algo especialmente crítico si el
> negocio pide una frecuencia muy alta de actualización.

Por ejemplo, si el negocio solicita actualizar los datos cada 30 minutos pero la carga (por ejemplo,
por incluir `Full Loads`) toma 40 minutos, es una limitación con la que hay que convivir. Por eso, al
decidir usar un `Full Load`, conviene evaluar también si el tamaño de la tabla lo permite dado el
tiempo disponible entre ejecuciones.

## Próximas clases

Ver cómo se aplica todo esto en la práctica.
