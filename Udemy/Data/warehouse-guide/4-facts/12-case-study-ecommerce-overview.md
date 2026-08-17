# Caso práctico: e-commerce — presentación del escenario

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Objetivo

Aplicar de forma práctica los [[10-fact-table-design-steps]] recorriendo cada paso sobre un caso
real, para entender cómo funcionan las cosas en la práctica y no solo en teoría.

## El escenario

Trabajas en el departamento de IT de una gran empresa de e-commerce que vende varios productos en
**tres sitios web** distintos. Cada sitio web funciona de forma independiente y está gestionado por
departamentos distintos.

- Se venden alrededor de **1.000 productos individuales**: comestibles, productos de cocina y todo
  tipo de productos del hogar.
- La empresa recopila muchos datos, en varios puntos distintos del proceso de negocio.

## Puntos de recolección de datos

El punto más importante es el **checkout del carrito de compra**: cuando un cliente añade productos
al carrito y finaliza la compra, se recopilan datos como nombre del cliente, `ID` del cliente, `ID`
de pedido, `ID` de línea de pedido, cantidad, precio unitario, importe de venta, etc.

Ejemplo de cómo lucen esos datos (grano del sistema origen: **una fila = una línea de pedido**, es
decir, un producto dentro de un pedido concreto):

| ID Cliente | Nombre Cliente | ID Pedido | ID Línea de Pedido | Producto     | Cantidad | Precio Unitario | Importe de Venta |
| ---------- | -------------- | --------- | ------------------ | ------------ | -------- | --------------- | ---------------- |
| ...        | ...            | 2314      | ...                | Gafas de sol | 2        | ...             | ...              |

> ⚠️ Un mismo producto dentro de un pedido puede tener una cantidad mayor a uno — en el ejemplo, el
> cliente compró **dos** gafas de sol en una sola línea de pedido.

Además del checkout, también se recopilan datos en otros puntos del almacén de la empresa: fecha de
recogida (`picking`), cumplimiento del pedido (`order fulfillment`), entrega del proveedor
(`vendor delivery`), entre otros.

## Objetivos del negocio

Al hablar con los responsables de la empresa, se identifican estos objetivos:

- Hacer más **eficiente la logística** en el almacén.
- **Maximizar el beneficio** — objetivo general, pero complejo, ya que involucra múltiples
  factores relacionados entre sí:
  - El **margen de beneficio** de cada venta.
  - **Anuncios, promociones y descuentos**, que pueden aumentar mucho el **volumen de ventas**.

> ⚠️ Los descuentos son un arma de doble filo: pueden disparar el volumen de ventas, pero también
> pueden generar **pérdidas** en ventas concretas si el descuento es demasiado grande. Por eso hace
> falta un análisis estratégico — y de ahí la necesidad de construir un `Data Warehouse`.

## Próximos pasos

Se recorrerán los cuatro pasos de diseño de una `Fact Table` sobre este caso práctico, empezando
por el paso 1: identificar el proceso de negocio.
