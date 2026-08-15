# Data Warehouse – The Ultimate Guide — Apuntes de estudio

Este repositorio contiene los apuntes de Alvaro del curso de Udemy **"Data Warehouse - The Ultimate
Guide"**: fundamentos de data warehousing, arquitectura, modelado dimensional (hechos y dimensiones),
Slowly Changing Dimensions, procesos ETL/ELT, un caso de estudio completo y optimización de data
warehouses modernos.

## Rol de Claude en este repo

Claude actúa como asistente para **transformar transcripciones de clases del curso en apuntes en
Markdown**. El flujo de trabajo es:

1. El usuario indica en qué carpeta (módulo) deben ir los apuntes de la próxima clase.
2. El usuario pega la transcripción de la clase (texto crudo, puede venir con muletillas, repeticiones, etc.).
3. Claude debe:
   - Capturar **lo más importante** de la transcripción: conceptos clave, definiciones, comparativas,
     ejemplos numéricos (ej. tablas de hechos/dimensiones de muestra), pasos de práctica, tablas
     cuando ayuden a resumir, advertencias/notas importantes (usar `>` con ⚠️ cuando aplique).
   - Redactar el apunte en **español**, con estructura clara y nivel de detalle consistente con los
     archivos ya existentes en la carpeta correspondiente (ver ejemplos en carpetas ya pobladas).
   - Proponer **2-3 nombres de archivo candidatos** que respeten la nomenclatura del proyecto (ver
     sección siguiente) para que el usuario elija antes de escribir el archivo definitivo.
   - Escribir el apunte **directamente en la ruta final** (`<carpeta>/<numero>-<slug-elegido>.md`) una
     vez el usuario elige el nombre — no redactarlo primero en un scratchpad/tmp y copiarlo después.
4. Claude NO debe archivar por su cuenta transcripciones futuras sin que el usuario indique
   primero la carpeta destino.

### Transcripción: cuidado con errores de dictado y términos en inglés

Las transcripciones vienen de audio a texto y pueden contener **errores de reconocimiento de voz**,
especialmente sobre términos técnicos de data warehousing en inglés que el motor de transcripción
"traduce" o distorsiona fonéticamente. Antes de redactar el apunte, Claude debe interpretar el
contexto y corregir estos casos:

