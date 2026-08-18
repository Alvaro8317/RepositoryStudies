# Ensamblar el Job de Staging y depurar errores

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con las transformaciones `SetLastLoad Sales` y `GetLastLoad Sales` ya creadas (ver
[[4-staging-sales-delta-load]]), toca integrarlas en el `Job` de `Staging` y comprobar que el flujo
completo funciona.

## Integrar las transformaciones en el Job

1. Añadir dos pasos de tipo `Transformation` al `Job`, conectados en el flujo de trabajo.
2. Primer paso — `SetVariable para Ventas`: apunta a la transformación `SetLastLoad Sales`.
3. Segundo paso — `GetVariable para Ventas`: apunta a la transformación `GetLastLoad Sales`.

Al ejecutar el `Job` no aparecen errores — pero eso no es suficiente para confirmar que funciona:
siempre conviene también **verificar los datos directamente en la base de datos**.

## Primer problema: falta el Table Output

Al consultar la tabla de `Staging` en `pgAdmin`, la tabla aparece **vacía**. La causa: al construir
`GetLastLoad Sales` en la clase anterior, se dejó pendiente el paso de salida (`Table Output`).

Se añade el paso `Table Output` a `GetLastLoad Sales`:

- `Schema` de destino: `"Staging"` (entre comillas — sensible a mayúsculas/minúsculas).
- Tabla: `sales`.
- Se marca `Truncate table` (para no duplicar datos en cada ejecución).
- En `Database Fields`, se revisa el mapeo automático — se elimina el campo `LastLoadDate` (no debe
  escribirse en la tabla), y el resto de columnas coincide en nombre sin necesitar cambios.

## Segundo problema: tipos de datos incompatibles

Al volver a ejecutar, aparece un nuevo error: la columna `cost` es de tipo `numeric` en el destino,
pero la expresión de origen es de tipo `character`.

> ⚠️ Este tipo de discrepancia puede pasar aunque el modelo/diseño diga que una columna es numérica:
> conviene revisar el tipo real de la columna en los datos de origen (consultando la tabla), no
> asumirlo solo por el diseño.

### Solución: Select Values

Se añade un paso **`Select Values`** entre el `Table Input` y el `Table Output`:

1. En la pestaña `Meta-data`, se selecciona el campo `cost`.
2. Se cambia su tipo de dato a `Number` (sin cambiar el nombre).

Con los tipos de datos ya coincidentes, se guarda y se vuelve a ejecutar el `Job` — esta vez funciona
correctamente, y los datos aparecen en la tabla de `Staging`.

## Próximas clases

Diseñar las transformaciones de la capa `Core`, empezando por la dimensión de pago (`Payment
Dimension`).
