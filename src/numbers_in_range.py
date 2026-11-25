def numbers_in_range(sudoku):

    for row in sudoku:
        for number in row:
            if number > len(sudoku):
                return False
    else:
        return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert numbers_in_range(casosTest.correcto) == True
    assert numbers_in_range(casosTest.incorrecto_repeticion_fila) == True
    assert numbers_in_range(casosTest.incorrecto_repeticion_columna) == True
    assert numbers_in_range(casosTest.incorrecto_rango) == False
    assert numbers_in_range(casosTest.incorrecto__no_enteros) == True
    assert numbers_in_range(casosTest.incorrecto_flotantes) == True
    assert numbers_in_range(casosTest.incorrecto_longitud) == True