- Los **términos y nombres propios de data warehousing deben quedarse en inglés**, tal como aparecen
  en la literatura del área (ej. `Data Warehouse`, `Data Mart`, `Data Lake`, `Staging Area`, `ETL`,
  `ELT`, `OLAP`, `OLTP`, `Star Schema`, `Snowflake Schema`, `Fact Table`, `Dimension Table`, `Grain`,
  `Surrogate Key`, `Natural Key`, `Slowly Changing Dimensions` / `SCD Type 0-6`, `Change Data Capture`
  / `CDC`, `Junk Dimension`, `Conformed Dimension`, `Degenerate Dimension`) — no traducirlos al
  español aunque la transcripción los haya traducido o distorsionado (ej. "dimensión que cambia
  lentamente" en vez de `Slowly Changing Dimension`).
- Si el curso menciona herramientas/plataformas concretas (ej. `Redshift`, `Snowflake`, `BigQuery`,
  `dbt`, `Airflow`, `Fivetran`), mantener el nombre propio tal cual, sin traducir ni alterar.
- Si Claude detecta una palabra o frase que suena a una mala transcripción de un término técnico en
  inglés (fonéticamente parecida, fuera de contexto), debe usar el término correcto en inglés y, si
  hay ambigüedad real sobre a qué concepto se refería, preguntar al usuario antes de asumir.

## Convención de nombres de archivo

Cada carpeta de módulo numerada (`1-`, `2-`, `3-`...) contiene archivos Markdown numerados
secuencialmente dentro de esa misma carpeta, empezando en `1-`:

```text
<numero>-<slug-descriptivo-en-ingles>.md
```

Reglas:

- El número siempre va primero, seguido de un guion.
- El slug es corto, en minúsculas, **siempre en inglés**, palabras separadas por guiones (el
  contenido del apunte sí va en español, solo el nombre de archivo va en inglés).
- Los archivos de práctica/laboratorio suelen llevar el prefijo `practice-` (ej.
  `3-practice-star-schema.md`); los del caso de estudio del curso pueden llevar `case-study-` si
  ayuda a distinguirlos dentro de su carpeta.
- La numeración es **por carpeta**, no global — cada módulo reinicia en `1-`.
- No renombrar ni renumerar archivos ya existentes al añadir uno nuevo; el nuevo archivo simplemente
  continúa la secuencia del folder correspondiente.

## Estructura del repositorio

Estructura basada en el temario oficial del curso en Udemy:

```text
warehouse-guide/
├── 1-data-warehouse-basics/                  # Introducción al curso + conceptos base (qué es un DW, BI) + setup práctico (RDS/Postgres, DBeaver)
├── 2-data-warehouse-architecture/            # Arquitecturas de DW (capas, staging, core, data marts...)
├── 3-dimensional-modeling/                   # Modelado dimensional: star/snowflake schema, grain
├── 4-facts/                                  # Tablas de hechos: tipos, granularidad, medidas aditivas/no aditivas
├── 5-dimensions/                             # Tablas de dimensiones: jerarquías, conformed/junk/degenerate
├── 6-slowly-changing-dimensions/             # SCD Type 0-6, ejemplos prácticos
├── 7-etl-process/                            # Proceso ETL completo: extracción, transformación, carga
├── 8-etl-tools/                              # Panorama de herramientas ETL
├── 9-case-study-creating-a-data-warehouse/   # Caso de estudio end-to-end del curso
├── 10-etl-vs-elt/                            # Comparativa ETL vs. ELT
├── 11-using-a-data-warehouse/                # Consumo del DW (reporting, BI, consultas)
├── 12-optimizing-a-data-warehouse/           # Optimización: indexación, particionado, rendimiento
├── 13-modern-data-warehouses/                # DW modernos (cloud, lakehouse, tendencias actuales)
├── 14-bonus/                                  # Contenido bonus del curso
└── infra/                                    # CDK (Python) — infraestructura de AWS para practicar el curso
```

> ⚠️ Todas estas carpetas parten vacías (el curso recién empieza). Este árbol puede desactualizarse a
> medida que se añaden apuntes/carpetas nuevas — verifica primero con `ls` antes de asumir que está
> al día, y si algún módulo termina con más o menos clases de las listadas en Udemy, ajusta el árbol.

### Formato de cada apunte

Cada archivo `.md` sigue esta estructura:

- Título `#` con el nombre del tema/clase.
- Línea de contexto: `> Curso: Data Warehouse - The Ultimate Guide (Udemy)`
- Secciones con `##`/`###` por subtema.
- Tablas Markdown para comparativas o resúmenes de conceptos (ej. columnas de una tabla de hechos,
  tipos de SCD, ETL vs. ELT).
- Ejemplos ilustrativos con tablas de datos de muestra cuando el tema lo pida (ej. una fila antes/
  después de aplicar SCD Type 2).
- Notas de advertencia con `> ⚠️ ...` cuando algo es un detalle importante o contraintuitivo.

## Carpeta `infra/`

IaC en **AWS CDK (Python)** para desplegar los recursos de AWS usados en la práctica del curso (ej.
el caso de estudio de `9-case-study-creating-a-data-warehouse/`).

- `app.py` — entry point del CDK app. Lee `DB_PASSWORD` desde `.env` (vía `python-dotenv`, nunca
  hardcodeado ni commiteado — `.env` está en `.gitignore`, hay un `.env.example` como plantilla).
  Cuenta/región se resuelven vía el profile `local` (definido en `cdk.json`) y las variables
  `CDK_DEFAULT_ACCOUNT`/`CDK_DEFAULT_REGION`. Detecta automáticamente la IP pública actual (para el
  security group de la BD) contra `https://checkip.amazonaws.com`; se puede sobreescribir con
  `cdk deploy -c myIp=x.x.x.x` si la detección falla o cambia la IP tras el deploy.
- `cdk/cdk_stack.py` — stack único (`CdkStack`, id `data-warehouse-guide-course`) con:
  - Una VPC sin NAT gateways (solo subnets públicas — el curso no necesita más, y así se evita el
    costo de NAT).
  - Un Security Group que permite el puerto 5432 (PostgreSQL) únicamente desde la IP detectada en
    `app.py`.
  - Una instancia RDS PostgreSQL (`db-postgres-warehouse`, engine `PostgresEngineVersion.VER_18_3`,
    `db.t4g.micro`, 20 GB `gp3`, single-AZ, sin Multi-AZ, `publicly_accessible=True`) — dimensionada
    para caer dentro del free tier de RDS. Usuario por defecto (`postgres`), contraseña tomada de
    `DB_PASSWORD` vía `Credentials.from_password(...)` en vez del secreto autogenerado en Secrets
    Manager que CDK crearía por defecto.
  - `removal_policy=DESTROY` y `deletion_protection=False` (entorno de práctica, no producción).
- `tests/unit/test_cdk_stack.py` — tests unitarios del stack (assertions sobre el template
  sintetizado: tipo de instancia, motor, storage, y la regla del security group).
- Proyecto CDK estándar: virtualenv en `.venv/`, dependencias en `requirements.txt` /
  `requirements-dev.txt`, comandos habituales `cdk synth`, `cdk diff`, `cdk deploy`.

> ⚠️ La instancia es públicamente accesible (para poder conectarse desde herramientas locales como
> psql/DBeaver/dbt) pero el security group solo permite tráfico desde la IP detectada al momento del
> deploy. Si tu IP cambia, hay que volver a desplegar (o pasar `-c myIp=...`) para poder conectarte.
