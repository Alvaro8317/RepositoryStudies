# AWS Database Migration Service (DMS)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS DMS?

**AWS Database Migration Service (DMS)** ayuda a migrar bases de datos de forma **segura y sencilla**
hacia AWS.

- Soporta **distintos motores de base de datos**, y el origen y el destino **no tienen por qué usar el
  mismo motor** (ej. Oracle → Aurora, MySQL → SQL Server, o al revés).
- Permite **replicación continua** con alta disponibilidad: es posible migrar la base de datos **sin
  tiempo de inactividad** en la fuente, con un impacto mínimo sobre esta — importante en entornos de
  producción.

## Cómo funciona

- DMS usa una **instancia EC2** para alojar la **instancia de replicación**, responsable de gestionar y
  ejecutar la transferencia de datos entre las bases de datos de origen y destino.
- Esta instancia está **totalmente gestionada** por AWS.
- Los datos se **cifran en tránsito** mediante SSL/TLS.
- **Modelo de precios pay-per-use:** se paga por el uso de la instancia EC2 de replicación, más posibles
  costes adicionales de transferencia de datos.

## Fuentes y destinos soportados

- Prácticamente todos los motores de base de datos de uso común son compatibles como **fuente**.
- Como **destino**, DMS soporta tanto bases de datos de AWS (**Aurora, RDS**) como otros servicios de
  analítica y almacenamiento: **Redshift, DynamoDB, S3, Kinesis Data Streams**.

## Tipos de migración

### Migración homogénea

Origen y destino usan el **mismo motor de base de datos** (ej. Aurora → Aurora) — no requiere ningún
cambio de esquema.

Pasos:

1. Configurar la base de datos de origen y destino como **endpoints** en DMS (dirección, puerto,
   credenciales).
2. Lanzar una **instancia de replicación**, que actúa como intermediaria y gestiona la transferencia.
3. Elegir el tipo de carga:
   - **Full load:** copia todos los datos de una vez.
   - **Full load + replicación continua:** además sincroniza continuamente los cambios nuevos usando
     **CDC (Change Data Capture)**.
4. Ejecutar el proceso — DMS gestiona la replicación garantizando consistencia de los datos y un impacto
   mínimo en el rendimiento de la base de datos de origen.

### Migración heterogénea

Origen y destino usan **motores de base de datos distintos**.

> ⚠️ Antes de iniciar la migración es necesario usar el **AWS Schema Conversion Tool (SCT)** — un punto
> clave a recordar de cara al examen.

- El **SCT** convierte el esquema (y el código del motor) de la base de datos de origen a uno compatible
  con el destino.
- Normalmente se instala en el entorno **on-premise**, y se conecta tanto al origen como al destino para
  evaluar y convertir el esquema.
- Una vez convertido el esquema, se sigue el **mismo proceso** que en la migración homogénea (endpoints →
  instancia de replicación → configurar opciones → ejecutar).

> ⚠️ La diferencia clave entre ambos tipos de migración es este paso previo de conversión de esquema con
> SCT, necesario únicamente en migraciones heterogéneas.
