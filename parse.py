from common import *


def parse_sudoku(sudoku):
    clauses = []
    sudoku = sudoku.replace("\n", "")
    sudoku = sudoku.split(" ")
    for i in range(COUNT):
        if sudoku[i] != "?":
            num = "{:0>{}}".format(bin(int(sudoku[i]) - 1)[2:], BITS)
            for j in range(BITS):
                if num[j] == "1":
                    clauses.append(f"{BITS * i + j + 1} 0")
                else:
                    clauses.append(f"-{BITS * i + j + 1} 0")
    return len(clauses), "\n".join(clauses)


def parse_output(values):
    values = [int(i) for i in values.split(" ")]
    bits = []
    for i in range(BITS * COUNT):
        bits.append(int(values[i] > 0))
    numbers = []
    for i in range(COUNT):
        binary = ""
        for j in range(BITS):
            binary += str(bits[BITS * i + j])
        numbers.append(int(binary, base=2))
    return numbers
