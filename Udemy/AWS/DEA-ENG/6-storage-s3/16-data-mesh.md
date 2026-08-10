# Data Mesh

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)
> ⚠️ **Data Mesh no es un servicio de AWS** — es un **concepto arquitectónico**: un conjunto de
> principios y buenas prácticas para organizar y gestionar datos, que se puede implementar combinando
> varios servicios de AWS.

## Propósito

**Data Mesh** es un enfoque estratégico que **descentraliza la propiedad y gestión de los datos**
dentro de una organización, en lugar de concentrarlas en un único equipo central. Esto mejora la
**calidad** y la **gobernanza** de los datos.

## Cómo funciona

- Trata los datos **como un producto**.
- Asigna la responsabilidad de los datos de forma **orientada al dominio**: cada dominio de la
  organización (ej. marketing, ventas) es propietario de sus propios datos, y por tanto responsable de
  su gobernanza, calidad y accesibilidad.

## Principios básicos

1. **Propiedad de datos orientada al dominio (domain ownership)** — la propiedad de los datos se
   asigna al dominio más cercano a ellos (ej. datos de ventas → equipo de ventas). Quien mejor conoce
   los datos es quien mejor los puede gestionar.
2. **Datos como producto (data as a product)** — cada dominio trata sus propios datos como un
   producto, centrándose en su **calidad**, **descubribilidad (discoverability)** y **usabilidad**, ya
   que es responsable de ellos y también quien los consume.
3. **Infraestructura de datos de autoservicio (self-service data infrastructure)** — se dota a cada
   dominio de las herramientas y plataformas necesarias para gestionar sus datos de forma
   independiente.
4. **Gobernanza de datos federada (federated governance)** — garantiza el cumplimiento y la seguridad
   en **toda** la organización, sin dejar de permitir autonomía a cada dominio individual.

## Servicios de AWS que ayudan a implementarlo

| Servicio               | Rol dentro del Data Mesh                                       |
| ---------------------- | -------------------------------------------------------------- |
| **S3**                 | Almacenamiento escalable de los datos.                         |
| **AWS Glue**           | Catalogación de datos y procesos ETL.                          |
| **Redshift**           | Almacenamiento de datos (data warehouse) y análisis.           |
| **AWS Lake Formation** | Gobernanza de seguridad y configuración general del data lake. |
| **Athena**             | Consultas serverless y consultas ad hoc sobre los datos.       |
| **API Gateway**        | Exponer los productos de datos de cada dominio como APIs.      |
