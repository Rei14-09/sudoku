def is_integrer(sudoku):
    for row in sudoku:
        for number in row:
            if not isinstance(number, int):
                return False
    return True

if __name__ == "__main__":
    