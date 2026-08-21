# Amazon Managed Grafana

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon Managed Grafana** es un servicio **totalmente gestionado** que trae la herramienta de
visualización open source **Grafana** a AWS, sin necesidad de gestionar la configuración ni la
infraestructura subyacente.

## ¿Qué es Grafana?

Herramienta de visualización open source usada para crear **dashboards** y visualizaciones,
especialmente útil para **métricas, logs y trazas** con fines de monitorización. Muy popular en
comunidades de **IT Operations** y **DevOps**, porque ayuda a detectar problemas rápidamente al
supervisar sistemas y aplicaciones.

## Casos de uso

- Dashboards de monitorización para datos de logs o de sensores (ej. dispositivos **IoT**).
- Conexión directa a **CloudWatch** para monitorizar aplicaciones dentro de AWS.
- Monitorización en tiempo real del estado de la infraestructura, agregando métricas de distintas
  fuentes en un mismo dashboard.
- Alertas basadas en umbrales o condiciones específicas, enviadas a distintos canales.

## Componentes clave

- **Workspaces**: instancias individuales y aisladas de Grafana. Cada workspace tiene sus propias
  configuraciones, datos y gestión de usuarios separadas — importante por seguridad y claridad
  organizativa.
- **Data sources**: se integra con múltiples fuentes de datos de AWS y no-AWS.

| Fuente de datos                             | Uso típico                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **CloudWatch**                              | Monitorización operativa y de rendimiento de servicios AWS — una de las fuentes más comunes |
| **Amazon Timestream**                       | Datos de **series temporales** (ej. dispositivos IoT con timestamp)                         |
| **Amazon OpenSearch** (antes Elasticsearch) | Visualización de datos almacenados en OpenSearch                                            |
| **Amazon Redshift**                         | Datos de un data warehouse                                                                  |
| Otras fuentes AWS y no-AWS                  | —                                                                                           |

- **Autenticación**: integración con proveedores de identidad, ej. **SAML 2.0**, y con **IAM
  Identity Center**.

## Flujo de configuración típico

1. Crear el **workspace**.
2. Gestionar el acceso de usuarios (SAML 2.0 o IAM).
3. Crear una o varias **data sources**.
4. Configurar **dashboards** para visualizar los datos de esas fuentes.
