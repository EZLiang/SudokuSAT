def parse_sudoku(sudoku):
    clauses = []
    sudoku = sudoku.splitlines()
    sudoku = [list(i) for i in sudoku]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != "?":
                num = bin(int(sudoku[i][j]) - 1)[2:]
                idx = 9 * i + j
                for k in range(4):
                    if num[k] == 1:
                        clauses.append(f"{4 * idx + k + 1} 0")
                    else:
                        clauses.append(f"-{4 * idx + k + 1} 0")
    return len(clauses), "\n".join(clauses)


def parse_output(values):
    values = [int(i) for i in values.split(" ")]
    bits = []
    for i in range(324):
        bits.append(int(values[i] > 0))
    numbers = []
    for i in range(81):
        numbers.append(int(f"{bits[4 * i]}{bits[4 * i + 1]}{bits[4 * i + 2]}{bits[4 * i + 3]}", base=2) + 1)
    return numbers
