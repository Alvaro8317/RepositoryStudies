# Extras de almacenamiento de AWS

## 📊 Comparativa de AWS Snow Family

| Característica                 | **Snowcone**                              | **Snowball Edge**                                                                     | **Snowmobile**                                            |
| ------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 📦 Tamaño y portabilidad       | Muy portátil (2.1 kg)                     | Medio (como una maleta grande)                                                        | Enorme (tráiler de 45 pies)                               |
| 💾 Capacidad de almacenamiento | Hasta 8 TB (SSD)                          | - 80 TB (modo solo transferencia) - 42 TB HDD / 28 TB NVMe (modo computación)         | Hasta 100 PB por Snowmobile (exabytes al combinar varios) |
| ⚙️ Capacidades de cómputo      | Limitado (uso básico de Edge Computing)   | Alta (Soporta EC2, Lambda, S3 local)                                                  | No tiene cómputo integrado                                |
| 🌍 Edge computing              | ✅ Sí, uso en terreno remoto              | ✅ Sí, con soporte de contenedores y EC2                                              | ❌ No                                                     |
| 🔌 Energía y conectividad      | Requiere batería/cables externos          | Energía y red cableada estándar                                                       | En sitio con infraestructura propia                       |
| ☁️ Integración con servicios   | Compatible con **AWS DataSync**           | AWS OpsHub, EC2, S3 compatible, Lambda                                                | Directo a S3 una vez que se conecta en AWS                |
| 🚚 Modo de transferencia       | - Online con DataSync - Offline con envío | - Offline - Con AWS DataSync online                                                   | Sólo offline (entrega física)                             |
| 🔒 Seguridad                   | Cifrado automático con AWS KMS            | Cifrado con AWS KMS, carcasa resistente                                               | Nivel militar, monitoreo GPS, acceso biométrico           |
| 🛠️ Casos de uso típicos        | Sitios remotos, IoT, drones, sensores     | Migración de datos, aplicaciones en terreno, grabación médica, procesamiento en sitio | Migraciones masivas (data centers)                        |
| 🌐 Reutilizable                | Sí                                        | Sí                                                                                    | No (AWS lo instala y retira una vez)                      |

---

### 🧠 ¿Qué es **Edge Computing**?

Edge computing se refiere a **procesar datos cerca de donde se generan**, en lugar de enviarlos directamente a la nube. Es útil en entornos con poca o intermitente conectividad (campos petroleros, barcos, zonas militares, etc.).

---

### ✅ ¿Cuándo usar cada uno?

- **Snowcone**: Ideal si necesitas algo **ligero y portátil** para sitios remotos, con poco volumen de datos (hasta 8 TB).
- **Snowball Edge**: Para **migraciones medianas**, entornos industriales, y computación en terreno (puede ejecutar EC2 y Lambda local).
- **Snowmobile**: Cuando necesitas **migrar grandes centros de datos** (10 PB en adelante), de forma física y ultra segura.

## 🧊 ❌ ¿Por qué **no se puede mover directamente a Glacier** desde Snowball?

Cuando se usan dispositivos **AWS Snowball** para **importar datos a AWS**, hay una **restricción importante**:

### 🚫 No es posible mover datos **directamente** desde Snowball a S3 Glacier o Glacier Deep Archive

---

## ✅ ¿Cómo se hace entonces?

Para almacenar datos en Glacier, **debes seguir este flujo**:

1. **Importar datos con Snowball** → Se almacenan en **Amazon S3 estándar**.
2. Una vez en S3, configuras una **regla del ciclo de vida** en el bucket.
3. La regla moverá automáticamente los objetos a:

   - ❄️ S3 Glacier
   - 📦 Glacier Deep Archive

---

### 📘 Ejemplo práctico

Supón que importaste 50 TB con un **Snowball Edge** a un bucket S3 llamado `imported-data`.

Puedes definir una **regla de ciclo de vida** como esta:

