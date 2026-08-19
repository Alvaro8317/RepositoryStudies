# AWS Macie

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Macie?

**AWS Macie** es un servicio **totalmente gestionado** de **seguridad y privacidad de datos**.

- Utiliza algoritmos de **aprendizaje automático (machine learning)** para **escanear
  automáticamente buckets de S3** e **identificar y clasificar datos confidenciales**.
- Los datos confidenciales que puede detectar incluyen, por ejemplo:
  - **PII** (**Personally Identifiable Information** — información de identificación personal).
  - **Datos financieros**.
  - **Información sanitaria** (health information).
- Para la clasificación usa **clasificadores predefinidos**, pero también permite definir
  **criterios de clasificación personalizados** mediante **expresiones regulares** o
  **coincidencias de palabras clave**.
- Además de identificar datos sensibles, usa modelos de ML para detectar **patrones de acceso
  anómalos** — comportamiento que puede indicar una **violación de datos (data breach)** o un
  **acceso no autorizado**.

## Casos de uso principales

Macie cubre básicamente dos casos de uso:

1. **Identificación y clasificación de datos sensibles** en S3.
2. **Detección de actividad de acceso anómala/sospechosa** sobre esos datos.

## Alertas e integración

- Macie genera **alertas detalladas** cuando detecta datos sensibles o actividad sospechosa.
- Esas alertas se pueden **integrar con otros servicios** para recibir notificaciones en tiempo
  real:
  - **CloudWatch**
  - **Lambda**
  - **SNS**

## Dashboard y hallazgos (findings)

- Macie ofrece un **cuadro de mandos (dashboard)** completo con una visión general del entorno S3:
  problemas de seguridad destacados, riesgos detectados, etc.
- Los **resultados detallados (findings)** también se pueden usar para elaborar **informes de
  cumplimiento (compliance)** o con fines de **auditoría**.

## Casos de uso

| Caso de uso                     | Descripción                                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Cumplimiento normativo**      | Ayuda a cumplir requisitos de manejo de datos sensibles bajo regulaciones como **GDPR** y **HIPAA**, identificando PII y datos sensibles. |
| **Supervisión de la seguridad** | Monitoriza el acceso a los datos para detectar actividad inusual que pueda indicar una amenaza de seguridad.                              |
| **Evaluación de riesgos**       | Evalúa e informa de los riesgos asociados a los datos almacenados en S3, ayudando a priorizar esfuerzos de seguridad.                     |

> ⚠️ Macie usa **machine learning** tanto para clasificar datos sensibles como para detectar
> patrones de acceso anómalos, lo que le permite hacer este trabajo de forma eficiente a gran
> escala sin reglas manuales exhaustivas.
