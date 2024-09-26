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

## Redundancia de almacenamiento

Azure storage realiza múltiples copias de los datos que es automático, mínimo 3 copias y es invisible para el usuario final. Cuenta con múltiples opciones de redundancia en diferentes alcances de ubicación que son

### Región única

#### Zona única - Redundancia local (LRS)

Una AZ, opción de costo más bajo con protección básica frente a errores en la unidad y el bastidor del servidor, ideal para escenarios no críticos.

- Crea automáticamente tres copias en la región primaria para garantizar la durabilidad
- La más económica
- Diseñado para proteger los datos contra fallos en el hardware de almacenamiento
- Todo el almacenamiento y replicación se realiza dentro de una única región
- Al ser local, no ofrece protección contra interrupciones de zona o regionales

#### Múltiples zonas - Redundancia de zona (ZRS)

Varias AZ, ideal pra escenarios de alta disponibilidad

- A diferencia de LRS, se replican los datos en diferentes AZ, al igual que LRS, ZRS mantiene tres copias de los datos pero distribuidos en diferentes AZ
- Diseñado para salvaguardar los datos incluso si una zona completa enfrenta problemas
- ZRS tiene un costo más alto pero no protege contra eventos catastróficos que puedan afectar a una región completa

### Múltiples regiones

### Múltiples regiones (GRS)

Varias AZ en varias regiones

- Protege contra desastres regionales
- Mantiene 3 copias en la región primaria y 3 en la secundaria
- Ante un fallo en la región primaria, se puede acceder a la región secundaria
- Tiene un costo superior a LRS y ZRS
- GRS es ideal para organizaciones y aplicaciones que necesitan el más alto nivel de protección y disponibilidad para sus datos

### Redundancia de zona geográfica (GZRS)

La combinación de GRS y ZRS, ideal para datos críticos, significa 3 copias de los datos distribuidas en diferentes AZ en la región primaria y 3 copias adicionales en la región secundaria pero dentro de una misma AZ

- Es la opción más costosa

### Resumen de la redundancia de almacenamiento

A mayor disponibilidad, mayor costo, todas las opciones incluyen 3 copias en la región primaria y 3 copias en la región secundaria (para múltiples regiones)

Azure storage replica automáticamente los datos para garantizar la redundancia, cuenta con 3 copias en una única región por defecto

## Movimiento de datos

Existen diferentes soluciones para mover datos del local a la cloud, para esto existen diversas herramientas que se pueden elegir en base a:

- Frecuencia de transferencia
- Tamaño de los datos
- Ancho de banda de la red

Para el AZ900 se enfoca en transferencias pequeñas y ocasionales, se puede usar AzCopy, Azure Storage Explorer y Azure File Sync

### AzCopy

CLI que permite copiar datos hacia y desde servicios de almacenamiento de Azure (Blob storage), útil para transferir blobs y azure files o programar transferencias de datos

### Azure Storage Explorer

GUI que permite administrar los datos para Windows, MacOS y Linux

### Azure File Sync

Sincroniza Azure Files con servidores de archivos locales, da rendimiento de servidor de archivos locales + disponibilidad en la nube, ideal para:

1. Respaldar el servidor de archivos local
2. Sincroniza archivos entre varias ubicaciones locales
3. Los usuarios remotos acceden a Azure Files
4. Transición a usar exclusivamente Azure Files como servidor de archivos

## Opciones de migración adicionales

### Azure Data Box

Ideal para transferencia de grandes cantidades de datos y/o ancho de banda limitado, necesario cuando se debe de transferir muchos datos a través de internet, Azure Data Box es un elemento físico para transferir datos sin conexión hacia y desde Azure, permite copiar datos a un dispositivo físico de almacenamiento. Útil para migrar datos de nivel masivo. Ideal para recuperación de desastres o requisitos de seguridad.

### Azure Migrate

Permite analizar cargas de trabajo locales y proporciona recomendaciones sobre los requisitos, permite analizar de manera local para identificar y evaluar autoáticamente las aplicaciones y servidores locales para facilitar una migración fluida dando una estimación de los costos. Permite probar las migraciones antes de realizarlas.

## Almacenamiento premium

Hay diferentes opciones de rendimiento, se debe de tener algunas consideraciones, como yipos de almacenamiento disponibles para cada opción de rendimiento

Opciones de rendimiento

