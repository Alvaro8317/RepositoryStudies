# Introducción a Python

## Características de los lenguajes de programación

Existen diversas generaciones para los lenguajes de programación como:

1. Lenguajes de primera generación -> Los más dependientes del hardware de donde se ejecuten, usan el código maquina (
   basado en código binario)
2. Lenguajes de segunda generación -> Se denominan de **bajo nivel**, no son menos potentes que los de alto nivel, solo
   que requieren tener un mayor control al programar y conocer bien el hardware en el que se ejecutará el código, aquí
   entran lenguajes como assembler
3. Lenguajes de tercera generación .> Añaden una capa de abstracción frende a los de segunda, añaden estructuras de
   datos, variables complejas y estos se les conocen como **alto nivel**, aquí entran lenguajes como C, Fortran, C++,
   Java, etc.
4. Lenguajes de cuarta generación -> Son lenguajes que tienen parecido al lenguaje humano, usados para programar bases
   de datos u otros sistemas. Aquí entran lenguajes como Perl, Ruby, PHO, SQL y otros.
5. Lenguajes de quinta generación, son lenguajes que disponen de herramientas visuales para su desarrollo o lenguajes de
   inteligencia artificial, aquí entran Prolog o Mercury

## Paradigmas

Un paradigma es una teoría o conjunto de teorías aceptado por los integrantes que usan el paradigma, un paradigma de
programación indica el método y la forma en la que se deben de estructurar y organizar las tareas a programar. ***Python
implementa múltiples paradigmas***

### Paradigma imperativo

Compuesto por instrucciones secuenciales para formar algoritmos. Es el más utilizado, es como una guía paso a paso.

### Paradigma procedural

Es un derivado del imperativo, pero añade la creación de procedimientos o funciones permitiendo estár organizado y
modularizado en funciones especificas.

### Paradigma orientado a objetos

Uno de los más populares junto con el imperativo y se basa en encapsular las entidades principales del programa en
objetos. Es útil puesto que favorece mucho la modularidad, encapsulamiento, reusabilidad y escalabilidad.

### Paradigma funcional

Se basa en funciones matemáticas que se centran en los cambios de estado del programa por medio de la mutación de
variables. Tiene su origen en el calculo lambda y presenta características como recursividad, uso de funciones de orden
superior y el uso de las funciones puras. Python no permite implementar este paradigma al 100% pero otros si lo son como
Haskell o Miranda.

## Tipado

Dependiendo del tipado del lenguaje, el compilador o intérprete permite configurar en la ejecución del código cuanta
memoria se reservará por cada variable y donde colocarla. Python presenta un típado dinámico, es decir, el tipo de
variable se asigna en tiempo de ejecución y no de compilación. Esto permite una mayor agilidad al programar pero puede
dar algunos problemas.
**Python es un lenguaje fuertemente tipado**, es decir, una vez definido el tipo de dato de una variable, esta siempre
actuará conforme a su tipo. Ejemplo, el cáracter 1 + el número 1, en JS podría dar 2 porque infiere el tipo de dato,
python por otro lado no, dará una excepción.

## Características de python

Python es un lenguaje de alto nivel, propósito general, multiparadigma, principalmente imperativo, orientado a objetos y
funcional. De tipado dinámico y fuertemente tipado. Presenta una sintaxis sencilla, simple y clara. Posee un sistema de
recolección de basura que permite que el desarrollador se despreocupe de la gestión de memoria y que el lenguaje se
pueda centrar en otros aspectos de alto nivel. Cuando un código python hacxe uso de las buenas prácticas, se denomina
código pythónico y suele ser una señal de excelencia. Python es un lenguaje interpretado, significa que no necesita
compilar los programas cada vez que se hace un cabio en el código y así, no depende del hardware en el que se ejecuta,
ayuda a que el lenguaje sea multiplataforma gracias al uso de su máquina virtual. Además, es posible ejecutar código
python ejecutando código C, C++, Java o .Net.

