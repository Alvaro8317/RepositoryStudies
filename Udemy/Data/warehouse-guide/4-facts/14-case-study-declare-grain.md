# Caso práctico: paso 2 — declarar el grano

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Contexto

Segundo paso del framework visto en [[10-fact-table-design-steps]], continuando el
[[13-case-study-identify-business-process]]. El `Grain` define el nivel de detalle: a qué
corresponde una fila de la `Fact Table`.

## Decisión: grano atómico

Se recomienda usar el **grano atómico**, es decir, el máximo nivel de detalle disponible — es lo
que aporta el mayor valor analítico posible.

En este caso, una fila representa **una única línea de pedido dentro de un pedido concreto**: un
artículo del carrito del cliente. Esto convierte la tabla en una `Transactional Fact Table`, con la
máxima dimensionalidad posible.

## Comparativa: grano atómico vs. grano agregado

Si en vez del grano atómico se usara el nivel de **pedido** (una fila = un pedido completo), los
datos de varias líneas de pedido se agregarían en una sola fila:

| Grano                     | Filas para el pedido 2314 | Cantidad total | Importe total de venta |
| ------------------------- | ------------------------- | -------------- | ---------------------- |
| Línea de pedido (atómico) | 3 filas (una por línea)   | —              | —                      |
| Pedido (agregado)         | 1 fila                    | 6              | ~$88                   |

> ⚠️ Con el grano agregado por pedido se **pierden dimensiones** asociadas al nivel de detalle más
> atómico (ej. qué producto específico, a qué precio unitario). Por eso no es la opción ideal.

## Por qué usar el grano atómico

- Ofrece el **mayor valor analítico**, al no perder ninguna dimensión disponible en el sistema
  origen.
- El rendimiento **no suele ser un problema real**: las bases de datos actuales procesan con
  facilidad este volumen de datos.
- Deja la tabla **abierta a todos los casos de uso posibles**, incluyendo agregaciones futuras (que
  siempre se pueden derivar desde el grano atómico, pero no al revés).

## Próximo paso

Con el grano ya declarado, el siguiente paso es definir las dimensiones.
