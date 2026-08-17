# ¿Qué es el modelado dimensional?

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Definición

El **modelado dimensional** (`Dimensional Modeling`) es un conjunto de métodos para organizar los
datos de una manera específica, habitualmente usada en un `Data Warehouse`.

Un `Data Warehouse` tiene requisitos particulares de **usabilidad** y **rendimiento**, ya que sus
datos se usan para reporting y casos de uso `OLAP`. El modelado dimensional suele ser el enfoque que
mejor se adapta a esos requisitos — las ventajas concretas se profundizarán en la siguiente clase.

## Hechos y dimensiones

En un modelo dimensional, todos los datos se organizan en **hechos** (`Facts`) o **dimensiones**
(`Dimensions`):

| Concepto                    | Qué representa                                                      | Ejemplos                                       |
| --------------------------- | ------------------------------------------------------------------- | ---------------------------------------------- |
| **Hecho** (`Fact`)          | Algo que se **mide**, típicamente agregable (ej. sumar, promediar). | Beneficio (`profit`), ventas.                  |
| **Dimensión** (`Dimension`) | **Contexto adicional** para interpretar la medición.                | Mes, período de tiempo, categoría de producto. |

Combinar un hecho con sus dimensiones convierte una simple medición en una **vista con
significado**: por ejemplo, "beneficio" (hecho) no dice mucho por sí solo, pero "beneficio **por**
año" o "beneficio **por** categoría de producto" (hecho + dimensión) sí aporta un análisis útil.

> ⚠️ La palabra clave "por" (`by`) suele delatar una dimensión: si una pregunta de negocio incluye
> "... por [algo]", ese "algo" (año, categoría, región, etc.) es casi siempre una dimensión.

## Star Schema

En este modelo, el hecho suele estar **en el centro**, rodeado de sus múltiples dimensiones — una
disposición visual que recuerda a una estrella, de ahí el nombre **`Star Schema`**. Este esquema, y
sus alternativas, se cubrirán en más detalle más adelante en el curso.

## Por qué importa

El modelado dimensional es una técnica pensada específicamente para el propósito de un `Data
Warehouse`: **recuperación de datos rápida**, orientada al rendimiento y la usabilidad — justo lo
que se necesita para reporting y casos de uso `OLAP`.

## Próxima clase

Profundizar en **por qué** se usa un modelo dimensional en el `Data Warehouse`: las ventajas
concretas que aporta.
