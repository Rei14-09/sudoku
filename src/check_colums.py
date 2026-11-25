def check_colums(sudoku):
    assert isinstance(sudoku, list)
    for row in sudoku:
        assert isinstance(row, list)
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


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import casos_test.casos_test_sudoku as casosTest

    assert check_colums(casosTest.correcto) is True
    assert check_colums(casosTest.incorrecto_repeticion_columna) is False
    assert check_colums(casosTest.incorrecto__no_enteros) is True
    assert check_colums(casosTest.incorrecto_flotantes) is True
