# Amazon Athena — Workgroups

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son los Workgroups?

Los **Workgroups** permiten **aislar consultas** en Athena según el equipo, caso de uso o carga de
trabajo que las genera. Por ejemplo:

- Consultas de **generación de informes** (ej. desde **QuickSight**).
- Consultas **ad hoc** de un equipo de data scientists.
- Distintas aplicaciones con distintos requisitos.

Cada Workgroup agrupa un tipo de carga de trabajo bajo su propia configuración, lo que permite además
**separar y controlar el coste** de cada una de ellas de forma independiente.

## Configuración por Workgroup

Cada Workgroup puede tener su propia configuración, entre otras cosas:

| Configuración | Descripción |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| **Ubicación de resultados** | Bucket de S3 donde se almacenan los resultados de las consultas ejecutadas en ese Workgroup. |
| **Control de acceso** | Mediante políticas de IAM basadas en identidad, a nivel de recurso. |
| **Control de coste** | Límites y seguimiento de coste específicos para ese Workgroup. |
| **Motor de consulta** | Athena SQL (por defecto) o **Apache Spark**. |

- El acceso a un Workgroup se controla con **políticas de IAM**: quien tenga permiso puede
  seleccionarlo (desde un desplegable en la consola) para ejecutar sus consultas en él.
- Para usar **Apache Spark** en vez del motor SQL estándar, hay que crear un Workgroup nuevo y
  configurar su motor como Spark.

## Límites y Workgroup por defecto

- Se pueden crear hasta **1000 Workgroups por región**.
- Cada cuenta tiene, por defecto, un **Workgroup principal (`primary`)**:
  - Siempre está disponible.
  - Por defecto, sus permisos permiten el acceso a **todos los usuarios autenticados**.
  - **No se puede eliminar.**
- Para cualquier Workgroup adicional creado, el acceso se configura mediante **políticas de IAM**.

> ⚠️ Los Workgroups no solo organizan consultas: son también el mecanismo principal para aislar
> costes y aplicar configuraciones distintas (motor, ubicación de resultados, permisos) por equipo o
> caso de uso.
