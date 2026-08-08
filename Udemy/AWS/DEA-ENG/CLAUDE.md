# DEA-ENG — Apuntes de estudio para AWS Certified Data Engineer – Associate (DEA-C01)

Este repositorio contiene los apuntes de Alvaro para preparar la certificación **AWS Certified Data
Engineer – Associate (DEA-C01)**, basados en un curso de Udemy. También incluye la IaC (AWS CDK en
Python, carpeta `infra/`) que se usa para practicar los conceptos del curso en una cuenta real de AWS.

## Rol de Claude en este repo

Claude actúa como asistente para **transformar transcripciones de clases del curso en apuntes en
Markdown**. El flujo de trabajo es:

1. El usuario indica en qué carpeta (módulo) deben ir los apuntes de la próxima clase.
2. El usuario pega la transcripción de la clase (texto crudo, puede venir con muletillas, repeticiones, etc.).
3. Claude debe:
   - Capturar **lo más importante** de la transcripción: conceptos clave, definiciones, comparativas,
     pasos de práctica, tablas cuando ayuden a resumir, advertencias/notas importantes (usar `>` con ⚠️
     cuando aplique, como en los archivos existentes).
   - Redactar el apunte en **español**, con el mismo tono y nivel de detalle que los archivos ya
     existentes en `1-data-ingestion/` (ver ejemplos abajo).
   - Proponer **2-3 nombres de archivo candidatos** que respeten la nomenclatura del proyecto (ver
     sección siguiente) para que el usuario elija antes de escribir el archivo definitivo.
   - Escribir el apunte **directamente en la ruta final** (`<carpeta>/<numero>-<slug-elegido>.md`) una
     vez el usuario elige el nombre — no redactarlo primero en un scratchpad/tmp y copiarlo después.
     Si el usuario decide renombrar el archivo más adelante, basta con hacer `mv`/renombrar, no hace
     falta reescribir el contenido.
4. Claude NO debe archivar por su cuenta transcripciones futuras sin que el usuario indique
   primero la carpeta destino.

### Transcripción: cuidado con errores de dictado y términos en inglés

Las transcripciones vienen de audio a texto y pueden contener **errores de reconocimiento de voz**,
especialmente sobre términos técnicos en inglés que el motor de transcripción "traduce" o distorsiona
fonéticamente. Antes de redactar el apunte, Claude debe interpretar el contexto y corregir estos casos:

- Ejemplo típico: **"pegamento"** (traducción literal de *glue*) probablemente es un error de
  transcripción de **Glue** / **AWS Glue** / **Glue Crawler**, no una traducción real que deba usarse.
- Los **términos y nombres propios de servicios/conceptos de AWS deben quedarse en inglés**, tal como
  aparecen en la documentación oficial y en los apuntes existentes (ej. `Glue Crawlers`, `Glue Data
  Catalog`, `ETL Jobs`, `Data Lake`, `Lifecycle Rules`, `Versioning`, `Bucket`, `Key`, etc.) — no
  traducirlos al español aunque la transcripción los haya traducido o distorsionado.
- Si Claude detecta una palabra o frase que suena a una mala transcripción de un término técnico en
  inglés (fonéticamente parecida, fuera de contexto, etc.), debe usar el término correcto en inglés y,
  si hay ambigüedad real sobre a qué servicio/concepto se refería, preguntar al usuario antes de asumir.

## Convención de nombres de archivo

Cada carpeta de módulo numerada (`1-`, `2-`, `3-`...) contiene archivos Markdown numerados
secuencialmente dentro de esa misma carpeta, empezando en `1-`:

```text
<numero>-<slug-descriptivo-en-ingles-o-espanol-corto>.md
```

Ejemplos reales en `1-data-ingestion/`:

- `1-s3.md`
- `2-data-ingestion.md`
- `3-glue.md`
- `4-practice-glue.md`

Reglas:

- El número siempre va primero, seguido de un guion.
- El slug es corto, en minúsculas, palabras separadas por guiones.
- Los archivos de práctica/laboratorio suelen llevar el prefijo `practice-` (ej. `4-practice-glue.md`).
- La numeración es **por carpeta**, no global — cada módulo reinicia en `1-`.
- No renombrar ni renumerar archivos ya existentes al añadir uno nuevo; el nuevo archivo simplemente
  continúa la secuencia del folder correspondiente.

## Estructura del repositorio

```text
DEA-ENG/
├── 1-data-ingestion/         # S3, patrones de ingestión (batch/streaming), AWS Glue, práctica de crawler
├── 2-query-athena/           # Athena, federated queries, coste/rendimiento, workgroups
├── 3-glue-deep-dive/         # Glue avanzado: coste, budgets, jobs, bookmarks, workflows, DataBrew...
├── 4-serverless-lambda/      # Lambda, práctica Lambda+S3, Lambda Layers
├── 5-data-streaming/         # Kinesis (overview, Data Streams, Firehose), replayability, enhanced fan-out
├── 6-storage-s3/             # (vacío por ahora)
├── 7-other-storage-services/ # EBS, snapshots/volumes, EFS, AWS Backup
├── 8-dynamo-db/              # (vacío por ahora)
├── 9-redshift-data-warehouse/ # (vacío por ahora)
├── 10-other-db-services/     # (vacío por ahora)
└── infra/                    # CDK (Python) — infraestructura de AWS para practicar el curso
```

