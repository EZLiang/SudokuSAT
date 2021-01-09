import subprocess
import sys
import parse
from common import *

f = open("sudoku.in", "w")  # where the sudoku clauses will be written to
with open("sudoku.txt") as h:
    SUDOKU_CLAUSES = h.read() # read in the provided clauses
CLAUSES = len(SUDOKU_CLAUSES.splitlines()) - 1

# get the sudoku, either through file of stdin
if len(sys.argv) == 2:
    with open(sys.argv[1]) as h:
        sudoku = h.read()
else:
    print("--- Begin Sudoku ---")
    sudoku = ""
    for i in range(LENGTH):
        sudoku += input().strip() + "\n"
    print("--- End Sudoku ---")

n_clauses, clauses = parse.parse_sudoku(sudoku.strip())  # parse the sudoku

# write CNF clauses and close file
f.write(f"p cnf {BITS * COUNT} {CLAUSES + n_clauses}\n")
f.write(SUDOKU_CLAUSES)
f.write("\n")
f.write(clauses)
f.close()

# run solver and get result
output = subprocess.run(["kissat.exe", "sudoku.in"], capture_output=True, text=True).stdout
raw = ""
for i in output.splitlines():
    if i[0] == "v":
        raw += i

if "s UNSATISFIABLE" in output:
    print("Sudoku has no solution")
else:
    raw = raw.replace("v", "")[1:-2]
    numbers = parse.parse_output(raw)
    for i in range(LENGTH):
        for j in range(LENGTH):
            print(numbers[LENGTH * i + j], end=" ")
        print("")
