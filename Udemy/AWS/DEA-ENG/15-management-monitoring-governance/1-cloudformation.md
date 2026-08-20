# AWS CloudFormation

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS CloudFormation?

**AWS CloudFormation** permite **definir y aprovisionar infraestructura como código
(Infrastructure as Code)** usando **plantillas (templates)**.

- En vez de crear recursos manualmente en la consola, se despliegan a partir de **código** (las
  plantillas), lo que permite aprovisionar **pilas de recursos** de forma **escalable**.
- Es, en esencia, una forma de **gestión de infraestructura**.

### Ventajas de Infrastructure as Code con CloudFormation

- **Reutilizable**: las plantillas se pueden reutilizar y compartir (incluso plantillas creadas
  por otras personas).
- **Replicable**: permite replicar fácilmente la misma infraestructura en **distintas regiones**.
- **Controlable y consistente**: al desplegar siempre a partir de código, se evitan cambios
  manuales inconsistentes o errores de configuración — el proceso es **sistemático**.
- **Ágil**: agiliza el proceso de creación de recursos.
- **Gestión de dependencias**: la plantilla puede describir el **orden** y las **relaciones** entre
  recursos (qué recurso debe crearse antes que otro), y CloudFormation se encarga de desplegar toda
  la pila respetando esa secuencia.

## Plantillas (templates)

- Una **plantilla** es básicamente un **archivo de texto** que describe **todos los recursos** que
  se quieren crear, incluyendo su **configuración** y sus **dependencias**.
- CloudFormation usa esa plantilla para **aprovisionar y configurar automáticamente** los recursos.
- Formato: **JSON** o **YAML**.
- Se pueden **versionar**, **compartir** y **reutilizar**.
- Se almacenan siempre en un **bucket de S3**, desde donde CloudFormation las usa para desplegar la
  pila.

Ejemplo básico de plantilla YAML que crea un bucket de S3:

```yaml
Resources:
  PrimerBucketS3:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: primer-bucket-s3
```

## Stacks (pilas)

Un **stack** es una **colección de recursos** que se gestiona como **una sola unidad**.

- Al desplegar una plantilla, todos los recursos definidos en ella (ej. una instancia EC2, una
  VPC, buckets S3, etc.), junto con sus relaciones y dependencias, se agrupan en un **stack**.
- CloudFormation se encarga de **aprovisionar y configurar** todos esos recursos según lo
  especificado en la plantilla, respetando el orden de dependencias (ej. crear primero la VPC,
  luego el volumen EBS, y después la instancia EC2 que lo usa).

> ⚠️ Al **eliminar un stack**, se eliminan **todos los recursos** que contiene — el stack se
> gestiona siempre como una unidad, tanto para crearlo como para eliminarlo.

Esto convierte a CloudFormation en una forma muy útil de gestionar infraestructura de manera
**repetible** y **consistente**.
