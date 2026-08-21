# Amazon QuickSight

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon QuickSight** es el servicio de **inteligencia de negocios (BI)** de AWS, usado para
visualizar datos y crear informes/dashboards — por ejemplo, a partir de resultados de consultas de
[Amazon Athena](../2-query-athena/1-athena-intro.md).

## Qué permite hacer con los datos empresariales

- **Crear visualizaciones** e informes/dashboards.
- Realizar **análisis ad hoc**.
- **Recibir alertas sobre anomalías** detectadas en los datos.
- Obtener rápidamente **conocimientos (insights) empresariales** a partir de los datos.

## Dashboards

Un **dashboard** de QuickSight es, en esencia, una **versión publicada de un análisis**. Sobre los
dashboards:

- Los datos se pueden **refrescar automáticamente**, con una programación periódica — importante
  cuando se necesitan insights sensibles al tiempo (siempre actualizados).
- Se pueden **compartir fácilmente** con otros miembros del equipo o stakeholders, publicándolos
  para distribuirlos a los usuarios que deban consumirlos.
- Se pueden **incrustar (embed)** en un sitio web o aplicación.
- Son **responsive**: se pueden consumir tanto en escritorio como en móvil, permitiendo interactuar
  con ellos desde cualquier dispositivo.

## SPICE

**SPICE** (Super-fast, Parallel, In-memory Calculation Engine) es el **motor de cálculo** de
QuickSight:

- Motor de cálculo **en memoria**, **paralelo** y **columnar** (almacenamiento en columnas),
  optimizado para un rendimiento de lectura muy alto.
- Está diseñado para ser **súper rápido**: los cálculos de datos y el renderizado de
  visualizaciones son muy rápidos, porque los datos ya están en la caché de SPICE y no hace falta
  esperar a que la fuente de datos original los devuelva.
- Ofrece **10 GB de almacenamiento por usuario**, asignados **automáticamente** — sin necesidad de
  configuración manual — lo que permite que muchos usuarios disfruten de un rendimiento alto a la
  vez.
- Es **altamente disponible y duradero**.

## Fuentes de datos

QuickSight admite una gama muy amplia de fuentes de datos, entre otras:

- **Amazon S3** (distintos tipos de archivo, o carga directa de ficheros).
- Bases de datos AWS: **Redshift**, **Aurora**, **Athena**, **OpenSearch**.
- Otras bases de datos, incluidas de terceros, vía fuentes **ODBC** y **JDBC**.

> ⚠️ En general, prácticamente cualquier lugar donde se almacenen datos se puede conectar a
> QuickSight.

### Pipeline típico hacia QuickSight

Es habitual construir un pipeline de datos desde el almacenamiento original hasta QuickSight en
vez de conectarlo directamente a los datos en bruto. Un ejemplo típico:

1. **S3** — almacenamiento de los datos en bruto.
2. **Glue Crawler** — descubre los datos y los cataloga.
3. **Athena** — sirve como motor de consulta sobre los datos ya catalogados en S3.
4. **QuickSight** — visualiza los datos consultados a través de Athena.

> ⚠️ Este patrón (S3 → Glue Crawler → Athena → herramienta de visualización) es común incluso
> cuando se usan herramientas de visualización distintas de QuickSight — Athena suele actuar como
> paso intermedio de consulta.

## Buenas prácticas: qué evitar

- **Dashboards con demasiados elementos visuales**: provocan cálculos complejos, rendimiento más
  lento y peor experiencia de usuario. Lo ideal es que, al ver un dashboard, se pueda extraer el
  insight de inmediato — hay que simplificar para que sea fácil de entender.
- **Descuidar la configuración de seguridad de los datos**: hay que configurar permisos y control
  de acceso adecuados (ej. con **IAM**) para proteger información sensible, y asegurarse de no
  exponer datos que ciertos usuarios no deberían ver — por ejemplo mediante **seguridad a nivel de
  fila (row-level security)** o tokenización de datos sensibles.
