# AWS Batch

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Batch?

AWS Batch es un servicio que permite ejecutar **trabajos por lotes (batch jobs)** basados en
**imágenes Docker**, encargándose de todos los aspectos operativos de esos trabajos.

Un trabajo por lotes es un trabajo que, por ejemplo, procesa grandes cantidades de datos de una
sola vez, sin necesidad de interacción del usuario mientras se ejecuta.

## Batch vs. Lambda vs. Glue

Es fácil confundir cuándo usar Batch frente a Lambda o Glue, ya que los tres "ejecutan tareas" por
nosotros. La diferencia está en el tipo de carga de trabajo:

| Servicio   | Enfoque                                                                    | Cuándo usarlo                                                                                                          |
| ---------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Lambda** | Tareas ligeras, dirigidas por eventos (*event-driven*)                     | Reaccionar en tiempo real a eventos ejecutando código puntual. Modelo serverless.                                      |
| **Glue**   | Servicio ETL gestionado / integración de datos, usa **Spark** bajo el capó | Tareas de integración de datos (ETL) y catalogación de datos con el **Glue Data Catalog**.                             |
| **Batch**  | Uso general, amplia gama de trabajos de cómputo por lotes                  | Tareas informáticas amplias e intensivas en cómputo (pueden incluir procesamiento de datos, pero no se limitan a ETL). |

## Características principales

- **Autoescalado**: AWS Batch asigna automáticamente la cantidad y el tipo de recursos adecuados
  para los trabajos en función de la demanda.
- **Programación (scheduling)**: los trabajos pueden programarse.
- **Integración con AWS Step Functions**: permite orquestar flujos de trabajo más complejos entre
  trabajos por lotes, gestionar dependencias entre trabajos, implementar mecanismos de reintento y
  gestión de errores.
- **Cómputo subyacente flexible**:
  - **Fargate** para un modelo completamente serverless (no gestionamos infraestructura).
  - **Instancias EC2** o **instancias Spot EC2** cuando se necesita gestionar los recursos de
    cómputo directamente.

## Precio

Se paga en función de los **recursos informáticos consumidos** al ejecutar los trabajos, medidos en
**horas de instancia**:

- Coste de instancia EC2 / instancia Spot, o
- Coste de Fargate (si se usa ese modelo serverless).

> ⚠️ Si un trabajo dura un par de horas, solo se paga por ese tiempo de cómputo — no hay coste fijo
> adicional por el propio servicio Batch.

## Flujo de configuración de un entorno Batch

1. **Definir los trabajos por lotes** que se necesitan ejecutar: el contenedor Docker (que incluye
   el código), los requisitos de CPU y memoria, la cola de trabajos y las dependencias entre
   trabajos.
2. **Enviar los trabajos a la cola de trabajos (job queue)**, donde esperan a ser programados. Se
   pueden tener varias colas con distintas prioridades, de modo que los trabajos de alta prioridad
   se procesen antes.
3. **Programación (scheduling)**: AWS Batch programa el trabajo en el entorno informático adecuado,
   teniendo en cuenta los requisitos del trabajo y las políticas configuradas en el contenedor.
4. **Ejecución**: el trabajo se ejecuta en el entorno informático y AWS Batch gestiona esos recursos
   por nosotros.
