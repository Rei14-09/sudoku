def is_integrer(sudoku):
    assert isinstance(sudoku, list)
    for row in sudoku:
        assert isinstance(row, list)
        for number in row:
            if not isinstance(number, int):
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert is_integrer(casosTest.correcto) is True
    assert is_integrer(casosTest.incorrecto_repeticion_fila) is True
    assert is_integrer(casosTest.incorrecto_repeticion_columna) is True
    assert is_integrer(casosTest.incorrecto_rango) is True
    assert is_integrer(casosTest.incorrecto__no_enteros) is False
    assert is_integrer(casosTest.incorrecto_flotantes) is False
    assert is_integrer(casosTest.incorrecto_longitud) is True
