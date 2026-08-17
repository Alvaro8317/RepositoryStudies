# Natural Keys vs. Surrogate Keys

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Natural Key

Una `Natural Key` es la clave tal cual viene del sistema de origen. Por ejemplo:

- El `ID` de producto en una dimensión de producto: suele ser un valor alfanumérico voluminoso.
- El `ID` de transacción en una tabla transaccional: puede ser aún más grande.

Estas claves, tal como llegan del sistema origen, no son la forma ideal de gestionar los datos en
el `Data Warehouse` y traen varias desventajas asociadas.

## Surrogate Key

Una `Surrogate Key` (también llamada `Artificial Key`) es una clave **artificial**, generada
durante el proceso ETL — típicamente un simple número entero autoincremental, mucho más sencillo
que la `Natural Key` original.

Por convención, se suelen usar los sufijos `PK` (clave primaria) y `FK` (clave foránea) para
identificar de inmediato que una columna es una `Surrogate Key`.

> ⚠️ Generar la `Surrogate Key` durante el ETL suele ser un proceso muy sencillo (poco esfuerzo
> adicional), pero aporta bastantes beneficios — ver siguiente sección.

## Beneficios de usar Surrogate Keys

| Beneficio                                    | Detalle                                                                                                                                       |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Menor tamaño**                             | Un entero simple (puede ocupar tan poco como 4 bytes) frente a cadenas alfanuméricas largas — menos almacenamiento.                           |
| **Mejor rendimiento**                        | Como índice y en `JOINs`, los enteros son mucho más eficientes que claves alfanuméricas.                                                      |
| **Mejor manejo de valores ficticios**        | Si falta un valor (ej. una fecha inexistente), se puede usar un número negativo o muy alto reservado como `dummy value` de forma consistente. |
| **Integración de múltiples sistemas origen** | Si dos sistemas fuente usan el mismo valor de clave natural para entidades distintas, las claves duplicadas dejan de ser un problema.         |
| **Más fácil de gestionar y actualizar**      | Especialmente relevante en `Slowly Changing Dimensions`, donde actualizar valores es más simple con `Surrogate Keys`.                         |
| **Solución cuando no hay Natural Key**       | A veces el sistema origen simplemente no provee una clave natural — la `Surrogate Key` se genera igualmente de forma automática.              |

## Directrices prácticas

- Usar siempre `Surrogate Keys` como clave primaria (`PK`) y clave foránea (`FK`), tanto en tablas
  de hechos como en tablas de dimensiones.
- **Excepción**: la `Date Dimension`. Su clave es predecible por naturaleza, por lo que no hace
  falta generar una `Surrogate Key` — se puede seguir usando la clave de fecha directamente.
- Es válido **conservar también la `Natural Key`** como columna adicional (sobre todo en
  dimensiones, donde el volumen de datos no suele ser un problema), por si se necesita más adelante
  — aunque en la práctica rara vez hace falta.

## Resumen

Durante el proceso ETL se genera una `Surrogate Key` asignando un número entero simple a cada fila.
Esta práctica debe aplicarse de forma habitual en las tablas del `Data Warehouse`, con la excepción
de la `Date Dimension`.
