# Notificaciones de Eventos en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

Un **evento** es cualquier cosa que sucede en un bucket (ej. se sube un archivo). Las
**notificaciones de eventos de S3** permiten reaccionar automáticamente a esos eventos, activando
alguna acción — por ejemplo, procesar un archivo recién subido con una función Lambda.

## Tipos de eventos

- **Creación de objetos** (`ObjectCreated`).
- **Eliminación de objetos** (`ObjectRemoved`).
- **Restauración de objetos** (ej. desde Glacier).
- **Replicación de objetos**.
- Eventos relacionados con el **ciclo de vida** — ej. expiración de una Lifecycle Rule, o transición a
  otra clase de almacenamiento.
- **Archivado automático inteligente** (relacionado con Intelligent-Tiering).
- **Etiquetado de objetos** (object tagging).
- **`ObjectAcl:Put`** — cambios en la ACL de un objeto.

## Destinos de las notificaciones

Una notificación de evento puede enrutarse a:

- **Amazon SNS** — para enviar un mensaje/notificación.
- **Amazon SQS** — para encolar el evento y procesarlo después.
- **AWS Lambda** — para invocar una función directamente (caso de uso muy común: procesar un archivo
  recién subido, guardar metadatos, etc.).
- **Amazon EventBridge** — para enrutar el evento y aplicar lógica más compleja (reglas, múltiples
  destinos, etc.).

## Filtrado de eventos

### Por método de creación

Dentro de `ObjectCreated` se puede filtrar por el método concreto usado para subir el objeto — por
ejemplo `Put` o `Post`. Usando un comodín (`*`) se capturan todos los métodos de creación sin
distinguir cuál se usó.

### Por prefijo y sufijo

- **Filtro de prefijo** — limita el evento a objetos dentro de un directorio/carpeta concreto del
  bucket (ej. solo objetos subidos a `imagenes/`).
- **Filtro de sufijo** — limita el evento según la extensión/terminación del nombre del archivo (ej.
  solo archivos que terminan en `.jpeg`).

Estos filtros permiten, por ejemplo, activar una función Lambda **solo** cuando se sube un CSV a una
carpeta específica, en lugar de para cualquier objeto del bucket.

## Ejemplo de uso

Configurar una notificación para el evento `ObjectCreated:Put` en todo el bucket, que active una
función Lambda cada vez que se suba un archivo con ese método — por ejemplo, para almacenar el
archivo (o metadatos sobre esa operación) en una base de datos RDS.