### Puntos debiles

Al ser un lenguaje interpretado, puede considerarse un lenguaje lento en comparación con los compilados, ya que no posee
un compilador JIT (just-in-time). Aún así, python 3 ha hecho mejoras de rendimiento y existe Numba que es una librería
que permite marcar porciones de código para ser compiladas en tiempos de ejecución usando un JIT o CPython, que permite
escribir código C compatible con python e integrarlo de manera natural para mejorar la velocidad de procesamiento. En
otras situaciones, se usa **Pandas** que se escribió en un lenguaje compilado y permite el uso de operaciones numéricas
y cientificas de forma muy eficiente; Esta librería está escrita en C en su mayoría pero esto es transparente para el
desarrollador python

## Ambitos de uso en python

Python puede ser utilizado en:

1. Programación a nivel de SO -> Scripts o programas completos que interactuan con el sistema operativo
2. Aplicaciones con interfaz de usuario -> Hace uso de la librería argparse y click. Además, existe tkinter o para más
   avanzadas aplicaciones, se puede usar GTK con PyGTK o PyQT. Para la creación de CLIs se puede usar ncurses o urwid.
3. Aplicaciones web e interacción con servicios web -> Permite aplicaciones web desde paginas web estáticas con Pelican
   hasta juegos usando PyJamas, esta convierte código Python a JS. También existe Django que es un framework de
   propósito general, este es muy usado por su extensa funcionalidad, cuenta con su propio ORM, sistema de migraciones
   de datos, autenticación, enrutador de URL, motores de renderizado. Además, existe microframeworks para cosas muy
   especificas como Flask o Pyramid. Finalmente, existen los frameworks diseñados para usi especifico como
   optimizaciones, aquí se destaca Falcon o Starlette, del cuál FastAPI está basado.
4. Interacción con servicios de internet -> Uso de API's o uso de FTP para compartir archivos a través de internet,
   Python cuenta con ftplib. Además, soporta uso de smtplib y email para envío de correos nativo de python.
5. Gestion de contenido -> Aquí se pueden destacar los CMS (Content management system) para gestionar contenido como
   páginas web, blogs,
   subscripciones, emails, etc. Aquí puede destacar Django-CMS. Este framework permite la extensibilidad de funciones de
   Django y es usado por la NASA, Canonical o National Geographic. Por otro lado de los CMS, destacan los ERP (
   Enterprise resources planning) que son aplicaciones que ayudan a la gestión de empresas en sus diferentes areas como
   contabilidad, facturación, inventario, pedidos, relación con clientes, etc. De los más poplares está Odoo. Cuenta con
   varios modulos diferentes como CRM, creador de sitios web, creador de comercios en línea, entre otros.
6. Aplicaciones científicas y manejo de datos -> Para el manejo de cdatos está NumPy y Pandas, estas permiten manipular
   grandes cantidades de datos y hacer operaciones masivas sobre las mismas. Numpy está orientado a operar de forma
   altamente eficiente con vectores N dimensionales y cuenta con integración con código C++ y Fortran. Pandas en cambio,
   tiene un enfoque de operaciones altamente eficientes sobre conjuntos de datos grandes de varias dimensiones. Ambas
   librerías forman parte del proyecto SciPy. Además cuenta con librerias como matplotlib para visualizaciones de datos,
   luego va Seaborn que añade visualizaciones más orientadas a la estadística a comparación con matplotlib. Finalmente
   está Bokeh que permite mostrar gráficos tanto en dos dimensiones como en tres dimensiones y hacerlos interactivos con
   el usuario. Para evitar hacer uso de múltiples instalaciones en un entorno virtual, existe la distribución científica
   aAnaconda que gracias a sus herramientas añadidas, comprende desde Jupyter Notebook hasta visualizado de datos.
   Además, cuenta conherramientas de inteligencia artificial como Scikit-Learn o TensorFlow y gestiona las dependencias
   con Conda.
