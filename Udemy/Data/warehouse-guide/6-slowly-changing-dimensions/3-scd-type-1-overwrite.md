# SCD Type 1 — Overwrite

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es

En `SCD Type 1`, los cambios en un atributo se reflejan **sobrescribiendo** el valor antiguo con el
nuevo. La tabla de dimensión siempre refleja únicamente el **estado actual** — no conserva ningún
historial de los valores anteriores.

### Ejemplos

- El nombre de un producto cambia de "galletas de avena" a "deliciosas galletas de avena" → se
  actualiza el valor directamente en la fila existente.
- La categoría de un producto cambia (ej. de "dulces" a "galletas") → se actualiza el valor de
  categoría de la misma forma.

## Cómo se implementa

Es la estrategia **más simple** de las `SCD`: solo se actualiza (`UPDATE`) el valor en la fila
existente de la tabla de dimensión. No se requiere ningún cambio adicional en la `Fact Table` — las
claves foráneas siguen apuntando a la misma fila, que ahora simplemente tiene el valor actualizado.

## Limitaciones a tener en cuenta

### 1. Se pierde el historial

Una vez aplicado el cambio, ya no es posible ver cómo se agrupaban los datos con el valor anterior.
Por ejemplo, si la categoría de un producto cambia de "dulces" a "galletas", todo el histórico de
ventas de ese producto pasará a contarse bajo "galletas" — la categoría "dulces" mostrará menos ventas
de las que realmente tuvo en su momento.

> ⚠️ Si el cambio es poco significativo (ej. un nombre de producto ligeramente distinto), esta
> pérdida de historial normalmente no afecta el análisis y se puede ignorar sin problema. Pero si el
> cambio es más relevante (ej. un cambio de categoría), hay que evaluarlo con más cuidado, ya que sí
> puede alterar la interpretación de reportes históricos.

### 2. Puede romper consultas o reportes existentes

Si hay lógica en `SQL` o en reportes que depende de un valor exacto — por ejemplo, una columna
calculada con `CASE WHEN` que compara contra un nombre específico — el valor actualizado podría dejar
de cumplir esa condición y romper esa consulta o reporte.

> ⚠️ Esto no suele ocurrir con la mayoría de los cambios, pero conviene revisar las consultas
> existentes cuando el cambio es delicado (ej. afecta a un valor usado en lógica condicional), para
> actualizarlas si es necesario.

## Resumen

| Tipo         | Estrategia                                    | Historial     | Complejidad de implementación |
| ------------ | ---------------------------------------------- | ------------- | -------------------------------- |
| `SCD Type 1` | Sobrescribir el valor antiguo con el nuevo.     | No se conserva | Muy baja — solo un `UPDATE`.     |
