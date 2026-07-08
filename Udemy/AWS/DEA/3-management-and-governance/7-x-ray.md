# AWS X-Ray

## El problema: cómo se depura habitualmente

Proceso típico de depuración en producción:

1. Ejecutar tests localmente para ver si pasan.
2. Si hay un problema: añadir **logs, prints, visualizaciones** por todo el código para localizar dónde falla y qué valores tienen las variables.
3. Una vez encontrado el problema, solventarlo y **volver a desplegar** en producción.

### Dificultades de este enfoque

- La **estructura y formato de los logs** varía entre aplicaciones, lo que dificulta el análisis (incluso usando CloudWatch).
- Depurar un **monolito** es relativamente más sencillo que depurar una arquitectura de **microservicios**.
- Con microservicios distribuidos (ej. 10 microservicios en contenedores Docker), localizar un problema implica:
  - Revisar logs de cada microservicio por separado.
  - Cruzar información por **timestamp** para saber en qué momento se ejecutó cada parte.
  - No existe una **vista común** de toda la arquitectura.

## ¿Qué es AWS X-Ray?

Un servicio que permite **depurar de forma rápida y visual**, mostrando el **performance, ejecución y estado** de los distintos servicios utilizados mediante un **mapa de servicios**.

- El mapa de servicios se construye a partir de **segmentos y trazas** que X-Ray recoge.
- Al ser una visualización gráfica e intuitiva, también ayuda a **personas no técnicas** a entender y solucionar problemas más rápido.

## Ventajas principales

- Analizar **cuellos de botella** o errores de performance (ej. queries lentas).
- Comprender **dependencias** entre servicios en una arquitectura de microservicios.
- Localizar problemas en un servicio concreto.
- Revisar el **comportamiento de las peticiones**.
- Encontrar **errores**.
- Verificar si se cumple el **SLA de tiempo**.
- Identificar **dónde está el cuello de botella** exactamente.

## Integraciones

X-Ray se integra con múltiples servicios del ecosistema AWS, pudiendo desencadenar acciones posteriores a partir de situaciones detectadas (ej. un cuello de botella).

## Rastreo (Tracing)

- El **rastreo** es la forma integral de **seguir una petición** a través de todo el sistema.
- Cada componente que participa en procesar la petición añade su propio seguimiento.
- El conjunto de esta información forma las **trazas**, compuestas por **segmentos y subsegmentos**.
- Se pueden añadir **anotaciones** a las trazas para incluir información adicional de análisis.

### Opciones de muestreo (sampling)

- Rastrear **cada petición**.
- Rastrear una **muestra** de peticiones (ej. por porcentaje o tasa por minuto).

## Seguridad

- Autorización mediante **usuarios/roles IAM**.
- **Cifrado en reposo** mediante claves **KMS**.

## Cómo activar X-Ray — Flujo general

1. **Modificar el código** de la aplicación (Java, Python, Go, Node.js, .NET) importando el **SDK de AWS X-Ray**.
   - Requiere pocos cambios en el código.
   - El SDK captura automáticamente:
     - Llamadas a servicios de AWS
     - Peticiones HTTP/HTTPS
     - Llamadas a bases de datos (MySQL, PostgreSQL, DynamoDB, etc.)
     - Interacciones con colas **SQS**

2. **Instalar el daemon (demonio) de X-Ray**
   - Permite interceptar **paquetes UDP de bajo nivel**.
   - Envía la información recogida hacia AWS X-Ray.
   - Puede ejecutarse junto a otros servicios de AWS (Lambda, EC2, APIs, etc.).

3. **Configurar permisos IAM**
   - Necesarios para que la aplicación pueda **escribir datos en X-Ray**.

```text
Código de la app (SDK X-Ray)
        │
        ▼
Daemon de X-Ray (captura UDP)
        │
        ▼
AWS X-Ray (segmentos, trazas, mapa de servicios)
```

## Idea clave

AWS X-Ray resuelve el problema de depurar arquitecturas distribuidas (microservicios) al ofrecer una **visión unificada y visual** del recorrido de cada petición, en lugar de tener que cruzar logs manualmente entre múltiples servicios.
