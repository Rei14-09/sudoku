def check_rows(sudoku):

    for row in sudoku:
        for number in row:
            if row.count(number) > 1:
                return False
    return True

if __name__ == "__main__":
