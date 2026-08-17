# Mezclar SCD Type 1 y Type 2 en una misma dimensión

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## La pregunta

Habiendo visto [[3-scd-type-1-overwrite]] y [[4-scd-type-2-add-new-row]], surge una pregunta natural:
¿hay que elegir un único tipo de `SCD` para toda una tabla de dimensión?

## La respuesta: se decide por atributo, no por tabla

**No.** La decisión de qué tipo de `SCD` aplicar no se toma a nivel de toda la tabla de dimensión,
sino **atributo por atributo**. Dentro de una misma dimensión, algunos atributos pueden manejarse con
`Type 1` y otros con `Type 2`, según lo que tenga sentido para cada uno.

### Ejemplo

En una `Product Dimension`:

- **Nombre del producto** → `Type 1`. No suele ser importante conservar el historial completo de
  cambios de nombre — para el análisis, no hay problema en sobrescribir el valor y usar el mismo
  nombre para todo el histórico.
- **Categoría del producto** → `Type 2`. Un cambio de categoría sí puede ser lo bastante significativo
  como para querer rastrearlo y conservar el historial correctamente particionado.

## Quién decide: los usuarios de negocio, no el modelador de datos

> ⚠️ Esta no es una decisión puramente técnica que el modelador de datos o diseñador del `Data
> Warehouse` deba tomar por su cuenta. Depende principalmente de los **usuarios de negocio**, que son
> quienes finalmente usan estos datos y quienes deben definir si necesitan el historial de un atributo
> o si está bien sobrescribirlo.

El rol del modelador es **ayudar y discutir las opciones** con ellos — explicar las implicaciones de
cada tipo — pero la decisión final le corresponde al negocio. Tampoco son reglas fijas e inamovibles:
la elección puede revisarse si cambian las necesidades de análisis.

## Resumen

- Una tabla de dimensión puede combinar atributos `Type 1` y `Type 2` sin problema.
- La elección se hace atributo por atributo, según su relevancia para el análisis histórico.
- La decisión final debe tomarse junto con los usuarios de negocio, no solo desde el punto de vista
  técnico.

## Próxima clase

Un enfoque intermedio entre `Type 1` y `Type 2`: `SCD Type 3`.
