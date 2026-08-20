# Redshift: ETL vs. ELT y transformaciones in-database

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Dos patrones para mover datos al data warehouse

Para mover datos desde los sistemas de origen hasta un almacén de datos como Redshift existen dos
patrones: **ETL** y **ELT**. Redshift da soporte a ambos.

### ETL (Extract, Transform, Load)

- Es el enfoque **más tradicional**.
- Los datos se **extraen** del sistema de origen, se **transforman** y **después** se **cargan**
  en el sistema de destino (ej. Redshift).
- Los datos que llegan al almacén de datos ya están **transformados/agregados**.
- Requiere un tiempo específico para cargar periódicamente los datos con esas transformaciones ya
  aplicadas — las transformaciones pueden ser **intensivas en cómputo** según el volumen de datos,
  por lo que tradicionalmente se hacían **antes** de cargar, fuera del data warehouse.

### ELT (Extract, Load, Transform)

- Patrón **cada vez más común**.
- Los datos se **cargan tal cual** desde el sistema de origen (con quizás pequeños cambios), y las
  **transformaciones principales se aplican después, sobre la marcha, en el sistema de destino**.
- Es posible gracias a que las bases de datos modernas (como Redshift) tienen mucha más
  **potencia de cómputo** disponible.
- Aporta más **flexibilidad**: no hace falta anticipar todos los casos de uso de antemano — las
  transformaciones se aplican **cuando se necesitan**, manteniendo todos los casos de uso
  disponibles sobre los datos crudos.

> ⚠️ La diferencia clave es **cuándo** ocurre la transformación: **antes** de cargar (ETL) frente a
> **después** de cargar, sobre la marcha (ELT).

## Transformaciones in-database (soporte a ELT)

Redshift permite procesar y transformar los datos **directamente dentro del propio data
warehouse** — esto es lo que hace posible el patrón ELT:

- **Transformación con SQL**: soporte completo de SQL para ejecutar consultas que transforman los
  datos — agregaciones, limpieza de datos, `JOIN`s, creación de columnas adicionales, etc.
- **Stored procedures**: para transformaciones más complejas, facilitando su **reutilización**.
- **User-Defined Functions (UDFs)**: funciones definidas por el usuario, escritas en **Python** o
  **SQL**, para implementar transformaciones personalizadas más difíciles de lograr con SQL
  estándar.

## Integración con herramientas ETL externas

Cuando se prefiere usar una herramienta externa para las transformaciones, Redshift puede
conectarse a cualquier plataforma ETL mediante **controladores JDBC y ODBC**.

Algunas plataformas populares se integran directamente con Redshift:

- **Informatica**
- **Matillion**
- **dbt**
- Herramientas nativas de AWS, como **AWS Glue**

## Resumen: ETL vs. ELT

| Aspecto                 | ETL                                             | ELT                                                              |
| ----------------------- | ----------------------------------------------- | ---------------------------------------------------------------- |
| **Orden**               | Extract → Transform → Load                      | Extract → Load → Transform                                       |
| **Cuándo transforma**   | Antes de cargar los datos                       | Después de cargar, sobre la marcha                               |
| **Datos en el destino** | Ya transformados/agregados                      | Crudos (o con cambios mínimos), listos para transformarse        |
| **Flexibilidad**        | Menor — hay que anticipar los casos de uso      | Mayor — las transformaciones se aplican cuando se necesitan      |
| **Requisito**           | Proceso de transformación externo bien definido | Data warehouse con suficiente potencia de cómputo (ej. Redshift) |
