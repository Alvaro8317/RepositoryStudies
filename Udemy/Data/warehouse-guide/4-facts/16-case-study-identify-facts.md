# Caso práctico: paso 4 — identificar los hechos

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Contexto

Cuarto y último paso del framework visto en [[10-fact-table-design-steps]], continuando el
[[15-case-study-identify-dimensions]]. Se trata de identificar las medidas relevantes para el
rendimiento que se quiere analizar.

> ⚠️ Los hechos deben **cumplir con el grano** ya definido. Si aparece una métrica que no encaja con
> el grano pero se considera necesaria, hay que volver al paso 1 y reevaluar el diseño desde el
> principio — no forzar la métrica en el grano actual.

En este caso, todas las medidas identificadas sí cumplen con el grano (línea de pedido): por
ejemplo, el importe de venta (`Sales Amount`) es simplemente el importe de esa fila concreta.

## Aditividad: el criterio clave

En este paso también se pueden **eliminar** hechos innecesarios o **añadir** hechos calculados a
partir de los ya existentes. El criterio principal a la hora de decidir qué guardar es la
**aditividad** — ver [[1-fact-additivity-types]] —, ya que determina cuánto valor analítico aporta
un hecho al poder agregarse libremente a través de las dimensiones.

| Hecho                        | Aditividad                                  | Decisión                                                                                                                                                      |
| ---------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Sales Amount`               | Aditivo                                     | Se mantiene.                                                                                                                                                  |
| `Product Cost`               | Aditivo                                     | Se mantiene.                                                                                                                                                  |
| `Unit Price`                 | Semi-aditivo (hay que tener cuidado)        | Se mantiene, pero se advierte a los usuarios de negocio que no debe sumarse directamente para obtener un total — para eso está `Sales Amount`.                |
| `Discount Amount` (absoluto) | Aditivo (una vez multiplicado por cantidad) | Se **añade** como hecho derivado: precio unitario menos precio con descuento, multiplicado por la cantidad.                                                   |
| `Discount %` (porcentaje)    | **No aditivo**                              | Se **descarta** — los porcentajes/ratios no son aditivos (ver [[1-fact-additivity-types]]); mejor calcularlo en la herramienta de BI (ej. Power BI, Tableau). |
| `Profit` (beneficio)         | Aditivo                                     | Se **añade** como hecho derivado: `Sales Amount` menos (`Product Cost` × cantidad).                                                                           |

> ⚠️ Aunque `Profit` podría calcularse directamente en la herramienta de BI, almacenarlo físicamente
> en el `Data Warehouse` reduce el riesgo de cálculos inconsistentes entre usuarios — todos ven
> exactamente el mismo número, sin depender de cómo cada quien lo calcule.

## Diseño final de la tabla de hechos

**Dimensiones asociadas**: `Website`, `Customer`, `Product`, `DateTime` (ver
[[15-case-study-identify-dimensions]]).

**Hechos finales**: cantidad (`Quantity`), precio unitario (`Unit Price`), descuento
(`Discount Amount`), importe de venta (`Sales Amount`), coste del producto (`Product Cost`) y
beneficio (`Profit`).

Con esto queda completo el diseño de la `Fact Table` del caso práctico, siguiendo los cuatro pasos
del framework.

## Próxima sección

El curso continúa profundizando en las dimensiones.
