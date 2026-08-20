# Redshift Serverless

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Redshift ofrece dos tipos de clúster: **provisioned** (aprovisionado, tratado en otras partes del
curso) y **serverless**.

## El problema con el enfoque tradicional (provisioned)

Tradicionalmente había que **aprovisionar y gestionar** el clúster manualmente, con un tamaño y
capacidad **fijos** en cómputo y almacenamiento — independientemente de cuál fuera el uso real.

## Qué es Redshift Serverless

Con **Redshift Serverless**, AWS aprovisiona y gestiona el clúster **automáticamente** en función
de la carga de trabajo real:

- No es necesario gestionar el clúster ni aprovisionar nada manualmente.
- Escala automáticamente **hacia arriba** cuando hace falta y **hacia abajo** cuando no.
- Ayuda a **reducir costes**, ya que la facturación se basa en el **consumo real** — en función de
  las **unidades de procesamiento de datos (RPUs)** y el **almacenamiento** usados.

## Serverless vs. Provisioned

| Aspecto                       | Redshift Serverless                                                                | Redshift Provisioned                                                                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Aprovisionamiento             | Automático — el clúster no es visible ni configurable por el usuario.              | Manual — se elige el tipo de nodo y el número de nodos, lo que determina el rendimiento y la capacidad de almacenamiento.                    |
| Escalado                      | Automático, según la carga de trabajo (con posibles umbrales de control de coste). | Requiere habilitar manualmente **concurrency scaling** para añadir capacidad adicional ante ráfagas de carga — no está activado por defecto. |
| Puertos de conexión           | Solo se puede conectar desde los rangos **5431–5455** u **8191–8215**.             | Se puede elegir cualquier puerto para la conexión.                                                                                           |
| Redimensionamiento (resizing) | No aplica — no hay visibilidad ni control sobre los nodos aprovisionados.          | El clúster se puede redimensionar (añadir o quitar nodos) cuando sea necesario.                                                              |
| Cifrado                       | Siempre cifrado con **AWS KMS** (clave gestionada por AWS o por el cliente).       | Los datos pueden estar cifrados con KMS (clave gestionada por AWS o por el cliente) **o sin cifrar**.                                        |

> ⚠️ En Redshift Serverless, el cifrado con KMS es **obligatorio** — a diferencia de Provisioned,
> donde también es posible tener los datos sin cifrar.
>
> ⚠️ Con Provisioned, el escalado ante ráfagas de carga (**concurrency scaling**) es una función
> que hay que **habilitar explícitamente** — no ocurre de forma automática como en Serverless.
