# Caso práctico: paso 3 — identificar las dimensiones

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Contexto

Tercer paso del framework visto en [[10-fact-table-design-steps]], continuando el
[[14-case-study-declare-grain]]. Identificar las dimensiones consiste en describir las medidas: el
contexto descriptivo con el que los usuarios interpretan los hechos (tiendas, ubicaciones,
productos, categorías, sitios web, etc.).

Las dimensiones se derivan de forma natural y directa a partir del `Grain` ya definido (línea de
pedido dentro de un pedido).

## Dimensiones identificadas

- **Cliente** (`Customer`).
- **Producto** (`Product`) — asociado a cada línea de pedido.
- **Promoción** (`Promotion`).
- **Fecha/hora** (`DateTime`).
- **Sitio web** (`Website`) — no aparecía explícito en los datos origen, pero es una dimensión
  igualmente válida: identifica de qué sistema fuente proviene cada fila, ya que los datos vienen de
  **tres sitios web distintos** (tres sistemas fuente distintos).

> ⚠️ No hay que limitarse solo a las columnas explícitas del sistema origen — el propio origen de
> los datos (en este caso, de qué sitio web/sistema proviene cada fila) también puede convertirse en
> una dimensión relevante para el análisis.

## Claves foráneas (Surrogate Keys) para las dimensiones

Al construir la `Fact Table`, se generan `Surrogate Keys` (sufijo `FK`) para las dimensiones:

- **Clave primaria de la fila**: el sistema origen no tenía ninguna clave que identificara de forma
  única cada fila (cada línea de pedido), así que se genera una nueva — un entero autoincremental
  simple — como `Surrogate Key` de la propia `Fact Table`.
- **Website FK, Customer FK, Product FK, Promotion FK**: en estos casos los `ID` de origen ya eran
  enteros simples, así que no hizo falta sustituirlos por un nuevo valor — simplemente se les
  renombra con el sufijo `FK` para señalar que ahora apuntan a una dimensión.
- **DateTime FK**: se genera una nueva `Surrogate Key`, sustituyendo la fecha/hora original por un
  entero más largo que codifica año, mes, día, etc. (ej. `20220423...` para el 23 de abril de 2022).
  En este caso se decidió **redondear la hora** y usar una única dimensión combinada de fecha y
  hora, en vez de separarlas en dos dimensiones distintas (`Date` y `Time`) — ambas opciones son
  válidas, es una decisión de diseño.

## Próximo paso

Con las dimensiones ya identificadas, el último paso es identificar los hechos (`Facts`).
