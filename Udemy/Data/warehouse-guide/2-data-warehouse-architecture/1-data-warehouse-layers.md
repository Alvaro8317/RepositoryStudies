# Capas de un Data Warehouse

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Idea general

Un `Data Warehouse` no es una única capa monolítica, sino que está compuesto por **varias capas**
por las que pasan los datos a medida que avanza el proceso `ETL`, desde las fuentes de origen hasta
el punto donde son consumidos por usuarios finales o aplicaciones.

Flujo general:

```text
Fuentes de datos → (ETL) → Staging Area → (ETL) → Core Layer → [Data Marts] → Reporting / BI / análisis
                                              ↑
                                     [Cleansing Zone] (opcional)
```

## Staging Area

Es la **primera capa** a la que llegan los datos, justo después de ser extraídos de las fuentes de
origen (archivos `CSV`, bases de datos, etc.) por la herramienta `ETL`.

- El objetivo es extraer los datos **tal cual están** en el origen y volcarlos en tablas.
- No se aplican transformaciones de datos en este punto — se busca dejar los datos **lo más
  intactos posible**.
- Es normal que datos equivalentes lleguen en tablas separadas si provienen de fuentes distintas
  (ej. una tabla de empleados por cada departamento, cada una en su propio formato de origen).

### Ejemplo: tablas de empleados por departamento

Supongamos que cada departamento tiene su propia tabla de empleados, extraída desde distintos
formatos de origen (`CSV`, bases de datos, etc.). Al llegar a la `Staging Area`, tenemos varias
tablas con estructura similar pero no idéntica:

| id  | nombre | posición        |
| --- | ------ | --------------- |
| 1   | Ana    | Analista Senior |
| 2   | Luis   | Analista Junior |

| id  | nombre | posición_nivel |
| --- | ------ | -------------- |
| 1   | Marta  | Sr. Analyst    |
| 2   | Pedro  | Jr. Analyst    |

Aquí ya se detectan varios problemas típicos que hay que resolver más adelante:

- **Nombres de columna distintos** para el mismo concepto (`posición` vs. `posición_nivel`).
- **Formato de datos inconsistente** entre tablas (una tabla escribe el valor completo, la otra lo
  abrevia).
- **IDs que reinician en cada tabla** (cada departamento vuelve a empezar en `1`), lo que generaría
  colisiones de clave si simplemente se combinan las tablas.

> ⚠️ Aunque la `Staging Area` en principio no transforma datos, si la estructura de dos o más tablas
> es prácticamente la misma, ya se pueden hacer pequeñas transformaciones de integración —como
> anexar (`append`) filas de tablas equivalentes en una sola tabla de empleados— sin que esto deje
> de considerarse parte del "aterrizaje" de los datos.

## Core Layer

Es la capa a la que se llevan los datos **desde la Staging Area**, aplicando ya las transformaciones
necesarias durante la copia:

- Resolver inconsistencias entre fuentes (nombres de columna, formatos, generación de nuevas claves
  para evitar colisiones de IDs, etc.).
- Integrar los datos de las distintas tablas de staging en una estructura unificada.
- Remodelar los datos según el modelo dimensional que se quiera tener en el `Data Warehouse` (por
  ejemplo, reestructurar en tablas de hechos y dimensiones).

Esta es la capa que habitualmente **consumen los usuarios finales y las aplicaciones**: a partir de
aquí se generan reportes, se hace minería de datos o análisis predictivo.

> ⚠️ La `Core Layer` suele percibirse como "el Data Warehouse" en sí, porque es el punto de acceso
> final y la única fuente de verdad para la mayoría de usuarios. Sin embargo, técnicamente el
> `Data Warehouse` está compuesto por **todas** las capas (staging, core, data marts, cleansing
> zone), no solo por esta.

## Data Marts (capa opcional)

Cuando el `Data Warehouse` es muy grande (muchas tablas, muchos casos de uso distintos), puede
construirse una capa adicional de `Data Marts` sobre la `Core Layer`.

- Un `Data Mart` contiene solo las tablas **relevantes para un caso de uso específico**, en lugar de
  todo el `Data Warehouse`.

Beneficios:

| Beneficio               | Descripción                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Facilidad de uso        | El grupo de usuarios no se ve abrumado por tablas que no necesita.                                                                |
| Rendimiento de consulta | Solo ese grupo de usuarios consulta contra el `Data Mart`, sin competir por recursos con el resto del `Data Warehouse`.           |
| Especialización         | Puede apoyarse en bases de datos especializadas (in-memory, cubos OLAP) para maximizar el rendimiento en ese caso de uso puntual. |

No todos los `Data Warehouse` necesitan `Data Marts` — son útiles principalmente cuando la escala y
diversidad de casos de uso lo justifican.

## Cleansing Zone (capa opcional)

Zona dedicada exclusivamente a la **limpieza de datos**, útil cuando los datos de origen son muy
crudos y requieren un trabajo de limpieza considerable antes de integrarse en la `Core Layer`.

No siempre es necesaria — depende de la calidad de los datos de origen.

## ¿Cuál es "el" Data Warehouse?

Con tantas capas, es fácil confundirse sobre cuál es realmente el `Data Warehouse`:

- La **`Core Layer`** (o los `Data Marts`, si existen) es la capa que perciben los usuarios finales
  como "el Data Warehouse", porque es la capa de acceso final y la fuente única de verdad.
- Pero, en sentido estricto, el `Data Warehouse` **incluye todas las capas**: `Staging Area`,
  `Cleansing Zone` (si existe), `Core Layer` y `Data Marts` (si existen).

## Próxima clase

Profundizar en la `Staging Area`, una capa siempre presente y muy importante dentro del proceso.
