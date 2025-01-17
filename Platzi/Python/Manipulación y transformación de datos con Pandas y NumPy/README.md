# Curso de Manipulación y Transformación de Datos con Pandas y NumPy  

En este curso aprenderás a trabajar con **NumPy**, una librería diseñada para cálculos numéricos y manejo de arrays, y **Pandas**, una herramienta poderosa para manipulación y análisis de datos. Ambas librerías son esenciales en el ecosistema de Python para la ciencia de datos.  

---

## Introducción a NumPy  

NumPy (Numerical Python) fue creada en **2005** y es una librería de código abierto alojada en GitHub.  

### **¿Por qué usar NumPy?**  
- **Velocidad**: NumPy está escrito en C y Fortran, lo que permite un manejo de datos rápido y eficiente en comparación con listas estándar de Python.  
- **Optimización de memoria**: Almacena datos en estructuras compactas y especializadas.  
- **Flexibilidad**: Permite manejar diversos tipos de datos (enteros, flotantes, booleanos, etc.).  
- **Versatilidad**: Base de muchas otras librerías científicas, utilizada para cálculos avanzados como redes neuronales, álgebra lineal, y procesamiento de imágenes.  

---

## Arrays en NumPy  

El array es la estructura central en NumPy. Representa datos de manera estructurada e indexada, permitiendo acceso rápido y eficiente a uno o varios elementos.  

**Crear un array en NumPy**:  
```python
import numpy as np

# Crear un array unidimensional
array_1d = np.array([1, 2, 3, 4])

# Crear un array bidimensional (matriz)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Crear un array con valores consecutivos
array_rango = np.arange(1, 10, 2)  # [1, 3, 5, 7, 9]
```

---

### **Indexing**  

El acceso a los elementos de un array en NumPy se realiza mediante **índices**.  

**Ejemplo de Indexing**:  
```python
# Crear un array bidimensional
array_2d = np.array([[10, 20, 30], [40, 50, 60]])

# Acceder a un elemento específico
elemento = array_2d[0, 1]  # Devuelve 20

# Acceder a una fila completa
fila = array_2d[1, :]  # Devuelve [40, 50, 60]

# Acceder a una columna completa
columna = array_2d[:, 2]  # Devuelve [30, 60]
```

---

## Dimensiones en NumPy  

Las dimensiones determinan la estructura de los datos en un array.  

1. **Escalar (dim=0)**: Un solo valor, como un número entero o flotante.  
2. **Vector (dim=1)**: Una lista de valores.  
3. **Matriz (dim=2)**: Una tabla de datos con filas y columnas.  
4. **Tensor (dim=n)**: Datos con más de dos dimensiones, como imágenes, videos o series de tiempo.  

**Ejemplos prácticos de dimensiones**:  
```python
# Escalar
escalar = np.array(5)  # Dimensión 0

# Vector
vector = np.array([1, 2, 3])  # Dimensión 1

# Matriz
matriz = np.array([[1, 2], [3, 4]])  # Dimensión 2

# Tensor
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Dimensión 3
```

---

### Método `squeeze` de NumPy  

El método `squeeze()` elimina las dimensiones de tamaño 1 en un array, permitiendo simplificar su estructura sin alterar los datos.  

**Ejemplo práctico del método `squeeze`**:  
```python
# Crear un array con una dimensión extra
array = np.array([[[1, 2, 3]]])  # Dimensión (1, 1, 3)

# Usar squeeze para eliminar las dimensiones de tamaño 1
array_squeezed = np.squeeze(array)  # Dimensión (3,)

print(array.shape)         # Resultado: (1, 1, 3)
print(array_squeezed.shape)  # Resultado: (3,)
```

## Métodos para Trabajar con Arrays en NumPy  

NumPy proporciona métodos potentes para inicializar, manipular y analizar arrays. A continuación, se describen algunos de los más utilizados:

---

### **1. Generación de Arrays Aleatorios**  

- **`randint`**: Genera números enteros aleatorios en un rango específico.  
- **`random`**: Genera números flotantes aleatorios entre 0 y 1.  

**Ejemplos prácticos**:  
```python
import numpy as np

# Generar un array de números enteros aleatorios
array_enteros = np.random.randint(1, 10, size=(3, 3))  # Matriz 3x3 con números del 1 al 9

# Generar un array de números flotantes aleatorios
array_flotantes = np.random.random((2, 4))  # Matriz 2x4 con valores entre 0 y 1

print("Enteros aleatorios:\n", array_enteros)
print("Flotantes aleatorios:\n", array_flotantes)
```

---

### **2. Inicialización con Ceros y Unos**  

- **`zeros`**: Crea un array lleno de ceros.  
- **`ones`**: Crea un array lleno de unos.  

**Ejemplos prácticos**:  
```python
# Crear un array de ceros
array_ceros = np.zeros((2, 3))  # Matriz 2x3 llena de ceros

# Crear un array de unos
array_unos = np.ones((4, 2))  # Matriz 4x2 llena de unos

print("Array de ceros:\n", array_ceros)
print("Array de unos:\n", array_unos)
```

---

## Shape y Reshape  

### **`shape`**  

El atributo **`shape`** describe las dimensiones del array, es decir, el número de filas y columnas.  

**Ejemplo**:  
```python
array = np.array([[1, 2, 3], [4, 5, 6]])  # Matriz 2x3

print("Dimensiones del array:", array.shape)  # Resultado: (2, 3)
```

---

### **`reshape`**  

El método **`reshape`** permite cambiar la forma (dimensiones) de un array sin alterar sus datos.  