7. Inteligencia artificial -> Usado principalmente para big-data, inteligencia artificial general y deep learning. Para
   el deep learning existe TensorFlow, CNTK o Theano que son herramientas para analizar datos expresados de forma
   matricial o tensorial mediante capas de redes neuronales, no obstante, se puede hacer uso de cualquiera de estas 3
   usando Keras, ya que esta tiene la integración y utilización de cualquiera de las tres herramientas de forma fácil.

## Python enhancement proposals (PEP)

Estas son propuestas que fomentan la mejora del lenguaje python, hay de 3 tipos:

1. Propuesta estándar -> Una funcionalidad o implementación
2. Propuesta informacional -> Describe un problema de diseño pero no propione ninguna nueva funcionalidad.
3. Propuestas de proceso -> SImilares a las estándar pero enfocadas a áreas diferentes del lenguaje en sí.

Una de las propuestas más relevantes es pep-8, que es la guía de estilos donde se propone como escribir el código más
pythónico posible donde se puede destacar lo siguiente:

1. Indentación, usar 4 espacios es mejor que usar tabulaciones aunque puede prevalecer la tabulación cuando ya se usa de
   manera predominante.
2. Longitud de líneas, la máxima recomendada es de 79 caracteres para el código y 72 para comentarios / documentación.
   Para los equipos de desarrollo que quieran extenderse, se puede llegar hasta un límite de 99 caracteres para el
   código y prevalecen los 72 para documentación y comentarios. Cuando la longitud de una línea sea mayor que la
   cantidad máxima predefinida, se utiliza el caracter "\" para hacer un salto de línea
3. Espacios, saltos de línea y líneas en blanco, en python se recomienda evitar cualquier tipo de espacio añadido que
   parezca exagerado; Los saltos de línea se añaden antes que los operadores lógicos y deben estar alineados al mismo
   nivel y las líneas en blanco deben de tener en cuenta lo siguiente: Las funciones generales o clases deben de estar
   rodeadas de dos líneas en blanco, los métodos definidos dentro de clases se rodean de una sola línea en blanco, se
   pueden usar líneas en blanco de forma moderada entre bloques de funciones o entre secciones lígicas y algunos
   editores de texto reconocen el CTRL + L como separador de página, por tanto, puede ser usado para separar las partes
   de código. Ejemplo:

```python
# Mal
def foo(var1, var2):
    bruto = 1
    interes = 1
    alquiler = 1
    Beneficio = (bruto +
                 interes +
                 alquiler)
    print("Bar")


# Bien
def foo(var1, var2):
    bruto = 1
    interes = 1
    alquiler = 1
    Beneficio = (bruto
                 + interes
                 + alquiler)
    print("Bar")
```

4. Otros consejos generales es hacer uso de las herramientas del lenguaje para comparaciones de objetos verdaderos o
   falsos, un claro ejemplo es que la siguiente expresión: `if len(1) > 0` no es tan recomendable como lo sería `if l`.
   La forma correcta de comprobar si una variable tiene un valor de True, False o None es con el operador is o is not,
   ejemplo: `if a is not b | if coche is None`. Finalmente, la importación se hará al principio de cada fichero y el
   orden es 1. Modulos de la librería estándar 2. Modulos de terceros 3. Módulos propios. Esto manteniendo un orden
   alfabético dentro de cada sección.
5. Comentarios y documentación, es mejor no tener comentarios que tener comentarios que contradigan el código, los
   comentarios deben de estar compuestos de una o varias frases completas terminando con un punto al final y comensar
   con mayúsculas a no ser que comiencen con un identificador que esté en minúscula. Procurar escribir el código en
   inglés, los bloques de comentarios afectan al código que está indentado al mismo nivel y entre párrafo y párrafo
   habrá que añadir dos líneas en blanco. Los comentarios de una sóla línea deberán usarse de forma moderada, la
   documentación o docstring se hará con triple comilla doble y los módulos públicos, funciones, clases y métodos deben
   tener un docstring. Solo los métodos privados puede no tenerlo, aunque deben tener un comentario junto después de la
   definición de la cabecera del mismo.
