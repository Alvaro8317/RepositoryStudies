# Junk Dimensions

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El problema: banderas sueltas en la Fact Table

A veces una `Fact Table` transaccional tiene varios indicadores o banderas (`flags`) que en realidad
son dimensionales, pero que no encajan bien en ninguna dimensión existente. Por ejemplo, en una tabla
de transacciones de venta:

- Tipo de pago (¿entrante o saliente?)
- ¿Está asociada a una bonificación o no?

## Opciones para tratarlas

| Opción                                              | Cuándo tiene sentido                                                                                              | Problema                                                                                            |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Eliminarlas**                                     | Si no son relevantes para el análisis.                                                                            | No siempre es una opción — puede haber usuarios de negocio que sí las necesiten.                    |
| **Dejarlas tal cual en la Fact Table**              | Si son solo indicadores simples y no vale la pena crear una dimensión adicional.                                  | Si son valores de texto largos/voluminosos, la `Fact Table` puede crecer mucho en tamaño.           |
| **Crear una dimensión separada por cada indicador** | Cuando un indicador tiene suficiente peso propio.                                                                 | Si la `Fact Table` ya es muy ancha, añade más claves foráneas — peor para rendimiento y usabilidad. |
| **Crear una `Junk Dimension`**                      | Cuando hay varios indicadores de **baja cardinalidad** (pocos valores posibles) que no encajan en otra dimensión. | Riesgo de explosión combinatoria si hay demasiados indicadores — ver más abajo.                     |

## Qué es una Junk Dimension

Una `Junk Dimension` es una dimensión separada que agrupa **varios indicadores o banderas de baja
cardinalidad** (ej. valores sí/no, o solo 2-4 opciones posibles) que no encajan en ninguna otra
dimensión.

> Se puede pensar en ella como la caja en la que guardamos en casa objetos sueltos que no tienen un
> lugar propio — en vez de crear un espacio de almacenamiento separado para cada uno, los agrupamos
> todos juntos en una sola caja.
> ⚠️ El término "`Junk Dimension`" (dimensión basura) se usa normalmente solo entre consultores o
> modeladores de datos. Al hablar con clientes o usuarios de negocio, conviene usar un nombre más
> agradable, como `Transactional Indicator Dimension` (dimensión de indicadores transaccionales), para
> no dar a entender que los datos en sí son "basura".

## Cómo se implementa

Se reemplazan todos los indicadores de la `Fact Table` por una única clave foránea hacia la `Junk
Dimension`. Esa dimensión contiene una fila por cada **combinación posible** de los valores de esos
indicadores, con su propia clave primaria.

Con esto, los usuarios pueden seguir agrupando y filtrando fácilmente por cualquiera de esos
indicadores (ej. agrupar el importe por tipo de pago, o por si hubo bonificación), que es justamente
el objetivo del modelado dimensional.

## Cuidado con la explosión combinatoria

El número de filas de la `Junk Dimension` es el **producto** del número de valores posibles de cada
indicador. Por ejemplo, con indicadores de 3, 2 y 2 valores posibles respectivamente, el total es
3 × 2 × 2 = **12 combinaciones**.

> ⚠️ Este número puede crecer muy rápido: con 9 indicadores de 4 valores cada uno, se llega a más de
> **260,000 combinaciones** — una tabla demasiado grande para que tenga sentido.

### Cómo mitigarlo

- **Extraer solo las combinaciones que realmente ocurren**: en vez de generar todas las combinaciones
  teóricas, poblar la `Junk Dimension` únicamente con las combinaciones observadas en la `Fact Table`.
  Riesgo: alguna combinación rara podría no estar contemplada si nunca ha ocurrido en el pasado.
- **Dividir en varias Junk Dimensions**: en vez de agrupar todos los indicadores en una sola
  dimensión, repartirlos en dos (o más) dimensiones separadas. Esto reduce drásticamente el número
  total de combinaciones — por ejemplo, dividir en grupos de 5 indicadores en vez de 9 puede reducir
  el total a poco más de 1,000 combinaciones.

## ¿No añade esto complejidad innecesaria?

Una duda razonable: ¿por qué no simplemente dejar los indicadores en la `Fact Table`, aunque se
repitan las combinaciones? Al final, se cambia una tabla más ancha por una tabla adicional y un
`JOIN` extra.

El beneficio principal es de **almacenamiento y ancho de tabla**, no de "limpieza" por sí misma. En
una `Fact Table` transaccional con millones o miles de millones de filas, mantener los indicadores
inline significa repetir esos mismos valores (a veces texto) en cada fila. Con la `Junk Dimension`,
cada fila de la `Fact Table` solo guarda un entero (la `Surrogate Key`), y las combinaciones reales
viven una sola vez en una tabla pequeña — lo cual reduce bastante el tamaño físico de la tabla que
suele ser la más grande del modelo.

> ⚠️ El trade-off real es: una tabla más y un `JOIN` adicional en las consultas, a cambio de una
> `Fact Table` más angosta y más rápida de escanear. Si el volumen de filas es pequeño o solo hay uno
> o dos indicadores, esa complejidad extra no se justifica y dejarlos inline en la `Fact Table` es
> perfectamente razonable. La `Junk Dimension` tiene sentido sobre todo cuando hay **varios**
> indicadores de baja cardinalidad y la tabla de hechos es lo bastante grande como para que el ahorro
> de espacio y rendimiento pese más que la complejidad añadida.

## Resumen

Las `Junk Dimensions` sirven para agrupar indicadores/banderas de baja cardinalidad que no encajan en
otras dimensiones, evitando tanto una `Fact Table` demasiado ancha como una proliferación de
dimensiones pequeñas. El principal riesgo a vigilar es la explosión combinatoria de filas, que se
puede mitigar poblando solo las combinaciones reales o dividiendo los indicadores en varias
dimensiones.
