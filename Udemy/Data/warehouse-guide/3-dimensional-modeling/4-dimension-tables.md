# Dimension Tables

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Propósito de las dimensiones

En el `Star Schema`, las `Dimension Tables` están agrupadas alrededor de la `Fact Table`. Su
propósito es **categorizar los hechos** para darles un contexto significativo — sin dimensiones, una
medida como "cantidad total de unidades vendidas" no dice mucho por sí sola.

El carácter de una dimensión es **descriptivo y de apoyo**, no medible. Sus tres objetivos
principales sobre los hechos son:

- **Filtrar**
- **Agrupar**
- **Etiquetar**

A este trío de operaciones se le suele llamar coloquialmente **"cortar y trocear"** (`slice and
dice`) los datos — por ejemplo, usar una dimensión como filtro en un reporte, o para agrupar
valores en un gráfico de barras.

## Cómo distinguir una dimensión de un hecho

| Característica      | Fact                                            | Dimension                                                           |
| ------------------- | ----------------------------------------------- | ------------------------------------------------------------------- |
| ¿Agregable?         | Sí                                              | **No**, incluso si el valor es numérico.                            |
| ¿Numérica?          | Sí, típicamente                                 | Puede ser numérica o no — pero eso no la hace agregable.            |
| Carácter            | Medible                                         | Descriptivo                                                         |
| Naturaleza del dato | Ligado a eventos/transacciones — cambia seguido | Más **estática** — normalmente no cambia (aunque sí puede hacerlo). |

> ⚠️ Que una dimensión sea numérica no la convierte en agregable. Ejemplo clásico: el `año` en una
> dimensión de fecha es numérico, pero sumar `2019 + 2020` no produce ninguna información útil —
> sigue siendo una dimensión, no un hecho.

## Estructura de una Dimension Table

- Tiene su propia **clave primaria**, que identifica de forma única cada fila de la dimensión.
- A veces también puede tener una **clave foránea adicional** — esto se vuelve relevante más
  adelante al hablar de `Snowflake Schema`.

## Casos de uso comunes

Ejemplos típicos de dimensiones:

- Personas: empleados, clientes, gerentes.
- Productos y categorías de producto.
- Lugares: regiones, ciudades, direcciones.
- Tiempo/fecha.

Ejemplo de dimensión de cliente: una tabla con `customer_id` como clave primaria, y columnas
descriptivas adicionales (nombre, segmento, etc.).

> ⚠️ Las dimensiones también pueden cambiar con el tiempo (ej. un cliente cambia de dirección). Este
> caso se trata como un tipo específico de dimensión: `Slowly Changing Dimension` (`SCD`), que se
> cubrirá en detalle más adelante en el curso.

## Próxima clase

Profundizar en los esquemas usados para organizar hechos y dimensiones: `Star Schema` y `Snowflake
Schema`.
