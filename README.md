# SudokuSAT
Using SAT solvers to solve Sudoku puzzles

SudokuSAT works by encoding Sudoku puzzles into [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form) format,
and then feeds it into a SAT solver, [kissat](https://github.com/arminbiere/kissat). Kissat was chosen because of its
speed, getting first place in the [SAT Competition 2020](https://satcompetition.github.io/2020/).

## Inputting a Sudoku
Input a Sudoku as a square grid of values separated by spaces. Each number will be input as-is, while every blank square will be repalced
by a `?`. A sample Sudoku input is shown below, ripped from
[WebSudoku](https://www.websudoku.com/?level=2&set_id=6895630888):
```
7 ? 2 ? 8 ? ? 9 ?
? 4 ? ? ? 2 8 ? 1
5 6 ? ? ? 9 ? ? 2
8 ? 6 ? ? ? ? ? ?
? 9 ? ? ? ? ? 7 ?
? ? ? ? ? ? 6 ? 9
9 ? ? 7 ? ? ? 8 6
4 ? 1 6 ? ? ? 3 ?
? 3 ? ? 1 ? 9 ? 4
```

## Using SudokuSAT
First, if `sudoku.txt` is missing or empty, run `init.py` to fix this problem. If you want to change the Sudoku size,
you can skip this step.

If you want to change the size of the Sudoku, run `python recompile.py size`, or whatever command you use to run a
Python 3 file. Here, `size` is the side length of each block in the Sudoku. For example, a normal Sudoku has `size=3`.

Then run `python main.py [input]`, or whatever command you use to run a Python 3 file. `input` is optional, if provided
it specifies a path to a file in the format described in [Inputting a Sudoku](#inputting-a-sudoku). Otherwise, input a
Sudoku in that format line by line into stdin.
