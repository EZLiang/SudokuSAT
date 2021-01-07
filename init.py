f = open("sudoku.txt", "w")

# helper function, writes the formula stating that the cell at position idx is valid
def write_isvalid(idx):
    f.write(f"-{4 * i + 1} -{4 * i + 2} 0\n")
    f.write(f"-{4 * i + 1} -{4 * i + 3} 0\n")
    f.write(f"-{4 * i + 1} -{4 * i + 4} 0\n")

# helper function, writes the formula stating that the cells at positions idx and idx2 are not equal
def write_isneq(idx, idx2):
    masks = []
    for i in range(16):
        mask = []
        for j in range(4):
            if i & (2 ** j):
                mask.append("-")
            else:
                mask.append("")
        masks.append(mask)
    for i in masks:
        f.write(f"{i[0]}{4 * idx + 1} {i[0]}{4 * idx2 + 1} ")
        f.write(f"{i[1]}{4 * idx + 2} {i[1]}{4 * idx2 + 2} ")
        f.write(f"{i[2]}{4 * idx + 3} {i[2]}{4 * idx2 + 3} ")
        f.write(f"{i[3]}{4 * idx + 4} {i[3]}{4 * idx2 + 4} 0\n")


for i in range(81):  # make sure every cell is valid
    write_isvalid(i)

for row in range(9):  # make sure no two different cells in the same row are equal
    for i in range(9):
        for j in range(9):
            if i != j:
                write_isneq(9 * row + i, 9 * row + j)

for col in range(9):  # make sure no two different cells in the same column are equal
    for i in range(9):
        for j in range(9):
            if i != j:
                write_isneq(col + 9 * i, col + 9 * j)

for x in range(3):  # make sure no two cells in the same 3x3 block not in the same rwo or column are equal
    for y in range(3):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if (i != k) and (j != l):
                            write_isneq(3 * x + i + 27 * y + 9 * j, 3 * x + k + 27 * y + 9 * l)

f.close()
