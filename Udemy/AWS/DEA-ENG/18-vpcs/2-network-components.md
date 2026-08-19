# Componentes de red de la VPC

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Por qué se necesitan?

Como se vio en el apunte anterior ([1-vpc.md](1-vpc.md)), las VPC están **aisladas por defecto** y no
pueden comunicarse directamente con Internet. Para permitir esa comunicación entre los recursos de una
VPC e Internet se necesitan componentes de red específicos: **Internet Gateway**, **Egress-only
Internet Gateway** y **NAT**.

## Internet Gateway (IGW)

- Es la **puerta de enlace a Internet** que debe estar conectada a la VPC para que sus recursos puedan
  comunicarse con Internet.
- Permite la comunicación **bidireccional** entre los recursos de la VPC e Internet.

## Egress-only Internet Gateway

- Se utiliza **únicamente para tráfico IPv6**.
- Permite que instancias con IPv6 habilitado en una **subred privada** inicien comunicación
  **saliente** hacia Internet por IPv6.
- Por otro lado, **impide el tráfico entrante** iniciado por un host IPv6 externo.

## NAT (Network Address Translation)

Permite que las instancias de una **subred privada** se conecten a Internet o a otros servicios de
AWS, pero **impide que Internet inicie conexiones** con dichas instancias.

- Las subredes públicas y privadas protegen los recursos de una conexión directa a Internet, pero una
  instancia en subred privada (ej. una base de datos) puede necesitar salir a Internet o a otros
  recursos de AWS — para eso se usa un dispositivo **NAT**.
- AWS ofrece dos tipos de dispositivos NAT:

| Tipo             | Descripción                               |
| ---------------- | ----------------------------------------- |
| **NAT Gateway**  | Servicio gestionado por AWS.              |
| **NAT Instance** | Instancia EC2 configurada para hacer NAT. |

- Ambos permiten a las instancias de una subred privada iniciar tráfico **IPv4** saliente hacia
  Internet (o hacia otros recursos de AWS), pero impiden que el tráfico entrante llegue a esas
  instancias.
- Ambos se lanzan en una **subred pública**, ya que requieren conectividad a Internet.

### Diferencia clave

> ⚠️ Un **NAT Gateway**, por defecto, **no permite** que el tráfico entrante iniciado desde fuentes
> externas llegue a las instancias en subredes privadas. Una **NAT Instance**, en cambio, **sí puede
> configurarse** para permitir tráfico entrante si es necesario.
