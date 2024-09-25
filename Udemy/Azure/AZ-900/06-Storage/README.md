# Almacenamiento

La nube de azure está dividido en 3 pilares de servicios principales que son computación, redes y almacenamiento

## Azure Blob Storage

Blob se refiere a Binary Large Object, es un almacenamiento de objetos seguro y escalable de forma masiva para cargas de trabajo nativas de nube, archivos lagos de datos, informática de alto rendimiento y aprendizaje automático.

Es **Escalable, duradero y disponible**, da durabilidad por diseño con replicación geográfica y flexibilidad.

Es **protegido** con autenticación con el ID de Microsoft Entra y control de acceso basado en roles (RBAC)

Es **optimizado para lagos de datos** con un acceso multiprotocolo que permite ejecutar cargas de trabajo de análisis para obtener conclusiones a partir de los datos.

Finalmente tiene una **administración de datos completa** del ciclo de vida de un extremo a otro, control de acceso basado en directivas y almacenamiento inmutable

Se puede almacenar imagenes, streaming de audio y vídeo, log files, almacén de datos para almacenar, archivar, copias de seguridad, restaurar y recuperar en caso de desastres. **Permite guardar cualquier tipo de archivo**.

### Tipos de Blob

#### Block

Almacena texto y datos binarios de hasta 4.7 TB compuesto por bloques de datos gestionados de forma individual.

#### Append (Anexar)

Bloques de blobs optimizados para operaciones de anexado. Funciona bien para registros donde los datos se anexan constantemente.

#### Page (Pagina)

Almacena archivos de hasta 8TB. Cualquier parte del archivo podría ser accedida en cualquier momento, por ejemplo, un disco duro virtual.

### Tipos de niveles de acceso

#### Hot

Archivos accedidos frecuentemente. Tiempos de acceso bajos y costo de acceso más altos

#### Cool (Frío)

Costos de almacenamiento más bajos y tiempos de acceso más altos. Los datos permanecen aquí al menos 30 días

#### Archive (Archivo)

Los costos más bajos pero tiempos de acceso más altos.

## Azure Disk Storage

Almacenamiento en bloque de alta durabilidad y gran rendimiento para Azure Virtual Machines. Cuenta con:

- Almacenamiento en disco rentable
- Resistencia sin precedentes - Durabilidad con tasa de error anual del 0%
- Escalabilidad de conexión directa - Atiende la demanda sin afectar rendimiento
- Seguridad incorporada - Cifrado automático

Disco gestionado, uno no se preocupa por las copias de seguridad, Azure garantiza el tamaño y el rendimiento, además actualizar el tipo de dato es sencillo

### Tipos de disco

- HDD
- SSD Estándar
- SSD Premium - Super rápido, ideal para cargas de trabajo críticas
- Ultra disk - Cargas de trabajo exigentes y con alta intensidad de datos, discos de hasta 64 TB

## Azure File Storage

Diseñado para tener recursos compartidos de archivos en la nube de grado empresarial sencillo, seguro y serverless.

Enfocado a compartir archivos sin servidor, diseñado para entornos híbridos con File Sync, con TCO optimizado y compatible con varios protocolos.

De los beneficios de file storage es que permite compartir el acceso al almacenamiento de archivos de azure entre máquinas, es gestionado por Azure, resiliente para que una interrupción de red y energia no afecte el almacenamiento y es muy útil con los siguientes escenarios:

- Cloud híbrida
- Levanta y mueve, donde se translada los almacenameintos existentes a Azure.

## Azure archive storage

Solución para almacenar a largo plazo datos raramente accedidos, permite movimiento entre niveles de almacenamiento. Cuenta con herramientas integradas para fácil clasificación, busqueda y administración de datos. Cifrado, autenticación y cumplimiento de estándares y regulaciones de la industria.

Útil para requerimientos, como políticas, legislación y recuperación. Es el servicio más economico para el almacenamiento en azure, unos cuantos dolares permiten teras de espacio, es duradero, cifrado y estable. Adecuado para datos que se acceden con poca frecuencia.

Permite liberar almacenamiento local como de servidores on-premise, este es un modulo totalmente seguro que permite cualquier dato confidencial.

Es un almacenamiento blob, al final la misma herramienta funcionará para ambos
