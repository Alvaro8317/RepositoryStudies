# Cálculos "to-date" (Year-to-Date, Month-to-Date, etc.)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Una petición común... y problemática

Los usuarios de negocio suelen pedir con frecuencia cálculos como `Year-to-Date` (`YTD`),
`Month-to-Date` (`MTD`), `Quarter-to-Date`, etc. — por ejemplo, "ingresos acumulados en lo que va
del año" — para verlos directamente en sus reportes de BI.

La tentación es **calcular estos valores de antemano y almacenarlos físicamente** como columnas en
el `Data Warehouse`. Esto es un error que hay que evitar.

## Por qué es problemático

> ⚠️ Un valor `to-date` (ej. `YTD`) **no respeta el grano** definido de la `Fact Table`.

Si el grano de la tabla es, por ejemplo, "ingresos por día", cada fila debe representar únicamente
el ingreso de **ese día específico**. Un valor `YTD` en esa misma fila representaría en realidad un
acumulado de *muchos* días — mezclando dos niveles de granularidad distintos en la misma tabla.

Esto se vuelve especialmente grave si los usuarios finales luego intentan **agregar** esos valores
(sumarlos a través de la dimensión de fecha, o de cualquier otra dimensión): al sumar valores que ya
son acumulados con otros valores del mismo tipo, el resultado queda **sobreestimado** y es
simplemente incorrecto.

## La alternativa correcta

En vez de almacenar el resultado ya calculado, se debe:

1. Almacenar únicamente el **valor subyacente**, en el grano definido de la tabla (ej. ingresos por
   día).
2. Calcular las variaciones `to-date` (`YTD`, `MTD`, `QTD`, etc.) **en la herramienta de consumo**:
   herramientas de BI como `Power BI` o `Tableau`, o incluso cubos `OLAP`, manejan este tipo de
   cálculos acumulados de forma nativa y correcta.

Este es el método preferido: nunca almacenar físicamente un cálculo `to-date` en el `Data
Warehouse` — calcularlo siempre en la capa de consumo, a partir del valor base correctamente
granular.

## Próxima clase

Profundizar en las distintas variaciones de tablas de hechos, empezando por el tipo más común: la
`Transactional Fact Table`.