**Ejemplo práctico de reshape**:  
```python
# Crear un array unidimensional
array_original = np.arange(1, 13)  # [1, 2, 3, ..., 12]

# Cambiarlo a una matriz 3x4
array_3x4 = array_original.reshape((3, 4))

# Cambiarlo a una matriz 2x6
array_2x6 = array_original.reshape((2, 6))

print("Array original:\n", array_original)
print("Array 3x4:\n", array_3x4)
print("Array 2x6:\n", array_2x6)
```

---

### **Notas sobre reshape**:  
- La cantidad total de elementos antes y después de usar `reshape` debe ser la misma.  
- Si no estás seguro del número exacto de una dimensión, puedes usar **`-1`** y NumPy calculará automáticamente el tamaño necesario para esa dimensión.  

**Ejemplo con `-1`**:  
```python
array = np.arange(1, 13)  # Array con 12 elementos

# Cambiar forma a una matriz con 4 filas y calcular automáticamente las columnas
array_auto = array.reshape((4, -1))  

print("Array con dimensión automática:\n", array_auto)
```


---

## Introducción a Pandas  

Pandas fue creada en **2008** como una herramienta de código abierto también alojada en GitHub.  

### **¿Por qué usar Pandas?**  
- **Rapidez**: Hereda la optimización de NumPy, lo que la hace eficiente en el manejo de grandes volúmenes de datos.  
- **Simplicidad**: Permite realizar operaciones complejas con pocas líneas de código.  
- **Formatos variados**: Soporta múltiples formatos de datos como CSV, Excel, JSON y bases de datos SQL.  
- **Alineación inteligente**: Realiza operaciones entre datos automáticamente alineando índices y columnas.  

**Ejemplo básico con Pandas**:  
```python
import pandas as pd

# Crear un DataFrame desde un diccionario
data = {'Nombre': ['Ana', 'Luis', 'María'],
        'Edad': [23, 34, 29],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}
df = pd.DataFrame(data)

print(df)
```


## Series y DataFrames en Pandas  

Pandas utiliza dos estructuras principales para manejar y analizar datos: **Series** y **DataFrames**. Estas estructuras se construyen sobre NumPy y añaden funcionalidades para trabajar con datos etiquetados y estructurados.  

---

### **1. Pandas Series**  

Una **Serie** es similar a un array unidimensional, pero con la ventaja de estar indexada, lo que permite asignar etiquetas a los datos.  

**Características principales de las Series**:  
- Similar a un **array unidimensional** en NumPy.  
- Los datos están indexados (el índice puede ser numérico o etiquetado).  
- Soporta operaciones aritméticas elemento por elemento.  
- Puede contener diferentes tipos de datos: enteros, flotantes, cadenas, etc.  

**Ejemplo básico con Series**:  
```python
import pandas as pd

# Crear una Serie a partir de una lista
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Acceso por índice
print("Elemento con índice 'b':", serie['b'])  # Resultado: 20

# Operaciones aritméticas
print("Serie multiplicada por 2:\n", serie * 2)

# Slicing
print("Slicing de la Serie:\n", serie['b':'d'])
```

**Salida esperada**:  
```
Elemento con índice 'b': 20
Serie multiplicada por 2:
a    20
b    40
c    60
d    80
dtype: int64
Slicing de la Serie:
b    20
c    30
d    40
dtype: int64
```

---

### **2. Pandas DataFrames**  

Un **DataFrame** es una estructura bidimensional que organiza los datos en filas y columnas, similar a una hoja de cálculo o una tabla en una base de datos.  

**Características principales de los DataFrames**:  
- Basado en **arrays de NumPy**, con soporte para índices y etiquetas.  
- Los datos están organizados en **filas** y **columnas**.  
- Cada columna puede tener un tipo de dato diferente (como en una tabla de base de datos).  
- Optimización de memoria y soporte para tamaños de datos variables.  
- Ofrece funcionalidades avanzadas para búsqueda, selección y transformación de datos.  

**Ejemplo básico con DataFrames**:  
```python
# Crear un DataFrame a partir de un diccionario
data = {'Nombre': ['Ana', 'Luis', 'María'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame:\n", df)

# Acceso a una columna
print("\nColumna 'Edad':\n", df['Edad'])

# Filtrar filas según una condición
print("\nFilas donde la edad es mayor de 30:\n", df[df['Edad'] > 30])
```

**Salida esperada**:  
```
DataFrame:
   Nombre  Edad     Ciudad
0    Ana    25     Madrid
1   Luis    30  Barcelona
2  María    35   Valencia

Columna 'Edad':
0    25
1    30
2    35
Name: Edad, dtype: int64

Filas donde la edad es mayor de 30:
  Nombre  Edad    Ciudad
2  María    35  Valencia
```

---

### **Diferencias entre Series y DataFrames**  

| **Característica**         | **Series**                         | **DataFrame**                              |
|----------------------------|------------------------------------|-------------------------------------------|
| **Dimensión**              | Unidimensional                    | Bidimensional                             |
| **Tipo de datos**          | Homogéneo                         | Heterogéneo (distinto por columna)        |
| **Indexación**             | Etiquetas o índices numéricos     | Índices en filas y columnas               |
| **Uso típico**             | Representar una sola columna o vector | Representar datos tabulares (filas y columnas) |

---

### **Operaciones comunes en DataFrames**  

1. **Selección de columnas**:  
```python
df['Nombre']  # Devuelve una Serie con la columna 'Nombre'
```

2. **Selección de filas por índice**:  
```python
df.loc[1]  # Devuelve la fila con índice 1
```

3. **Añadir una nueva columna**:  
```python
df['Salario'] = [2000, 2500, 3000]
```

4. **Eliminación de columnas**:  
```python
df.drop(columns=['Ciudad'], inplace=True)  # Elimina la columna 'Ciudad'
```
