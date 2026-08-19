# Amazon ECR (Elastic Container Registry)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon ECR?

**Amazon ECR** es un registro de contenedores Docker **totalmente gestionado**. Su objetivo principal es
permitir **almacenar, gestionar y desplegar** imágenes Docker de forma segura.

- Por debajo, ECR se apoya en un **bucket de S3** administrado por el propio servicio, donde se
  almacenan las imágenes de forma segura.
- Se integra con otros servicios de AWS, en particular con **ECS**.
- Admite **cifrado en reposo** por defecto.

## Integración con ECS

- **ECR** es el registro donde se almacenan las imágenes Docker.
- **ECS** ejecuta esas imágenes como contenedores, definidos como **tareas**.
- Al especificar la imagen del contenedor en una task definition, ECS puede **extraerla directamente de
  ECR** y desplegarla como parte de la aplicación en contenedores del cluster.
- **IAM** se usa para controlar el acceso a los repositorios y las imágenes.

## Funcionalidades principales

| Funcionalidad                            | Descripción                                                                                                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lifecycle policies**                   | Reglas para gestionar el ciclo de vida de las imágenes en el repositorio; permiten limpiar automáticamente las imágenes que ya no se necesitan tras un tiempo determinado. |
| **Image scanning**                       | Identifica vulnerabilidades en las imágenes. Cada repositorio puede configurarse para **escanear en cada push**.                                                           |
| **Replicación entre regiones y cuentas** | Facilita tener las imágenes disponibles allá donde se necesiten, mejorando también la durabilidad.                                                                         |
| **Versionado**                           | Usa **versionado semántico** para organizar los recursos y asegurar identificadores únicos, evitando así accidentes al acceder a versiones concretas.                      |
| **Etiquetado (tagging)**                 | Ayuda con la organización y gestión general de las imágenes.                                                                                                               |

## Repositorios públicos vs. privados

| Tipo                      | Descripción                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Repositorios públicos** | Accesibles por cualquiera; las imágenes pueden extraerse (pull) sin necesidad de permisos ni credenciales especiales. |
| **Repositorios privados** | Solo accesibles con autorización; el acceso se controla mediante **usuarios y políticas IAM**.                        |
