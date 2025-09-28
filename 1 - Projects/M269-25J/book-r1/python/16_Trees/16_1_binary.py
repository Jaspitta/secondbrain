# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2025 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.1 Binary tree

### 16.1.1 Terminology

#### Exercise 16.1.1

### 16.1.2 ADT and data structure

# CELL 1

# this code is also in m269_tree.py


class Tree:
    """A rooted binary tree."""

    def __init__(self) -> None:
        """Create an empty tree."""
        self.root = None
        self.left = None
        self.right = None

# CELL 2

# this code is also in m269_tree.py


def is_empty(tree: Tree) -> bool:
    """Return True if and only if tree is empty."""
    return tree.root == tree.left == tree.right == None


def join(item: object, left: Tree, right: Tree) -> Tree:
    """Return a tree with the given root and subtrees."""
    tree = Tree()
    tree.root = item
    tree.left = left
    tree.right = right
    return tree

# CELL 3

THREE = join(3, Tree(), Tree())  # a leaf has empty subtrees
FOUR = join(4, Tree(), Tree())
SUM = join("+", THREE, FOUR)  # the subtree for 3 + 4

# CELL 4

# this code is also in m269_tree.py


def leaf(item: object) -> Tree:
    """Return a node with the item and empty subtrees."""
    return join(item, Tree(), Tree())


# The leaves for all the example trees.
THREE = leaf(3)
FOUR = leaf(4)
FIVE = leaf(5)
SIX = leaf(6)

# CELL 5

# this code is also in m269_tree.py

TPM = join("*", join("+", THREE, FOUR), join("-", FIVE, SIX))  # (3+4)*(5-6)
PMT = join("+", THREE, join("-", join("*", FOUR, FIVE), SIX))  # 3+((4*5)-6)
MPT = join("-", join("+", THREE, join("*", FOUR, FIVE)), SIX)  # (3+(4*5))-6

#### Exercise 16.1.2

# CELL 6

# %run -i ../m269_tree

pass

# CELL 7

# this code is also in m269_tree.py


def is_leaf(tree: Tree) -> bool:
    """Return True if and only if the tree is a single leaf."""
    return not is_empty(tree) and is_empty(tree.left) and is_empty(tree.right)

# CELL 8

is_leaf(THREE)

# CELL 9

is_leaf(Tree())

# CELL 10

is_leaf(TPM)