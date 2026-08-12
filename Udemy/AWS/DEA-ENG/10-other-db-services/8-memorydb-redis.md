# Amazon MemoryDB for Redis

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Amazon MemoryDB for Redis** es un servicio de base de datos **en memoria**, totalmente compatible
con **Redis**: compatible con las APIs de Redis y sus distintas estructuras de datos.

**Redis** es un almacén de estructuras de datos en memoria de código abierto. Es posible instalarlo y
gestionarlo uno mismo en servidores o máquinas virtuales propias, pero MemoryDB ofrece esa misma
interfaz familiar y facilidad de uso, **totalmente gestionada por AWS**, aportando además la
durabilidad y fiabilidad que necesitan las aplicaciones modernas — al ser nativo de la nube, simplifica
el despliegue, la escalabilidad y la gestión frente a un Redis autogestionado, apoyándose en la
infraestructura de AWS para dar durabilidad Multi-AZ y failover automatizado.

## Características

- **Almacenamiento en memoria**: rendimiento muy alto, con latencia muy baja y acceso de alto
  throughput.
- **Escalado automático** ante cambios en la carga de trabajo y el volumen de datos.
- **Persistencia** mediante snapshots y replicación en varias Availability Zones.
- Integración con **IAM** para autenticación y autorización.
- **Cifrado en reposo y en tránsito**.

## Casos de uso

Adecuado para cualquier aplicación que necesite acceso muy rápido a los datos, junto con
escalabilidad y alta disponibilidad:

- **Caching de alto rendimiento**: reduce la carga sobre las bases de datos y mejora los tiempos de
  respuesta en aplicaciones con datos pesados que requieren acceso muy rápido.
- **Datos en tiempo real con alto tráfico**: por ejemplo, tablas de clasificación en videojuegos, o
  contadores de publicaciones/comentarios/"me gusta" en redes sociales.
- **Gestión de sesiones en aplicaciones web**: recuperación rápida y persistencia de la información de
  sesión entre distintas sesiones de usuario, clave para mantener una buena experiencia en
  aplicaciones con muchos usuarios.

## Precios

- Según el **tipo y número de nodos** desplegados — cada tipo de nodo ofrece distintas combinaciones
  de CPU, memoria y rendimiento de red.
- **Transferencia de datos**: se cobra al transferir datos dentro y fuera de MemoryDB, pero no cuando
  la transferencia ocurre dentro de la misma región.
- **Almacenamiento de backups** adicional más allá del nivel gratuito, cobrado por GB al mes.
- **Instancias reservadas**: comprometiéndose a un periodo de 1 a 3 años se obtiene un descuento sobre
  el precio estándar.
