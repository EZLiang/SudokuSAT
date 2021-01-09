def parse_sudoku(sudoku):
    clauses = []
    sudoku = sudoku.replace("\n", "")
    sudoku = list(sudoku)
    for i in range(81):
        if sudoku[i] != "?":
            num = "{:0>4}".format(bin(int(sudoku[i]) - 1)[2:])
            for j in range(4):
                if num[j] == "1":
                    clauses.append(f"{4 * i + j + 1} 0")
                else:
                    clauses.append(f"-{4 * i + j + 1} 0")
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
