# Ingesta de datos: Stateful vs. Stateless

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Sistemas con estado (Stateful) vs. sin estado (Stateless)

### Stateful

Un sistema **con estado** mantiene el **estado/contexto** de cada interacción con un usuario o cliente
entre solicitudes.

- Ejemplo: un sitio web donde, tras iniciar sesión y cambiar preferencias de usuario, esas preferencias
  se recuerdan en visitas posteriores.
- **Ventaja**: mejora la experiencia de usuario, ya que las interacciones previas se recuerdan y se
  reutilizan en solicitudes posteriores.

### Stateless

Un sistema **sin estado** procesa **cada nueva solicitud de forma independiente**, ignorando por
completo las interacciones anteriores.

- Ejemplo: una API RESTful, donde cada request debe incluir toda la información necesaria, ya que no
  existen datos de sesión almacenados entre llamadas.

## Aplicado a la ingesta de datos

### Ingesta stateful

El sistema de carga **recuerda lo que se ha procesado previamente** en un evento de ingestión, usando
mecanismos como:

- **Timestamps** (marcas de tiempo).
- **Offsets** (desplazamientos).
- **Estado de procesamiento**.

Esto permite cargar únicamente los datos **nuevos** que aún no se han procesado (carga incremental).

### Ingesta stateless

El sistema **no almacena nada** sobre ejecuciones anteriores; en cada ejecución se puede volver a cargar
todo desde cero.

- No es necesariamente malo: a veces simplemente **no es necesario** recordar el historial, y esto
  simplifica el sistema.
- Ejemplo: **AWS Lambda** ejecutando código en respuesta a un evento — se procesa únicamente el objeto
  asociado a ese evento concreto (el que dispara el trigger), sin necesidad de recordar cargas
  anteriores.

> ⚠️ La elección entre stateful y stateless depende del caso de uso. Por ejemplo, si en una carpeta de un
> bucket S3 van apareciendo archivos adicionales con el tiempo, puede interesar una ingesta **stateful**
> para aprovechar la información de cargas anteriores y no reprocesar lo ya cargado.

## Ejemplos en AWS

| Servicio                        | Soporte stateful               | Detalle                                                                                                                                                     |
| ------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon Kinesis Data Streams** | Sí                             | Necesita mantener el **número de secuencia** de los datos ya procesados, para poder reanudar la ingesta tras un fallo desde el punto exacto donde se quedó. |
| **AWS Data Pipeline**           | Ambos                          | Soporta tanto ingesta stateful como stateless según la configuración.                                                                                       |
| **AWS Glue (ETL Jobs)**         | Sí, mediante **Job Bookmarks** | Los bookmarks permiten habilitar **carga incremental**: Glue hace seguimiento de qué datos ya se han procesado y solo carga los datos nuevos.               |
