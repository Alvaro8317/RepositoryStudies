# ¿Por qué usar el modelado dimensional?

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El objetivo: recuperación rápida de datos

El objetivo del modelado dimensional es la **recuperación rápida de datos**, lo cual se traduce en
dos beneficios concretos: mejor **rendimiento** de consulta y mejor **usabilidad**. Para entender de
dónde vienen ambos beneficios, conviene ver un ejemplo práctico.

## El problema: una tabla ancha con datos repetidos

Supongamos una única tabla de siete columnas donde queremos calcular el beneficio total (agregar).

- Una base de datos explora las tablas **por filas**, ya que así se almacenan los datos.
- Las tablas **anchas** (muchas columnas) tienen peor rendimiento de consulta que las tablas
  **estrechas**, incluso con optimizadores de consultas de por medio.
- Además, mantener toda la información en una única tabla ancha genera **datos duplicados**
  innecesarios: por ejemplo, el nombre de un mismo cliente o de un mismo producto se repite en cada
  fila donde aparece esa venta.

> ⚠️ Ni el ancho de la tabla ni la duplicación de datos son gratuitos: ambos factores degradan el
> rendimiento de las consultas.

## La solución: separar en hechos y dimensiones

En vez de mantener todo en una sola tabla ancha, se separa la información relacionada en tablas de
**dimensiones** independientes:

- Información de cliente (ej. nombre) se mueve a una **dimensión de cliente**, dejando solo el
  `ID` de cliente como clave foránea en la tabla de hechos.
- Información de producto y categoría se mueve a una **dimensión de producto**, de la misma forma.
- Información de fecha (ej. un `ID` de fecha compuesto por año, mes y día) se mueve a una
  **dimensión de fecha**.

Cada tabla de dimensión tiene su propia clave primaria, y la tabla de hechos guarda la clave
foránea correspondiente que apunta a ella.

## Los dos beneficios resultantes

| Beneficio       | Por qué se obtiene                                                                                                                                                                                                                                                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rendimiento** | Tablas más estrechas y sin duplicación de datos redundante — más eficientes de escanear y agregar.                                                                                                                                                                                                  |
| **Usabilidad**  | Los datos quedan organizados en **unidades lógicas** (toda la info de producto junta, toda la de fecha junta, etc.), en vez de dispersos entre cientos de columnas de una tabla de hechos. Esto facilita mucho encontrar la información relevante y desglosar (`by month`, `by day of week`, etc.). |

## Conclusión

El modelado dimensional se hace precisamente para lograr esta recuperación rápida de datos: alto
rendimiento de consulta y alta usabilidad, gracias a estructurar los datos en tablas de hechos y
tablas de dimensiones. Por eso es la técnica preferida en un `Data Warehouse`, donde los datos se
usan para reporting y casos de uso `OLAP` que exigen justamente eso.

## Próxima clase

Profundizar en el detalle de las tablas de hechos (`Fact Tables`) y las tablas de dimensiones
(`Dimension Tables`).
