# Programación de jobs de ETL (Scheduling)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Una vez desarrollado e implementado el proceso `ETL`, hay que programarlo para que se ejecute de forma
continua — extrayendo, transformando y cargando los datos — de modo que estén siempre tan actualizados
como se necesita en el `Data Warehouse`.

Los workflows y transformaciones se suelen empaquetar en **`jobs`** o **paquetes** (la terminología
exacta depende de la herramienta `ETL` usada), y son estos `jobs`/paquetes los que se programan para
ejecutarse en momentos concretos o con una frecuencia determinada.

## Dónde se puede programar la ejecución

- **Dentro de la propia herramienta ETL**: suele requerir una versión de pago/empresarial — por
  ejemplo, en `Pentaho` esto no está disponible en la versión `Community` (gratuita).
- **Con una herramienta externa**: si la programación no es posible dentro de la herramienta ETL (por
  ejemplo, por estar en una versión gratuita), se puede programar la ejecución con una herramienta
  externa que simplemente dispare (ejecute) el job — por ejemplo, el `Windows Scheduler` u otras
  herramientas similares.
- Es habitual, además, **desplegar esos jobs/paquetes en un servidor** dedicado específicamente a
  ejecutar los procesos `ETL`.

## Guías para decidir cómo programar el ETL

### 1. Partir de los requisitos del negocio

El punto de partida es hablar con los usuarios de negocio y preguntarles con qué frecuencia necesitan
que se actualicen los datos. El objetivo es cumplir esos requisitos tan bien como sea técnicamente
posible.

### 2. Contrastar con la realidad: cuánto tarda el ETL

Hay que comprobar cuánto tiempo tarda realmente el proceso `ETL` en ejecutarse — puede ser cuestión de
1, 5 o 10 minutos, o bien mucho más si hay grandes volúmenes de datos o transformaciones más
complejas.

> ⚠️ Si el negocio pide actualizaciones cada 30 minutos pero el `ETL` tarda una hora en completarse,
> hay un conflicto claro entre el requisito y la realidad técnica. En ese caso hay que llegar a un
> compromiso con el negocio, o buscar la forma de optimizar el `ETL` para acercarse al requisito.

### 3. Elegir un buen momento de ejecución

Además de la frecuencia, hay que decidir **cuándo** debe ejecutarse el `ETL`. El proceso de extracción
accede a los sistemas fuente, que suelen ser **sistemas productivos**, y el tiempo que el `ETL` pasa
leyendo datos de ellos puede afectarlos: puede ralentizarlos o incluso bloquearlos por completo si se
consumen demasiados recursos, impidiendo que realicen sus propias operaciones.

Para averiguar ese impacto, se pueden probar extracciones rápidas de prueba y discutir junto con las
personas responsables de esos sistemas fuente qué tan fuerte es el efecto real.

### Initial Load vs. Delta Load

El impacto sobre los sistemas productivos no es el mismo en todos los casos:

| Tipo de carga  | Impacto típico en sistemas fuente                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Initial Load` | Mucho más pesada y lenta — carga todos los datos históricos de una vez.                                                             |
| `Delta Load`   | Ligera — normalmente solo se leen brevemente los datos nuevos, así que el efecto suele ser manejable para los sistemas productivos. |

Aun así, conviene buscar un buen horario, especialmente para la `Initial Load`: de noche, en fin de
semana, o antes de las 6:00 AM suelen ser buenos momentos. Pero, como se mencionó, la decisión final
debe tomarse hablando con las personas responsables de los sistemas fuente y haciendo pruebas junto
con ellas.
