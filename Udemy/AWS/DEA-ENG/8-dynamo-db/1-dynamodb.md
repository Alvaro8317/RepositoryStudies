# DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**DynamoDB** es la base de datos **NoSQL** de AWS — a diferencia de **RDS**, no es una base de datos
relacional. También se conoce como base de datos **"not only SQL"** o **no relacional**.

## NoSQL vs. base de datos relacional

|                                  | **Base de datos relacional** (ej. RDS)                                                            | **Base de datos NoSQL** (ej. DynamoDB)                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Esquema                          | **Fijo y predefinido** — tablas con columnas y filas; cada fila tiene siempre las mismas columnas | **Sin esquema fijo (schema-less)** — cada registro/item puede tener campos distintos, añadidos sobre la marcha |
| Tipo de datos                    | Datos **estructurados**                                                                           | Datos estructurados, **semiestructurados y no estructurados**                                                  |
| Escalado                         | **Vertical** — hay que ampliar la máquina existente (RAM, CPU)                                    | **Horizontal** — se añaden máquinas adicionales fácilmente; base de datos distribuida                          |
| Consultas complejas              | Soporta **joins y agregaciones**                                                                  | **No soporta joins ni agregaciones** — las formas de consultar dependen del modelo de datos NoSQL usado        |
| Rendimiento en lectura/escritura | Bueno, pero limitado por el escalado vertical                                                     | **Muy rápido**, especialmente con grandes volúmenes de datos y mucho tráfico                                   |
| Casos de uso típicos             | Informes, sistemas financieros, integridad transaccional, modelado relacional                     | Big data, analítica en tiempo real, alto tráfico, esquema cambiante                                            |

> El esquema flexible de NoSQL permite, por ejemplo, un modelo de **documentos** tipo JSON con
> estructuras jerárquicas anidadas — algo muy distinto del modelo rígido de filas/columnas de una base
> de datos relacional.
> ⚠️ La ausencia de joins y agregaciones en NoSQL no es una limitación temporal ni un detalle menor:
> es una consecuencia directa de cómo se modelan los datos. Si el caso de uso requiere consultas
> complejas con uniones, una base de datos relacional sigue siendo la opción adecuada.

## DynamoDB en detalle

- **Modelo de datos**: soporta tanto el modelo **clave-valor** como el modelo de **documentos**.
- **Base de datos distribuida totalmente gestionada** — AWS se encarga de toda la carga
  administrativa: instalación, configuración, replicación, parches y escalado del clúster.
- **Alto rendimiento bajo tráfico y cargas de trabajo elevadas** — escala fácilmente y de forma
  automática según el volumen de peticiones.
- **Distribución automática de datos** — al ser una base de datos distribuida, los datos se reparten
  automáticamente; se almacenan en unidades **SSD**.
- **Alta disponibilidad y durabilidad** — los datos se **replican automáticamente entre varias Zonas
  de Disponibilidad** de una región.
- **Cifrado en reposo** — protección de datos sensibles integrada.
- **Latencias de milisegundos** — tanto en lectura como en escritura, lo que se traduce en buena
  experiencia de usuario y respuesta rápida.
