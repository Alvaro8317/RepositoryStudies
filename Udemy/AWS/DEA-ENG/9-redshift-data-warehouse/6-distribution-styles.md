# Redshift: Distribution Styles

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es un Distribution Style?

- Los **clusters** almacenan los datos distribuidos entre los **nodos de computación**.
- Para controlar esa distribución se usan las **Distribution Keys**.
- El **Distribution Style** es lo que determina **dónde se almacenan los datos** (en qué nodo de
  computación) — es decir, la estrategia con la que se reparten las filas de una tabla entre los
  nodos.
- El objetivo es **distribuir la carga de trabajo de forma uniforme** entre los nodos del cluster y
  **minimizar el movimiento de datos (data movement)** durante la ejecución de las consultas.

> ⚠️ Cuanto menos movimiento de datos se necesite entre nodos para resolver una consulta (por
> ejemplo, en un `JOIN`), más rápido se ejecutará esa consulta — de ahí la importancia de elegir
> bien el Distribution Style de cada tabla.

Redshift ofrece cuatro estilos de distribución: **KEY**, **ALL**, **EVEN** y **AUTO**.

## KEY distribution

- Las filas se distribuyen **según los valores de una columna** (la **Distribution Key**).
- El **nodo líder** coloca los valores coincidentes en la **misma node slice**.
- Es útil para tablas que **participan frecuentemente en JOINs**: si las tablas relacionadas
  comparten la misma clave de distribución, las filas que se necesitan juntar ya están en la misma
  slice, evitando mover datos entre nodos durante el `JOIN`.

## ALL distribution

- Se distribuye una **copia completa de la tabla** a **todos los nodos**.
- **Multiplica el almacenamiento** necesario por el **número de nodos** del cluster.
- Solo es apropiado para tablas **relativamente pequeñas y que cambian poco**.
- A cambio, permite operaciones de consulta **más rápidas** (no hay que mover datos entre nodos
  para hacer `JOIN` con esta tabla).

## EVEN distribution

- El **nodo líder** distribuye las filas entre las slices **sin tener en cuenta los valores de
  ninguna columna en particular**.
- Es apropiado cuando:
  - La tabla **no participa en JOINs**.
  - **No hay una elección clara** entre usar **KEY distribution** o **ALL distribution**.

## AUTO distribution

- Es el **estilo de distribución por defecto**.
- Redshift **asigna automáticamente** el estilo de distribución óptimo según el **tamaño de los
  datos** de la tabla.
- Funcionamiento: a medida que la tabla crece, Redshift va cambiando de estilo siguiendo esta
  progresión:

  ```text
  ALL → KEY → EVEN
  ```

- El cambio de estilo de distribución ocurre **en segundo plano**, con **impacto mínimo** en las
  consultas de los usuarios.

## Resumen

| Distribution Style | Cómo distribuye                                                                           | Cuándo usarlo                                                       |
| ------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **KEY**            | Según los valores de una columna (Distribution Key), filas coincidentes en la misma slice | Tablas que participan frecuentemente en JOINs                       |
| **ALL**            | Copia completa de la tabla en cada nodo                                                   | Tablas pequeñas y de cambio lento                                   |
| **EVEN**           | Reparto uniforme, sin tener en cuenta columnas                                            | Tablas sin JOINs, o sin una elección clara entre KEY y ALL          |
| **AUTO**           | Redshift elige automáticamente (ALL → KEY → EVEN según crece la tabla)                    | Por defecto — cuando no se quiere gestionar la elección manualmente |
