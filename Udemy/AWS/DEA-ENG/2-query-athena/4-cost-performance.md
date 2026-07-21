# Amazon Athena — Coste y rendimiento

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Modelo de coste

Athena cobra únicamente por lo que se utiliza:

- Se paga **por consulta**, en función de la **cantidad de datos escaneados** por esa consulta.
- Las **consultas fallidas no se cobran** — solo las que se llegan a ejecutar.
- Reducir el rendimiento (menos datos escaneados) reduce directamente el coste: son la misma
  optimización vista desde dos ángulos.
- Para cargas de trabajo predecibles, existe la opción de contratar **capacidad reservada**, como
  ahorro adicional frente al pago por consulta.

## Particionamiento y poda de particiones (partition pruning)

Particionar los datos es la optimización de rendimiento más importante en Athena.

- Los datos se estructuran en particiones dentro de la jerarquía de directorios de S3 (por ejemplo,
  por región o por fecha).
- Los metadatos de esas particiones se almacenan en el **Glue Data Catalog**.
- Cuando se ejecuta una consulta con un filtro (ej. `WHERE region = 'eu'` o un filtro por fecha),
  Athena aplica **poda de particiones (partition pruning)**: elimina, antes de procesar el resto de la
  consulta, las particiones que no son relevantes.
- Esto evita escanear datos innecesarios, mejorando rendimiento y coste a la vez.

Normalmente, antes de podar, Athena hace una llamada al Glue Data Catalog para obtener las particiones
(`GetPartitions`). Con un número muy alto de particiones, esta llamada puede afectar al rendimiento.

## Proyección de particiones (partition projection)

Es una técnica para evitar el coste de recuperar particiones del Glue Data Catalog en tablas muy
particionadas.

- En vez de mantener las particiones registradas manualmente en el Glue Data Catalog (o en un
  **Hive Metastore** externo), se configuran directamente en Athena.
- Se especifica un **rango de valores** y un **tipo de proyección** para cada columna de partición
  (por ejemplo, columnas de fecha o columnas numéricas con secuencias predecibles, como un ID).
- Durante la ejecución, Athena **proyecta** los valores de partición en lugar de recuperarlos del
  Data Catalog.

Ventajas:

- **Automatiza la gestión de particiones**: no hace falta añadir manualmente cada partición nueva.
- **Reduce el tiempo de ejecución de la consulta**, especialmente en tablas altamente particionadas.

## Índices de partición (partition indexes)

Athena también soporta **índices de partición** sobre el Glue Data Catalog:

- Sin índice, al consultar una tabla con muchas particiones, Athena debe recuperar **todas** las
  particiones disponibles del Data Catalog y luego determinar cuáles podar.
- Con un índice de partición configurado en el Glue Data Catalog, Athena puede obtener directamente
  un **subconjunto** de particiones en lugar de cargar la tabla de particiones completa.
- Esto mejora la planificación de la consulta y reduce su tiempo de ejecución, manteniendo la gestión
  dentro del Glue Data Catalog (a diferencia de la proyección de particiones, que la traslada a
  Athena).

## Reutilización de resultados de consulta (query result reuse)

Permite reutilizar el resultado de una consulta anterior en lugar de volver a escanear los datos.

- Athena ya almacena el resultado de cada consulta en S3 como un archivo CSV; esta función simplemente
  aprovecha ese resultado guardado.
- Se activa indicando una **edad máxima** aceptable del resultado (por ejemplo, hasta 60 minutos). Si
  existe un resultado dentro de ese margen para una consulta coincidente, se reutiliza directamente.
- Beneficios: menor coste (no se vuelve a escanear) y mayor rendimiento (respuesta inmediata).

Especialmente útil cuando:

- La fuente de datos no cambia con frecuencia.
- Se ejecutan consultas repetidas.
- El resultado es pequeño pero requiere escanear grandes volúmenes de datos para generarlo (consultas
  complejas sobre grandes datasets).

## Formato de los datos

- **Comprimir los datos** reduce su tamaño, lo que mejora el rendimiento y reduce tanto el volumen
  escaneado como el coste.
- Usar un **formato columnar** (en vez de CSV o JSON) para cargas analíticas:
  - **Parquet** o **Apache ORC** permiten recuperar datos más rápido y almacenarlos de forma más
    eficiente.
  - Al estar organizados por columnas, una consulta puede leer solo las columnas necesarias sin
    escanear las demás — a diferencia de un formato por filas (CSV), donde hay que recorrer la fila
    completa aunque solo interese una columna.

> ⚠️ Coste y rendimiento en Athena están directamente ligados: casi toda optimización de
> rendimiento (particionamiento, formatos columnares, compresión, reutilización de resultados) se
> traduce también en menos datos escaneados y, por tanto, menor coste.
