# Práctica: configurar la Staging Area con esquemas

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Objetivo

Ver cómo implementar en la práctica las capas del `Data Warehouse` (empezando por la `Staging
Area`) en un entorno de base de datos real, usando `DBeaver` conectado a una instancia `PostgreSQL`
en `AWS RDS`.

## Bases de datos vs. esquemas como capas

No hay una única forma correcta de implementar las capas (`Staging Area`, `Core Layer`, etc.) en la
base de datos. Las dos opciones más comunes son:

| Enfoque                         | Descripción                                                                 |
|-----------------------------------|--------------------------------------------------------------------------------|
| **Esquemas** (la más habitual)   | Cada capa es un `schema` dentro de la misma base de datos (ej. esquema `staging`). Un esquema es básicamente un contenedor de tablas. |
| Bases de datos separadas         | Cada capa es una base de datos completamente distinta (ej. una base de datos `staging`). |

En este curso se implementan las capas como **esquemas**, por ser el enfoque más común en la
práctica.

## Estructura en DBeaver

Dentro de la conexión a la instancia `PostgreSQL`, se pueden tener varias bases de datos, y cada
base de datos actúa como contenedor principal de sus propios esquemas y tablas. Toda base de datos
nueva trae siempre disponible, por defecto, el esquema `public`.

## Crear una base de datos

### Vía interfaz gráfica

Clic derecho sobre `Databases` → `Create New Database` → asignar un nombre (ej. `DataWarehouseX`) →
codificación `UTF8`.

> ⚠️ Al crear la base de datos puede aparecer el error `permission denied for tablespace
> pg_default`. Esto ocurre porque el usuario de la instancia no es superusuario y no tiene permiso
> para crear nuevos tablespaces. El `tablespace` es solo el espacio en disco donde se almacenan los
> datos — **solución**: al crear la base de datos, cambiar el tablespace a `default` en vez de
> intentar crear uno nuevo. Con eso el error desaparece y la base de datos se crea con normalidad.

### Vía SQL

```sql
CREATE DATABASE datawarehousey;
```

Se ejecuta con `Ctrl + Enter` (o el botón de ejecutar). Tras crear la base de datos, hay que
refrescar (clic derecho sobre `Databases` → `Refresh`) para verla en el árbol de `DBeaver`.

### Eliminar una base de datos

Vía interfaz: clic derecho → `Delete`. Vía SQL:

```sql
DROP DATABASE datawarehousey;
```

## Crear el esquema de Staging Area

Igual que con las bases de datos, se puede crear un esquema desde la interfaz (clic derecho sobre
`Schemas` → `Create Schema`) o vía SQL:

```sql
CREATE SCHEMA staging;
```

- Si el nombre se escribe entre comillas (`CREATE SCHEMA "Staging";`), se vuelve **case-sensitive**
  y respeta las mayúsculas tal cual se escribieron.
- Sin comillas, el nombre del esquema se guarda en minúsculas, lo cual es el enfoque más común y
  simple.

Con esto queda creada la capa de `Staging Area` como esquema dentro de la base de datos del
`Data Warehouse`.

## Buena práctica: detener la instancia RDS cuando no se usa

Para evitar mantener recursos corriendo innecesariamente (y su costo asociado), se puede detener
temporalmente la instancia de `RDS` desde la consola de `AWS` cuando no se está usando activamente:

- Seleccionar la instancia → **Stop temporarily**: detiene la instancia hasta por **7 días**: pasado
  ese plazo, `AWS` la reinicia automáticamente sola.
- Al querer volver a usarla, basta con seleccionarla y elegir **Start** de nuevo.
- Detener la instancia toma cierto tiempo, ya que `AWS` genera automáticamente un snapshot de
  respaldo antes de completarse el apagado.

> ⚠️ Si se planea seguir usando la instancia el mismo día o al día siguiente, no vale la pena
> detenerla — el proceso de apagado/reinicio toma tiempo. Detenerla temporalmente es útil sobre
> todo entre sesiones de práctica más espaciadas en el tiempo.

Alternativa para pausas más largas (varios meses): guardar una **snapshot manual** de la instancia y
eliminarla, para luego restaurarla desde esa snapshot cuando se necesite de nuevo. Esto tiene un
pequeño costo de almacenamiento (bajo, ya que el almacenamiento en sí no es caro), pero evita el
costo de tener la instancia corriendo.

## Resumen

- Las capas del `Data Warehouse` se implementan comúnmente como **esquemas** dentro de una misma
  base de datos, aunque también es posible usar bases de datos separadas.
- Se puede crear/eliminar bases de datos y esquemas tanto desde la interfaz gráfica de `DBeaver`
  como con comandos SQL (`CREATE DATABASE`, `DROP DATABASE`, `CREATE SCHEMA`).
- Un error común al crear bases de datos con un usuario no superusuario es el permiso denegado sobre
  el tablespace — se resuelve usando el tablespace `default`.
- Buena práctica: detener la instancia `RDS` cuando no se esté usando activamente, para evitar
  costos innecesarios.
