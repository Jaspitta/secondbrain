# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2025 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 27.1 Turing machine

### 27.1.1 Definition

### 27.1.2 Parity bit

### 27.1.3 Implementation

# CELL 1

# %run -i ../m269_tm

# CELL 2

parity = {
    # (state now, symbol read):  (symbol written, move, next state)
    ('start', None):    (None, RIGHT, 'even'),

    ('even', None):     (0, LEFT, 'back'),
    ('even', 0):        (0, RIGHT, 'even'),
    ('even', 1):        (1, RIGHT, 'odd'),

    ('odd', None):      (1, LEFT, 'back'),
    ('odd', 0):         (0, RIGHT, 'odd'),
    ('odd', 1):         (1, RIGHT, 'even'),

    # ('back', None):   stop
    ('back', 0):        (0, LEFT, 'back'),
    ('back', 1):        (1, LEFT, 'back')
}

# CELL 3

PARITY_IN = {0, 1}
PARITY_OUT = PARITY_IN

check_tm(parity, PARITY_IN, PARITY_OUT)

# CELL 4

wrong_parity = {
    # wrong name for initial state, which becomes unreachable
    ('begin', None):    (None, RIGHT, 'even'),
    # state, symbol and movement in wrong order, in both tuples
    (None, 'even'):     (0, 'back', LEFT),
    # missing movement
    ('odd', 1):         (1, 'even'),
    # typo in state name, which leads to another unreachable state
    ('eben', 1):        (0, RIGHT, 'even'),
    # symbol 2 is read (expected on the tape) but is not in input nor written by another transition
    ('even', 2):        (2, RIGHT, 'even'),
    # symbol 3 is written but not used in output or by another transition
    ('even', 1):        (3, RIGHT, 'odd')
}

check_tm(wrong_parity, PARITY_IN, PARITY_OUT)

# CELL 5

run_tm(parity, [None, 1, 0, 1])

# CELL 6

run_tm(parity, [None, 1, 0, 1], debug=True)

# CELL 7

parity_tests = [
    # name,       input,      debug,  output
    ('no bits',   [None],     False,  [None, 0]),
    ('just 0',    [None, 0],  False,  [None, 0, 0]),
    ('just 1',    [None, 1],  False,  [None, 1, 1]),
]

# CELL 8

check_tm_tests(parity_tests, PARITY_IN, PARITY_OUT)

# CELL 9

test_tm(parity, parity_tests)

# CELL 10

parity_tests_debug = [
    # name,       input,      debug,   output
    ('no bits',   [None],     True,    [None, 0]),
    ('just 0',    [None, 0],  False,   [None, 0, 0]),
    ('just 1',    [None, 1],  True,    [None, 1, 1]),
]

test_tm(parity, parity_tests_debug, show_tests=True)

### 27.1.4 Checking passwords

#### Exercise 27.1.1

#### Exercise 27.1.2

# CELL 11

VALID_IN = {"0", "a"}
VALID_OUT = {True, False}

is_valid = {
    ('start', 'a'):     ('a', RIGHT, 'letter'),
    ('start', '0'):     ('0', RIGHT, 'digit'),
    # add your transitions here
}

check_tm(is_valid, VALID_IN, VALID_OUT)

is_valid_tests = [
    # case,         input,            debug,  output
    ('empty pwd',   [],               False,  [False]),
    ('no digits',   ['a', 'a'],       False,  [False]),
    ('no letters',  ['0'],            False,  [False]),
    ('both',        ['0', 'a', '0'],  False,  [True])
]

check_tm_tests(is_valid_tests, VALID_IN, VALID_OUT)

test_tm(is_valid, is_valid_tests)

#### Exercise 27.1.3

#### Exercise 27.1.4