1. Standard General Purpose
2. Premium block blobs (Solo para block blobs) - Almacenamiento en bloque, ideal para blob de baja latencia como AI o IoT, solo soporta redundancia local y de zona, útiles para aplicaciones con acceso rápido y un tiempo de respuesta bajo con respecto al almacenamiento de datos
3. Premium file shares (Solo para Azure Files) - Recursos compartidos de archivos, usa protocolos como SMB y NFS, compatible con windows y linux, soportan solo redundancia local y de zona
4. Premium Page blobs - Usado para discos virtuales no gestionados, soporta redundancia local y de zona, page blobs útiles para escenarios que requieren I/O aleatorio como bases de datos y discos de maquinas virtuales

Todos estos servicios solo soportan LRZ y ZRS

## Resumen

Blob - Almacenamiento general, cuenta con tipos de blobs, block (bloque), append (anexar) y page (página). Un blob se encuentra dentro de un contenedor y este se encuentra dentro de una cuenta de almacenamiento.
Ofrece diferentes niveles de acceso que son hot, cool y archive.

Disco - Almacenamiento en bloque de alta durabilidad y gran rendimiento para Azure Virtual Machines, es un servcio de almacenamiento gestionado. Permite elegir entre HDD, SSD, Premium SSD y Ultra Disk.

File - Reduce la dependencia de sistemas de almacenamiento de archivos locales on premise, almacenamiento altamente disponible y resiliente. Facilita el compartir archivos.

Archive - Método extremadamente económico para almacenar grandes cantidades de datos, es un tipo de almacenamiento BLOB para datos que no acceden frecuentemente.

Redundancia de almacenamiento - Consiste en realizar múltiples copias de los datos de Azure Storage, se guardan al menos 3 copias y hay opciones de zonas únicas o regiones única o múltiples

Movimiento de datos - Existe AzCopy que es una CLI, Storage Explorer que es una GUI y finalmente Azure File Sync que sincroniza Azurre files con servidores de archivos en las instalaciones.

Opciones adicionales de migración - Azure Data Box para offline (el snow) y Azure Migrate que migra recursos en las instalaciones incluyendo servidores, bases de datos y aplicaciones

Opciones de rendimiento premium - Opciones de almacenamiento respaldadas por SSD, limitadas de redundancia y cuenta con tipos de almacenamiento premium

Ninguna de las opciones de rendimiento premium ofrece redundancia multirregión. Las Premium page blobs sólo tienen opciones de redundancia LRS. Las opciones de rendimiento premium cuestan más que sus versiones estándar.

LRS es la redundancia en una sola región con tres copias de datos en una sola zona/centro de datos. ZRS también es redundancia de región única, pero con tres copias en tres zonas de disponibilidad distintas de la misma región.

Azure Files puede utilizarse para sustituir por completo o complementar los servidores de archivos o dispositivos NAS locales tradicionales. Los sistemas operativos más populares, como Windows, macOS y Linux, pueden montar directamente recursos compartidos de archivos Azure en cualquier parte del mundo. Los archivos compartidos SMB de Azure también pueden replicarse con Azure File Sync en servidores Windows, ya sean locales o en el Cloud, para obtener rendimiento y almacenamiento distribuido en caché de los datos allí donde se utilicen.

El almacenamiento en disco es un disco duro virtual completo al que puedes acceder. Es ideal como disco para una máquina virtual. De hecho, cuando creas una máquina virtual, también se crea el almacenamiento en disco.

El almacenamiento Azure Blob es la solución de almacenamiento de objetos de Microsoft para el Cloud. El almacenamiento en bloques (Blob) está optimizado para almacenar cantidades masivas de datos no estructurados, como texto o datos binarios. El almacenamiento en bloques es ideal para almacenar datos para copias de seguridad y restauración, recuperación ante desastres y archivo.

Los contenedores de blobs en Azure actúan de forma similar a los directorios de un sistema de archivos. Pueden contener un número ilimitado de blobs.

Azure Storage Explorer está diseñado para trabajar con Azure Blob Storage y Azure Files, pero no está diseñado para gestionar máquinas virtuales (Azure VM).

Azure File Sync está diseñado principalmente para sincronizar archivos entre servidores locales y Azure Files, no realiza funciones relacionadas con bases de datos, backups de VM o análisis de datos.

Azure Data Box está diseñado para transferir grandes volúmenes de datos a Azure de manera offline, no para análisis de datos, creación de redes virtuales o gestión de identidades y accesos.

Azure Migrate está diseñado para asistir en la migración de aplicaciones y datos hacia Azure, no para desarrollo de aplicaciones, análisis de datos en tiempo real o monitorización de recursos.

azcopy cp "container1" "container2"
Esta opción representa el formato de comando correcto que AzCopy utiliza para copiar blobs de un contenedor a otro en Azure Blob Storage, usando el prefijo cp para la operación de copiado y especificando la dirección URL de los contenedores de origen y destino. Las otras opciones no siguen el formato de comandos válido de AzCopy.
