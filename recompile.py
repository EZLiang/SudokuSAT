import sys

if len(sys.argv) == 1:
    SIZE = 3
else:
    SIZE = sys.argv[1]

with open("size.py", "w") as h:
    h.write("SIZE = " + str(SIZE))

import init
