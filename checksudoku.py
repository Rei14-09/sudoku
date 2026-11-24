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

correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto_repeticion_fila = [[1, 2, 3, 4],[2, 3, 1, 3],[3, 1, 2, 3],[4, 4, 4, 4]]

incorrecto_repeticion_columna = [[1, 2, 3, 4],
            [2, 3, 1, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2]]

incorrecto_rango = [[1, 2, 3, 4, 5],
            [2, 3, 1, 5, 6],
            [4, 5, 2, 1, 3],
            [3, 4, 5, 2, 1],
            [5, 6, 4, 3, 2]]

incorrecto__no_enteros= [['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']]

incorrecto_flotantes = [[1, 1.5],
            [1.5, 1]]

incorrecto_longitud = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]]

def numbers_in_range(sudoku):

    for row in sudoku:
        for number in row:
            if number>len(sudoku):
                return False
    else:
        return True



def is_squere(sudoku):  

    if not sudoku:
        return False
    for fila in sudoku: 

        assert isinstance(fila, list)
        
        if len(fila) != len(sudoku):
            return False
    else:
        return True



def is_integrer(sudoku):
    for row in sudoku:
        for number in row:
            if not isinstance(number, int):
                return False
    return True
            


def check_rows(sudoku):

    for row in sudoku:
        for number in row:
            if row.count(number) > 1:
                return False
    return True



def check_colums(sudoku):

    primeraFila = sudoku[0]
    numeroDeFilas = len(sudoku) - 1

    for numero in primeraFila:

        indexFilaActual = 0

        while indexFilaActual < numeroDeFilas:

            indexFilaSiguiente = indexFilaActual + 1

            try:
                posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(numero)

            except ValueError:
                return False

            else:
            
                if posicionNumeroFilaSiguiente == primeraFila.index(numero):
                    return False
                else:
                    indexFilaActual += 1

    return True

def check_sudoku(sudoku):
    
    try:
        assert isinstance(sudoku,list) 

        return ( is_squere(sudoku)
            and is_integrer(sudoku)
            and numbers_in_range(sudoku)
            and check_rows(sudoku)
            and check_colums(sudoku)
    )
    except:
        return False




if __name__=='__main__':

    assert numbers_in_range(correcto)==True
    assert numbers_in_range(incorrecto_repeticion_fila)==True
    assert numbers_in_range(incorrecto_rango)==False

    assert is_squere(correcto)==True

    assert is_squere(incorrecto_repeticion_fila)==True

    assert is_squere(incorrecto_longitud)==False
    assert is_integrer(correcto)==True

    assert is_integrer(incorrecto_repeticion_fila)==True

    assert is_integrer(incorrecto_repeticion_fila)==True
    # >>> False

    assert check_rows(correcto)==True
    assert check_rows(incorrecto_repeticion_fila)==False
    assert check_rows(incorrecto_rango)==True

    assert check_colums(incorrecto_rango)==False
    # >>> False

    assert check_colums(correcto)==True
    # >>> True

    assert check_colums(incorrecto_repeticion_columna)==False
    # >>> False
    
    assert check_colums(incorrecto_rango)==False
    # >>> False

    assert check_sudoku(incorrecto_flotantes)==False
    # >>> False

    assert check_sudoku(correcto)==True
    # >>> True

    assert check_sudoku(incorrecto_repeticion_columna)==False
    # >>> False

    assert check_sudoku(incorrecto_rango)==False
    # >>> False

    assert check_sudoku(incorrecto__no_enteros)==False
    # >>> False

    assert check_sudoku(incorrecto_flotantes)==False
    # >>> False

    assert check_sudoku(incorrecto_longitud)==False
    # >>> False
