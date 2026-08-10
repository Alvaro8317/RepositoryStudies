# MSK Connect y MSK Serverless

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Dos servicios/variantes específicos dentro de **Amazon MSK** (ver [[12-amazon-msk]]).

## MSK Connect

Servicio **totalmente gestionado** que facilita la creación y ejecución de conectores
**Kafka Connect** — un componente de código abierto de Apache Kafka que simplifica la integración de
Kafka con otros sistemas (bases de datos, índices de búsqueda, sistemas de archivos, etc.).

- Permite transmitir datos **dentro y fuera de Kafka** sin necesidad de código personalizado para esa
  integración.
- Amazon MSK gestiona la infraestructura de Kafka Connect por completo, lo que agiliza el despliegue y
  la ampliación de los conectores.
- Escalar las integraciones de datos no requiere gestionar la complejidad subyacente de la
  infraestructura.
- Dispone de una amplia gama de **conectores** ya disponibles, que cubren escenarios como mover datos
  hacia otras fuentes/destinos — por ejemplo **Amazon S3** o **Apache Flink** (ver
  [[11-managed-service-apache-flink]]).

## MSK Serverless

Tipo de **clúster sin servidor** dentro de Amazon MSK, pensado para simplificar aún más las
operaciones de Kafka.

- **Elimina la necesidad de gestionar la capacidad del clúster**: los recursos de cómputo y
  almacenamiento se aprovisionan y escalan **automáticamente** según los requisitos reales de la
  carga de trabajo.
- Ideal para casos de uso con **volúmenes de datos variables**, ya que el servicio se ajusta
  dinámicamente a la carga que se experimenta en cada momento.
- Modelo de pago basado en el uso real — solo se paga por lo que realmente se consume.
- Conserva las funciones potentes de Kafka, pero con un enfoque mucho más "manos libres" (menos
  configuración manual que un clúster MSK provisionado tradicional).
