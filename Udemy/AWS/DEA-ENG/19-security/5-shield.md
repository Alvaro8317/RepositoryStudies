# AWS Shield

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Shield?

**AWS Shield** es el servicio diseñado para **proteger contra ataques DDoS** (**Distributed Denial
of Service** — denegación de servicio distribuida).

- En un ataque DDoS, **múltiples sistemas** intentan **inundar un objetivo** (por ejemplo, nuestra
  aplicación) con una gran cantidad de tráfico, consumiendo todo el **ancho de banda** disponible.
- El objetivo del atacante es que el servicio **caiga (se vaya abajo)**, de modo que los usuarios
  legítimos **no puedan usarlo**.

AWS Shield tiene **dos niveles**: **Standard** y **Advanced**.

## AWS Shield Standard

- Se **activa automáticamente** y es **gratuito** — no requiere ninguna configuración.
- Protege contra los ataques DDoS **más comunes y frecuentes** en:
  - **Capa de red y transporte** (capas **3** y **4** del modelo OSI).
  - **Capa de aplicación** (capa **7**) — por ejemplo, ataques de **HTTP slow read** o ataques
    **volumétricos**.
- Ofrece protección frente al **96%** de los ataques DDoS más comunes.
- Funciona junto con servicios como:
  - **Amazon CloudFront**
  - **Elastic Load Balancing (ELB)**
  - **Route 53**
- Incluye métricas en **AWS CloudWatch** y **notificaciones del AWS Health Dashboard** durante
  ataques de mayor envergadura.

## AWS Shield Advanced

- Ofrece **protección mejorada** para mayores niveles de seguridad, con **cargo adicional**.
- Protege contra ataques **más grandes y sofisticados**, incluyendo ataques en la **capa de
  aplicación**.
- Incluye **protección contra cargos por escalado (Cost Protection)**: cubre los costes
  adicionales que resultarían del **auto scaling** de los servicios de AWS como consecuencia de un
  ataque DDoS.
- Los suscriptores tienen acceso al **DDoS Response Team (DRT)**, que proporciona **asistencia
  inmediata** durante los ataques.
- Ofrece **diagnósticos detallados de ataques**: informes en tiempo real y análisis más detallados
  posteriores al evento, integrados con **AWS WAF** y **AWS Firewall Manager**.
- Permite añadir **protección adicional a recursos específicos**, como:
  - Instancias **EC2**.
  - **Elastic IP addresses**.
  - Endpoints de **Global Accelerator**.

> ⚠️ Shield Advanced está pensado para organizaciones que requieren **mayor protección** —
> especialmente aquellas muy visibles o que ya han sido **objetivo de ataques DDoS**
> anteriormente.

## Resumen: Standard vs. Advanced

| Característica                         | Shield Standard                       | Shield Advanced                                                      |
| -------------------------------------- | ------------------------------------- | -------------------------------------------------------------------- |
| **Coste**                              | Gratis                                | Cargo adicional                                                      |
| **Activación**                         | Automática                            | Hay que suscribirse                                                  |
| **Cobertura**                          | Ataques DDoS comunes (capas 3, 4 y 7) | Ataques más grandes y sofisticados (incluye capa 7)                  |
| **Cost Protection**                    | No                                    | Sí — cubre costes de auto scaling por el ataque                      |
| **DDoS Response Team (DRT)**           | No                                    | Sí — asistencia inmediata durante ataques                            |
| **Diagnósticos detallados**            | No                                    | Sí — informes en tiempo real y post-evento, con WAF/Firewall Manager |
| **Protección de recursos específicos** | No                                    | Sí — EC2, Elastic IP, Global Accelerator, etc.                       |
