# Define a procedure,check_colums,
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

incorrecto_repeticion_numeros = [[1, 2, 3, 4],[2, 3, 1, 3],[3, 1, 2, 3],[4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
            [2, 3, 1, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
            [2, 3, 1, 5, 6],
            [4, 5, 2, 1, 3],
            [3, 4, 5, 2, 1],
            [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
            [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
            [0, 1, 0],
            [0, 0, 0, 1]]



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




if __name__=='__main__':

    assert check_colums(incorrecto_repeticion_numeros)==False
    # >>> False

    assert check_colums(correcto)==True
    # >>> True

    assert check_colums(incorrecto2)==False
    # >>> False
    
    assert check_colums(incorrecto3)==False
    # >>> False