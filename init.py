from common import *

f = open("sudoku.txt", "w")

# helper function, writes the formula stating that the cell at position idx is valid
def write_isvalid(idx):
    ...

# helper function, writes the formula stating that the cells at positions idx and idx2 are not equal
def write_isneq(idx, idx2):
    masks = []
    for i in range(2 ** BITS):
        mask = []
        for j in range(BITS):
            if i & (2 ** j):
                mask.append("-")
            else:
                mask.append("")
        masks.append(mask)
    for i in masks:
        for j in range(BITS):
            f.write(f"{i[j]}{BITS * idx + j + 1} {i[j]}{BITS * idx2 + j + 1} ")
        f.write("0\n")


for i in range(COUNT):  # make sure every cell is valid
    write_isvalid(i)

for row in range(LENGTH):  # make sure no two different cells in the same row are equal
    for i in range(LENGTH):
        for j in range(LENGTH):
            if i != j:
                write_isneq(LENGTH * row + i, LENGTH * row + j)

for col in range(LENGTH):  # make sure no two different cells in the same column are equal
    for i in range(LENGTH):
        for j in range(LENGTH):
            if i != j:
                write_isneq(col + LENGTH * i, col + LENGTH * j)

for x in range(SIZE):  # make sure no two cells in the same 3x3 block not in the same rwo or column are equal
    for y in range(SIZE):
        for i in range(SIZE):
            for j in range(SIZE):
                for k in range(SIZE):
                    for l in range(SIZE):
                        if (i != k) and (j != l):
                            write_isneq(SIZE * x + i + POW3 * y + LENGTH * j, SIZE * x + k + POW3 * y + LENGTH * l)

f.close()
