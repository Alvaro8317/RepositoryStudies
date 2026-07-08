# Agente de CloudWatch (EC2 y On-Premises)

## El problema: los logs no llegan a CloudWatch por defecto

Un caso muy común es querer **monitorizar instancias EC2** y registrar sus logs en CloudWatch. Sin embargo:

> ⚠️ **Por defecto, los logs de una instancia EC2 NO se envían a CloudWatch.**

Para conseguirlo es necesario:

1. **Instalar y ejecutar un agente de CloudWatch** en la instancia EC2 (o servidor) para enviar los logs deseados.
2. **Configurar permisos IAM** adecuados para que la instancia pueda comunicarse con CloudWatch.

## No solo aplica a EC2

Este agente también puede instalarse en **servidores on-premises** (en un centro de datos propio de la empresa), permitiendo enviar sus logs hacia CloudWatch Logs igualmente.

```text
Instancia EC2  ──► Agente de CloudWatch ──►
                                              CloudWatch Logs
Servidor On-Prem ──► Agente de CloudWatch ──►
```

## Dos versiones del agente

### 1. Agente de logs de CloudWatch (versión antigua)

- Solo permite **enviar logs** hacia CloudWatch Logs.
- Es la versión original/legacy del agente.

### 2. Agente unificado de CloudWatch (CloudWatch Unified Agent)

- Versión **más actualizada y completa**.
- Además de enviar logs, permite recoger **métricas adicionales a nivel de sistema**: RAM, CPU, procesos, y más.
- Estas métricas también pueden enviarse a CloudWatch, combinando en un mismo lugar **logs + métricas de sistema**.

| Agente                   | Logs | Métricas de sistema                 |
| ------------------------ | ---- | ----------------------------------- |
| Agente de logs (antiguo) | ✅    | ❌                                   |
| Agente unificado         | ✅    | ✅ (CPU, RAM, disco, procesos, etc.) |

## Métricas que puede extraer el agente unificado

- **CPU**
- **Disco** (métricas de uso/rendimiento)
- **RAM (memoria)**
- **NetStat:** número de conexiones TCP/UDP, paquetes, bytes
- **Procesos**
- **Espacio de intercambio (swap)**
- Y muchas más

> Nota: aunque CloudWatch es la opción nativa de AWS para esto, existen otras herramientas del mercado para extraer y visualizar métricas, como **Prometheus** y **Grafana**.

## Idea clave

Si ya se tienen instancias EC2 (o servidores on-premises) en ejecución, instalando el **agente unificado de CloudWatch** se obtiene visibilidad mucho más completa: no solo los logs de la aplicación, sino también métricas de sistema a bajo nivel, todo centralizado en CloudWatch.
