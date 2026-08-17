# Transactional Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Los tres tipos de Fact Table

Existen solo tres tipos de `Fact Table`:

1. **`Transactional Fact Table`** — la más fundamental (este apunte).
2. **`Periodic Snapshot Fact Table`**.
3. **`Accumulating Snapshot Fact Table`**.

Entender bien la `Transactional Fact Table` facilita mucho entender los otros dos tipos, ya que es
la base sobre la que se comparan.

## Qué es una Transactional Fact Table

En una `Transactional Fact Table`, **cada fila representa un evento o una transacción** — algo que
ocurre en un momento y lugar determinados (ej. una transacción de venta, una llamada).

> ⚠️ La transacción es, literalmente, la definición del **grano**: una transacción = una fila.

### Ejemplos

**Transacción de venta**: cada fila es una venta individual.

- Medidas: `unidades vendidas` (y otras medidas asociadas a esa venta).
- Claves foráneas: producto, hora, fecha, y otras dimensiones relevantes.

**Llamada** (`call`): cada fila es una llamada individual (un evento).

- Medidas: duración de la llamada (y otras medidas del evento).
- Claves foráneas: las dimensiones correspondientes a esa llamada.

## Características

| Característica               | Detalle                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tipo más común               | Es el tipo de `Fact Table` más habitual en un `Data Warehouse`.                                                                                   |
| Alta flexibilidad analítica  | Suele tener **muchas claves foráneas** (muchas dimensiones asociadas), lo que permite analizar los datos desde muchos ángulos distintos.          |
| Hechos generalmente aditivos | Los valores medidos en este tipo de tabla suelen ser **completamente aditivos**, dando mucha flexibilidad para agregarlos en cualquier dimensión. |

## El principal reto

> ⚠️ Estas tablas pueden alcanzar un **tamaño enorme** y crecer muy rápido, ya que se agrega una
> fila por cada evento/transacción individual que ocurre. Por eso, a menudo es necesario **agregar**
> estas tablas (resumir a un grano menos detallado) para mantener un buen rendimiento de consulta.

## Próxima clase

El segundo tipo: `Periodic Snapshot Fact Table`.
