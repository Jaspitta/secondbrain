# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2025 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 5.3 Coding style

### 5.3.1 The Zen of Python

# CELL 1

import this

### 5.3.2 Linters

# CELL 2

# %load_ext algoesup.magics
# %ruff on --extend-ignore E711

# CELL 3

def length(list):
    count = 0
    for value in list:
        count = count + 1

# CELL 4

def length(values: list) -> int:
    """Return the number of items in the list."""
    count = 0
    for value in values:  # noqa: B007
        count = count + 1
    return count

# CELL 5

import platform

# CELL 6

if platform.system() in ("Linux", "Darwin"):
    # %allowed on --config m269-25j --unit 5 --method
else:
    # %allowed on --config m269-25j --unit 5

# CELL 7

from math import sqrt


def some_function(n: int) -> int:
    """To be implemented."""
    arabic_to_roman = {1: "I", 5: "V"}
    numbers = [1, 2, 1, 0]
    numbers.count(1)
    pass