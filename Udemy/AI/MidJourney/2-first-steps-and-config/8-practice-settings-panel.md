# Práctica: panel de configuraciones

> Curso: Midjourney (Udemy)

## Objetivo

Practicar las funciones clave del panel de **Settings** de la web (ver [[6-web-settings-menu]]) y
observar cómo afectan el resultado final: **tamaño de imagen**, **estilización**, **rareza**,
**variedad**, **modelo/versión** y **velocidad**.

> Estas mismas configuraciones se pueden lograr con comandos (`--ar`, `--s`, `--w`, `--c`, `--v`), sin
> necesidad de usar el panel — los ejercicios de esta lección se hicieron desde los sliders/botones de
> la interfaz para practicar esa vía alternativa.

## Image Size

Prompt de ejemplo: un dragón (mismo prompt reutilizado con **Use**).

- **Square** (por defecto) → imagen cuadrada.
- **Landscape** llevado hasta `2:1` (extra ancho) → cambia la composición: se ve más cielo/entorno,
  menos protagonismo del sujeto respecto al fondo.
- **Portrait** → probado con un prompt de `una bailarina clásica en el escenario, fondo oscuro con
  luces cálidas`, ajustado hasta `2:3` para una imagen vertical.

Conclusión: el formato cambia qué tanto entorno/fondo entra en la composición, además de la
orientación general.

## Stylization (equivale a `--stylize`)

Prompt de ejemplo: `una bailarina clásica en el escenario, fondo oscuro con luces cálidas --ar 2:3`

- **Stylization alta** (~1000) → imagen más artística y estilizada.
- **Stylization baja** → imagen más realista y técnica.

Comparar ambos resultados con el mismo prompt permite identificar cuál se ve más técnico y cuál más
artístico.

## Weirdness (equivale a `--weird`)

Prompt de ejemplo: `un reloj derretido flotando en el desierto, estilo surrealista --ar 1:1`

- **Weirdness bajo** (0–300, ej. 100) → resultado más reconocible/realista.
- **Weirdness alto** (1500–2000+) → resultado mucho más abstracto y raro.

Comparar cuál parece real y cuál se vuelve completamente abstracto.

## Variety (equivale a `--chaos`)

Prompt de ejemplo: `un robot antiguo sentado en una biblioteca --ar 1:1`

- **Variety en 0** → las 4 imágenes generadas son muy parecidas entre sí.
- **Variety al máximo** → las 4 imágenes son completamente distintas (mezcla de estilos: realismo,
  cartoon, imágenes extrañas).

> ⚠️ Al hacer varias pruebas seguidas puede quedar activado sin querer el **modo Draft** (genera más
> rápido pero con menor calidad) — conviene revisar que el modo esté en **Standard** antes de comparar
> resultados.

## Version / Model

Se puede cambiar la versión del modelo tanto desde el panel de Settings como con el comando `--v`:

```text
--v <versión>
```

Ejemplo probado: `un bosque mágico con árboles flotantes y caminos de cristal, niebla matinal --v 5`
generó un resultado distinto al de la versión 7 (incluyó elementos como burbujas que no aparecen igual
en v7).

- Cambiar la versión desde el panel afecta a las siguientes generaciones hasta que se cambie de nuevo
  o se resetee.
- El comando `--v` permite fijar la versión para un prompt puntual sin tener que cambiar la
  configuración general del panel.

## Botón Reset

Después de experimentar con varias configuraciones (tamaño, estilización, rareza, variedad, versión),
se puede usar **Reset** para volver a los valores por defecto (Square, versión más reciente, Standard,
Fast).

## Conclusión

Practicar el panel de configuraciones permite dominar el flujo de trabajo visual en Midjourney,
ajustando no solo *qué* genera, sino *cómo* se interpreta, compone y estiliza la imagen. Cuantas más
pruebas se hagan, mayor control se logra sobre el resultado creativo.
