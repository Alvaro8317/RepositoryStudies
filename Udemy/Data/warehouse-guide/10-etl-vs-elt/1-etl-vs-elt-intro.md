# Introducción a ELT

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

A lo largo del curso se ha hablado mucho del proceso `ETL`, pero existe también el término `ELT`, un
enfoque más moderno que **no sustituye** al `ETL`, pero que vale la pena conocer porque tiene casos de
uso, escenarios y ventajas propias.

## Repaso: ETL

El `ETL` es la abreviatura de sus tres pasos — `Extract`, `Transform`, `Load`:

1. Se extraen los datos hacia una capa de preparación (`Staging Area`).
2. Se aplican las transformaciones sobre esos datos.
3. Los datos ya transformados se cargan en el `Data Warehouse`.

Es decir, en `ETL` las transformaciones se aplican **mientras los datos se están moviendo**, antes de
llegar a su destino final.

## ¿Qué es ELT?

En `ELT` simplemente se cambia el orden de la carga y la transformación:

1. Se extraen los datos.
2. Se cargan **inmediatamente** en el `Data Warehouse`, sin transformar.
3. Las transformaciones se aplican **después**, ya con los datos dentro del `Data Warehouse`, normalmente
   mediante comandos `SQL` ejecutados directamente sobre la propia base de datos de destino.

|                       | ETL                                                 | ELT                                                                         |
| --------------------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| Orden de fases        | Extract → Transform → Load                          | Extract → Load → Transform                                                  |
| ¿Dónde se transforma? | En una capa/herramienta intermedia, antes de cargar | En la propia base de datos de destino (`Data Warehouse`), después de cargar |
| Cómo se transforma    | Con la herramienta ETL                              | Normalmente con `SQL` (consultas, vistas)                                   |

## Por qué ahora es posible: potencia de cálculo del destino

Como en `ELT` las transformaciones se aplican sobre datos que ya están en el `Data Warehouse` (es
decir, sobre la marcha, en el momento en que se necesitan), hace falta aprovechar la **potencia de
cálculo de la base de datos de destino** — mucha más que en un `ETL` tradicional.

Esto es factible gracias al auge de los `Data Warehouses` en la nube (por ejemplo `Snowflake`), que
pueden usar procesamiento paralelo masivo (`Massive Parallel Processing` / `MPP`, tema que se verá más
adelante en el curso). Esa potencia de cálculo es la que permite aplicar las transformaciones sobre la
marcha.

## Ventajas de ELT

- **Más flexibilidad en las transformaciones**: no es necesario planificarlas de antemano como en
  `ETL` — se pueden aplicar sobre la marcha según se necesiten.
- **Cada analista puede transformar a su manera**: con varios analistas trabajando sobre el mismo
  `Data Warehouse`, cada uno puede ejecutar sus propias consultas `SQL` (por ejemplo, creando vistas)
  para obtener las transformaciones que necesita, de forma flexible y en el momento.
- **Extracción y carga mucho más rápidas**: al no transformar los datos antes de cargarlos, el proceso
  de `Extract` + `Load` es mucho más rápido, ya que las transformaciones suelen ser la parte más
  intensiva en cómputo de todo el proceso.
- **Permite frecuencias de carga mucho más altas**: un `ETL` tradicional puede tardar más porque
  siempre aplica las transformaciones antes de cargar. Si solo se extrae y se carga de inmediato (como
  en `ELT`), se puede ser mucho más rápido — lo que resulta clave cuando se necesitan datos en tiempo
  real en el `Data Warehouse`.

> ⚠️ Siempre que existan fuentes de datos en streaming, que deban introducirse en el `Data Warehouse`
> tan pronto como aparecen, `ELT` es una buena opción para cubrir esas necesidades de tiempo real.

## La herramienta puede ser la misma

No hace falta una herramienta distinta para hacer `ELT`: se puede seguir usando la misma herramienta
`ETL` (por ejemplo `Pentaho`), simplemente configurándola para que solo extraiga y cargue los datos, sin
transformarlos. Lo único indispensable es tener una base de datos de destino con mucha potencia de
cálculo, para poder beneficiarse del enfoque `ELT`.

### Ejemplo: dbt

`dbt` (`data build tool`) es un ejemplo de herramienta pensada específicamente para la parte
`Transform` de un `ELT`: no extrae datos de las fuentes ni los carga en el `Data Warehouse` (eso lo
hace otra herramienta, por ejemplo `Fivetran` o `Airbyte`, encargada solo de `Extract` + `Load`).
`dbt` trabaja después, sobre los datos que ya están en el `Data Warehouse`, transformándolos con
`SQL` directamente ahí — el patrón `Extract → Load → Transform`. Por eso, igual que con cualquier
`ELT`, necesita una base de datos de destino con buen rendimiento (`Snowflake`, `BigQuery`,
`Redshift`, Postgres, etc.).

## ¿Queda entonces obsoleto el ETL?

No. El `ETL` sigue siendo el proceso más utilizado para cargar y transformar datos en un `Data
Warehouse`. El `ELT` simplemente ofrece beneficios y casos de uso concretos en los que puede
convenir más que un `ETL` tradicional.

## Próximas clases

Comparar `ETL` frente a `ELT`: ventajas, desventajas, y en qué situaciones conviene usar uno u otro.
