# Características adicionales de VPC

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Repaso breve de algunas características adicionales de VPC que pueden ser relevantes.

## VPC Flow Logs

- Capturan información sobre el **tráfico IP** que entra y sale de las interfaces de red de la VPC.
- Útiles para:
  - **Solución de problemas** (troubleshooting).
  - **Análisis de seguridad**.
  - **Cumplimiento normativo** (compliance).

## Reachability Analyzer

- Permite analizar la **alcanzabilidad de red** entre recursos dentro de tu VPC y endpoints externos.

## Puertos efímeros (Ephemeral Ports)

- Puertos temporales que utilizan las aplicaciones cliente para las comunicaciones **salientes**.

## VPC Sharing

- Permite **compartir selectivamente** recursos de una VPC (subredes, tablas de rutas, security
  groups, NACLs) con otras cuentas de AWS dentro de tu **AWS Organization**.
