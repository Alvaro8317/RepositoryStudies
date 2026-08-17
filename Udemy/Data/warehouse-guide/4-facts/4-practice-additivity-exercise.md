# Práctica: identificar el tipo de aditividad de un hecho

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Ejercicio aplicando los tres tipos de aditividad vistos en [[1-fact-additivity-types]], sobre tres
tablas con grano "por producto y por día" (`Date`, `Product_FK`, y el hecho correspondiente).

## Pregunta 1: `Discount` — No aditivo

La tabla muestra el porcentaje de descuento de cada producto en un día dado.

| Date       | Product_FK | Discount |
| ---------- | ---------- | -------- |
| 20-07-2022 | 1          | 0%       |
| 20-07-2022 | 2          | 21%      |
| 20-07-2022 | 3          | 9%       |
| 20-07-2022 | 4          | 23%      |
| 21-07-2022 | 1          | 15%      |
| 21-07-2022 | 2          | 19%      |
| 21-07-2022 | 3          | 14%      |
| 21-07-2022 | 4          | 13%      |
| 22-07-2022 | 1          | 17%      |
| 22-07-2022 | 2          | 19%      |
| 22-07-2022 | 3          | 3%       |
| 22-07-2022 | 4          | 7%       |
| 23-07-2022 | 1          | 9%       |
| 23-07-2022 | 2          | 7%       |
| 23-07-2022 | 3          | 9%       |
| 23-07-2022 | 4          | 16%      |

**Respuesta: no aditivo.**

`Discount` es un **porcentaje**, y los porcentajes son uno de los ejemplos típicos de hechos no
aditivos ya mencionados en la clase teórica. Sumar los descuentos de varios productos (ej. `0% +
21% + 9% + 23%` del 20-07-2022) no produce ningún número con significado de negocio — no existe tal
cosa como "el descuento total". Ni siquiera tiene sentido sumarlos dentro de una misma fecha, que es
justo lo que distingue a un hecho no aditivo de uno semi-aditivo (que sí se puede sumar en *alguna*
dimensión).

## Pregunta 2: `Quantity sold` — Completamente aditivo

La tabla muestra cuántas unidades se vendieron de cada producto en un día dado.

| Date       | Product_FK | Quantity sold |
| ---------- | ---------- | ------------- |
| 20-07-2022 | 1          | 15            |
| 20-07-2022 | 2          | 24            |
| 20-07-2022 | 3          | 0             |
| 20-07-2022 | 4          | 19            |
| 21-07-2022 | 1          | 8             |
| 21-07-2022 | 2          | 21            |
| 21-07-2022 | 3          | 22            |
| 21-07-2022 | 4          | 17            |
| 22-07-2022 | 1          | 6             |
| 22-07-2022 | 2          | 32            |
| 22-07-2022 | 3          | 24            |
| 22-07-2022 | 4          | 22            |
| 23-07-2022 | 1          | 34            |
| 23-07-2022 | 2          | 21            |
| 23-07-2022 | 3          | 0             |
| 23-07-2022 | 4          | 33            |

**Respuesta: completamente aditivo.**

`Quantity sold` representa un **evento/flujo** (unidades vendidas *durante* ese día), no un nivel o
estado en un punto del tiempo. Esto es clave: se puede sumar en **cualquier** dimensión y el
resultado sigue teniendo sentido:

- **Sumar por fecha** (mismo producto, varios días): `15 + 8 + 6 + 34 = 63` unidades del producto 1
  vendidas entre el 20 y el 23 de julio — tiene sentido, es el total vendido en ese rango de fechas.
- **Sumar por producto** (misma fecha, varios productos): `15 + 24 + 0 + 19 = 58` unidades vendidas
  en total el 20-07-2022 — también tiene sentido, es el total del día.

Como se puede agregar sin restricciones en ambas dimensiones, es completamente aditivo — el mismo
tipo que "unidades vendidas" en el ejemplo de la clase teórica.

## Pregunta 3: `Items in stock` — Semi-aditivo

La tabla muestra cuántas unidades de cada producto hay en el almacén en un día dado.

| Date       | Product_FK | Items in stock |
| ---------- | ---------- | -------------- |
| 20-07-2022 | 1          | 15             |
| 20-07-2022 | 2          | 1              |
| 20-07-2022 | 3          | 18             |
| 20-07-2022 | 4          | 6              |
| 21-07-2022 | 1          | 34             |
| 21-07-2022 | 2          | 14             |
| 21-07-2022 | 3          | 34             |
| 21-07-2022 | 4          | 10             |
| 22-07-2022 | 1          | 27             |
| 22-07-2022 | 2          | 14             |
| 22-07-2022 | 3          | 31             |
| 22-07-2022 | 4          | 12             |
| 23-07-2022 | 1          | 13             |
| 23-07-2022 | 2          | 4              |
| 23-07-2022 | 3          | 15             |
| 23-07-2022 | 4          | 8              |

**Respuesta: semi-aditivo.**

A diferencia de `Quantity sold`, `Items in stock` no es un evento — es un **nivel** o **snapshot**:
representa cuánto stock *hay* en ese momento, no cuánto *entró* ese día. Esa es exactamente la misma
naturaleza que el ejemplo del saldo de cuenta (`account balance`) de la clase teórica, y por eso se
comporta igual:

- **Sumar por producto** (misma fecha, varios productos) **sí tiene sentido**: `15 + 1 + 18 + 6 =
  40` unidades en stock en total el 20-07-2022 — es una foto real del inventario total de ese día.
- **Sumar por fecha** (mismo producto, varios días) **no tiene sentido**: sumar el stock del
  producto 1 en los cuatro días (`15 + 34 + 27 + 13 = 89`) no representa "89 unidades" de nada real
  — el stock del día 23 (`13`) ya *incluye* (o reemplaza) el nivel de días anteriores; no es algo
  que se acumule sumando snapshots.

Por eso es semi-aditivo: aditivo a través de la dimensión de **producto**, pero no a través de la
dimensión de **fecha** — igual que el saldo de cuenta era aditivo por tipo de cartera pero no por
fecha.

## La diferencia clave para reconocerlos

| Pregunta a hacerse                                                                       | Si la respuesta es sí →                                                                                                              |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| ¿El hecho representa algo que **ocurre/se genera** en ese período (un evento, un flujo)? | Tiende a ser **completamente aditivo** (ej. unidades vendidas, ingresos).                                                            |
| ¿El hecho representa un **nivel o estado en un punto del tiempo** (una "foto")?          | Tiende a ser **semi-aditivo** — sumable entre entidades en la misma fecha, pero no a través del tiempo (ej. stock, saldo de cuenta). |
| ¿El hecho es un **ratio, porcentaje o precio**?                                          | Tiende a ser **no aditivo** en cualquier dimensión (ej. descuento, precio unitario).                                                 |
