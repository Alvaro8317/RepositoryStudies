# Amazon Athena — Apache Iceberg y transacciones ACID

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Por defecto, las tablas de Athena (basadas en Hive) **no soportan transacciones ACID** —
operaciones como `UPDATE` o `DELETE` fila a fila no están garantizadas de forma atómica y
consistente.

Athena soporta transacciones ACID: **garantías estrictas** sobre las transacciones, de modo que
varios **usuarios concurrentes** pueden acceder a la misma fila al mismo tiempo y todo funciona de
forma **consistente**.

Bajo el capó, este soporte se implementa con **Apache Iceberg**, que facilita la gestión y
optimización de tablas en un entorno de almacenamiento distribuido.

## Cómo activarlo: `table_type = 'ICEBERG'`

Para tener soporte de **transacciones ACID** en Athena, la tabla debe crearse con el formato de
tabla **Apache Iceberg**, especificando `table_type = 'ICEBERG'` al crear la tabla:

```sql
CREATE TABLE mi_tabla (
    ...
)
LOCATION 's3://mi-bucket/mi-tabla/'
TBLPROPERTIES (
    'table_type' = 'ICEBERG'
);
```

> ⚠️ Sin especificar `table_type = 'ICEBERG'`, Athena no soporta transacciones ACID sobre la
> tabla — es este parámetro el que activa dicho soporte.

Con esto, varios usuarios pueden acceder a las mismas filas y hacer **modificaciones o
eliminaciones a nivel de fila** de forma totalmente segura, sin pisarse entre ellos.

## Compatibilidad

El formato de tabla Apache Iceberg es compatible con:

- **Amazon EMR**.
- **Apache Spark**.
- Cualquier otra plataforma que soporte el formato de tabla **Apache Iceberg**.

## Alternativa: tablas gobernadas (governed tables) de Lake Formation

Las **tablas gobernadas (governed tables)** de **AWS Lake Formation** son otra forma de conseguir
soporte ACID, en este caso sobre tablas S3 gestionadas desde Lake Formation — es una vía
alternativa a Iceberg para obtener esta misma característica.

## Compactación periódica (periodic compaction)

- Reescribe y reorganiza los datos automáticamente para buscar el **mejor rendimiento en las
  consultas** y mantener la **eficiencia de almacenamiento**.
- Se aplica sin interrumpir las modificaciones a nivel de fila que estén ocurriendo: los usuarios
  pueden seguir accediendo de forma concurrente y modificando filas sin comprometer la integridad
  de los datos.

## Operaciones de viaje en el tiempo (time travel)

Permiten recuperar **estados anteriores** de los datos de una tabla Iceberg, por ejemplo:

```sql
-- Consultar la tabla tal como estaba en un momento (timestamp) concreto
SELECT * FROM mi_tabla FOR TIMESTAMP AS OF TIMESTAMP '2026-08-01 00:00:00';

-- Consultar una versión (snapshot) concreta de la tabla
SELECT * FROM mi_tabla FOR VERSION AS OF 12345;
```

- Muy útil para **auditorías históricas** y para analizar los datos en distintos momentos del
  tiempo, manteniendo la integridad de los datos.
