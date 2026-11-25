# Sudoku

Proyecto en Python que comprueba si una matriz cuadrada representa una solución válida de Sudoku.

## Qué hace

La función `check_sudoku()` recibe una matriz de números y devuelve:

- `True` si todas las filas y columnas contienen exactamente una vez los números del `1` al tamaño de la matriz.
- `False` si la matriz no es cuadrada, contiene valores no enteros o repetidos, o tiene números fuera del rango permitido.

Ejemplo:

```python
from src.check_sudoku import check_sudoku

sudoku = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

print(check_sudoku(sudoku))  # True
```

## Requisitos mínimos según la implementación

### Python

Se necesita Python 3 para ejecutar el proyecto.

### Formato de entrada

La entrada debe ser una lista de Python que contiene las filas de la matriz:

```python
[[1, 2, 3], [2, 3, 1], [3, 1, 2]]
```

- `check_sudoku()` rechaza cualquier entrada que no sea una lista.
- La matriz no puede estar vacía.
- Cada fila debe ser una lista.
- La matriz debe ser cuadrada: el número de filas debe ser igual al número de columnas.

### Tipo y rango de los valores

- Todos los valores deben ser números enteros.
- No se permiten textos, decimales u otros tipos.
- En una matriz de tamaño `n`, los valores deben estar entre `1` y `n`.

Por ejemplo, una matriz de `3 x 3` solo puede contener los números `1`, `2` y `3`.

### Filas y columnas

- Cada fila debe contener todos los valores permitidos sin repetirlos.
- Cada columna debe contener todos los valores permitidos sin repetirlos.

Las validaciones correspondientes están repartidas en las funciones `check_rows()` y `check_colums()`.

## Limitación actual

El proyecto **no implementa la comprobación de los bloques o regiones** que también puede requerir un Sudoku tradicional de `3 x 3`. Actualmente comprueba la estructura cuadrada, el tipo de los datos, el rango, las filas y las columnas.

## Dependencias

No se necesitan paquetes externos. El proyecto utiliza únicamente módulos propios y la biblioteca estándar de Python.