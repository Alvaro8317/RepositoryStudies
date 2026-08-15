# ¿Qué es un Data Warehouse? (profundizando)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Definición

Un **Data Warehouse** es básicamente una base de datos que se utiliza y optimiza con fines
analíticos.

## Características importantes

- **Fácil de usar**: no debe ser super técnico. Nombres y estructura deben ser fáciles de entender
  para que analistas de datos puedan recuperar, procesar y trabajar con los datos sin fricción.
- **Rendimiento de consulta muy rápido**: permite extraer y procesar grandes volúmenes de datos
  rápidamente.
- **Optimizado para el análisis**: en general, todo el diseño busca permitir un análisis de datos
  mejor y más fácil.

## De los sistemas operativos al Data Warehouse

Una empresa tiene distintos **sistemas de datos operativos** (fuentes), por ejemplo:

- Datos de ventas
- Sistema de RRHH
- Sistema CRM

Cada una de estas fuentes suele tener un **formato y una estructura distintos**. El trabajo consiste
en reunir todos los datos relevantes de estas fuentes y almacenarlos en un **lugar centralizado**: el
Data Warehouse.

## El proceso ETL

Este proceso de centralizar y preparar los datos se llama **ETL** (Extract, Transform, Load).

> ⚠️ El proceso ETL es el proceso más importante al construir un Data Warehouse — se invierte
> aproximadamente el **80-90% del tiempo** del proyecto en él.

| Paso | Qué hace |
|---|---|
| **Extract** | Extraer los datos de las distintas fuentes, cuidando de no consumir el rendimiento/recursos de esos sistemas operativos ni ralentizarlos. |
| **Transform** | Integrar todas las fuentes distintas en una misma estructura para poder trabajar con ellas de forma consistente (puede incluir agregaciones). |
| **Load** | Cargar los datos ya transformados en la ubicación centralizada (el Data Warehouse), optimizada para el análisis de datos. |

El proceso ETL, cómo construir un Data Warehouse y cómo modelar los datos se profundizará en
conferencias posteriores.

## Objetivo del Data Warehouse (resumen)

- Es un **lugar centralizado** donde los datos de distintas fuentes están disponibles de forma
  **coherente**.
- Debe tener **acceso muy rápido**: una consulta debe devolver resultados rápidamente.
- Debe ser **fácil de usar**: modelado de forma que sea fácil de entender y todos puedan trabajar
  con él.
- Requiere un proceso **ETL** consistente y repetible para copiar y transformar los datos.
- El objetivo final es **crear reportes y visualizaciones de datos** a partir del Data Warehouse —
  esa es la razón principal por la que se construye.
