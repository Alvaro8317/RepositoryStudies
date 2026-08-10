# S3 Object Lambda

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**S3 Object Lambda** permite **transformar los datos sobre la marcha** a medida que se recuperan de
S3, usando una función Lambda — sin necesidad de crear ni almacenar una copia separada de los datos
transformados.

Útil cuando se necesitan los mismos datos en **distintas versiones** — por ejemplo, en un formato
distinto, o con cierta información rectificada — sin duplicar el dataset original.

## Casos de uso

- **Filtrar información sensible** — ej. redactar datos de identificación personal (PII) antes de
  entregarlos para análisis.
- **Redimensionar imágenes**.
- **Cambiar el formato de los datos** — ej. convertir XML a JSON.
- **Aumentar los datos (data augmentation)** — añadir información adicional proveniente de otros
  servicios o bases de datos.

## Mecanismo de funcionamiento

1. Un usuario o aplicación inicia una solicitud para acceder a los datos del bucket, pero la dirige al
   **S3 Object Lambda Access Point** en lugar de al bucket directamente.
2. Este access point actúa como **intermediario**: en lugar de devolver el objeto tal cual, invoca a
   la **función Lambda** conectada a él.
3. La función Lambda accede a los datos originales a través de un **access point estándar** de S3, y
   aplica la lógica de transformación definida (redactar PII, convertir formato, enriquecer datos,
   etc.).
4. La función Lambda devuelve los datos ya transformados al **S3 Object Lambda Access Point**.
5. El access point devuelve esos datos transformados al usuario/aplicación que hizo la solicitud
   original.

> El dato original en el bucket **no se modifica ni se duplica** — la transformación ocurre "al vuelo"
> en cada solicitud, a través de la función Lambda.
