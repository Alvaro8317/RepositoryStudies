# Caso práctico: paso 1 — identificar el proceso de negocio

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Contexto

Primer paso del framework visto en [[10-fact-table-design-steps]], aplicado al
[[12-case-study-ecommerce-overview]]. Como este es el **primer** `Data Warehouse` de la empresa, hay
que decidir cuál es el proceso de negocio más adecuado para empezar.

## Criterios para elegir el proceso de negocio

- Elegir el proceso de negocio **más crucial** para la empresa.
- Tener en cuenta la **disponibilidad** y la **calidad** de los datos: si los datos de ese proceso
  son difíciles de acceder o de baja calidad, conviene evaluar otros procesos candidatos, sopesando
  su importancia relativa para el negocio frente a esa dificultad.

## Decisión: transacciones de ventas

Para este caso práctico, el proceso de negocio elegido son las **transacciones de ventas** (`Sales
Transactions`).

Este proceso permite analizar aspectos como:

- Qué productos se han vendido.
- El beneficio (`profit`) obtenido en las ventas, desglosado por categoría y por sitio web.
- El rendimiento general de ventas y de beneficio a lo largo de distintas características de fecha
  y del resto de dimensiones a crear.
- El rendimiento en el tiempo (`performance over time`).

## Próximo paso

Con el proceso de negocio ya identificado, el siguiente paso es declarar el `Grain` de la `Fact
Table`.
