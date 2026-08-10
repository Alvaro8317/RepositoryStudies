# Componentes de DynamoDB: tablas, items y atributos

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

DynamoDB se construye a partir de tres bloques básicos: **tablas**, **items** y **atributos**. Ver
también [[1-dynamodb]] y [[2-practice-create-table]].

## Tabla

- Es simplemente una **colección de datos** — el equivalente a una tabla en cualquier otro sistema de
  bases de datos.
- Puede tener cero o más items.
- Toda tabla debe tener siempre definida una **clave primaria** (se trata en detalle en la siguiente
  lección).

## Item

- Es el equivalente a una **fila** en otros sistemas de bases de datos, pero en DynamoDB (NoSQL) se
  llama **item**.
- Cada item es un **registro individual** — ej. en una tabla `libros`, cada libro concreto sería un
  item.

## Atributo

- Es el **elemento de dato fundamental** dentro de un item — la unidad en la que se desglosa la
  información del item.
- Ejemplo (tabla `libros`): `id_libro`, `autor`, `numero_de_paginas`, `precio` son todos atributos.
- La mayoría de los atributos son **escalares**: contienen **un único valor** (no significa
  necesariamente numérico). El tipo de dato de ese valor puede ser string, number, etc.
- La **clave primaria** (ej. `id_libro`) debe ser siempre de tipo escalar.

## Sin esquema (schema-less)

- Los atributos **no están predefinidos** y pueden variar de un item a otro dentro de la misma tabla
  — un item puede tener tres atributos y otro item de la misma tabla tener atributos completamente
  distintos.
- Los atributos de un item también pueden **cambiar con el tiempo** sin que eso sea un problema.

> En una base de datos relacional, cambiar la estructura de los datos implica añadir, eliminar o
> renombrar columnas — una operación que afecta a **toda la tabla** y puede requerir migración. En
> DynamoDB, al no haber un esquema fijo compartido por todos los items, esta flexibilidad no supone
> ningún problema.
