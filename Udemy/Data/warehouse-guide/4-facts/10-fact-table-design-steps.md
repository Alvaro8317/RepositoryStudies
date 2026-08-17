# Pasos para diseñar una Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Idea general

A la hora de diseñar una `Fact Table` hay que tomar una serie de **decisiones clave**, y esas
decisiones se toman respondiendo a preguntas sobre las **necesidades del negocio**. A partir de esas
decisiones se puede establecer el diseño final de la tabla y sus columnas.

Solo hay **cuatro pasos clave** a seguir:

1. Identificar el proceso de negocio.
2. Definir el grano.
3. Identificar las dimensiones relevantes.
4. Identificar los hechos (`Facts`).

## 1. Identificar el proceso de negocio

Es el proceso que se quiere analizar: ventas, procesamiento de pedidos, cumplimiento de pedidos
(`order fulfillment`), o cualquier otro proceso de negocio relevante. Por ejemplo, una tabla de
ventas con todos sus aspectos asociados.

## 2. Definir el grano

El `Grain` es el nivel de detalle de la tabla — a qué corresponde cada fila. Es una decisión
**crucial**, ya que condiciona directamente qué tipo de análisis se puede hacer después.

Ejemplos de grano:

- Una fila = una transacción u orden concreta.
- Una fila = un período (ej. diario), como en una `Periodic Snapshot Fact Table`.
- Una fila = una combinación de período y otra dimensión (ej. diario **por ubicación**).

> ⚠️ Se recomienda usar el grano más fino posible (nivel más atómico, mayor detalle). Si los datos
> no vienen pre-agregados, esto deja abiertas todas las posibilidades de análisis futuro. Datos
> pre-agregados limitan de antemano cómo se pueden analizar más adelante. Con un grano
> transaccional atómico siempre es posible agregar después (por ejemplo, en `Data Marts` para casos
> de uso específicos), pero no al revés.

## 3. Identificar las dimensiones relevantes

Se identifican respondiendo a las preguntas clásicas: **qué**, **cuándo**, **dónde**, **cómo** y
**por qué** está ocurriendo el evento. A partir de ahí surgen dimensiones como tiempo, ubicación,
producto, cliente, etc. — lo que sea relevante en el escenario de negocio.

Las dimensiones son los puntos de entrada para el análisis de datos: dan la capacidad de **filtrar**
y **agrupar**. Por eso a veces se las llama el "alma" (*soul*) del data warehouse para el análisis
de datos.

## 4. Identificar los hechos (Facts)

Por último, se identifican las medidas (`Facts`) y, si hace falta, se agregan según el grano ya
definido.

## Resumen

| Paso | Pregunta que responde                       |
| ---- | ------------------------------------------- |
| 1    | ¿Qué proceso de negocio se quiere analizar? |
| 2    | ¿A qué corresponde cada fila? (grano)       |
| 3    | ¿Qué, cuándo, dónde, cómo, por qué?         |
| 4    | ¿Qué se mide?                               |

## Próxima clase

Se profundizará en los aspectos ETL relacionados con las tablas de hechos.
