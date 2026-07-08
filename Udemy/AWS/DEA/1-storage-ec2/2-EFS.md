# Amazon EFS (Elastic File System)

## ¿Qué es?

Amazon EFS es un servicio de **NFS gestionado** (sistema de archivos de red) que puede montarse en miles de instancias EC2 simultáneamente, funcionando además en **múltiples zonas de disponibilidad (Multi-AZ)**.

## Diferencia clave con EBS Multi-Attach

| Característica          | EBS Multi-Attach              | Amazon EFS                       |
| ----------------------- | ----------------------------- | -------------------------------- |
| Nº de instancias        | Limitado (pocas)              | Miles                            |
| Zonas de disponibilidad | Misma AZ                      | Múltiples AZ                     |
| Caso de uso             | 2-3 instancias en la misma AZ | Compartir archivos a gran escala |

**Regla práctica:** si necesitas compartir un sistema de archivos entre múltiples instancias, la recomendación es ir directo a EFS. EBS Multi-Attach queda para casos puntuales con pocas instancias en la misma AZ.

## Casos de uso típicos

- Compartir resultados de pruebas de performance
- Almacenamiento centralizado de logs
- Cualquier escenario donde varias instancias EC2 necesiten acceder a los mismos datos

## Características principales

- **Alta disponibilidad y escalabilidad**: diseñado para escalar a nivel de **petabytes** según demanda, sin interrumpir las aplicaciones.
- **Pago por uso**: se paga según los datos almacenados (es un servicio algo más costoso que otras alternativas, pero optimizable).

## Clases de almacenamiento

EFS permite gestionar el **ciclo de vida** de los archivos moviéndolos entre clases según el tiempo sin acceso, con el objetivo principal de **reducir costes**.

### 1. Estándar

- Para archivos de **acceso frecuente**.
- Soporta Multi-AZ.
- Ideal para **entornos de producción**.

### 2. Acceso Infrecuente (IA - Infrequent Access)

- Para archivos que **no se acceden frecuentemente** pero se necesitan conservar.
- Costo de almacenamiento mucho menor (impacto notable en la factura mensual).

### 3. One Zone

- Almacenamiento en **una sola zona** (no Multi-AZ).
- Ideal para **entornos de desarrollo** o backups, donde no se necesita alta disponibilidad.
- También existe la variante **One Zone-IA** (acceso infrecuente + una sola zona).

> 💡 Combinando Acceso Infrecuente + One Zone se puede lograr un ahorro superior al **90%** en costes de almacenamiento.

## Políticas de ciclo de vida

- Se define una **política de ciclo de vida** (lifecycle policy) sobre el sistema de archivos.
- Ejemplo: si un archivo no se accede durante **7 días**, se mueve automáticamente de la clase Estándar a la clase IA.
- El archivo **no deja de estar disponible**: simplemente cambia de clase de almacenamiento.
- Si se vuelve a acceder al archivo, este **regresa automáticamente a la clase Estándar**.

## Conclusión

Amazon EFS es un servicio ampliamente usado en la industria para compartir archivos entre instancias EC2 a gran escala, con buen rendimiento en producción y mecanismos integrados para optimizar costes mediante clases de almacenamiento y políticas de ciclo de vida.
