def is_squere(sudoku):

    if not sudoku:
        return False
    for fila in sudoku:
        assert isinstance(fila, list)

        if len(fila) != len(sudoku):
            return False
    else:
        return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert is_squere(casosTest.correcto) is True
    assert is_squere(casosTest.incorrecto_repeticion_fila) is True
    assert is_squere(casosTest.incorrecto_repeticion_columna) is True
    assert is_squere(casosTest.incorrecto_rango) is True
    assert is_squere(casosTest.incorrecto__no_enteros) is True
    assert is_squere(casosTest.incorrecto_flotantes) is True
    assert is_squere(casosTest.incorrecto_longitud) == False
