# Índice B-tree

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

El índice `B-tree` es el **índice estándar**: cuando se habla de "un índice" sin especificar el tipo,
normalmente se está hablando de un `B-tree`.

## Cómo funciona

Un índice `B-tree` es una estructura de árbol de varios niveles que usa lógica de árbol para dividir
los datos en distintas páginas o bloques. Por ejemplo, un índice sobre el nombre de una persona se
puede desglosar por su primer carácter, y dentro de cada rama, por el segundo carácter, y así
sucesivamente — hasta llegar a un puntero con la ubicación real de la fila.

```text
A
└── D → fila 20   (ej. "Adam")
```

Así, para buscar "Adam", el árbol lleva directo a la fila 20 sin necesidad de recorrer toda la tabla.

## Cuándo conviene usarlo

El índice `B-tree` es la mejor opción para columnas con **cardinalidad alta**: columnas únicas, o al
menos con un rango muy amplio de valores distintos, donde cada valor aparece pocas veces (idealmente
una sola vez). Ejemplos típicos: claves sustitutas (`Surrogate Key`), números de teléfono,
direcciones, nombres completos.

> ⚠️ Un índice `B-tree` suele crearse automáticamente sobre la clave primaria de una tabla en cuanto
> esta se define — no siempre hace falta crearlo explícitamente.

## Próximas clases

Ver el índice de mapa de bits (`Bitmap Index`), especialmente útil en `Data Warehouses`.
