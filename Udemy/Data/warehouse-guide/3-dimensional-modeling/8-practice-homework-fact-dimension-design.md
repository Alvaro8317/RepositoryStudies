# Tarea: diseño de Fact Tables y Dimension Tables

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Apunte de dos ejercicios de tarea del curso (rol: BI Consultant), aplicando lo visto en este módulo
sobre `Fact Tables`, `Dimension Tables`, `grain`, `Star Schema` y `Snowflake Schema`.

## Ejercicio 1: horas registradas (herramienta de gestión de proyectos)

### Requisito

Los project managers y division managers necesitan analizar cuántas horas se registraron según
distintos atributos, incluyendo por `Month`, `Quarter` y `Year`.

### Propuesta inicial y corrección

La primera propuesta ya identificaba bien los hechos y dimensiones base (`hours_logged` como medida
aditiva, `dim_projects`, `dim_employees`), pero le faltaba una pieza clave: no había ninguna tabla
para soportar el análisis por `Month`/`Quarter`/`Year` — se dejaba `update_date` como columna suelta
en la fact table, lo cual no permite agrupar por trimestre sin lógica repetida en cada consulta.

> ⚠️ Cuando un requisito pide explícitamente analizar por `Month`, `Quarter` o `Year`, es la señal
> para crear una `dim_date`: en vez de una columna de fecha cruda en la fact table, se usa una clave
> foránea (`date_id`) hacia una dimensión de fecha con esas columnas ya precalculadas.

### Diseño final

**Fact Table: `fact_logged_hours`**

- `log_id` — Primary Key (`Degenerate Dimension`: identificador transaccional sin atributos
  descriptivos propios).
- `date_id` — Foreign Key → `dim_date`.
- `project_id` — Foreign Key → `dim_projects`.
- `employee_id` — Foreign Key → `dim_employees`.
- `hours_logged` — Medida aditiva.

**Dimension Table: `dim_projects`**

- `project_id` — Primary Key.
- `project_name`
- `project_priority`

**Dimension Table: `dim_employees`**

- `employee_id` — Primary Key.
- `employee_name`
- `division`
- `head_of_division`

**Dimension Table: `dim_date`**

- `date_id` — Primary Key.
- `full_date`
- `month`
- `quarter`
- `year`

> Este diseño es un `Star Schema`: `dim_employees` mantiene `division` y `head_of_division`
> desnormalizados en vez de separarlos en una `dim_division` propia. Normalizar `division` en su
> propia tabla convertiría esto en un `Snowflake Schema` — un trade-off válido, pero no necesario
> para los requisitos descritos.

## Ejercicio 2: transacciones de ventas

### Requisito 1

Los managers responsables necesitan analizar tanto la **cantidad vendida** como el **monto de la
transacción**, y también poder analizarlo por `Month`, `Quarter` y `Year`.

### Propuesta inicial y correcciones

La segunda propuesta ya incorporaba correctamente la lección del ejercicio anterior (creó `dim_dates`
sin que hiciera falta señalarlo de nuevo) y aplicó bien el concepto de `Degenerate Dimension` con
`transaction_id`. Sin embargo, tenía dos problemas de modelado al normalizar hacia un `Snowflake
Schema`:

1. **`category_name` anidada dentro de `dim_brands`**: esto asume una relación 1:1 entre marca y
   categoría (una marca → una única categoría), lo cual casi nunca es cierto en la práctica (una
   misma marca puede vender en varias categorías, ej. `Electronics` y `Home Appliances`). La
   categoría es un atributo del **item**, no de la marca — no hay una dependencia funcional real
   entre ambos. Corrección: modelar `brand` y `category` como dos ramas **independientes** colgando
   de `dim_items`, en vez de anidar una dentro de la otra.
2. **`location_manager_id` como Foreign Key directa en la fact table**: esto rompía la consistencia
   con cómo se trató `item`/`brand` (donde el FK hacia `dim_brands` vive dentro de `dim_items`, no
   en la fact). Un manager es un atributo de la ubicación, no de la transacción en sí. Corrección:
   `location_manager_id` debe colgar de `dim_locations`, no conectarse directo a la fact table.

> ⚠️ Al construir un `Snowflake Schema`, cada nivel adicional de normalización debe colgar de la
> dimensión a la que pertenece semánticamente (`fact → dimensión → sub-dimensión`), no conectarse en
> paralelo directo a la fact table — de lo contrario se rompe la jerarquía que se busca representar.

### Diseño final 1

**Grain**: una fila por cada item vendido dentro de una transacción de venta.

**Fact Table: `fact_sales_transactions`**

- `transaction_id` — Primary Key (`Degenerate Dimension`).
- `date_id` — Foreign Key → `dim_dates`.
- `item_id` — Foreign Key → `dim_items`.
- `location_id` — Foreign Key → `dim_locations`.
- `quantity` — Medida aditiva.
- `transaction_amount` — Medida aditiva.

**Dimension Table: `dim_dates`**

- `date_id` — Primary Key.
- `full_date`, `day`, `month`, `quarter`, `year`.

**Dimension Table: `dim_items`**

- `item_id` — Primary Key.
- `item_name`
- `brand_id` — Foreign Key → `dim_brands`.
- `category_id` — Foreign Key → `dim_categories`.

**Dimension Table: `dim_brands`**

- `brand_id` — Primary Key.
- `brand_name`

**Dimension Table: `dim_categories`**

- `category_id` — Primary Key.
- `category_name`

**Dimension Table: `dim_locations`**

- `location_id` — Primary Key.
- `country`, `state`, `city`.
- `location_manager_id` — Foreign Key → `dim_location_managers`.

**Dimension Table: `dim_location_managers`**

- `location_manager_id` — Primary Key.
- `location_manager_name`

Este diseño es un `Snowflake Schema` consistente: `dim_items` se ramifica en `dim_brands` y
`dim_categories` como ramas independientes, y `dim_locations` se ramifica en
`dim_location_managers` — sin anidar dimensiones que no tienen una dependencia funcional real entre
sí.

## Aprendizajes clave de ambos ejercicios

- Un requisito de análisis "por `Month`/`Quarter`/`Year`" es la señal directa para crear una
  `dim_date`, en vez de dejar una columna de fecha cruda en la fact table.
- Un identificador transaccional sin atributos propios (`log_id`, `transaction_id`) se modela como
  `Degenerate Dimension`: vive como PK en la fact table, sin tabla de dimensión asociada.
- Al normalizar hacia un `Snowflake Schema`, cada sub-dimensión debe colgar de la dimensión con la
  que tiene una relación funcional real (`1 dimensión → muchos valores` en la sub-dimensión), nunca
  de una relación asumida sin verificar (ej. marca-categoría) ni conectada en paralelo directo a la
  fact table.
