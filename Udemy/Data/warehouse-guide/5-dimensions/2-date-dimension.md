# Date Dimension

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Por qué es la dimensión más importante

La `Date Dimension` es la dimensión más utilizada de todas: está disponible en prácticamente todos
los procesos y, por lo tanto, casi siempre presente en un `Data Warehouse`. Esto se debe a que
normalmente queremos medir el rendimiento del negocio **a lo largo del tiempo** y a través de los
distintos aspectos temporales — por eso es una de las dimensiones más importantes, si no la más
importante.

## ¿Por qué no basta con el tipo de dato fecha nativo?

Las herramientas de `BI` ya permiten filtrar y calcular sobre columnas de tipo `date` de forma muy
flexible, pero eso no elimina la necesidad de una `Date Dimension`:

- **Lógica de negocio centralizada**: cosas como el año fiscal, si un día es festivo, o cómo se
  define exactamente una semana, no se pueden derivar de un tipo de dato `date` nativo — hay que
  definirlas explícitamente. Si no existe la dimensión, cada reporte o herramienta de `BI` tendría
  que reimplementar esa lógica por su cuenta.
- **Consistencia**: al centralizar esos atributos en una sola tabla, se garantiza que toda la
  organización usa exactamente la misma definición de "fin de semana", "trimestre fiscal", etc. — sin
  eso, distintos analistas podrían calcularlo de forma distinta en cada reporte.
- **Rendimiento**: unir la `Fact Table` con la `Date Dimension` por una `Surrogate Key` entera suele
  ser más rápido que aplicar funciones de fecha en cada fila en tiempo de consulta, sobre todo en
  tablas de hechos grandes.

## Atributos típicos

Contiene todas las características relacionadas con la fecha que queremos analizar. Algunos ejemplos:

- `Año`
- `Mes` — tanto el nombre (ej. "enero") como el número (ej. `1`)
- `Día del mes`
- `Trimestre` (`Quarter`)
- `Semana`
- `Día de la semana` — tanto el nombre (ej. "lunes") como el número (ej. lunes = `1`, martes = `2`,
  etc.)

## La Surrogate Key de la Date Dimension

A diferencia del resto de dimensiones, donde la `Surrogate Key` suele ser un entero autoincremental
sin ningún significado, en la `Date Dimension` es común usar una **clave sustituta significativa**:
un entero formado únicamente por año, mes y día (formato `YYYYMMDD`).

Por ejemplo, el 2 de abril de 2022 se convierte en la clave entera `20220402`, que actúa como clave
primaria de la dimensión.

## Fila dummy para fechas ausentes

Al igual que otras dimensiones, la `Date Dimension` debería tener siempre una **fila extra que
represente un valor ficticio** (`dummy value`), por ejemplo `1900-01-01`.

> ⚠️ Las claves foráneas en la `Fact Table` no deben tener valores nulos o perdidos. Si el sistema
> fuente no trae un valor de fecha para algún registro, se debe referenciar esta fila dummy en lugar
> de dejar la clave foránea en `NULL` — así se mantiene la integridad referencial y todas las
> relaciones siguen funcionando correctamente.

## ¿Separar una Time Dimension?

Si el aspecto temporal con mayor granularidad también es relevante (por ejemplo, si el sistema fuente
trae un `timestamp` además de la fecha), lo recomendable es **crear una `Time Dimension` separada**
en vez de mezclar fecha y hora en la misma dimensión. Esto no siempre es necesario — depende de si esa
granularidad de tiempo importa para el análisis.

## Prellenado a futuro

La `Date Dimension` es una de las pocas dimensiones altamente **calculables y predecibles**. Por eso
se puede (y se debe) rellenar por adelantado, incluyendo días futuros que aún no existen en la `Fact
Table` — aunque los eventos futuros todavía no estén registrados en los hechos.

## Buenas prácticas adicionales

| Práctica                         | Detalle                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombres largos y abreviados**  | Incluir ambas variantes (ej. "enero" y "ene") según lo que necesiten los reportes de negocio — no es obligatorio, depende del caso de uso.                                                               |
| **Combinaciones de atributos**   | Además de mantener el trimestre solo, incluir combinaciones útiles como `"2022 Q1"` para que el usuario final pueda agrupar directamente por ahí.                                                        |
| **Fechas fiscales**              | Añadir atributos como el año fiscal (`fiscal year`) si el negocio lo requiere.                                                                                                                           |
| **Banderas (`flags`)**           | Columnas booleanas para preguntas de sí/no, ej. `¿es fin de semana?`, `¿es festivo?`.                                                                                                                    |
| **No fijar el formato de fecha** | Guardar la fecha en un tipo de dato `date` nativo, sin preocuparse por el formato de presentación (guiones, barras, etc.) — el formato se resuelve en la herramienta de `BI`, no en el `Data Warehouse`. |

> ⚠️ Para las banderas, usar `1`/`0` tiene la ventaja de poder agregarse y sumarse fácilmente, pero
> puede no ser tan claro para el usuario final. Usar texto plano (ej. `"weekend"` / `"weekday"`) es
> más legible. Ambas opciones son válidas — la elección depende de los usuarios de negocio y los
> requisitos de reporting.

## Ejemplo de columnas en una Date Dimension

| Columna              | Ejemplo      |
| -------------------- | ------------ |
| `date_key` (PK)      | `20220402`   |
| `full_date`          | `2022-04-02` |
| `year`               | `2022`       |
| `month_number`       | `4`          |
| `month_name`         | `April`      |
| `quarter`            | `Q1`         |
| `year_quarter`       | `2022 Q1`    |
| `day_of_week_number` | `6`          |
| `day_of_week_name`   | `Saturday`   |
| `is_weekend`         | `1`          |
