# Amazon EFS — Práctica: Creación y Configuración

> Este documento complementa el resumen teórico de Amazon EFS con los pasos prácticos de creación desde la consola de AWS.

## Preparación previa: instancias EC2

Antes de crear el sistema de archivos, se necesitan **dos instancias EC2 en ejecución** donde luego se montará el EFS:

- Nombre: `demo EFS`
- AMI: **Amazon Linux**
- Tipo: **T2 Micro**
- Conexión: **EC2 Instance Connect** (no es obligatorio crear un par de claves SSH si se usa Instance Connect)
- Se etiquetan luego como **A** y **B** para identificarlas al momento de montar el sistema de archivos

## Creación del sistema de archivos EFS

### 1. Nombre y tipo

- Nombre: `demo.FS`
- Tipo de sistema de archivos:
  - **Regional** (valor por defecto, distribuido en varias AZ)
  - **Una única zona** (menor coste, sin Multi-AZ)

### 2. Copias de seguridad

- Se pueden habilitar backups automáticos integrados con **AWS Backup**.

### 3. Administración del ciclo de vida (Lifecycle Management)

Aquí se configuran las transiciones automáticas entre clases de almacenamiento:

| Transición | Ejemplo de configuración |
|---|---|
| Estándar → Acceso Infrecuente (IA) | Ej: tras **7 días** sin acceso |
| IA → Archive | Ej: tras **30 días** sin acceso |
| Vuelta a Estándar | Configurable (ej. "en el primer acceso" o "ninguno") |

**Novedad destacada:** además de la clase de Acceso Infrecuente, AWS ha lanzado la clase **Archive**, aún más económica, pensada para archivos con muy poco o ningún acceso. Esto da dos niveles de reducción de costes progresivos: Estándar → IA → Archive.

### 4. Cifrado

- Se puede cifrar los datos **en reposo** usando una **clave KMS**.
- Por defecto se puede usar la clave KMS gestionada por AWS sin configuración adicional.

### 5. Configuración de rendimiento (performance)

- Existen distintos modos según el caso de uso (recomendable revisar la documentación oficial para casos avanzados).
- Modo recomendado por defecto: **Elástico**, ya que escala automáticamente según la demanda sin intervención manual.
- Alternativa: modo **aprovisionado**, donde se fija manualmente el rendimiento.

### 6. Etiquetas

- Opcional, permite organizar y clasificar el recurso.

### 7. Acceso a la red

- Se define la **VPC** y las **zonas de disponibilidad** donde estará disponible el sistema de archivos (en el ejemplo: VPC en Norte de Virginia).

### 8. Política del sistema de archivos (opcional)

- Paso opcional donde se puede definir una **política en formato JSON** (similar a las políticas IAM/S3) para:
  - Conceder o denegar permisos de acceso
  - Controlar quién puede leer/escribir en el sistema de archivos

### 9. Revisión y creación

- Último paso: revisar la configuración y confirmar la creación del sistema de archivos.

## Montaje del sistema de archivos en las instancias EC2

### 1. Configurar el grupo de seguridad para NFS

Antes de montar el EFS es imprescindible abrir el puerto necesario para NFS, tanto en el grupo de seguridad del propio sistema de archivos como en el de las instancias EC2:

- Ir a **EFS → Red** para ver los grupos de seguridad asociados por zona de disponibilidad.
- Editar las **reglas de entrada** del grupo de seguridad y agregar una regla:
  - **Tipo:** TCP personalizado
  - **Puerto:** `2049`
  - **Origen:** el necesario según el caso (en la demo, abierto a cualquier dirección)
- Repetir la misma regla en el **grupo de seguridad de las instancias EC2** (en la demo, ambas instancias usaban el grupo `Launch Wizard 8`).

> ⚠️ Si no se abre el puerto 2049 en ambos grupos de seguridad, el montaje fallará con un error de conexión.

### 2. Crear el directorio de montaje

Dentro de cada instancia EC2 (conectando por Instance Connect):

```bash
df -k                          # lista los sistemas de archivos ya montados
sudo mkdir -p fs/wp_content     # crea el directorio donde se montará el EFS
cd fs/wp_content
```

> Ejemplo de caso de uso: un directorio pensado para guardar los archivos/imágenes de un WordPress.

### 3. Instalar Amazon EFS Utils

Es necesario instalar el paquete **`amazon-efs-utils`** en la instancia antes de poder montar el sistema de archivos.

### 4. Configurar el montaje persistente (`/etc/fstab`)

Para que el sistema de archivos se monte automáticamente incluso después de un reinicio de la instancia:

```bash
sudo vi /etc/fstab
```

Dentro del archivo se añade una línea con el comando de montaje de EFS, sustituyendo:

- El **ID del sistema de archivos** (se obtiene desde la consola de EFS).
- El **directorio de montaje** creado en el paso anterior (`fs/wp_content`).

Se guarda con los comandos de `vi`: `Esc` → `:wq`.

Se puede verificar que la línea quedó registrada con:

```bash
cat /etc/fstab
```

### 5. Montar el sistema de archivos

```bash
sudo mount fs/wp_content
df -k    # confirma que el nuevo sistema de archivos aparece montado
```

### 6. Probar el uso compartido entre instancias

En la **instancia A**:

```bash
cd fs/wp_content
sudo touch demo_fs.txt   # se necesita sudo para crear archivos en el punto de montaje
```

En la **instancia B**, tras repetir exactamente los mismos pasos de instalación, configuración de `fstab` y montaje (usando el mismo ID de sistema de archivos y directorio):

```bash
cd fs/wp_content
ls
```

✅ El archivo `demo_fs.txt` creado desde la instancia A aparece también en la instancia B, confirmando que **ambas instancias comparten el mismo almacenamiento persistente en la nube** a través de Amazon EFS.

### Recomendación de monitoreo de costes

Una vez el EFS está en uso, se recomienda **monitorizar activamente** qué datos tienen acceso frecuente frente a los que tienen acceso infrecuente o deberían pasar a la clase Archive, ya que es ahí donde se logra el mayor ahorro en la factura mensual.

## Limpieza de recursos (fin de la demo)

Para no generar costes innecesarios tras la práctica:

1. **Detener/terminar las instancias EC2** (A y B).
2. **Eliminar el sistema de archivos EFS** desde la consola.
3. **Eliminar la regla de entrada NFS** (puerto 2049) del grupo de seguridad *default* que se había modificado.
4. **Eliminar los grupos de seguridad** creados específicamente para las demos que ya no se vayan a usar (Acciones → Eliminar grupos de seguridad → confirmar escribiendo "Eliminar").

---

### Resumen de decisiones tomadas en la demo

| Configuración | Valor elegido |
|---|---|
| Tipo de sistema de archivos | Regional |
| Backups automáticos | Disponible vía AWS Backup |
| Ciclo de vida | IA tras 7 días, Archive tras 30 días |
| Cifrado en reposo | Clave KMS por defecto |
| Rendimiento | Elástico (automático) |
| Política de acceso | No definida (opcional) |
| Puerto NFS requerido | TCP 2049 |
| Directorio de montaje usado | `fs/wp_content` |
| Persistencia tras reinicio | Configurada vía `/etc/fstab` |