- **Usarlo como herramienta ETL**: QuickSight admite transformaciones ligeras, pero no está
  diseñado como herramienta ETL — para ETL real conviene usar un servicio como **Glue**.

## Integración con Redshift

> ⚠️ Para que QuickSight pueda consultar un clúster de **Redshift**, ambos deben estar en la
> **misma región** — igual que ocurre entre Redshift y los buckets de S3 que consulta con
> [Redshift Spectrum](../9-redshift-data-warehouse/13-redshift-spectrum.md).

## Ediciones, roles de usuario y precios

QuickSight ofrece dos **ediciones de licencia**:

| Edición        | Pensada para                                                                  | Funcionalidades destacadas                                                                                                                                         | Precio                                                    |
| -------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **Standard**   | Usuarios individuales o grupos pequeños, sin necesidad de funciones avanzadas | 10 GB de SPICE incluidos por usuario                                                                                                                               | **$9/usuario/mes** (plan anual); más caro en plan mensual |
| **Enterprise** | Organizaciones más grandes, con más usuarios y necesidades más avanzadas      | **Row-level security**, refresco horario, mayor rendimiento de datos, **ML Insights**, federación de gestión de usuarios, auditoría adicional, cifrado **at rest** | Precio por usuario superior a Standard                    |

- En **Standard** se paga **por usuario**; cualquier capacidad de SPICE que exceda los 10 GB
  incluidos por usuario tiene un coste adicional.
- En **Enterprise**, además del pago por usuario, existe un modelo de **pago por sesión** para el
  rol de lector, normalmente mucho más económico.

### Roles de usuario (edición Enterprise)

| Rol                 | Qué puede hacer                                                                                                                               | Precio                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Author** (autor)  | Se conecta a los datos, crea dashboards y los comparte con los usuarios de la cuenta                                                          | Precio por usuario más alto; varía según tenga o no activado **QuickSight Q**            |
| **Reader** (lector) | Solo puede **ver, exportar e imprimir** un dashboard — **no puede guardarlo como un análisis** ni crear visualizaciones nuevas a partir de él | Pago **por sesión**, hasta **$5/mes** (hasta **$10/mes** si tiene QuickSight Q activado) |

- **QuickSight Q**: función (Enterprise) que permite hacer preguntas en lenguaje natural sobre los
  datos y obtener una respuesta junto con una visualización.
- **SPICE** (más allá de la capacidad incluida): **$0.38/GB/mes** adicional.

## Seguridad

### Rol de IAM para acceder a otras fuentes de datos

- QuickSight necesita un **rol de IAM** que pueda asumir para interactuar con otros servicios (ej.
  leer datos de un **bucket S3**).
- Hay que crear ese rol y añadir en su **política de IAM** el acceso necesario a las fuentes de
  datos que QuickSight debe leer, y luego seleccionarlo dentro de la configuración de QuickSight.

### Gestión de acceso de usuarios

- QuickSight se integra con **IAM** para gestionar permisos a nivel de **usuario** y de **grupo**:
  quién puede acceder a qué datasets, dashboards, etc.
- **Active Directory** (función de la edición **Enterprise**): conector directo que permite usar
  las credenciales y la pertenencia a grupos ya existentes para gestionar el acceso a QuickSight.
- Soporta **MFA** (autenticación multifactor) para los usuarios.

### Acceso a datos en una VPC

- Cuando la fuente de datos (ej. una base de datos) está dentro de una **VPC**, hay que habilitar
  el acceso mediante una **ENI (Elastic Network Interface)** — una interfaz de red virtual que
  actúa como puente para el tráfico entre QuickSight y la VPC.

### Acceso a datos on-premises

- Si los datos no pueden moverse a la nube (ej. por requisitos de compliance), QuickSight puede
  acceder a ellos sin salir de la red privada usando **AWS Direct Connect**.

