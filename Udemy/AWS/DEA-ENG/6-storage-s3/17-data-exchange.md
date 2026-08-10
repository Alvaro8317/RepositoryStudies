# AWS Data Exchange

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**AWS Data Exchange** es un **catálogo de datos centralizado** que permite a los clientes **encontrar,
suscribirse y usar** datos de terceros en la nube, simplificando el proceso de trabajar de forma
segura con esos datasets/fuentes de datos externas.

## Casos de uso habituales

| Sector | Ejemplo de datos de terceros |
| --- | --- |
| **Servicios financieros** | Datos de mercado en tiempo real, datos financieros históricos, índices económicos — útiles para estrategias de trading o gestión de riesgo. |
| **Salud** | Datos de investigación médica, datos de pacientes ofrecidos por proveedores externos. |
| **Geoespacial** | Imágenes satelitales, datos meteorológicos, datos de ubicación — útiles para planificación urbana, entre otros. |
| **Retail** | Datos sobre comportamiento de clientes, tendencias de ventas. |

## Integración con otros servicios de AWS

- **AWS Marketplace** — los datasets pueden publicarse como productos en el Marketplace; el proveedor
  de datos debe estar **registrado como vendedor** allí.
- **AWS Lake Formation** — Data Exchange admite datasets basados en permisos de Lake Formation: los
  suscriptores pueden acceder a datos almacenados en el data lake del proveedor, y **consultarlos,
  transformarlos y compartir su acceso** desde su propio data lake.
- **Amazon S3** — los proveedores de datos pueden importar y almacenar archivos en sus buckets de S3;
  los suscriptores pueden **exportar** esos archivos a sus propios buckets de S3.
