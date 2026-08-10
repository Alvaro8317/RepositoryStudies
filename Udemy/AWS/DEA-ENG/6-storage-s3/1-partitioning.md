# Particionamiento de datos en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es particionar?

**Particionar** significa organizar los datos dentro de un bucket S3 mediante una **estructura de
carpetas (directorios)**, en lugar de dejarlos todos sueltos en un mismo nivel.

Esa estructura se basa en uno o varios **atributos** de los datos — normalmente aquellos por los que
se suelen **filtrar o agregar** las consultas. El caso más común es particionar por **tiempo**:

```text
bucket/
└── datos/
    └── year=2023/
        └── month=01/
        └── month=02/
    └── year=2024/
        └── month=01/
```

También es habitual particionar por otros atributos, como la **región**, dependiendo de cómo se
acceda normalmente a los datos.

> ⚠️ La estructura de carpetas normalmente sigue un esquema **clave-valor** (`year=2023/month=01/...`),
> que es el método más común para nombrar las particiones.

## Por qué mejora el rendimiento

Cuando los datos están particionados, motores de consulta como **Amazon Athena** (o el propio
procesamiento con **AWS Glue**) no necesitan escanear todo el bucket: solo tienen que acceder a las
particiones que realmente son relevantes para la consulta, ignorando el resto.

- Se reduce la cantidad de datos escaneados.
- Mejora el rendimiento de las consultas (Athena) y del procesamiento (Glue).
- Como Athena cobra en función de los datos escaneados, particionar también reduce el **coste** de
  las consultas.

## Metadatos: el rol del Data Catalog

La estructura de carpetas por sí sola no es suficiente: para que un motor de consulta sepa cómo están
particionados los datos, esa información (las **claves de partición**) debe quedar registrada como
**metadatos** en el **Glue Data Catalog**.

- Los **Glue Crawlers** pueden encargarse de esto automáticamente: al recorrer el bucket, reconocen la
  estructura de carpetas y crean las claves de partición correspondientes, guardando los metadatos en
  el Data Catalog.
- Sin este registro de metadatos, aunque los datos estén físicamente organizados en carpetas, el motor
  de consulta no sabría interpretarlas como particiones.

## Otros beneficios: gestión de datos

Además del rendimiento en consultas, tener los datos particionados en carpetas también facilita la
**gestión de datos** en general — por ejemplo, aplicar **Lifecycle Rules** de forma más sencilla sobre
subconjuntos concretos de datos (como los de un año o mes determinado).

## Cómo decidir el esquema de partición

La regla general es particionar los datos **según se filtran o agregan habitualmente** en las
consultas. Si las consultas casi siempre filtran por fecha, particionar por fecha (año/mes/día) es lo
que más beneficio aporta; si se filtra sobre todo por región, conviene particionar por región, etc.
