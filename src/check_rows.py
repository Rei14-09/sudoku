def check_rows(sudoku):

    for row in sudoku:
        for number in row:
            if row.count(number) > 1:
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert check_rows(casosTest.correcto) == True
    assert check_rows(casosTest.incorrecto_repeticion_fila) == False
    assert check_rows(casosTest.incorrecto_repeticion_columna) == True
    assert check_rows(casosTest.incorrecto_rango) == True
    assert check_rows(casosTest.incorrecto__no_enteros) == True
    assert check_rows(casosTest.incorrecto_flotantes) == True
    
