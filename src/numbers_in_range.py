def numbers_in_range(sudoku):
    assert isinstance(sudoku, list)
    for row in sudoku:
        assert isinstance(row, list)
        for number in row:
            if number > len(sudoku):
                return False
    else:
        return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert numbers_in_range(casosTest.correcto) is True
    assert numbers_in_range(casosTest.incorrecto_repeticion_fila) is True
    assert numbers_in_range(casosTest.incorrecto_repeticion_columna) is True
    assert numbers_in_range(casosTest.incorrecto_rango) is False
    assert numbers_in_range(casosTest.incorrecto_flotantes) is True
