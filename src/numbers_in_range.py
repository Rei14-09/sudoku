def numbers_in_range(sudoku):

    for row in sudoku:
        for number in row:
            if number>len(sudoku):
                return False
    else:
        return True


if __name__ == "__main__":
