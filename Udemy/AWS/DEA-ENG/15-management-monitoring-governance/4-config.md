# AWS Config

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**AWS Config** ofrece **gestión centralizada de configuración**: permite valorar, auditar y
evaluar la configuración de los recursos de la cuenta, haciendo un seguimiento de todos los
**cambios de configuración** que se producen sobre ellos.

> ⚠️ AWS Config está **desactivado por defecto** — hay que habilitarlo explícitamente.

## Conceptos clave

| Concepto | Descripción |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Configuration item** (elemento de configuración) | Representación del **estado actual** de un recurso específico en un momento dado. Puede capturar metadatos: atributos del recurso, ajustes de configuración y relaciones con otros recursos. Se genera cada vez que se detecta un cambio en un recurso, mediante la **configuration recorder**. |
| **Configuration history** (historial) | Colección de los configuration items de un recurso durante un periodo determinado. Se almacena en un **bucket S3**. |
| **Configuration snapshot** (instantánea) | Captura el estado de **toda** la infraestructura de AWS en un momento específico. |
| **Configuration stream** (flujo) | Lista **actualizada automáticamente** de todos los configuration items de un recurso dado — cada cambio (creación, modificación, borrado) añade un nuevo elemento al flujo. |

## Config Rules

Las **reglas de Config** evalúan si un recurso cumple (*compliance*) con una configuración
deseada — por ejemplo, buenas prácticas de seguridad o normativas específicas.

### Resultados posibles de una evaluación

| Resultado | Significado |
| -------------------- | -------------------------------------------------------------------------------- |
| **Compliant** | El recurso cumple la regla. |
| **Non-compliant** | El recurso **no** cumple la regla. |
| **Error** | Alguno de los parámetros de la regla no es válido (ej. tipo o formato incorrecto). |
| **Not applicable** | La lógica de la regla no aplica a ese recurso en concreto. |

### Tipos de regla

| Tipo | Descripción |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Managed rules** (gestionadas) | Reglas predefinidas y personalizables, creadas por AWS. |
| **Custom rules** (personalizadas) | Creadas desde cero, mediante una función **Lambda** o mediante **Guard** (un lenguaje de política — *policy-as-code*). |

> Cada regla está siempre asociada a una **función Lambda** que comprueba la conformidad del
> recurso evaluado.

### Flujo de evaluación (ejemplo)

1. Cambia la configuración de un recurso (ej. una instancia EC2).
2. Se activa automáticamente la evaluación de la regla correspondiente.
3. La función Lambda asociada a la regla comprueba la conformidad.
4. Si el recurso incumple la regla, se marca como **non-compliant** y el cambio se registra en un
   bucket S3.

### Cuándo se dispara una evaluación

- Ante un **cambio en la configuración** del recurso.
- De forma **periódica**, según un intervalo definido.
- Una **combinación** de ambos: por cambio y por periodo.

### Modos de evaluación

| Modo | Momento de la evaluación |
| ------------------- | ------------------------------------------------------------- |
| **Proactive** | El recurso se evalúa **antes** de ser desplegado (durante el aprovisionamiento). |
| **Detective** | El recurso se evalúa **justo después** de haber sido desplegado. |
