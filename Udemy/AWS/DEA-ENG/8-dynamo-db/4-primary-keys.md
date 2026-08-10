# Claves primarias en DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Toda tabla de DynamoDB debe tener siempre definida una **clave primaria**. Ver también
[[3-components]].

## Restricciones de la clave primaria

- Debe ser **escalar** — un único valor (no significa necesariamente un número).
- El tipo de dato solo puede ser **string, number o binary**. Los atributos que **no** son clave
  (ej. `precio`, `género`) no tienen esta restricción de tipo.
- Debe ser **única**: no puede haber dos items con la misma clave primaria.
- Se define **al crear la tabla** y **no se puede cambiar** después — es una decisión de diseño fija.

## Por qué es tan importante

- DynamoDB es una **base de datos distribuida**: los datos pueden repartirse entre varios servidores.
- La clave primaria determina **dónde se almacenan físicamente los datos**, y por tanto es lo que
  permite **recuperarlos y gestionarlos de forma consistente**.
- Es un concepto central en la arquitectura de DynamoDB: se usa para **almacenar, acceder y gestionar**
  los datos.

## Dos tipos de clave primaria

|                 | **Clave de partición (partition key)**       | **Clave compuesta (composite key)**                                                   |
| --------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- |
| También llamada | Clave primaria simple, **hash attribute**    | Clave de partición (**hash**) + clave de ordenación (**range attribute**)             |
| Nº de atributos | Uno solo                                     | Dos: partition key + sort key                                                         |
| Unicidad        | El propio atributo debe ser único            | Solo la **combinación** de ambos atributos debe ser única                             |
| Flexibilidad    | Menor — cada item necesita un valor distinto | Mayor — permite varios items con la misma partition key, distinguidos por la sort key |

### Clave de partición simple — ejemplo

Tabla `estudiantes`, clave primaria = `numero_de_carnet`. Si hay un solo item por estudiante, el
número de carnet identifica de forma única cada item — sirve como clave de partición simple. El resto
de atributos (edad, título, etc.) pueden variar libremente entre items, e incluso faltar en algunos
(esquema flexible).

### Clave compuesta — ejemplo

Si el número de carnet de estudiante **puede repetirse entre distintos años** (ej. se reutiliza el
mismo número cada nueva promoción), un solo atributo ya no basta para identificar el item de forma
única. En ese caso se usa una clave compuesta:

- **Clave de partición** → `numero_de_carnet`.
- **Clave de ordenación** → `año_de_graduacion`.

Solo la combinación de ambos valores es única.

## Por qué existen también las claves secundarias

La clave de partición determina cómo se reparten físicamente los datos, y consultar por ella (o por
la clave primaria en general) es la forma estándar de recuperar datos. Pero cuando el **patrón de
acceso** necesario es distinto — por ejemplo, consultar todos los libros de un autor concreto, o todos
los productos de una categoría, en vez de por su clave primaria — hace falta un mecanismo adicional:
los **índices secundarios**, que permiten acceder a los datos de forma eficiente según otros atributos.
Se tratan en la siguiente lección.
