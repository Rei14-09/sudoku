# Define a procedure, check_sudoku,
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

import sys

sys.path.append("..")

from src.is_square import is_squere
from src.is_integer import is_integrer
from src.numbers_in_range import numbers_in_range
from src.check_rows import check_rows
from src.check_colums import check_colums


def check_sudoku(sudoku):

    try:
        assert isinstance(sudoku, list)

        return (
            is_squere(sudoku)
            and is_integrer(sudoku)
            and numbers_in_range(sudoku)
            and check_rows(sudoku)
            and check_colums(sudoku)
        )
    except:
        return False


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert check_sudoku(casosTest.correcto) == True
    assert check_sudoku(casosTest.incorrecto_repeticion_fila) == False
    assert check_sudoku(casosTest.incorrecto_repeticion_columna) == False
    assert check_sudoku(casosTest.incorrecto_rango) == False
    assert check_sudoku(casosTest.incorrecto__no_enteros) == False
    assert check_sudoku(casosTest.incorrecto_flotantes) == False
    assert check_sudoku(casosTest.incorrecto_longitud) == False
