# Seguridad en VPC

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Security Groups

- Actúan como **cortafuegos virtuales** que controlan el tráfico **entrante y saliente** de las
  instancias, basándose en reglas.
- Una instancia puede tener **más de un** security group asociado.

> ⚠️ Si se envía una solicitud desde tu instancia, el tráfico de **respuesta** a esa solicitud se
> permite fluir de vuelta **independientemente de las reglas de entrada** del security group (los
> security groups son *stateful*).

## Network ACLs (NACLs)

- Proporcionan una **capa adicional de seguridad**, controlando el tráfico a **nivel de subred**.
- Pueden **bloquear o permitir** rangos de IP y protocolos específicos.

### Relación con las subredes

| Relación            | Cardinalidad                                             |
| ------------------- | -------------------------------------------------------- |
| Una subred → NACL   | 1 a 1 (una subred solo puede estar vinculada a una NACL) |
| Una NACL → subredes | 1 a N (una NACL puede estar vinculada a varias subredes) |
