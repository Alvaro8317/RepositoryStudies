# Conectividad híbrida e interconexión de VPCs

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Conexión con una red corporativa (on-premises)

### VPN (Virtual Private Network)

- Conexión segura que se establece **a través de una red pública** entre la VPC y la infraestructura
  on-premises.
- Componentes:

| Componente                        | Descripción                                                                                        |
| --------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Virtual Private Gateway (VGW)** | Concentrador VPN en el lado de **AWS** de la conexión; se conecta a tu VPC.                        |
| **Customer Gateway (CGW)**        | Dispositivo físico o software en tu lado de la conexión; reside en tu centro de datos on-premises. |

### Direct Connect (DX)

- Servicio de **conexión de red dedicada** que proporciona conectividad **privada**, de **gran ancho
  de banda** y **baja latencia** entre los centros de datos/redes corporativas y AWS.
- El tráfico **nunca sale de la red de AWS**.
- Comparado con una VPN, es **más caro** y **lleva más tiempo configurar**.

## Interconexión de múltiples VPCs

### VPC Peering

- Permite **conexiones de red directas** entre dos VPC para que se comporten como si estuvieran en la
  misma red.
- Puede establecerse:
  - **Intra-región:** entre VPC de la misma región.
  - **Inter-región:** entre VPC de regiones distintas.

### Transit Gateway

- Actúa como un **hub centralizado** para conectar múltiples VPC y redes on-premises.
- Permite conectar **miles de VPC y redes locales** a través de una única gateway.
