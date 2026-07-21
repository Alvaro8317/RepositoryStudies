# AWS Glue — Coste

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## DPUs (Data Processing Units)

La unidad base de facturación en Glue es la **DPU (Data Processing Unit)**: la potencia de cómputo
que se provisiona para ejecutar Crawlers, ETL Jobs, Notebooks e Interactive Sessions.

- Se paga una **tarifa por hora de DPU**, facturada **por segundos**.
- La tarifa de referencia (puede variar con el tiempo — conviene comprobarla en la web de AWS) es de
  **$0.44 por hora de DPU**.

## Glue Crawlers

- Tarifa por hora según el número de DPUs usadas, facturada por segundos.
- **Mínimo de facturación: 10 minutos** por ejecución.

## Glue Data Catalog

- **Gratuito hasta 1 millón de objetos** almacenados.
- Por encima del millón de objetos: **$1 por cada 100.000 objetos adicionales al mes**.
- Para fines de práctica/formación, es muy improbable llegar a ese límite.

## ETL Jobs

Tarifa por hora de DPU (~$0.44/hora), facturada por segundos, con un mínimo de facturación que
depende de la versión de Glue:

| Versión de Glue | Mínimo de facturación |
| --------------------- | ---------------------- |
| **0.8 / 0.9** | 10 minutos |
| **2.0 y posteriores** | 1 minuto |

### ¿Cuántas DPUs se usan?

El número de DPUs es configurable, pero cada tipo de job tiene un mínimo y un valor por defecto:

| Tipo de job | DPUs por defecto | DPUs mínimas |
| ---------------------------- | ----------------- | -------------- |
| **Spark** (ETL estándar) | 10 | 2 |
| **Spark Streaming** | 2 | 2 |
| **Ray** (preview, ML/AI) | 6 | 2 |
| **Python Shell** | Muy inferior a Spark (job simple, sin cómputo distribuido) | — |

> ⚠️ Por defecto, un ETL Job de Spark usa **10 DPUs**. Para fines de práctica/formación conviene
> reducir este valor al mínimo (2 DPUs) para no disparar el coste innecesariamente.

Los **Ray Jobs** están actualmente en preview y son especialmente potentes para cargas de Machine
Learning / AI. Usan un tipo especial de unidad llamada **M-DPU**, con el doble de memoria que una DPU
estándar (32 GB en vez de 16 GB).

Los **Python Shell Jobs** son para cargas más simples que no requieren la potencia de cómputo
distribuido de Spark, y usan una cantidad de DPUs mucho menor.

## Notebooks e Interactive Sessions

Glue permite desarrollar código ETL de forma interactiva mediante **Notebooks** e **Interactive
Sessions**.

- El coste depende del **tiempo que la sesión está activa** y del **número de DPUs** usadas.
- Se puede configurar un **timeout** — es importante cerrar la sesión cuando ya no se necesita, para
  no seguir generando coste.
- **Mínimo de facturación: 1 minuto.**
- Igual que con los otros tipos de Glue Jobs ya vistos: **mínimo de 2 DPUs**, con un valor por
  defecto de **5 DPUs**.

## Ejemplos de cálculo

**ETL Job (Spark)**: se ejecuta durante 15 minutos (¼ de hora) usando 6 DPUs.

```text
0.25 h × 6 DPU × $0.44/DPU-h = $0.66
```

**Interactive Session**: se mantiene activa 24 minutos (⅖ de hora) usando 5 DPUs (valor por defecto).

```text
0.4 h × 5 DPU × $0.44/DPU-h = $0.88
```

## Control de coste

Para mantener el coste bajo control, es recomendable configurar **presupuestos (Budgets)** —
por ejemplo, un presupuesto de gasto cero y otro de $5 como alerta temprana — especialmente al
practicar en una cuenta real de AWS.
