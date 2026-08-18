# Ensamblar el Job de Core

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con la transformación de la `Fact Table` de ventas ya construida (ver [[7-sales-fact-etl]]), toca
ensamblar el `Job` de `Core` completo y verificar que los datos se cargan correctamente.

## Construir el Job

1. Se guarda primero la transformación de la `Fact Table` de ventas, para asegurar que el `Job` use la
   versión más reciente.
2. Se crea un nuevo `Job`, empezando por un paso `Start`.
3. Se añade un paso `Transformation` para la dimensión de producto (`dim_product`), apuntando a la
   transformación `core_dim_product`.
4. Se añade un segundo paso `Transformation` para la `Fact Table` de ventas (`f_ventas`), apuntando a
   la transformación `core_sales_fact`.
5. Se guarda el `Job` como `core_job` y se ejecuta.

## Verificar los datos

La ejecución no arroja errores, pero eso no basta — hay que confirmar en la base de datos:

```sql
SELECT * FROM core.sales;
SELECT * FROM core.dim_payment;
```

Ambas consultas devuelven los datos esperados: la `Fact Table` de ventas y la dimensión de pago están
correctamente cargadas en `Core`.

## Próximas clases

Probar que la `Delta Load` funciona correctamente, no solo la carga completa inicial.
