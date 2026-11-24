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