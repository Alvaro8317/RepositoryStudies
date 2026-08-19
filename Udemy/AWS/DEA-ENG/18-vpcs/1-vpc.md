# Amazon VPC (Virtual Private Cloud)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es una VPC?

Una **VPC** es una **red virtual dedicada a tu cuenta** que te permite lanzar tus recursos dentro de
una sección **lógicamente aislada** de la nube de AWS.

- Es un **servicio regional**: una VPC vive dentro de una región concreta.
- Sobre una VPC también se puede construir una **arquitectura de nube híbrida**, conectando tu
  infraestructura on-premises a AWS mediante **VPN** o **Direct Connect** (se verá en detalle más
  adelante en el curso).

> ⚠️ Como las VPC están **aisladas por defecto**, no pueden comunicarse directamente con Internet ni
> con otras redes. Los componentes que habilitan esa comunicación (Internet Gateway, NAT Gateway,
> VPN Gateway...) se verán en la siguiente clase.

## Subredes (Subnets)

Una **subnet** es un **rango de direcciones IP** dentro de una VPC. Las subredes permiten segmentar
el rango de direcciones IP de la VPC en redes más pequeñas.

Cada subred se clasifica según su **tipo de conectividad**:

| Tipo de subred | Conectividad | Uso típico |
| ------------------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Pública (Public Subnet)** | Acceso directo a Internet a través de un **Internet Gateway**. | Recursos que requieren acceso directo a Internet (ej. servidor web, ALB). |
| **Privada (Private Subnet)** | Sin acceso a Internet por defecto; depende de un **NAT Gateway** para tráfico saliente. | Recursos internos que necesitan salir a Internet pero no ser accesibles. |
| **Solo VPN (VPN-only Subnet)** | Conectividad segura a redes on-premises a través de una **VPN Gateway**. | Comunicación privada entre la VPC y la red local. |
| **Aislada (Isolated Subnet)** | Sin rutas hacia ninguna gateway (ni Internet ni VPN); completamente aislada del exterior. | Servicios sensibles o críticos que deben quedar totalmente aislados. |

- Cada subred está asociada a una **tabla de rutas (Route Table)**, que determina hacia dónde y cómo
  se dirige el tráfico de esa subred (ej. hacia un Internet Gateway o una VPN Gateway).
