# Operational Data Store (ODS)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Qué es un ODS?

Un `Operational Data Store` (`ODS`) es, en la superficie, muy similar a un `Data Warehouse`: también
integra datos de distintos sistemas operativos en una única base de datos, típicamente mediante un
proceso `ETL`.

La distinción entre `ODS` y `Data Warehouse` no siempre es clara, y su definición exacta puede variar
según a quién se le pregunte. Lo importante para efectos prácticos es la **diferencia clave de
propósito**:

- Un `Data Warehouse` se usa para **decisiones analíticas y estratégicas**.
- Un `ODS` se usa para **decisiones operativas**, muy rápidas y del día a día.

## Requisitos de un ODS

Como un `ODS` sirve decisiones operativas, sus requisitos son distintos a los de un `Data
Warehouse`:

| Aspecto                     | Data Warehouse                                                         | ODS                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Historial                   | Necesario — se mantiene historial de los datos.                        | No necesario — solo importa el **estado actual**.                                                      |
| Frecuencia de actualización | Puede ser una vez al día o incluso una vez por hora.                   | Debe reflejar los sistemas de origen casi en **tiempo real**.                                          |
| Lógica de carga             | Normalmente se **anexan** (`append`) los datos, preservando historial. | Normalmente se **actualiza/reemplaza** (`update`/`replace`) el dato existente, sin mantener historial. |

> ⚠️ En un `ODS` no queremos tomar decisiones operativas con datos desactualizados — de ahí la
> necesidad de un estado casi en tiempo real, a diferencia del `Data Warehouse`, donde un cierto
> desfase (horas o un día) suele ser aceptable para decisiones estratégicas.

## Ejemplo práctico

Una empresa de servicios financieros cuyos clientes pueden invertir en `ETF`s, acciones,
criptomonedas, o mantener saldo en cuenta — cada uno gestionado por un sistema distinto (ej. un
sistema para cripto, otro para trading de acciones).

Para decidir en el momento si se le puede otorgar un crédito a un cliente, hace falta ver el saldo
global combinado de todos esos sistemas, reflejado casi en tiempo real. Esta es una decisión
**operativa** inmediata, no un análisis estratégico — el caso de uso típico de un `ODS`.

## ¿Se puede tener un ODS y un Data Warehouse a la vez?

Sí. Hay dos formas comunes de combinarlos:

1. **En paralelo**: un `ETL` independiente alimenta el `ODS` (casi en tiempo real, para decisiones
   operativas), y otro `ETL` independiente alimenta el `Data Warehouse` (con una cadencia más baja,
   ej. una vez al día o por hora, para decisiones analíticas/estratégicas).
2. **Integración secuencial** (la opción más común): el `ODS` ya hizo el trabajo pesado de integrar
   los datos de los sistemas operativos, así que el `ETL` del `Data Warehouse` puede construirse
   **sobre el ODS**, usándolo como fuente — como si fuera su propia `Staging Area`. Esto ahorra
   mucho esfuerzo de integración, ya que no hay que repetir ese trabajo desde los sistemas de origen.

## Relevancia actual

> ⚠️ El `ODS` es cada vez menos relevante en la práctica, en parte por el mejor rendimiento del
> hardware actual (que permite cargar datos mucho más rápido sin necesidad de esta capa dedicada) y
> por la existencia de otras tecnologías que ya cubren el requisito de datos en tiempo real o casi
> en tiempo real.

Como con otros conceptos de arquitectura ya vistos (`Data Marts`, cubos), la recomendación del
instructor es no obsesionarse con la terminología exacta: si en la empresa ya existe un `ODS`, vale
la pena evaluar de forma pragmática si se puede reutilizar como fuente para el `ETL` del `Data
Warehouse`, en lugar de discutir definiciones.

## Próxima clase

Resumen de todo lo visto en esta sección sobre arquitecturas de `Data Warehouse`.