```json
{
  "Rules": [
    {
      "ID": "MoveToGlacier",
      "Filter": {
        "Prefix": ""
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 0,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

🔁 Esta política transicionará todos los objetos del bucket a Glacier **inmediatamente después** de su carga.

---

## 🎯 ¿Por qué existe esta restricción?

- ❗ **Snowball solo soporta mover objetos al almacenamiento S3 estándar.**
- Glacier es una **clase de almacenamiento fría y de archivo**, que **no está disponible como destino directo** en operaciones de importación.
- AWS requiere que los objetos existan primero como objetos S3 válidos y luego apliques la transición.

---

## 🧠 Notas adicionales

| Tema                             | Detalle                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ❄️ ¿Y si quieres solo Glacier?   | Se recomienda moverlo a S3 estándar **y luego** aplicar la política.                                         |
| ⏳ ¿Cuánto tarda la transición?  | Depende de la regla (`Days` en 0 es inmediato), pero la transición puede tardar algunas horas en ejecutarse. |
| 🔐 ¿Puedo cifrar el bucket?      | Sí, puedes importar los datos cifrados y mantener el cifrado durante la transición.                          |
| 📦 ¿Puedo usar versiones o tags? | Sí, las reglas del ciclo de vida pueden aplicarse por **etiquetas**, **versiones**, o **prefijos**.          |

## 📦 ¿Qué es Amazon FSx?

> **Amazon FSx** es un servicio completamente gestionado que permite lanzar sistemas de archivos de alto rendimiento de terceros (como Windows File Server, Lustre, NetApp ONTAP, OpenZFS) en AWS, como si fuera un **RDS pero para sistemas de archivos**.

---

## 🧠 Principales variantes de FSx

| Variante                        | Casos de uso principales                                                  | Protocolos / Integración      | Características clave                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **FSx for Windows File Server** | Aplicaciones que requieren un sistema de archivos Windows (SMB, NTFS, AD) | SMB, NTFS, Active Directory   | Cuotas por usuario, integración con AD, soporte para DFS (Distributed File System), backups automáticos en S3, Multi-AZ  |
| **FSx for Lustre**              | HPC, ML, procesamiento de video, simulaciones científicas                 | Compatible con S3, Linux, VPN | Sistema distribuido y paralelo, baja latencia, 100s de GB/s, IOPS altos, modo temporal y persistente, integración con S3 |
| **FSx for NetApp ONTAP**        | Migración de cargas con ONTAP/NAS, almacenamiento híbrido                 | NFS, SMB, iSCSI               | Snapshots automáticos, replicación, deduplicación, compresión, autoescalado, integrable con EC2, ECS, EKS y más          |
| **FSx for OpenZFS**             | Migración de cargas en ZFS, alto rendimiento con NFS                      | NFS v3 a v4.2                 | Snapshots, clonación instantánea, compresión, hasta 1 millón IOPS y latencia < 0.5ms, bajo costo                         |

---

### 📁 FSx for Windows File Server

- ✅ Soporta **SMB**, NTFS, DFS.
- 🏢 Integración con **Active Directory**.
- 📊 Cuotas por usuario.
- 🛡️ Multi-AZ opcional y backups diarios automáticos en S3.
- 📎 Se puede montar incluso en instancias **Linux**.

---

### ⚙️ FSx for Lustre

- ⚡ **Sistema de archivos distribuido** para alto rendimiento.
- 🧠 Casos: **Machine Learning**, HPC, modelado financiero, video.
- 📂 Integración directa con **Amazon S3**: Puedes montar un bucket como si fuera un sistema de archivos.
- 🧪 **Dos modos de despliegue**:

  1. **Temporal (In-memory)**: para procesamiento a corto plazo, **sin replicación**, más barato.
  2. **Persistente**: con replicación en la AZ, almacenamiento a largo plazo.

- 🚀 100s GB/s, latencia sub-ms.

---

### 🧬 FSx for NetApp ONTAP

- 💼 Solución madura para migrar cargas que ya usan NetApp.
- 🧩 Compatible con: Linux, Windows, macOS, VMware Cloud, EC2, ECS, EKS, WorkSpaces, AppStream 2.0.
- 🧠 Soporta: **NFS, SMB, iSCSI**.
- 💡 Funciones avanzadas:

  - Snapshots automáticos.
  - Replicación entre regiones.
  - Deduplicación y compresión.
  - Autoescalado de capacidad.

---

### 💽 FSx for OpenZFS

- 🧠 Ideal si ya usas **ZFS on-premise**.
- 🎯 Compatible con **NFS v3 – v4.2**.
- 📊 Hasta **1 millón de IOPS**, latencia **< 0.5 ms**.
- 🔁 Snapshots + clonación instantánea (muy útil en entornos dev/test).
- 💰 Bajo costo, compresión y escalabilidad.

---

## 🌐 Acceso híbrido y Multi-AZ

Todas las variantes permiten:

- 📡 Acceso desde **infraestructura on-premise** (con VPN o Direct Connect).
- 🛡️ Opciones de **Multi-AZ** para alta disponibilidad.
- 🔒 Backups automáticos en **S3** y cifrado con **KMS**.

## 🌩️ Nubes híbridas & AWS Storage Gateway

### ¿Qué es una **nube híbrida**?

Una **nube híbrida** es un entorno que **combina infraestructura local (on-premise)** con **servicios en la nube**, permitiendo:

- Continuidad del negocio.
- Flexibilidad para mover datos o cargas de trabajo.
- Costos optimizados y escalabilidad bajo demanda.

---

## 🧱 Almacenamiento nativo de AWS

AWS soporta:

- 📦 Almacenamiento de objetos: **Amazon S3, Glacier**
- 💾 Almacenamiento en bloques: **Amazon EBS, FSx, Storage Gateway**
- 📁 Almacenamiento de archivos: **Amazon EFS, FSx**

---

## 🚪 ¿Qué es AWS Storage Gateway?

**AWS Storage Gateway** es un **puente híbrido** entre tu infraestructura local y AWS. Virtualiza el acceso a almacenamiento en la nube, manteniendo caché local para datos frecuentes.

---

## 🧰 Casos de uso típicos

| Caso de uso                          | Descripción                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| 🎯 Recuperación ante desastres (DRP) | Almacena copias fuera del sitio local, accesibles desde AWS.     |
| 💾 Backups y restauraciones          | Automatiza backups desde on-premise a la nube.                   |
| 📚 Archivado por niveles             | Mueve datos fríos a S3 Glacier vía políticas de ciclo de vida.   |
| 🚀 Caché local de acceso rápido      | Mejora el rendimiento local para datos accedidos con frecuencia. |

---

## 🧩 Tipos de AWS Storage Gateway

### 1. 📁 **File Gateway (S3 File Gateway)**

- Montado como **NFS** o **SMB** desde servidores locales.
- Los archivos son almacenados como **objetos en S3**.
- Los **archivos recientes** se almacenan en **caché local**.
- Soporta:

  - Integración con **Active Directory**.
  - IAM Roles para permisos.
  - Reglas de ciclo de vida para mover a **Glacier**.

- 📥 Acceso ideal a datos como:

  - Archivos de aplicaciones empresariales.
  - Documentos compartidos.

> Ejemplo: Empresa de diseño gráfico guarda sus archivos PSD en S3 usando SMB desde su servidor Windows local.

---

### 2. 💽 **Volume Gateway**

> Proporciona **almacenamiento en bloque iSCSI** que las aplicaciones ven como discos duros.

- **Dos modos**:

  - **Volúmenes en caché**: Los datos se almacenan en **AWS S3** y el más reciente en **caché local**.
  - **Volúmenes almacenados**: Los datos se almacenan localmente y se **respalda en S3**.

- Compatibilidad con **snapshots EBS** para protección y restauración.

> Ejemplo: Servidor de base de datos local que mantiene discos sincronizados en la nube para restauración rápida.

---

### 3. 📼 **Tape Gateway**

> Emula una **librería de cintas virtuales (VTL)** respaldada por **S3 y Glacier**.

- Se integra con herramientas tradicionales como **Veeam, Commvault, Veritas**.
- Las empresas siguen usando su software de backup como siempre, pero ahora las cintas virtuales van a la nube.

> Ejemplo: Empresa bancaria que quiere dejar las cintas físicas, pero no quiere cambiar su sistema de backup.

---

### 4. 🗂️ **FSx File Gateway**

> Proporciona **acceso remoto en sitio** a **Amazon FSx for Windows File Server**.

- Los usuarios acceden a sus archivos compartidos desde servidores locales usando **SMB**.
- Los archivos de uso frecuente se almacenan en **caché local**.
- Ideal para:

  - Directorios personales.
  - Archivos compartidos empresariales.
  - Aplicaciones Windows que requieren NTFS o ACLs de Windows.

> Ejemplo: Oficinas regionales que acceden a los mismos archivos sin usar VPNs pesadas.

---

## 🖥️ Implementación de Storage Gateway

- Se instala como una **máquina virtual (VM)** en el centro de datos.
- También disponible como **dispositivo físico (hardware)** desde **amazon.com** si no se puede virtualizar.
- Protocolo de comunicación con AWS: **HTTPS cifrado**.
- Puede **conectarse a la nube por VPN o Direct Connect**.

---

Perfecto, aquí tienes los apuntes claros y estructurados sobre **AWS DataSync** y su diferencia con **AWS Storage Gateway**:

---

## 🚀 **AWS DataSync**

**AWS DataSync** es un servicio de transferencia **rápida, segura y automatizada** de grandes cantidades de datos entre:

- 📍 **On-premises** (infraestructura local)
- ☁️ **AWS servicios de almacenamiento**
- 🌐 **Nubes de terceros (por ejemplo, Google Cloud, Azure)**

---

### 🎯 Casos de uso

| Caso                                                    | Descripción                                            |
| ------------------------------------------------------- | ------------------------------------------------------ |
| 🧳 Migración de datos                                   | Mover datos de servidores locales a AWS (S3, EFS, FSx) |
| 🔁 Replicación y sincronización programada              | Mover datos periódicamente entre sistemas              |
| 🛠️ Backup/Archiving                                     | Copiar datos hacia Glacier, Deep Archive               |
| 🌐 Transferencias entre regiones de AWS o entre cuentas |                                                        |

---

### ⚙️ Características

| Característica                            | Detalles                                                           |
| ----------------------------------------- | ------------------------------------------------------------------ |
| 📦 **Soporta múltiples fuentes/destinos** | On-premises ↔️ AWS AWS ↔️ AWS (S3, EFS, FSx, S3 Glacier, S3 IA...) |
| ⏱️ **Transferencia eficiente**            | Usa protocolo propietario más rápido que rsync/robocopy            |
| 🔄 **Sincronización**                     | Copia incremental, detecta cambios                                 |
| 🔐 **Seguridad**                          | Cifrado en tránsito y en reposo                                    |
| 📅 **Programable**                        | Soporta tareas programadas y filtrado por patrones de archivos     |
| 📑 **Permisos y metadatos**               | Conserva timestamps, propietarios, ACLs                            |
| 🚀 **Alto rendimiento**                   | Un solo agente puede alcanzar hasta **10 Gbps** (reales)           |
| 🧪 **Verificación de integridad**         | Verifica automáticamente los archivos transferidos                 |

---

### 🛡️ Arquitectura básica

1. Instalas un **agente de DataSync** en un servidor local (VM o hardware).
2. Configuras una **tarea de sincronización** desde tu sistema de archivos local a un bucket S3, sistema EFS o FSx.
3. El agente se conecta con **AWS a través de HTTPS** para ejecutar la transferencia.

---

## 🆚 Comparativa: **DataSync vs Storage Gateway**

| Característica          | **AWS DataSync**                                               | **AWS Storage Gateway**                                        |
| ----------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| 📥 Propósito            | Transferencia **rápida** de datos                              | Extensión de almacenamiento local hacia la nube                |
| 🔁 Flujo                | Migración, sincronización, backup programado                   | Acceso en tiempo real a datos en AWS                           |
| ⏱️ Transferencia        | Rápida (hasta 10 Gbps) por agente                              | Moderada, con caché y menor prioridad de velocidad             |
| 🔄 Dirección            | Bidireccional, pero con control                                | Lectura/escritura con caché                                    |
| 🎯 Ideal para           | ETL, migraciones masivas, backups, sincronizaciones periódicas | Reemplazo de NAS, backups con VTL, trabajo híbrido local-cloud |
| 💾 Almacenamiento local | No se requiere                                                 | Necesita hardware físico o VM                                  |
| 🧠 Inteligencia local   | Solo transferencias                                            | Cacheo, sincronización incremental en caliente                 |
| 🧰 Tipos                | No aplica                                                      | File Gateway, Volume Gateway, Tape Gateway                     |

---

## 📌 Conclusión

- Si necesitas **mover grandes volúmenes de datos**, ya sea una **migración inicial** o una **sincronización recurrente**, lo ideal es **DataSync**.
- Si necesitas **trabajar en tiempo real desde tu entorno local con almacenamiento en la nube** (como si fueran discos locales), entonces es **Storage Gateway**.

## Comparativa

| **Servicio**                                | **Descripción**                                                             | **Casos de uso**                                                                   |
| ------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| S3                                          | Almacenamiento de objetos altamente duradero y escalable.                   | Backup, archivos estáticos, hosting de sitios estáticos, data lakes.               |
| S3 Glacier                                  | Almacenamiento de objetos para archivos a largo plazo, acceso infrecuente." | Archivado, cumplimiento, backups históricos.                                       |
| EBS                                         | Disco en bloque para EC2, persistente y de baja latencia."                  | Sistemas operativos, BD, apps que requieren disco rápido y persistente.            |
| Instance Store                              | Disco efímero físicamente unido a la instancia EC2.                         | Cache temporal, almacenamiento de buffers, procesamiento intermedio.               |
| EFS                                         | Sistema de archivos NFS totalmente gestionado, escalable y multi-AZ."       | Web apps, carpetas compartidas, almacenamiento de logs.                            |
| FSx for Windows                             | Sistema de archivos compartido con soporte SMB y NTFS.                      | Migración de cargas de trabajo Windows, aplicaciones AD, compartición de archivos. |
| FSx for Lustre                              | Sistema de archivos paralelo de alto rendimiento.                           | Machine Learning, análisis genómico, renderizado de vídeo.                         |
| FSx for ONTAP                               | NetApp ONTAP gestionado como servicio.                                      | Migración de ONTAP, NFS/SMB/iSCSI en cloud, snapshots y replicación.               |
| FSx for OpenZFS                             | Sistema de archivos ZFS en AWS con soporte NFS.                             | Carga de trabajo ZFS, alto rendimiento, snapshots, clones.                         |
| Storage Gateway                             | Puente entre almacenamiento local y AWS.                                    | DRP, backup, extensión NAS o VTL hacia cloud.                                      |
| AWS Transfer Family                         | Transfiere archivos a S3 o EFS mediante SFTP, FTP, FTPS."                   | Intercambio de archivos, integraciones con ERPs, CRMs, entornos heredados.         |
| AWS DataSync                                | Transfiere y sincroniza datos entre sitios on-premise y AWS.                | Migración de datos, sincronización de almacenamiento entre nubes o regiones.       |
| Snowcone                                    | Dispositivo portátil para edge computing y transferencia de datos (2.1 kg). | Entornos desconectados, edge computing, uso militar o en campo.                    |
| Snowball                                    | Dispositivo rugerizado para mover TBs o PBs a AWS.                          | Migración de grandes datasets, backup físico hacia AWS.                            |
| Snowmobile                                  | Camión para transferir exabytes de datos.                                   | Migraciones masivas de data centers enteros.                                       |
| "Bases de datos (RDS, Aurora, DynamoDB...)" | Almacenamiento estructurado, relacional o NoSQL, gestionado."               | Aplicaciones transaccionales, analíticas, ecommerce, IoT.                          |
