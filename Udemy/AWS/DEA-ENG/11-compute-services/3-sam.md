# AWS SAM (Serverless Application Model)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS SAM?

AWS SAM es un **marco (framework)** diseñado para ayudar a crear y administrar aplicaciones
**serverless** en AWS de forma más sencilla. Simplifica el proceso de implementación dentro de una
arquitectura sin servidor que puede incluir servicios como **AWS Lambda**, **Amazon API Gateway** o
**Amazon DynamoDB**.

## Plantilla SAM

La aplicación se define usando una **plantilla SAM**: un archivo de configuración **YAML** que
esboza los recursos de la aplicación (por ejemplo, funciones Lambda, APIs y bases de datos).

Una plantilla SAM tiene, entre otras, estas secciones:

- **Metadatos** — al principio de la plantilla.
- **Resources** — donde se especifican todos los recursos de AWS que se quieren crear (p. ej. una
  función Lambda y un endpoint de API Gateway).
- **Outputs** — donde se definen los resultados de la stack que se quieren guardar o exponer.

> ⚠️ A partir de la plantilla SAM, AWS genera automáticamente la **plantilla de CloudFormation**
> correspondiente que coincide con la arquitectura especificada.

## Desarrollo y pruebas en local

SAM permite probar la aplicación serverless en la máquina local antes de desplegarla en AWS, algo
que normalmente resulta más difícil con arquitecturas serverless:

- Proporciona un **entorno de desarrollo local que imita AWS**, permitiendo probar y depurar la
  aplicación antes del despliegue.
- Soporta la **invocación local de funciones Lambda**: se pueden ejecutar y probar funciones
  localmente sin necesidad de desplegarlas primero.
- La **SAM CLI** se integra con IDEs populares (Visual Studio Code, PyCharm, IntelliJ, entre otros) y
  proporciona herramientas de depuración paso a paso.

## Flujo de build y despliegue

Los tres comandos clave de la SAM CLI (importantes para el examen):

1. **`sam build`** — procesa la plantilla y construye el código fuente de las funciones Lambda,
   incluyendo la descarga e instalación de las dependencias definidas en el gestor de paquetes del
   runtime de la función.
2. **`sam package`** — empaqueta el código de la aplicación y todas sus dependencias en un paquete
   de despliegue, lo sube a un bucket S3 y genera una plantilla SAM actualizada que referencia esos
   artefactos subidos.
3. **`sam deploy`** — toma la plantilla empaquetada y crea una **stack de CloudFormation**;
   CloudFormation lee la plantilla y aprovisiona los recursos definidos en ella.

> ⚠️ El orden de los comandos importa para el examen: **build → package → deploy**.
