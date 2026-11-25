def check_rows(sudoku):
    assert isinstance(sudoku, list)
    for row in sudoku:
        assert isinstance(row, list)
        for number in row:
            if row.count(number) > 1:
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert check_rows(casosTest.correcto) is True
    assert check_rows(casosTest.incorrecto_repeticion_fila) is False
    assert check_rows(casosTest.incorrecto_repeticion_columna) is True
    assert check_rows(casosTest.incorrecto_rango) is True
    assert check_rows(casosTest.incorrecto__no_enteros) is True
    assert check_rows(casosTest.incorrecto_flotantes) is True
