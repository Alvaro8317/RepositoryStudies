# ETL vs. ELT: comparativa y casos de uso

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

En la clase anterior se vio en qué consiste `ELT`: extraer y cargar los datos inmediatamente, para
luego aplicar las transformaciones directamente en la base de datos de destino. Ahora se compara
`ETL` frente a `ELT` en cuanto a requisitos, ventajas, desventajas y casos de uso, para saber cuándo
conviene usar uno u otro.

## Requisito indispensable para poder usar ELT

Para poder plantearse siquiera usar `ELT` hace falta que la base de datos de destino tenga un
**rendimiento muy alto** — solo los `Data Warehouses` modernos en la nube suelen ofrecer esa
potencia. Sin ese requisito, `ELT` no es una opción viable.

## Estabilidad vs. flexibilidad de las transformaciones

- **`ETL`**: las transformaciones se definen de antemano, y los datos se cargan siempre siguiendo esa
  definición. Esto da como resultado transformaciones de datos muy **estables y consistentes**.
- **`ELT`**: las transformaciones se pueden cambiar rápidamente, ya que siempre se dispone de los
  datos en bruto (`raw`) en el `Data Warehouse` y se pueden transformar sobre la marcha. Es útil
  cuando todavía **no se está seguro de qué transformaciones hacen falta**, o cuando estas van a
  cambiar con frecuencia.

## Genérico vs. específico

- **`ETL`** conviene para casos de uso **genéricos**: cuando ya se sabe qué forma deben tener los
  datos y no hay necesidades muy específicas o muy distintas entre sí, tiene sentido definir las
  transformaciones una sola vez para que todo el mundo use los datos ya transformados fácilmente.
- **`ELT`** conviene cuando hay requisitos **muy sofisticados o específicos** — por ejemplo, científicos
  de datos que quieren aplicar transformaciones complejas y variadas, o "excavar" en los datos sin
  tener transformaciones genéricas predefinidas.

## Seguridad

Con `ETL` la seguridad se gestiona más fácilmente: al transformar los datos antes de cargarlos, se
puede usar solo la información no sensible, agregar datos, o cargar en el `Data Warehouse` datos ya
cifrados o anonimizados. Esto facilita cumplir requisitos de seguridad.

> ⚠️ En `ELT` los datos en bruto llegan primero al `Data Warehouse` tal cual, sin ese filtrado previo
> — algo a tener en cuenta si hay datos sensibles.

## Tiempo real

`ELT` permite cumplir más fácilmente requisitos en **tiempo real**, porque el proceso de extracción y
carga es mucho menos complejo y mucho más rápido al no aplicar transformaciones antes de cargar.

## Usuarios finales

- **`ETL`**: el resultado en el `Data Warehouse` solo tiene que ser definido una vez por los
  ingenieros de datos; después, los datos ya están listos para usarse, lo que facilita mucho el
  trabajo a los usuarios de negocio (`business users`).
- **`ELT`**: hacen falta analistas de datos más sofisticados, capaces de transformar los datos sobre
  la marcha.

## Resumen comparativo

| Criterio                      | ETL                                                           | ELT                                                                |
| ----------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| Requisito de la BD de destino | Estándar                                                      | Muy alto rendimiento (típico de `Data Warehouses` en la nube)      |
| Transformaciones              | Estables, definidas de antemano                               | Flexibles, se pueden cambiar sobre la marcha                       |
| Tipo de caso de uso           | Genérico                                                      | Específico / sofisticado (ej. exploración de científicos de datos) |
| Seguridad                     | Más fácil de gestionar (filtrado/anonimizado antes de cargar) | Datos en bruto llegan primero al `Data Warehouse`                  |
| Requisitos en tiempo real     | Más difíciles de cumplir                                      | Más fáciles de cumplir                                             |
| Usuarios finales              | Datos ya listos para `business users`                         | Requiere analistas de datos más sofisticados                       |
| Caso de uso típico            | Reporting                                                     | Exploración de datos, transformaciones ad-hoc, tiempo real         |
| Volumen de datos              | Puede ser insuficiente para volúmenes muy grandes             | Mejor opción ante volúmenes de datos muy grandes                   |

## Casos de uso típicos

- **`ETL` — Reporting**: es uno de los principales casos de uso de un `Data Warehouse`. Normalmente no
  hay requisitos de tiempo real y las transformaciones necesarias están bien definidas, por lo que
  `ETL` encaja perfectamente.
- **`ELT` — Ciencia de datos / tiempo real / grandes volúmenes**: cuando hay requisitos muy
  sofisticados (científicos de datos explorando y aplicando transformaciones complejas y variadas),
  cuando se necesitan datos en tiempo real (con una base de datos de destino con suficiente
  rendimiento), o cuando el volumen de datos es demasiado grande para que un `ETL` tradicional lo
  gestione bien.

## Próximas clases

Seguir explorando el proceso `ETL`/`ELT` y las herramientas disponibles para implementarlos.
