# Resumen: arquitectura del Data Warehouse

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Cierre de la sección de arquitectura, repasando las capas cubiertas en detalle en las clases
anteriores de este módulo (ver [[1-data-warehouse-layers]], [[2-staging-area]] y
[[4-data-marts]]).

## Flujo general de capas

```text
Fuentes de datos → Staging Area → Core Layer → [Data Marts] → aplicaciones / grupos de usuarios
```

## Staging Area

La **zona de aterrizaje**: aquí se cargan primero todos los datos de las distintas fuentes, en
tablas, aplicando las **menores transformaciones posibles**. El propósito es únicamente poner en
escena los datos, siendo lo menos intrusivos posible con las fuentes de origen.

## Core Layer

- Normalmente **no** es la capa de acceso final (aunque en casos muy simples, con un único caso de
  uso y lógica sencilla, puede llegar a serlo — esto es la excepción, no la norma).
- Contiene la **lógica de negocio**: aquí se aplican todas las transformaciones de datos, y los
  datos quedan modelados de forma dimensional.
- Funciona como el **único punto de verdad** (`single source of truth`): todos los datos
  transformados están disponibles en un único lugar, y los distintos `Data Marts` lo usan como su
  fuente de datos.

## Data Marts

- Es la capa de acceso final más habitual, construida **para un caso de uso específico**, tomando
  al `Core Layer` como fuente.
- Se busca que sea lo **menos compleja posible**, por razones de rendimiento y facilidad de uso.
- Si el rendimiento de una base de datos relacional estándar no es suficiente, se puede optimizar
  con tecnologías específicas: bases de datos **multidimensionales** (cubos `MOLAP`) o bases de
  datos **in-memory**.

## Próxima sección

Modelado dimensional: cómo modelar los datos en un `Star Schema`, y qué significa esto en la
práctica.
