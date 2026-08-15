# Práctica: crear una instancia RDS PostgreSQL en AWS

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Acceso a la consola de AWS

Se accede desde `console.aws.amazon.com`, con dos opciones de login:

- Usuario **IAM** (si ya se creó uno en la cuenta).
- Usuario **root** (el usado para crear la cuenta) — correo y contraseña definidos al crearla.

## RDS (Relational Database Service)

**RDS** es un servicio **gestionado** de AWS para configurar bases de datos: AWS se encarga de la
gestión de la infraestructura, lo que simplifica mucho el setup y el uso.

Para llegar ahí: buscar "RDS" en la consola → **Bases de datos** → **Crear base de datos**.

## Pasos de configuración

1. **Motor de base de datos**: entre las opciones (Aurora, MySQL, PostgreSQL, Microsoft SQL Server,
   etc.) se elige **PostgreSQL**, por ser un motor muy común. El proceso sería similar con los demás.
2. **Versión del motor**: se deja la más reciente, sin cambios adicionales.
3. **Plantilla**: se elige **Nivel gratuito (Free tier)** — limita las opciones a lo elegible para el
   free tier.
4. **Disponibilidad**: una única instancia, sin réplica (una sola zona de disponibilidad) — apropiado
   porque no son datos sensibles ni de producción.
5. **Identificador de la instancia de base de datos**: nombre único por cuenta y región (ej.
   `database-postgres-1`).
6. **Credenciales** (sección a expandir, muy importante):
   - **Nombre de usuario maestro**: por ejemplo `postgres` — hay que recordarlo, se usa para
     conectarse después.
   - **Contraseña maestra**: se define y se confirma.
7. **Configuración de la instancia**: con la plantilla free tier, solo aparecen tipos de instancia
   elegibles para el free tier compatibles con PostgreSQL (ej. `db.t3.micro`, `db.t4g.micro` — ambos
   dentro del free tier).
8. **Almacenamiento**: sin cambios; el valor mínimo disponible es **20 GB**.
9. **Conectividad / VPC**: sin cambios, salvo habilitar **acceso público**, para poder conectarse y
   mover datos fácilmente desde fuera de la VPC.
10. **Autenticación de base de datos**: se deja en **autenticación por contraseña**, usando el
    usuario maestro.
11. Sin más cambios necesarios más abajo → **Crear base de datos**.

## Free tier: qué cubre y cuánto cuesta fuera de él

> ⚠️ El free tier de RDS cubre **750 horas al mes durante los primeros 12 meses** de la cuenta, para
> ciertos tipos de instancia. 31 días × 24 horas = 744 horas, así que una sola instancia corriendo
> todo el mes completo sigue dentro de las 750 horas gratis.

- Esas 750 horas son un total compartido: si se tienen **dos instancias** corriendo todo el tiempo,
  la segunda **no** será gratis.
- Deshabilitar/eliminar o **detener temporalmente** la instancia evita que sigan acumulándose horas.
- Fuera del free tier (pasados los 12 meses, o si se excede), el tipo de instancia usado en el
  ejemplo cuesta aproximadamente **$11-12 al mes**, o alrededor de **1.5 centavos por hora** de uso.

## Buenas prácticas de limpieza

- Siempre que se configuren recursos en AWS con fines de práctica/formación, hay que
  **eliminarlos** una vez terminado el curso/ejercicio para evitar costos innecesarios.
- La instancia se puede **detener temporalmente** (Actions → Stop) mientras no se use, o
  **eliminar** (Actions → Delete) cuando ya no se necesite.
- Conviene revisar periódicamente el resumen de gastos/consumo en la consola de AWS (Billing) para
  confirmar que no queden recursos corriendo sin darse cuenta.

## Siguiente paso

Para acceder a la base de datos y ejecutar comandos hace falta una **interfaz gráfica (GUI)** de
cliente de base de datos, instalada localmente — se cubre en la siguiente clase.
