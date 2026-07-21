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
├── 1-data-ingestion/     # S3, patrones de ingestión (batch/streaming), AWS Glue, práctica de crawler
├── 2-query-athena/       # (vacío por ahora)
├── 3-glue-deep-dive/     # (vacío por ahora)
├── 4-serverless-lambda/  # (vacío por ahora)
├── 5-data-streaming/     # (vacío por ahora)
└── infra/                # CDK (Python) — infraestructura de AWS para practicar el curso
```

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
- `cdk/cdk_stack.py` — stack único (`CdkStack`) con los recursos actuales:
  - Bucket S3 (`alvaro8317-dea-certification-{env_name}`).
  - Glue Database (`customers_{env_name}`) — nombres de Glue solo admiten minúsculas, números y
    guion bajo.
  - IAM Role para el Glue Crawler (managed policy `AWSGlueServiceRole`), con permiso de lectura
    restringido a `documents/*` del bucket.
  - Glue Crawler (`customers-crawler-{env_name}`) apuntando a `s3://<bucket>/documents/`, sin
    schedule (solo on-demand), con `table_prefix="cdk-table"`.
- `tests/unit/test_cdk_stack.py` — tests unitarios del stack (assertions sobre el template sintetizado).
- Proyecto CDK estándar: virtualenv en `.venv/`, dependencias en `requirements.txt` /
  `requirements-dev.txt`, comandos habituales `cdk synth`, `cdk diff`, `cdk deploy`.

Esta infraestructura evoluciona en paralelo a los apuntes: a medida que el curso avanza (Athena,
Glue avanzado, Lambda, streaming), es esperable que `cdk_stack.py` crezca con nuevos recursos.
