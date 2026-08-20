# Redshift Data API

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

La **Redshift Data API** es una API ligera basada en **HTTPS** que se utiliza para ejecutar
consultas contra Redshift sin necesidad de gestionar una conexión persistente a la base de datos.

Permite acceder a los datos de Redshift desde aplicaciones basadas en servicios web, incluyendo:

- **AWS Lambda**.
- **Amazon SageMaker Notebooks**.
- **AWS Cloud9**.
- Cualquier otra aplicación basada en la web.

## Caso de uso

- **Arquitecturas serverless**: la conexión tradicional a bases de datos no siempre encaja bien en
  este tipo de arquitecturas, ya que implica gestionar conexiones persistentes (overhead
  operativo). Con la Data API, un servicio (ej. una función Lambda disparada por un evento) puede
  interactuar con Redshift de forma muy sencilla, sin gestionar la conexión.
- **Aplicaciones web**: pueden usar la Data API para acceder y mostrar datos de Redshift (ej.
  datos de usuario), simplificando la arquitectura.
- **Servicios o aplicaciones de terceros**: pueden usar la Data API como una forma **controlada y
  segura** de acceder a los datos del clúster, sin gestionar conexiones.

## Características principales

- **Sin conexión persistente**: permite ejecutar consultas sin mantener una conexión abierta con
  la base de datos — útil para aplicaciones que interactúan con Redshift de forma intermitente.
- **Procesamiento asíncrono**: se envía un comando SQL a través de la API y los resultados se
  pueden recuperar más tarde — especialmente útil para consultas de larga duración. Los resultados
  se retienen durante un periodo determinado antes de expirar.
- **Eficiencia de recursos**: con el enfoque tradicional (conexión → consulta → cierre de
  conexión) hay que gestionar la conexión a la base de datos, lo que añade complejidad y consumo
  de recursos. La Data API evita esa sobrecarga.
- **Alternativa a los drivers JDBC/ODBC**: no es necesario gestionar conexiones ni drivers,
  reduciendo el overhead operativo y simplificando la configuración.
- **Integración sencilla** con otros servicios de AWS (Lambda, SageMaker Notebooks, etc.).

## Límites y consideraciones

| Límite | Valor |
| --- | --- |
| Duración máxima de una consulta | 24 horas |
| Consultas activas máximas por clúster (iniciadas + en cola) | 200 |
| Tamaño máximo del resultado (tras compresión gzip) | 100 MB — si se supera, la llamada falla |
| Retención máxima del resultado de una consulta | 24 horas |
| Tamaño máximo de la sentencia SQL | 100 KB |

- La Data API soporta tanto **clústeres de un solo nodo** como **multi-nodo**, con tipos de nodo
  como **DC2** y **RA3**.

## Acceso

- Para acceder a la Data API, un usuario o servicio debe estar **autorizado** — típicamente
  adjuntando una **managed policy** a un usuario o rol.
- Redshift proporciona la managed policy **`AmazonRedshiftDataFullAccess`**, que incluye los
  permisos necesarios para:
  - Acceder a los datos de Redshift a través de la Data API.
  - Usar **AWS Secrets Manager** y operaciones de la API de **IAM**, necesarios para autenticar y
    acceder al clúster.

## Monitorización con EventBridge

- Los eventos de la Data API se pueden monitorizar en **Amazon EventBridge**. Un evento representa
  la ejecución de una consulta (ej. inserción o actualización de filas).
- Permite entregar un flujo de datos en **tiempo real** desde las propias aplicaciones u otros
  servicios de AWS.
- EventBridge **enruta** esos eventos a distintos destinos (ej. una función **Lambda**, **Amazon
  SNS**), mediante **reglas** que seleccionan los eventos de interés.
- También permite **programar** operaciones de la Data API según un horario, usando reglas basadas
  en calendario (schedule) en EventBridge.
