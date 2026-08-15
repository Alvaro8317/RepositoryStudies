# Práctica: conectarse a RDS PostgreSQL con DBeaver

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Instalación y primer arranque

Al abrir **DBeaver** por primera vez:

- Se puede excluir DBeaver de ser escaneado (para que arranque más rápido).
- Se puede crear una **base de datos de ejemplo**, útil para explorar funcionalidades básicas del
  cliente.
- Puede pedir descargar **archivos de drivers adicionales** — se descargan cuando se soliciten.

## Crear la conexión a la base de datos de RDS

1. **New Database Connection**.
2. En la lista de sistemas de bases de datos soportados, elegir **PostgreSQL** (buscar si no aparece
   a la vista) — es el motor usado porque la base de datos en RDS se configuró como PostgreSQL.
3. Completar los detalles de conexión, usando los datos de la instancia RDS creada:
   - **Host**: el *endpoint* de la instancia RDS (se copia desde la consola de AWS).
   - **Port**: `5432` (puerto por defecto de PostgreSQL).
   - **Database**: el identificador de la base de datos elegido al crearla.
   - **Username**: `postgres` (el usuario maestro configurado).
   - **Password**: la contraseña maestra configurada — se puede marcar la casilla para guardarla.
4. **Test Connection** — puede pedir descargar drivers adicionales antes de poder probar la conexión.

## Resolviendo el primer error: connection timeout

Al probar la conexión puede fallar por **timeout**. La causa más común es el **Security Group** de la
instancia RDS, que por defecto no permite el tráfico entrante necesario.

Solución, desde la consola de AWS:

1. Ir a **RDS** → la base de datos creada → pestaña **Conectividad y seguridad**.
2. Abrir el **Security Group de la VPC** asociado a la instancia.
3. En **Reglas de entrada (Inbound rules)** → **Editar reglas de entrada**.
4. Añadir una regla nueva: tipo **PostgreSQL**, origen **Anywhere-IPv4** (`0.0.0.0/0`), y eliminar
   la regla restrictiva anterior.
5. Guardar — los cambios pueden tardar un par de segundos en aplicarse.

> ⚠️ Abrir el security group a `0.0.0.0/0` (cualquier IP) es lo que se muestra en el curso por
> simplicidad, pero expone el puerto de PostgreSQL a todo internet (protegido solo por la
> contraseña). En un entorno real conviene restringir el origen a IPs de confianza.

## Resolviendo el segundo error: "database does not exist"

Tras arreglar el security group, puede aparecer un error de que la base de datos indicada no existe.
Solución: quitar el nombre de base de datos específico de la conexión y conectarse directamente al
host (marcando la opción de **mostrar todas las bases de datos**), sin especificar una base de datos
concreta de antemano.

## Resultado

Con la conexión funcionando, DBeaver muestra las bases de datos disponibles en la instancia
(incluida la base de datos por defecto `postgres`), junto con sus esquemas y tablas — actualmente
vacías, ya que todavía no se han cargado datos.

Con esto queda: la herramienta de integración de datos configurada, la base de datos en AWS creada,
y la conexión desde la máquina local funcionando.
