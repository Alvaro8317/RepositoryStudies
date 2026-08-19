# ECS: Roles IAM

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

ECS se apoya en roles IAM para gestionar los permisos de acceso a recursos de AWS y para realizar
acciones dentro del entorno de ECS. Hay dos roles esenciales: el **Task Execution Role** y el **Task
Role**.

## Task Execution Role

- Es el rol IAM que **ECS utiliza para gestionar la tarea en su nombre**.
- Se asocia con la instancia de contenedor.
- Permite, entre otras cosas:
  - Extraer (pull) imágenes de contenedores desde **Amazon ECR**.
  - Cargar logs en **Amazon CloudWatch**.
  - Interactuar con otros servicios necesarios para la **ejecución** de la tarea.
- Es, en esencia, un rol de **gestión** de la infraestructura de la tarea.

## Task Role

- Es el rol que se concede a los **contenedores dentro de la tarea** para que puedan realizar las
  acciones necesarias.
- Permite que la tarea acceda a recursos de AWS (ej. un bucket de S3, una tabla de base de datos, u otro
  recurso) en nombre de la aplicación.
- Los permisos se gestionan concediendo los accesos necesarios a este rol; la tarea lo usa para realizar
  esas acciones.

## Resumen

| Rol                     | Usado por                             | Propósito                                                                               |
| ----------------------- | ------------------------------------- | --------------------------------------------------------------------------------------- |
| **Task Execution Role** | ECS (en nombre de la infraestructura) | Gestionar la ejecución de la tarea: pull de imágenes desde ECR, logs a CloudWatch, etc. |
| **Task Role**           | Los contenedores dentro de la tarea   | Dar acceso de la aplicación a recursos de AWS (S3, bases de datos, etc.).               |
