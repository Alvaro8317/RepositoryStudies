# Práctica: Encriptación en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: crear un bucket, revisar la configuración de cifrado por defecto y anular ese valor
para un objeto ya cargado. Ver la teoría en [[10-encryption]].

## Creación del bucket

- Se crea un bucket con nombre + sufijo numérico (ej. `prueba-de-encriptacion-...`), dejando el resto
  de ajustes por defecto.
- En la configuración del bucket aparece la sección de **cifrado por defecto (default encryption)**,
  donde se puede elegir entre las opciones de cifrado del lado del servidor vistas en
  [[10-encryption]] (SSE-S3, SSE-KMS, etc.).
- En este ejemplo se deja el valor por defecto: **SSE-S3** (claves gestionadas por Amazon S3).

> El cifrado por defecto configurado a nivel de bucket se aplica a **todos los objetos nuevos** que se
> suban a partir de ese momento. Ese valor se puede **anular por objeto individual**, tanto durante la
> carga como después, sobre un objeto ya existente.

## Subir un objeto con el cifrado por defecto

- Al subir un archivo sin especificar una clave de cifrado propia, se usa el valor por defecto del
  bucket.
- En las **propiedades** del objeto ya cargado, la sección de cifrado del lado del servidor confirma
  que se está usando **SSE-S3** (clave gestionada por S3), heredado de la configuración del bucket.

## Anular el cifrado a nivel de objeto

- Desde las propiedades de un objeto ya cargado se puede **editar** el cifrado para sobrescribir la
  configuración por defecto del bucket.
- Se cambia a **SSE-KMS**, seleccionando una clave de AWS KMS (en este caso, la clave por defecto
  disponible en la cuenta).
- Al guardar, las propiedades del objeto muestran ahora el cifrado del lado del servidor con **AWS
  KMS**, junto con el **ARN de la clave** usada — desde ahí se puede navegar directamente a la consola
  de KMS para revisar o gestionar esa clave.

## Limpieza de recursos

> ⚠️ Al terminar la práctica, hay que **eliminar el bucket** creado para no dejar recursos sueltos:
> primero vaciarlo (**Empty**) y después eliminarlo (**Delete**). No basta con borrar los objetos —
> también hay que borrar el bucket en sí.
