# Amazon AppFlow

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon AppFlow** es un servicio de **integración totalmente administrado** (fully managed) que
facilita la transferencia **segura** y **automática** de datos entre servicios de AWS y
aplicaciones **SaaS** (Salesforce, Snowflake, Slack, ServiceNow, Zendesk, Google Analytics,
Datadog, Instagram Ads, Google Ads, GitHub, GitLab, etc.).

- Permite mover datos entre estas herramientas SaaS y servicios del cloud de AWS (por ejemplo, un
  **bucket S3**, **Amazon Redshift**, una base de datos) — o incluso entre distintas aplicaciones
  SaaS — **sin tener que desarrollar un ETL personalizado desde cero** ni escribir código.
- AppFlow se encarga de la **extracción** y **carga** de los datos, usando una **interfaz visual**
  muy sencilla: se selecciona la **fuente** y el **destino** de una lista de **conectores
  preconstruidos** para las aplicaciones SaaS populares — la fuente y el destino pueden estar
  dentro o fuera de AWS indistintamente.

> ⚠️ El principal valor de AppFlow es eliminar la necesidad de escribir y mantener código de
> integración personalizado para mover datos desde/hacia cada SaaS — AppFlow ya tiene resuelta esa
> estructura de extracción y carga mediante conectores preconstruidos, sin necesidad de dedicar
> tiempo a construir esas integraciones desde cero.

## Transformaciones y mapeo de datos

AppFlow también permite **transformar los datos** antes de la carga: limpieza, filtrado o
enriquecimiento — algo bastante común en la práctica al extraer datos de un SaaS como Salesforce,
GitHub o GitLab. Además, permite hacer **mapeo de datos** (*data mapping*) para asegurar que el
formato de los datos coincide entre el sistema origen y el sistema destino.

## Sincronización bidireccional

AppFlow soporta flujo de datos tanto **entrante** como **saliente**, permitiendo una
**sincronización bidireccional** entre servicios — funciona en ambos sentidos, no solo desde el
SaaS hacia AWS.

- Los flujos también se pueden activar **basados en eventos** que ocurren en la propia aplicación
  SaaS, logrando una integración de datos casi en **tiempo real**.

## Seguridad

- Los datos se mueven **cifrados** en reposo y en tránsito.
- Cumple con diversos **estándares de cumplimiento** de datos.
- Integración con **IAM** para control de acceso granular sobre los flujos.

## Frecuencia de transferencia

Los flujos (*flows*) de AppFlow se pueden ejecutar de tres formas:

| Modo                  | Descripción                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| **Programada**        | Se define un día y una hora concretos para la ejecución del flujo.       |
| **Basada en eventos** | El flujo se ejecuta automáticamente cuando ocurre un evento determinado. |
| **Bajo demanda**      | El flujo se ejecuta manualmente, bajo petición directa del usuario.      |

## Beneficios

- **Seguridad**: garantía de que los datos se transfieren de forma segura.
- **Facilidad de uso**: elimina la necesidad de escribir y mantener integraciones personalizadas.
- **Flexibilidad y escalabilidad**: escala entre diferentes tipos y volúmenes de transferencias de
  datos.
- **Automatización**: permite automatizar flujos de trabajo tanto basados en eventos como de forma
  programada.

> Amazon AppFlow es especialmente recomendable cuando se necesita transferir datos entre
> aplicaciones SaaS y servicios del cloud de AWS (o viceversa), de forma rápida, segura y a bajo
> coste.

## Casos de uso

- **Integración sencilla** entre servicios de AWS y aplicaciones SaaS populares (Salesforce,
  Snowflake, Zendesk, Slack, etc.).
- **Agregación de datos**: centralizar distintas fuentes SaaS en AWS para obtener análisis en
  profundidad.
- **Sincronización de datos de clientes** entre plataformas, para tener una visión unificada en
  AWS.
- **Automatización de flujos de trabajo** entre aplicaciones SaaS y servicios de AWS.

> ⚠️ AppFlow no es un servicio ETL totalmente gestionado como Glue: es una **integración ligera**
> pensada específicamente para conectar fácilmente aplicaciones SaaS con AWS, sin la sobrecarga de
> los servicios de procesamiento de datos más complejos.
