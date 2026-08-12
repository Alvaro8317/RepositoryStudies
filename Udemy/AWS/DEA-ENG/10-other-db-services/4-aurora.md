# Amazon Aurora

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Amazon Aurora** es un servicio de base de datos relacional totalmente gestionado, **compatible con
MySQL y PostgreSQL**. Es, en esencia, la versión de AWS de estos motores: cualquier herramienta,
código o aplicación que ya funcione contra una base de datos MySQL o PostgreSQL existente puede
funcionar igual sobre Aurora.

## Rendimiento

- Al ser una solución **nativa de la nube**, AWS afirma un rendimiento de hasta **5 veces superior**
  a MySQL y hasta **3 veces superior** a PostgreSQL.
- Alto rendimiento tanto en operaciones de lectura como de escritura.
- El almacenamiento **escala automáticamente**, desde **10 GB hasta 128 TB**.

## Read Replicas

Una **read replica** es una copia de la base de datos primaria dedicada a gestionar consultas de
lectura.

- Mejora el rendimiento descargando parte de la carga de lectura desde la instancia primaria hacia
  las réplicas.
- Especialmente útil cuando el volumen de operaciones de lectura es mucho mayor que el de escritura.

## Seguridad

Igual que en [[1-rds|RDS]]: integración con **IAM** y soporte de **cifrado en reposo y en tránsito**.

## Aurora Serverless

Modo de despliegue **sin servidor** que ajusta dinámicamente los recursos de cómputo según la
demanda real de la aplicación, sin intervención manual.

- No requiere gestionar instancias ni capacidad — todo se simplifica con este despliegue serverless.
- Especialmente rentable para cargas de trabajo **impredecibles**: se paga por uso, y la capacidad se
  ajusta automáticamente en función del consumo real.
- El consumo se mide en **Aurora Capacity Units (ACU)** — la unidad de medida de la capacidad
  consumida.

> ⚠️ Aurora Serverless es la opción a considerar cuando la carga de trabajo es difícil de predecir;
> para cargas estables y constantes, una instancia Aurora provisionada de tamaño fijo suele ser más
> económica.
