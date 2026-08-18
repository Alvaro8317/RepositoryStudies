# Categorías de herramientas ETL

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

En algún momento surge la pregunta de qué herramienta `ETL` usar en la empresa. Antes de poder
evaluarlas y elegir la más adecuada, conviene entender primero los distintos tipos o categorías de
herramientas `ETL` disponibles y sus diferencias.

## Herramientas empresariales (Enterprise)

Herramientas comerciales, desarrolladas y ofrecidas por empresas a un precio determinado.

- Son las herramientas más **maduras**.
- Suelen tener interfaces muy agradables y **fáciles de usar**.
- Suelen cumplir todos los requisitos para conectarse a prácticamente cualquier fuente de datos.
- Ofrecen **soporte** — algo muy importante en una gran empresa, sobre todo si los procesos `ETL` son
  críticos para el negocio: es clave tener a alguien responsable a quien acudir si algo falla.

## Herramientas de código abierto (Open Source)

Herramientas cuyo código está disponible públicamente.

- El código abierto **no significa necesariamente que sean gratuitas**, pero a menudo lo son.
- Hoy en día suelen ser bastante maduras y también tienen interfaz gráfica.
- Que el código sea público da confianza adicional: cualquiera puede entender cómo funciona la
  herramienta y revisar posibles problemas de seguridad.

> ⚠️ Si se usa una herramienta gratuita, normalmente **no viene acompañada de soporte**, y la
> facilidad de uso puede variar bastante entre una solución y otra — hay que evaluarlo caso por caso.
> ⚠️ Las categorías no son excluyentes: una herramienta empresarial también puede ofrecer partes de su
> código en código abierto, o tener una versión gratuita disponible.

## Soluciones nativas en la nube (Cloud-native)

Los grandes proveedores de nube (`AWS`, `Azure`, etc.) también ofrecen sus propias soluciones `ETL`.

- Si los datos ya están en la nube con un proveedor determinado, una solución nativa de ese mismo
  proveedor puede hacer el proceso mucho más eficiente.
- Si se trabaja con varios proveedores de nube a la vez, hay que evaluar qué tan flexible es la
  herramienta para conectarse y trabajar con datos de otros proveedores distintos al propio.

## Soluciones desarrolladas internamente (In-house)

Algunas empresas desarrollan su propia solución `ETL`.

> ⚠️ Esto suele surgir de una necesidad puntual (por ejemplo, alguien necesitó un conector específico),
> que luego se sigue desarrollando con el tiempo — no suele ser una decisión de diseño deliberada desde
> el inicio.

Esta no suele ser la solución ideal a la que aspirar, porque:

- Requiere muchos recursos de desarrollo.
- La solución resultante suele ser menos madura que las alternativas ya existentes.
- Alguien tiene que mantenerla, y además hay que formar a las personas que la usan.

## Resumen

| Categoría    | Madurez                              | Costo                        | Soporte         | Consideración clave                                              |
| ------------ | ------------------------------------ | ---------------------------- | --------------- | ---------------------------------------------------------------- |
| Enterprise   | Alta                                 | De pago                      | Sí              | Ideal si el ETL es crítico para el negocio                       |
| Open Source  | Variable (hoy en día suele ser alta) | A menudo gratis (no siempre) | Normalmente no  | Código público, transparencia                                    |
| Cloud-native | Alta (dentro de su ecosistema)       | Según proveedor              | Según proveedor | Eficiente si los datos ya están en esa nube; ojo con multi-cloud |
| In-house     | Baja/variable                        | Recursos internos            | Interno         | Evitar si hay alternativas maduras disponibles                   |

Dentro de cada una de estas categorías existen múltiples herramientas concretas, cada una con sus
propias ventajas e inconvenientes.

## Próximas clases

Ver cómo evaluar estas herramientas y elegir la más adecuada para la empresa.