6. Convención de nombres, pep8 define que si un proyecto ya tiene una convención de nombres establecida, se mantendrá
   para no romper la consistencia del proyecto. Para definir que un objeto está protegido, se añade un carácter "_" como
   prefijo del nombre ya que usando una importación con * omite los nombres escritos con _ al principio. Los nombres que
   terminan con _ se usan para evitar conflictos con palabras reservadas como class, def, if, etc. Cuando un nombre
   comienza por __ indica que el compilador lo cambiará internamente por <clase>__<nombre> lo que se conoce como Python
   mangling rules y evita colisiones de nombres. Si el nombre de la función comienza y termina con doble __ significa
   que es un **método mágico** y se recomienda que no se inventen nuevos nombres, sino que se usen los disponibles en la
   documentación. Para nombrar módulos se hará uso de snake_case intentando que sean los más cortos posibles. En cambio,
   para los **nombres y tipos de clases se harán con UpperCamelCase**. El primer parámetro para los métodos de
   instancias y para los métodos de clase serán self y cls respectivamente y para los nombres de las funciones será con
   snake_case, con prefijo de un _ si la función es local al módulo y prefijado con dos __ para evitar colisiones con la
   herencia al hacer uso de las python mangling rules. Finalmente, para las constantes se hará uso de las mayúsculas o
   de SCREAMING_SNAKE_CASE.

Existen dos herramientas que sirven para comprobar que el código cumple con pep8 y son ``pylint`` con ``pycodestyle``.

## Zen de python

Es una lista de 20 reglas (19 en realidad) escritas por Tim Peters que todo pythonista debería seguir, para listarla se
puede ir a la documentación de pep-20 o ejecutar ``import this`` desde una terminal interactiva de python.

## Python2 vs Python3

En el año 2020 se dejó de dar mantenimiento de seguridad y salió la última versión de python2, por lo que todos los
nuevos proyectos deben de hacerse en python 3.

### Diferencias entre python 3 y python 2

#### str, bytes y Unicode

De las principales diferencias es como se categorizan las cadenas de caracteres binarias y caracteres unicode, en py3
existen dos representanciones diferentes: bytes y str, los objetos tipo bytes representan cadenas binarias de 8bits y
los tipo str contienen caracteres unicode. No obstante, en py2 la categorización era diferente, existían str y unicode
como tipos de cadenas de caracteres y str incluía las cadenas ASCII y binarias de 8 bits. Unicode tenía los caracteres
unicode. En resumen, py3 unifica unicode y ASCII bajo el tipo de dato str, mientras que py2 tiene unicode y cadenas (
tanto binarias como ascii) separadas en dos tipos.

#### Comparaciones de tipos no ordenables

En py2 es posible comparar diferentes tipos de datos como listas o tuplas, en py3 no es posible, de caso de intentarlo,
arrojará la excepción TypeError.

#### Operaciones númericas diferentes

En py2 las divisiones por defecto daban como resultado enteros y se hacen unos cambios en los redondeos con round para
evitar menor margen de error.

#### Iteradores por defecto

Se devuelven objetos iteradores con el fin de mejorar el rendimiento en funciones como map, filter, zip o range.

#### print

En py2 se utilizaba como palabra reservada y se usaba así: ``print 'hola mundo'`` pero en py3 print es una función
normal, extendiendo su uso como para poder escribir sobre un archivo con el parámetro file,
ejemplo: `print("Hola mundo", file=f)`. No obstante, entre py2 y py3 se cambiaron muchísimas funciones.

#### Migrar de python 2 a python3

Existe la herramienta 2to3 en la documentación oficial de python, pero no es una herramienta perfecta por lo que se
recomienda escribir un set de pruebas sobre la aplicación escrita en 2, usar la herramienta y ejecutar el set de pruebas
en 3.