> ⚠️ Este árbol puede desactualizarse a medida que se añaden apuntes/carpetas nuevas. Si vas a
> confiar en él (por ejemplo, para saber qué carpetas existen o qué contienen), verifica primero con
> `ls` en vez de asumir que está al día.

### Formato de cada apunte

Cada archivo `.md` sigue esta estructura:

- Título `#` con el nombre del servicio/tema.
- Línea de contexto: `> Curso: AWS Certified Data Engineer – Associate (DEA-C01)`
- Secciones con `##`/`###` por subtema.
- Tablas Markdown para comparativas o resúmenes de conceptos.
- Notas de advertencia con `> ⚠️ ...` cuando algo es un detalle importante o contraintuitivo.

### Formateo automático

Cada `.md` que Claude escribe o edita se formatea automáticamente con **markdownlint-cli2** vía un
hook `PostToolUse` definido en `.claude/settings.json` (config en `.markdownlint-cli2.jsonc`). No
requiere acción manual — Claude no necesita ejecutar el linter a mano tras escribir un apunte.

## Carpeta `infra/`

IaC en **AWS CDK (Python)** para desplegar los recursos de AWS usados en los ejemplos prácticos del
curso.

- `app.py` — entry point del CDK app. Cuenta/región se resuelven vía el profile `local` (definido en
  `cdk.json`), variables `CDK_DEFAULT_ACCOUNT` / `CDK_DEFAULT_REGION`, y `ENVIRONMENT` (default `prod`).
- `cdk/cdk_stack.py` — stack único (`CdkStack`) que solo orquesta: crea el bucket S3 compartido
  (`alvaro8317-dea-certification-{env_name}`) y delega el resto de recursos a funciones en
  `cdk/resources/`, agrupadas por servicio. Todas esas funciones reciben el propio stack (`self`)
  como `scope` de sus recursos — mismo nivel que si estuvieran inline en `cdk_stack.py` — para no
  alterar los logical IDs de CloudFormation de recursos ya desplegados (`cdk diff` debe dar "no
  differences" tras cualquier refactor de este tipo).
  - `cdk/resources/streaming.py` (`add_streaming_resources`):
    - Kinesis Stream on-demand (`data-stream-{env_name}`).
    - Lambda `stream-consumer-{env_name}` (`cdk/lambda/stream_consumer/index.py`) que consume el
      stream como event source (consumidor estándar, `starting_position=LATEST`, `batch_size=100`) y
      escribe en `streaming-data/*` del bucket.
    - Firehose delivery stream `kds-to-s3-{env_name}` (origen: el mismo Kinesis Stream; destino: el
      bucket bajo `firehose-streaming-cdk/*`; buffer de 5 MB / 300 s) con transformación vía Lambda
      `firehose-transform-{env_name}` (`cdk/lambda/firehose_transform/index.py`).
    - Los roles IAM del Firehose (`firehose-delivery-role-{env_name}`) usan `Grant.apply_before(...)`
      sobre el `CfnDeliveryStream` — sin eso, CloudFormation puede crear el delivery stream antes de
      que la policy del rol exista, y falla con `not authorized to perform: kinesis:DescribeStream`.
  - `cdk/resources/glue.py` (`add_glue_resources`):
    - Glue Database (`customers_{env_name}`) — nombres de Glue solo admiten minúsculas, números y
      guion bajo.
    - IAM Role para el Glue Crawler (managed policy `AWSGlueServiceRole`), con permiso de lectura
      restringido a `documents/*` del bucket.
    - Glue Crawler (`customers-crawler-{env_name}`) apuntando a `s3://<bucket>/documents/`, sin
      schedule (solo on-demand), con `table_prefix="cdk-table"`.
    - Glue Job `documents-to-parquet-{env_name}` (script en `cdk/scripts/documents_to_parquet.py`,
      subido como `s3_assets.Asset`) que convierte `documents/*` a Parquet en `documents-target/*`,
      sin schedule (on-demand), Glue 4.0, 2 workers `G.1X`.
- `tests/unit/test_cdk_stack.py` — tests unitarios del stack (assertions sobre el template sintetizado).
- Proyecto CDK estándar: virtualenv en `.venv/`, dependencias en `requirements.txt` /
  `requirements-dev.txt`, comandos habituales `cdk synth`, `cdk diff`, `cdk deploy`.

Esta infraestructura evoluciona en paralelo a los apuntes: a medida que el curso avanza (Athena,
Glue avanzado, Lambda, streaming), es esperable que `cdk/resources/` crezca con nuevos módulos por
servicio (y `cdk_stack.py` con una línea más para invocarlos).
