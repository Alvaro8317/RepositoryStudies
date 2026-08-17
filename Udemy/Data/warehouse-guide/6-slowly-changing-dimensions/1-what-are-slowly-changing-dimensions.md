# ¿Qué son las Slowly Changing Dimensions?

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El problema: las dimensiones sí cambian

Hasta ahora se ha tratado a las dimensiones como si fueran estáticas — comparadas con los hechos,
las dimensiones suelen ser más estables y no se espera que cambien mucho, o incluso nada. Pero en el
mundo real, algunos atributos de las dimensiones **sí cambian con el tiempo**, y por eso se necesita
una estrategia para gestionar esos cambios.

A este concepto se le llama `Slowly Changing Dimension` (`SCD`) — un término muy popular en el mundo
del `Data Warehousing`. `SCD` es simplemente la abreviatura de `Slowly Changing Dimension`, y es la
forma más común de referirse a este concepto.

## Ser proactivo al identificar cambios

> ⚠️ Los usuarios de negocio a menudo no esperan que haya cambios en las dimensiones, por lo que
> normalmente **no van a avisar** de forma espontánea sobre qué atributos cambian ni cómo deben
> gestionarse esos cambios.

Por eso, como modelador de datos, hay que ser **proactivo** y preguntar explícitamente por posibles
cambios en los atributos de cada dimensión — no esperar a que los usuarios de negocio lo mencionen
por su cuenta.

Además, no basta con preguntar solo a los usuarios de negocio: también hay que consultar a las
personas de `IT` responsables de los sistemas fuente de esos datos, ya que a veces los usuarios de
negocio no son conscientes de estos cambios. Lo ideal es reunir a ambos grupos (negocio e `IT`) para
desarrollar en conjunto la estrategia de manejo de cambios.

## Una estrategia por atributo

Cada atributo de una dimensión puede requerir su propia estrategia de manejo de cambios, según la
situación y los requisitos del negocio. Esto da lugar a los distintos **tipos de `Slowly Changing
Dimension`**.

> ⚠️ Estos tipos fueron introducidos originalmente por `Kimball` en 1995, y siguen siendo el estándar
> más conocido y utilizado — por eso el curso se centra en ellos.

## Próximas clases

Profundizar en los distintos tipos de `SCD` (`Type 0` a `Type 6`), que representan las diferentes
estrategias disponibles para manejar los cambios en los atributos de una dimensión.
