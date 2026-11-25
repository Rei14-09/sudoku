def is_integrer(sudoku):
    for row in sudoku:
        for number in row:
            if not isinstance(number, int):
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert is_integrer(casosTest.correcto) == True
    assert is_integrer(casosTest.incorrecto_repeticion_fila) == True
    assert is_integrer(casosTest.incorrecto_repeticion_columna) == True
    assert is_integrer(casosTest.incorrecto_rango) == True
    assert is_integrer(casosTest.incorrecto__no_enteros) == False
    assert is_integrer(casosTest.incorrecto_flotantes) == False
    assert is_integrer(casosTest.incorrecto_longitud) == True
