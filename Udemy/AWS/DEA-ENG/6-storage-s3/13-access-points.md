# Access Points en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

Al almacenar cada vez más datos en un bucket, es habitual necesitar compartirlo entre distintos
usuarios o aplicaciones. Gestionar quién puede acceder a qué dentro de un mismo bucket puede
volverse complicado rápidamente.

Los **Access Points** resuelven esto permitiendo crear **puntos de entrada personalizados** a un
bucket, cada uno con su propio conjunto de políticas de control de acceso — sin necesidad de tocar
la estructura del bucket ni su Bucket Policy general.

## Características

- Cada Access Point tiene su propio **nombre DNS**.
- El **origen de la conexión** puede ser:
  - **Internet** — acceso desde fuera de AWS.
  - **VPC** — acceso únicamente desde dentro de una VPC concreta.
- Cada Access Point tiene su propia **Access Point Policy**, un documento (similar a una Bucket
  Policy) que define los permisos específicos de ese punto de entrada.

## Casos de uso

Permiten definir permisos personalizados por consumidor sobre el **mismo bucket subyacente**, por
ejemplo:

- Un Access Point de solo lectura para un equipo.
- Otro Access Point con lectura y escritura para otro equipo.
- Un Access Point distinto por departamento o por socio externo.

## Ventajas

- **Escalabilidad**: a medida que crece el proyecto, gestionar el acceso por Access Point es más
  simple que mantener una única Bucket Policy cada vez más compleja.
- **Sin cambios estructurales**: no hace falta reorganizar el bucket para adaptar los permisos.
- **Seguridad**: al limitar de forma granular quién y cómo accede a los datos, se reduce el riesgo
  de exposición accidental de datos sensibles.
