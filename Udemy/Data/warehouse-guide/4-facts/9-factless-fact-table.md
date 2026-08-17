# Factless Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es

Un tipo especial de `Fact Table`, que no supone ninguna contradicción: una `Fact Table` (la tabla) y
un `Fact` (el hecho) no son lo mismo.

- Un **`Fact`** es la medida numérica que registra el rendimiento de un proceso de negocio.
- Una **`Fact Table`** es la tabla completa que mantiene el registro de esos hechos, junto con sus
  claves foráneas y todo lo demás incluido en ella.

Como ambas cosas no son lo mismo, es posible que una `Fact Table` **no contenga ningún `Fact`** —
solo registre los aspectos dimensionales de un evento o transacción, sin ninguna métrica asociada. A
esto se le llama `Factless Fact Table`.

## Ejemplo: alta de nuevos empleados

Una empresa registra cada nuevo empleado que se da de alta. La tabla guarda todos los aspectos
dimensionales del evento, pero ningún hecho numérico:

- Fecha de entrada del empleado.
- Departamento en el que se registra.
- Región.
- Responsable (manager) del empleado.

No hay ninguna métrica — solo se registran los aspectos dimensionales de cada alta.

Con esta estructura se pueden responder preguntas como:

- ¿Cuántos empleados se han registrado el mes pasado? (filtrar por fecha y contar filas)
- ¿Cuántos empleados se han registrado en una determinada región o departamento? (filtrar por la
  dimensión correspondiente y contar filas)

Estas consultas se resuelven fácilmente tanto en SQL (filtrando por la dimensión y haciendo un
`COUNT` de filas) como en cualquier herramienta de BI.

## Otro ejemplo: promociones

Registrar promociones sin ninguna métrica asociada — solo el evento en sí, con sus dimensiones:

- Código promocional.
- Producto promocionado.
- Campaña asociada.

De nuevo, se hace seguimiento de la ocurrencia de estos eventos y sus aspectos dimensionales, sin
ninguna medida numérica.

## Idea clave

Si solo se quiere registrar la **ocurrencia de eventos**, sin ninguna métrica asociada, una
`Factless Fact Table` sigue siendo una `Fact Table` válida — no es una contradicción, simplemente un
caso particular donde el foco está en los aspectos dimensionales del evento y no en una medida.

## Próxima clase

Pasos a seguir para diseñar e implementar tablas de hechos.