### Despliegue aislado dentro de una VPC

- También es posible ejecutar QuickSight completamente aislado dentro de una VPC (requiere edición
  **Enterprise**), usando igualmente una **ENI**.
- Adicionalmente, se puede restringir el acceso por **dirección IP** (IP filtering), para que
  QuickSight solo sea accesible desde ubicaciones específicas.

### Acceso entre regiones y entre cuentas

Por defecto, una cuenta de QuickSight opera dentro de la región en la que se desplegó, por lo que
acceder a fuentes de datos en otra región (o en otra cuenta) requiere configuración adicional:

| Edición        | Mecanismo                                                                                                                                                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Standard**   | No se puede acceder desde una subred privada — hay que adjuntar un **security group** a la fuente de datos (en la otra cuenta/región) que permita conexiones entrantes desde QuickSight.                                                                                                       |
| **Enterprise** | Se puede desplegar QuickSight dentro de una subred, usando una **ENI**, y conectar esa subred con la de la fuente de datos vía **VPC peering** (dentro de una misma región) — o, para escenarios cross-account/a mayor escala, **AWS Transit Gateway**, **AWS PrivateLink** o **VPC sharing**. |

> ⚠️ El escenario (cuenta A / región A → cuenta B / región B) es el mismo tanto si el salto es entre
> **cuentas** distintas como entre **regiones** distintas.

### Row-Level Security (RLS)

- Función de la edición **Enterprise**: controla el acceso a los datos **a nivel de fila**, según
  el usuario/rol que consulta el informe.
- Ejemplo: un dataset con una columna `departamento` — a un usuario de una región solo se le
  muestran las filas correspondientes a su región, filtradas automáticamente según su perfil.

### Column-Level Security (CLS)

- También de edición **Enterprise**: permite restringir el acceso a **columnas** específicas de un
  dataset, de forma análoga a RLS pero a nivel de columna.

### ¿RLS/CLS en QuickSight o en Lake Formation?

Ambos servicios permiten aplicar seguridad a nivel de fila/columna (incluso celda, en Lake
Formation — ver [Lake Formation: permisos y seguridad](2-lake-formation-permissions.md)), pero
actúan en **capas distintas**:

| Aspecto                         | RLS/CLS en **QuickSight**                                                                                 | RLS/CLS/data filtering en **Lake Formation**                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Dónde se aplica el filtro       | En la capa de **BI/reporting** — sobre el dataset ya cargado en QuickSight (o en SPICE)                   | En la capa de **datos** — sobre las tablas del Glue Data Catalog, antes de que cualquier motor las consulte |
| Alcance de la protección        | Solo afecta a lo que se ve **dentro de QuickSight**                                                       | Se aplica de forma centralizada para **todos los consumidores**: Athena, Redshift, EMR, QuickSight, etc.    |
| Consistencia entre herramientas | Hay que replicar la lógica de acceso si otro servicio (ej. Athena) consulta los mismos datos directamente | Un único punto de control — todos los servicios que consultan esos datos respetan el mismo permiso          |
| Requisito de edición/servicio   | Requiere QuickSight **Enterprise**                                                                        | Requiere tener los datos gobernados por **Lake Formation**                                                  |
| Caso de uso típico              | Un dashboard puntual donde solo importa filtrar lo que ven los usuarios de ese informe                    | Datos sensibles consultados desde **varios** motores/servicios, donde se necesita gobernanza centralizada   |

> ⚠️ Regla general para el examen: si los mismos datos se consultan desde **varios servicios**
> (Athena, Redshift, QuickSight...), la seguridad a nivel de fila/columna debe implementarse en
> **Lake Formation**, para que el control de acceso sea consistente en todos ellos. El RLS/CLS de
> QuickSight solo tiene sentido cuando el filtrado es específico de **ese** dashboard y no necesita
> aplicarse fuera de QuickSight.