## Pip

Python cuenta con un gestionador de paquetes incluido desde python3.4 en el que descarga las librerías externas de
PyPI (Python Package Index), este cuenta con múltiples funcionalidades como busqueda de paquetes, mostrar información
sobre ellos, instalar, desinstalar, listar, etc.
Nota, hay algunos comandos que ya no soporta pip como pip search, para eso se recomienda ver
la [documentación de los métodos deprecados](https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods)
Ejemplo:

````shell
# Deprecated
pip search xmltodict

# Instala
pip install xmltodict

# Desinstala
pip unistall xmltodict

# Actualiza
pip --upgrade xmltodict

# Muestra la información de la librería ya instalada
pip show xmltodict

# Muestra requerimientos dañados o no coherentes
pip check

# Instala en base a una URL
pip install --index-url https://www.google.com
````

## Intérprete de python

Python al ser interpretado, significa que no necesita compilar el código máquina al hardware, sino que se ejecuta
directamente desde la máquina virtual de python. Cuando se instala python en una máquina, minimo se instala el
intérprete y la librería estándar de python. Dependiendo del intérprete, pudo haber sido escrito en C, Java, .Net, etc.
El intérprete se podría definir como un programa que se encarga de ejecutar otros programas.

### Estrúctura del intérprete de python

Por un lado está el código fuente que se compone de ficheros de texto plano que tienen una gramática especifica y por el
otro se encuentran los ficheros de byte code, estos son el resultado de una compilación rápida que se efectua justo
antes de comenzar la ejecución. El código escrito en byte code está listo para ser ejecutado en cualquier máquina
virtual de python. Por último, se encuentra la máquina virtual de python (PVM) que es encargada de ejecutar los ficheros
que tienen el byte code en la máquina. Por ende, esta si depende del hardware utilizado en la maquina virtual. **Lo que
se denomina intérprete de python es el programa completo que analiza el código fuente, genera los ficheros compilados y
ejecuta el código usando la PVM.
Código fuente python -> Compilador -> Byte code -> Maquina virtual de python
Los ficheros que tienen el byte code tienen una extensión .pyc. No es necesaria su creación, si por X o Y razón no
pueden crearse, se pueden insertar directamente en memoria. No se puede generar el código fuente desde los .pyc.

Cuando se lanza un proceso de compilación se puede:

- Evitar que se generen los .pyc
- Ejecutar módulos directamente
- Se puede pasar el programa como una cadena de caracteres
- Ajustar la cantidad de warnings emitidos por el intérprete
- Utilizar la optimización del código eliminando los asserts y los docstrings
  Si se quisiera crear los archivos compilados, se debe de ejecutar:

````shell
python -OO -m compileall /ficheros
````

### Implementaciones de python

Cuando se habla de implementaciones, usualmente se refiere a CPython, esta implementación del intérprete es la que
permite ejecutar librerías como pandas o numpy que fueron escritas en su mayoría en C, pero existen otras
implementaciones:

1. CPython, es el estándar, soporta interoperabilidad con librerías escritas en C y normalmente es muy rápida en tiempos
   de ejecución comparándose con las demás implementaciones.
2. Jython, implementación con Java, la principal ventaja es que permite ejecutarse junto a código Java, permite importar
   librerías python a Java y viceversa.
3. PyPy, solución a la lentitud de CPython implementando un JIT (Just in time compiler), manteniendo así el carácter
   interpretado e interactivo. También PyPy cuenta con stackless mode, permite desacoplar el código a la hora de
   ejecutarse, permitiendo generar minihilos de ejecucicón para conseguir una concurrencia de código masiva. PyPy
   implementa RPython que es una versión más reducida de python y por ende, no tiene total soporte de las librerías,
   aunque si cuenta con soporte para Django o Twisted.
4. IronPython, basada en C# y .NET
