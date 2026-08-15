# Data Lake vs. Data Warehouse

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Un malentendido común

Un Data Warehouse es una ubicación centralizada para el almacenamiento de datos, y lo mismo ocurre
con un **Data Lake**. Por eso es común pensar que son lo mismo, o que un Data Lake puede **sustituir**
a un Data Warehouse. No es así — son tecnologías distintas con propósitos distintos.

## Diferencias clave

|                              | **Data Lake**                                                               | **Data Warehouse**                                                         |
| ---------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Estado de los datos          | Datos sin procesar (raw), tal como salen de los sistemas de origen          | Datos transformados vía ETL, limpios                                       |
| Estructura                   | Datos no estructurados/semi-estructurados: CSV, JSON, imágenes, video       | Datos estructurados: tablas en una base de datos                           |
| Tecnología                   | Tecnologías de big data (por el gran volumen de datos)                      | Base de datos tradicional                                                  |
| Caso de uso                  | Poco definido — a veces no se sabe de antemano para qué se usarán los datos | Muy específico — el objetivo final (o varios) se define desde el principio |
| Calidad de los datos         | Más difícil de garantizar; más difícil de gestionar y navegar               | Alta, por el proceso ETL previo                                            |
| Nivel de habilidad requerido | Alto — típicamente usado por **científicos de datos**                       | Bajo — pensado para **usuarios de negocio** y otros profesionales de TI    |
| Facilidad de uso             | Baja                                                                        | Alta                                                                       |
| Rendimiento de consulta      | No es el foco                                                               | Alto                                                                       |

## ¿Cuándo usar cada uno?

> ⚠️ Un Data Lake y un Data Warehouse **no son mutuamente excluyentes** — no hay que elegir uno u
> otro, y un Data Lake no reemplaza a un Data Warehouse.

- Un **Data Lake** es muy útil por su escalabilidad para grandes volúmenes de datos (más aún con
  tecnologías cloud), pero conlleva riesgos: calidad de datos no garantizada, baja adopción, y menor
  facilidad de uso.
- Para sacar el máximo partido a los datos y convertirlos en información fácil de usar, se puede
  construir un **Data Warehouse sobre partes de un Data Lake**: se usa un proceso **ETL** para extraer
  los datos necesarios del Data Lake (cuando existe uno) y cargarlos, ya transformados, en el Data
  Warehouse — que queda disponible para las estrategias de Business Intelligence.
