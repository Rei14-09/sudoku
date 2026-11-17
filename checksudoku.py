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

incorrecto_repeticion_columnas = [[1, 2, 3, 4],
            [2, 3, 1, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
            [2, 3, 1, 5, 6],
            [4, 5, 2, 1, 3],
            [3, 4, 5, 2, 1],
            [5, 6, 4, 3, 2]]

incorrecto_letras= [['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']]

incorrecto_decimales = [[1, 1.5],
            [1.5, 1]]

incorrecto_repeticion_numeros = [[1, 0, 0, 0],
            [0, 1, 0],
            [0, 0, 0, 1]]


#def is_squere(sudoku):
 #   assert isinstance(sudoku,list)   

  #  if not sudoku:
   #     return False
    #for fila in sudoku: 

     #   assert isinstance(fila, list)
        
      #  if len(fila) != len(sudoku):
       #     return False
   # else:
    #    return True


#def numbers_in_range(sudoku):

 #   for row in sudoku:
  #      for number in row:
   #         if number>len(sudoku):
    #            return False
    #else:
     #   return True

def check_rows(sudoku):

    for row in sudoku:
        for number in row:
            if row.count(number) > 1:
                return False
    return True


#def check_sudoku(sudoku):





if __name__=='__main__':

    assert check_rows(correcto)==True
    assert check_rows(incorrecto_repeticion_fila)==False
    assert check_rows(incorrecto_repeticion_columnas)==True

    #assert numbers_in_range(correcto)==True
    #assert numbers_in_range(incorrecto_repeticion_fila)==True
    #assert numbers_in_range(incorrecto3)==False

    #assert is_squere(correcto)==True

    #assert is_squere(incorrecto_repeticion_fila)==True

    #assert is_squere(incorrecto_repeticion_numeros)==False

    #assert check_sudoku(incorrecto_repeticion_fila)==False
    # >>> False

    #assert check_sudoku(correcto)==True
    # >>> True

    #assert check_sudoku(incorrecto_repeticion_columnas)==False
    # >>> Falseincorrecto_

    #assert check_sudoku(incorrecto3)==False
    # >>> False

    #assert check_sudoku(incorrecto_letras)==False
    # >>> False

    #assert check_sudoku(incorrecto_decimales)==False
    # >>> False

    #assert check_sudoku(incorrecto_repeticion_numeros)==False
    # >>> False