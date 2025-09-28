# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2025 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.7 Reversal

### 4.7.1 Problem definition

### 4.7.2 Problem instances

# CELL 1

reverse_list_tests = [
    # case,             values,             reverse
    ('empty list',      [],                 []              ),
    ('length 1',        [4],                [4]             ),
    ('length 2',        [5, True],          [True, 5]       ),
    ('length 5',        [5, 6, 7, 8, 9],    [9, 8, 7, 6, 5] ),
    ('same items',      [0, 0, 0],          [0, 0, 0]       )
]

# CELL 2

import algoesup

algoesup.check_tests(reverse_list_tests, [list, list])

# CELL 3

from algoesup import check_tests

check_tests(reverse_list_tests, [list, list])

### 4.7.3 Algorithm

### 4.7.4 Complexity

### 4.7.5 Code

# CELL 4

def reverse_list(values: list) -> list:
    """Return the same items as values, in inverse order.

    Postconditions: the output is
    [values[-1], values [-2], ..., values[1], values[0]]
    """
    reverse = []
    for item in values:
        reverse.insert(0, item)
    return reverse

### 4.7.6 Tests

# CELL 5

from algoesup import test

test(reverse_list, reverse_list_tests)

### 4.7.7 Performance

# CELL 6

size = 10
for measurement in range(10):
    numbers = list(range(size))  # list [0, 1, 2, ..., size-1]
    print("Reversing", size, "numbers:")
    # %timeit -r 5 reverse_list(numbers)
    size = size * 2

#### Exercise 4.7.1

#### Exercise 4.7.2

#### Exercise 4.7.3

# CELL 7

def reverse_list_2(values: list) -> list:
    """Return the same items as values, in inverse order.

    This is a more efficient version of reverse_list.
    Postconditions: the output is
    [values[-1], values [-2], ..., values[1], values[0]]
    """
    # replace with your function body


test(reverse_list_2, reverse_list_tests)

#### Exercise 4.7.4

#### Exercise 4.7.5

#### Exercise 4.7.6

#### Exercise 4.7.7

# CELL 8

def reverse_in_place(values: list) -> None:
    """Write the docstring."""
    # replace this with your code
    # modify `values` variable and do NOT use a return statement


# `algoesup.test` can only test functions that return values,
# so I've written the testing code for you
for test in reverse_list_tests:
    name = test[0]
    values = test[1]
    reverse = test[2]
    reverse_in_place(values)
    if values != reverse:
        print(name, "FAILED:", values, "instead of", reverse)
print("Tests finished.")