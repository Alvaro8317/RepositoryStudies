# ETL de la dimensión de pago (Payment)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con la `Staging Area` de la `Fact Table` de ventas ya funcionando (ver
[[5-assembling-the-staging-job]]), empieza el diseño de la capa `Core`, comenzando por la dimensión de
pago (`Payment`), la `Junk Dimension` identificada en [[2-source-data-and-fact-table-design]].

## Diseñar la consulta en SQL primero

Antes de construir la transformación en `Spoon`, conviene probar y ajustar la lógica de extracción
directamente en `SQL`, sobre `pgAdmin`:

```sql
SELECT DISTINCT payment, loyalty_card
FROM staging.sales;
```

Esta consulta devuelve las 8 combinaciones posibles (4 valores de `payment` × 2 de `loyalty_card`).

### Tratar los valores nulos

En este caso, un `payment` nulo significa que el cliente pagó en efectivo en lugar de tarjeta. Se
sustituyen esos nulos usando `COALESCE` (equivalente disponible en la mayoría de sistemas de bases de
datos, aquí con sintaxis de `Postgres`):

```sql
SELECT DISTINCT COALESCE(payment, 'Cash') AS payment, loyalty_card
FROM staging.sales;
```

> ⚠️ La clave primaria (`payment_key`) no se incluye en esta consulta: se genera automáticamente al
> insertar, gracias a la secuencia autoincremental configurada en la tabla (ver
> [[3-setting-up-tables-in-pgadmin]]).

## Construir la transformación en Spoon

1. **Table Input**: se pega la consulta SQL anterior. Al ser un `SELECT DISTINCT` sobre `Staging`, esto
   funciona como una **carga completa** — siempre revisa todas las combinaciones existentes en
   `Staging` y detecta si hay alguna nueva.
2. **Insert/Update**: hacia el esquema `core`, tabla `dim_payment`.
   - Se compara por `payment` y `loyalty_card` para detectar si la combinación ya existe.
   - No se necesitan actualizaciones (se marcan los campos de actualización como no aplicables): si la
     combinación ya existe, no hay nada que cambiar.
   - Si es una combinación nueva, se inserta la fila completa y la `Surrogate Key` se genera
     automáticamente.

Se guarda la transformación como `core_dim_payment`.

## Próximas clases

Construir la transformación de la `Fact Table` de ventas: leer los datos de `Staging`, aplicar las
transformaciones finales, y cargar el resultado en `Core`.
