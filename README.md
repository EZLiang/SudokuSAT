# SudokuSAT
Using SAT solvers to solve Sudoku puzzles

SudokuSAT works by encoding Sudoku puzzles into [CNF][1] format, and then feeds it into a SAT solver, [kissat][2].
Kissat was chosen because of its speed, getting first place in the [SAT Competition 2020][3].

## Inputting a Sudoku
Input a Sudoku as a 9x9 grid of characters. Each number will be input as-is, while every blank square will be replaced
by a `?`. A sample Sudoku input is shown below, ripped from [WebSudoku][4]:
```
7?2?8??9?
?4???28?1
56???9??2
8?6??????
?9?????7?
??????6?9
9??7???86
4?16???3?
?3??1?9?4
```

## Using SudokuSAT
First, if `sudoku.txt` is missing or empty, run `init.py` to fix this problem.

Then run `python main.py [input]`, or whatever command you use to run a Python 3 file. `input` is optional, if provided
it specifies a path to a file in the format described in [Inputting a Sudoku](#inputting-a-sudoku). Otherwise, input a
Sudoku in that format line by line into stdin.

## How it works
SudokuSAT solves Sudokus by encoding it into a different format, and then uses a SAT solver to solve the resulting
problem. Specifically, it encodes the Sudoku into CNF format, which is input in [DIMACS format][5]. Most of the clauses,
or parts of the problem, are stored in the file `sudoku.txt`. Those 26163 clauses. define what it means to be a Sudoku.
Each number is represented as four bits, which gives 16 possible values, but only 9 are legal. The first 243 of the
clauses force the value of every square to be legal. Each square takes 3 clauses. The remaining 25920 clauses make sure
that no two cells in the smae row, column, or 3x3 block are equal. Each pair of values which cannot be equal take 16
clauses to specify. There are 810 such pairs, but `init.py` generates the clauses for each pair twice. This is the
reason for the number of clauses. The remaining clauses specify the given values of the Sudoku. Then, it feeds the
resultant file, `sudoku.in`, to the sat solver kissat, and then decodes kissat's solution back into a Sudoku.

[1]: https://en.wikipedia.org/wiki/Conjunctive_normal_form
[2]: https://github.com/arminbiere/kissat
[3]: https://satcompetition.github.io/2020/
[4]: https://www.websudoku.com/?level=2&set_id=6895630888
[5]: https://www.cs.utexas.edu/users/moore/acl2/manuals/current/manual/index-seo.php/SATLINK____DIMACS
