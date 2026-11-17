# Define a procedure, is_integrer,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto_repeticion_fila = [[1, 2, 3, 4],[2, 3, 1, 3],[3, 1, 2, 3],[4, 4, 4, 4]]

incorrecto_repeticion_columna = [[1, 2, 3, 4],
            [2, 3, 1, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2]]

incorrecto_numero_erroneo = [[1, 2, 3, 4, 5],
            [2, 3, 1, 5, 6],
            [4, 5, 2, 1, 3],
            [3, 4, 5, 2, 1],
            [5, 6, 4, 3, 2]]

incorrecto_letras = [['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']]

incorrecto_decimal = [[1, 1.5],
            [1.5, 1]]

incorrecto_longitud_erronea = [[1, 0, 0, 0],
            [0, 1, 0],
            [0, 0, 0, 1]]


def is_integrer(sudoku):
    for row in sudoku:
        for number in row:
            if not isinstance(number, int):
                return False
    return True





if __name__=='__main__':

    assert is_integrer(correcto)==True

    assert is_integrer(incorrecto_repeticion_fila)==True

    assert is_integrer(incorrecto_repeticion_fila)==True
    # >>> False

    assert is_integrer(incorrecto_repeticion_columna)==True
    # >>> False

    assert is_integrer(incorrecto_numero_erroneo)==True
    # >>> False

    assert is_integrer(incorrecto_letras)==False
    # >>> False

    assert is_integrer(incorrecto_decimal)==False
    # >>> False

    assert is_integrer(incorrecto_longitud_erronea)==True
    # >>> False