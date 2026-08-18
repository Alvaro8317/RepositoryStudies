# Massive Parallel Processing (MPP)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

La cantidad de datos en las empresas crece constantemente, y con ella también crece el número de
usuarios que necesitan consultarlos. Esto aumenta la exigencia sobre el sistema de base de datos y
sobre el rendimiento de las consultas. Una de las tecnologías modernas más importantes para
enfrentar este reto es el `Massive Parallel Processing` (`MPP`), o procesamiento paralelo masivo.

## El problema: procesamiento secuencial tradicional

Al ejecutar una consulta contra un sistema de base de datos, esa consulta es una tarea que
normalmente se compone de múltiples subtareas. De forma tradicional, todas esas subtareas se
procesan en **orden secuencial**: hay que esperar a que termine una para que empiece la siguiente,
y solo al final se obtiene el resultado completo.

## La solución: procesamiento en paralelo

Con `MPP`, todas las subtareas de una consulta pueden procesarse **en paralelo**, iniciándose al
mismo tiempo en lugar de esperar a que termine cada una por separado. Esto se logra distribuyendo
las subtareas entre varios `nodos` que trabajan de forma independiente, lo que se traduce en un
rendimiento de consulta mucho mejor: la consulta se devuelve mucho más rápido.

## Arquitecturas de MPP

### Shared disk (disco compartido)

- El almacenamiento sigue siendo una **ubicación central única** (un disco externo compartido).
- Solo la tarea se desglosa en subtareas.
- Los **recursos de cómputo no se comparten**: cada nodo procesa sus subtareas de forma
  independiente, pero todos leen/escriben sobre el mismo almacenamiento central.

### Shared nothing (nada compartido)

- Ni el almacenamiento **ni** los recursos de cómputo se comparten.
- Los datos se distribuyen físicamente entre varias capas de almacenamiento (por ejemplo, tres
  particiones distintas, cada una con un subconjunto de filas).
- Cada nodo tiene su propio recurso de cómputo, su propio almacenamiento y su propio sistema
  operativo — se puede pensar en cada `nodo` como en un ordenador individual.
- Los nodos están conectados entre sí mediante una **conexión de alta velocidad**, necesaria para
  que puedan colaborar en paralelo sobre la misma tarea.
- Al no compartir nada, la carga de trabajo se puede dividir y procesar de forma muy eficiente.

> ⚠️ La arquitectura `shared nothing` es la más eficiente de las dos porque elimina por completo la
> contención sobre un recurso central compartido (ni disco ni cómputo), permitiendo que cada nodo
> trabaje a máxima capacidad de forma totalmente independiente.

## Beneficios de MPP

- Permite procesar millones de filas mucho más rápido, al ejecutar las subtareas en paralelo en
  lugar de secuencialmente.
- Mantiene un buen rendimiento de las consultas incluso con **muchos usuarios concurrentes**, ya
  que las consultas de distintos usuarios también pueden procesarse en paralelo.
- Facilita centralizar grandes volúmenes de datos a los que muchos usuarios necesitan consultar al
  mismo tiempo, sin sacrificar rendimiento.

`MPP` es una de las tecnologías modernas más importantes para garantizar un alto rendimiento de
consultas, y la utilizan muchos proveedores de `Data Warehouses` en la nube, como por ejemplo
`Snowflake`.

## Próximas clases

La segunda gran tecnología optimizada para el `Data Warehouse` moderno: el almacenamiento de datos
en columnas (`columnar storage`) — qué significa y cómo se puede beneficiar de ella.
