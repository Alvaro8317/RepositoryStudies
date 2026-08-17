# Bases de datos in-memory

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Qué son y cuándo se usan?

Las bases de datos **in-memory** están muy optimizadas para el **rendimiento de consulta**. Su caso
de uso típico es cualquier escenario que requiera un alto rendimiento de consultas — típicamente
casos de uso **analíticos**.

- Por eso se usan habitualmente en los `Data Marts`: la capa de acceso final para usuarios y
  aplicaciones, donde no queremos que el usuario espere mucho tiempo hasta ver los datos en un
  visual o reporte.
- Esta tecnología es independiente de si los datos están estructurados de forma relacional o no
  relacional — existen opciones in-memory para ambos casos.

## Por qué son más rápidas

Las bases de datos **tradicionales** almacenan los datos en disco duro o SSD. Cuando se consultan
los datos, primero hay que **cargarlos del disco a memoria** para procesarlos — y ese tiempo de
carga es, de hecho, el origen de la mayor parte del tiempo de espera de una consulta.

Las bases de datos **in-memory** se construyen sin depender del disco: todos los datos residen
siempre en memoria. Al eliminar el tiempo de carga desde disco, el rendimiento de consulta mejora
drásticamente.

Además, suelen apoyarse en técnicas adicionales propias de esta tecnología:

- **Almacenamiento columnar** (`columnar storage`): los datos se escanean por columna en vez de por
  fila.
- **Planes de consulta en paralelo**: consultas grandes se dividen en partes que se procesan en
  paralelo en distintos hilos.

## El problema de la durabilidad

Las bases de datos in-memory no son la solución perfecta para todo — tienen un costo asociado.

> ⚠️ El reto principal es la **durabilidad** (`durability`): si la base de datos in-memory pierde
> alimentación eléctrica o se reinicia, los datos almacenados solo en memoria se **pierden por
> completo**. Esto es un problema serio, ya que la durabilidad es un requisito clave de cualquier
> base de datos.

Para resolverlo, se recurre a tecnología adicional:

- **Snapshots** (instantáneas): representan un estado específico de la base de datos in-memory,
  guardado en disco, al que se puede volver si se pierden los datos (por ejemplo, antes de un
  reinicio o una actualización de la base de datos).

## Costo: por qué no siempre conviene usarlas para todo

Aunque el hardware necesario para estas bases de datos se va abaratando con el tiempo, el volumen de
datos que las empresas necesitan manejar crece **incluso más rápido** que esa reducción de costo —
por lo que el costo sigue siendo un factor muy relevante a considerar.

> ⚠️ Las bases de datos tradicionales (basadas en disco) también siguen optimizándose y reduciendo
> su dependencia del disco para mejorar su propio rendimiento, así que la brecha de rendimiento no
> es estática — conviene evaluar caso por caso si una base de datos in-memory realmente se justifica.

Precisamente por este costo, si se usa una base de datos in-memory para un `Data Mart`, conviene ser
muy específico con el caso de uso y cargar **solo los datos relevantes** para ese caso puntual — una
de las razones por las que los `Data Marts` (subconjuntos acotados de datos) tienen sentido en la
práctica, más allá de la usabilidad.

## Ejemplos de productos

| Producto                         | Proveedor / tipo          |
| -------------------------------- | ------------------------- |
| `SAP HANA`                       | SAP                       |
| `Microsoft SQL In-Memory Tables` | Microsoft SQL Server      |
| Tecnología in-memory de `Oracle` | Oracle                    |
| `Amazon MemoryDB`                | Servicio en la nube (AWS) |

## Nota: ¿bases de datos in-memory en un lakehouse (S3 + Glue)?

> Nota propia (fuera de la transcripción del curso), aplicando el concepto a una arquitectura de
> lakehouse en AWS.

No directamente como parte del lakehouse en sí, pero sí como una capa adicional encima de él — el
mismo patrón `Core Layer` → `Data Mart` visto en este módulo.

- **Por qué no "dentro" del lakehouse**: `S3` es almacenamiento de objetos en disco, justo el tipo
  de storage que las bases in-memory buscan evitar. `Glue Data Catalog` solo guarda metadatos
  (esquemas, particiones, ubicación de archivos), no es un motor de consulta ni almacena datos en
  memoria. Motores típicos sobre este stack (`Athena`, `Redshift Spectrum`, `EMR`/`Spark`, `Trino`)
  consultan los datos en `S3` bajo demanda, sin mantener el dataset completo residente en memoria
  entre consultas.
- **Cómo sí se logra el patrón in-memory**: tratar el lakehouse (`S3` + `Glue`) como la `Core
  Layer`, y construir un `Data Mart` con una base in-memory (`Amazon MemoryDB`, `ElastiCache`) que
  cargue solo el subconjunto de datos relevante para un caso de uso específico (ej. un dashboard de
  BI que necesita baja latencia) — la misma razón de ser de los `Data Marts` explicada arriba.
- **Alternativas intermedias** muy usadas en la práctica: `Redshift` (con result caching y su propia
  capa de storage optimizada), o motores OLAP como `Apache Druid` / `ClickHouse`, que combinan
  indexación en memoria con datos de origen en `S3` para acelerar consultas repetidas sin mover todo
  el dataset a una base in-memory pura.

## Próxima clase

Los **cubos** (`cubes`), una forma más tradicional de aumentar el rendimiento de consulta en los
`Data Marts`.
