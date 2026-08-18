# Índices: introducción y por qué mejoran el rendimiento

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Una vez configurado el `Data Warehouse`, puede ocurrir que los usuarios de negocio experimenten un
mal rendimiento en sus consultas: tienen que esperar mucho tiempo para obtener resultados o informes,
o para recuperar datos al trabajar directamente en la base de datos. Lo primero en lo que hay que
pensar para mejorar el rendimiento de las consultas es en usar **índices**.

## El problema: cómo se almacenan los datos sin índices

En una tabla, los datos no se almacenan en ningún orden sistemático, sino allí donde haya espacio
libre disponible en disco. Esto es muy eficiente para **escribir** datos, pero problemático para
**recuperarlos**: si se filtra, por ejemplo, por un cliente concreto, la consulta tiene que recorrer
toda la tabla fila por fila, sin saber de antemano cuándo puede dejar de buscar (`full table scan`).

> ⚠️ Un `full table scan` es muy ineficiente para obtener datos, y en tablas grandes suele ser la
> parte que más tiempo consume de toda una consulta — por eso optimizarlo aporta tanto valor.

## Qué es un índice

Un índice almacena los datos de una columna en un **orden específico**, junto con un puntero a la
ubicación real de cada fila. Por ejemplo, un índice sobre el `ID` de cliente podría verse así:

| Valor de ID de cliente | Fila donde empieza |
| ---------------------- | ------------------ |
| 4                      | Fila 1             |
| 5                      | Fila 2             |
| 8                      | Fila 5             |

Con esta estructura ordenada y sus punteros, una consulta puede ir directamente a la ubicación
correspondiente en vez de escanear toda la tabla, haciendo la lectura de datos mucho más rápida.

## Ventajas y desventajas

- ✅ **Lecturas mucho más rápidas**: se evita el `full table scan`.
- ⚠️ **Escrituras y actualizaciones más lentas**: al insertar o actualizar datos, también hay que
  mantener el índice ordenado, en vez de poder escribir los datos donde haya espacio libre.
- ⚠️ **Más espacio de almacenamiento**: cada índice adicional ocupa espacio extra en disco — usar
  muchos índices distintos puede suponer un coste de almacenamiento considerable.

## Tipos de índices a cubrir

En las próximas clases se verán dos tipos de índices y, después, algunas directrices prácticas sobre
cuándo y cómo usarlos:

- **Índice `B-tree`** — el índice estándar por defecto.
- **Índice de mapa de bits** (`Bitmap Index`) — especialmente útil en `Data Warehouses`.

## Próximas clases

Ver en detalle cómo funcionan los índices `B-tree` y los índices de mapa de bits.
