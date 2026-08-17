# Fact Tables

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Los hechos en el Star Schema

En un `Star Schema` (el esquema más común al modelar datos de forma dimensional en un `Data
Warehouse`), la `Fact Table` está en el **centro**, con las `Dimension Tables` agrupadas a su
alrededor. Por ejemplo, una tabla de hechos de ventas rodeada de dimensiones como cliente, producto
o fecha.

La `Fact Table` es la **base** del `Data Warehouse`: contiene las **mediciones clave del negocio**
(ej. ventas, beneficio, unidades vendidas). Estos hechos son los que normalmente se quieren
**agregar** y analizar a través de las dimensiones.

## Cómo reconocer un hecho

La distinción entre hechos y dimensiones no siempre es obvia. Algunas señales que suelen (no
siempre) ayudar a identificar un hecho:

- **Aditivo**: se puede sumar y el resultado sigue teniendo sentido de negocio (ej. sumar unidades
  vendidas da la cantidad total vendida). Los hechos suelen ser, en general, agregables de alguna
  forma.
- **Numérico**, no descriptivo — a diferencia de una dimensión, que aporta contexto descriptivo, un
  hecho es algo **medible**.
- Suele estar basado en un **evento o transacción** (ej. una venta): algo que "sucede" en un momento
  determinado.

> ⚠️ Como los hechos suelen estar ligados a eventos/transacciones, es común que una `Fact Table`
> incluya una columna de fecha/hora. Pero esa columna de fecha en sí **no es un hecho** — es la
> referencia a la dimensión de fecha, no una medida.

## Estructura de una Fact Table

Una tabla de hechos típicamente contiene:

1. Una **clave primaria** que identifica de forma única cada fila.
2. Múltiples **claves foráneas**, cada una apuntando a una tabla de dimensión.
3. Los **hechos** en sí (las medidas: ventas, beneficio, presupuesto, etc.).

## El grano (Grain)

El **grano** (`Grain`) de una tabla de hechos es su **nivel más atómico**: qué representa
exactamente cada fila.

Ejemplo: una tabla de hechos con una fila por cada combinación de **región** y **día**, conteniendo
el beneficio de esa región en esa fecha. En este caso, el grano es "beneficio por región y por día"
— ese es el nivel más granular que la tabla puede representar.

> ⚠️ Existen distintas variaciones/tipos de hechos (se tratarán más adelante en el curso, con más
> detalle).

## Próxima clase

Profundizar en las **dimensiones** (`Dimension Tables`): qué son y qué las distingue de los hechos.
