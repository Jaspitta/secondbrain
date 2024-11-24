# Block 2 Part 4 Organising Your Python Code and Data

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/174623942/MEaVEPV24vT5kbCvhqyvOHWYd2qaeEl9Q24SXoYlpOg-cove_yMXEtKU.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 2 Part 4 Organising Your Python Code and Data
- Category: #books
- Summary: The text explains Python functions, how the interpreter works with code and data, and the process of defining and executing functions. It also emphasizes the importance of understanding each step in a program to effectively work with Python code.
- URL:

## Highlights
- problem decomposition is a key strategy that you are encouraged to use ([View Highlight](https://read.readwise.io/read/01hy3fzntheeh6sc85kpa286rf))
- construct a step-by-step algorithm ([View Highlight](https://read.readwise.io/read/01hy3fzwdbc7458wz2svys8zab))
- implement it in Python ([View Highlight](https://read.readwise.io/read/01hy3g06kat43txvd4azwckve5))
- package the code for these sub-problems into what are known as Python functions ([View Highlight](https://read.readwise.io/read/01hy3g0kte49gyk2n0fq32zyw0))
- code easier to understand and change ([View Highlight](https://read.readwise.io/read/01hy3g268h2988krb2qb451638))
- ready for reuse ([View Highlight](https://read.readwise.io/read/01hy3g1xp91qgzhj921v85svgn))
- test your code ([View Highlight](https://read.readwise.io/read/01hy3g1qe8kqd4ztvpqb0bjftn))
- think of the interpreter as a little robot or machine that carries out your code line by line ([View Highlight](https://read.readwise.io/read/01hy3gnhwvpr103nt2dn00mdm0))
### 4.1 Hiding complexity: Python functions
- Python language shields you from some of the complexity ([View Highlight](https://read.readwise.io/read/01hy3gq5j95vt86917vvwmgeb1))
#### **Box 4.3 Looking back**
#### 4.1.1 Functions in Python
##### Function names and arguments
- we have seen two kinds of basic expressions: variables and literals. ([View Highlight](https://read.readwise.io/read/01hya924cwmctq8vkjpymzsmgf))
- constructed expressions. These are the expressions that can be *constructed from* other expressions. ([View Highlight](https://read.readwise.io/read/01hya92k4qjssh46cz1hte4m8k))
- `[10, 5, 3, 8]` is an expression that is constructed with the literals `10`, `5`, `3` and `8` ([View Highlight](https://read.readwise.io/read/01hya936zrvt6452h7xqjxevrh))
- When a function name is combined with its argument, the result is an expression ([View Highlight](https://read.readwise.io/read/01hy3h5ztz62rp7qc3ek98vzxe))
##### Expressions
- represent data items ([View Highlight](https://read.readwise.io/read/01hy3h9syjrv7bgm6e77hcj5nx))
- The Python interpreter bridges the gap between expressions in your code and objects in its memory ([View Highlight](https://read.readwise.io/read/01hy3haj8drhmx5zngdhvv7m8x))
- expressions come in two varieties: basic and constructed. ([View Highlight](https://read.readwise.io/read/01hya9cgq3n3w23x0ywkxwtfth))
- by entering an expression in the shell, you can get the Python interpreter to show you a representation of the object ([View Highlight](https://read.readwise.io/read/01hy3hs3wh9gxybj5xab1xpjts))
- say that the expression evaluates to the object ([View Highlight](https://read.readwise.io/read/01hy3hvz5ye47wfs91kte62wb5))
- These standard representations of specific numbers and strings are known as literals. A literal always stands for that very same object ([View Highlight](https://read.readwise.io/read/01hy3nk294670e13zvv32mx76p))
- a function in a program does not automatically mean that the return value of the function is printed to the screen. To do so, you need to add code for printing ([View Highlight](https://read.readwise.io/read/01hyaa54q8n8dn01ygxajgzbfz))
- we recommend that you make use of intermediate variables. ([View Highlight](https://read.readwise.io/read/01hyaa6snw5m10r9v6zwn63p1d))
#### 4.1.2 Restaurant kitchens and functions
##### Hiding complexity: interfaces and implementations
- You don’t need to know how a function, such as `len()` or `print()`, does what it does. ([View Highlight](https://read.readwise.io/read/01hyaamdtn8cjbf1d2z7tzf74z))
- To use a function, all you need to know are:
  • the name of the function
  • what kind of argument(s) it needs
  • what it gives back as a return value
  • what other effects calling the function has. ([View Highlight](https://read.readwise.io/read/01hyaaq6nx6w61z09hm90zgzw3))
- name for the items you need to know: the interface of the function. ([View Highlight](https://read.readwise.io/read/01hyaawq032hh89w64s8xg2fg7))
- *Name of the function* *Type of arguments* *What the function gives back as a return value* *What other effects calling the function has* `len`       `print` ([View Highlight](https://read.readwise.io/read/01hyfdj8b0t450d66psn6akpg4))
- the implementation is separated from the interface ([View Highlight](https://read.readwise.io/read/01hyaz3jc6zsqjb9qdjrtwwh0p))
- an abstraction ([View Highlight](https://read.readwise.io/read/01hyaz3rx2rtvd1xe9xz1cjr27))
- Such functions do have a return value, but it is a special object called `None`. ([View Highlight](https://read.readwise.io/read/01hyaz72dvb7r5y4rrcdege0rz))
- print('hello') == None ([View Highlight](https://read.readwise.io/read/01hyaz6t8hgc0tmbqv8ppyqn5p))
##### How to upgrade the kitchen with a new recipe
#### 4.1.3 Defining your own function
- we can get the Python interpreter to master a new function by defining that function ([View Highlight](https://read.readwise.io/read/01hyazgsrct3t65j6wmgv0adzh))
- we follow the convention of using lower case with underscores ([View Highlight](https://read.readwise.io/read/01hyazj4e60dy87545mf6jabse))
- If a function has a return value, it is good practice for its name to describe that return value ([View Highlight](https://read.readwise.io/read/01hyazjfj7kdrse4fq5cvzspdg))
- keyword `def` ([View Highlight](https://read.readwise.io/read/01hyazntnyyb9s6nxq024zyebx))
- first line of the function definition, known as the header ([View Highlight](https://read.readwise.io/read/01hyazp4ynk7xf6x58tjjhkdwx))
- def list_length(a_list): ([View Highlight](https://read.readwise.io/read/01hyazrek1747qj5gmj39qnam8))
- parameters of the function, also known as its formal arguments ([View Highlight](https://read.readwise.io/read/01hyazrw2c0xtb9bq9enpvf6qq))
- return length ([View Highlight](https://read.readwise.io/read/01hyazvzbrkmfmvfb5k3mpsg8n))
- 4.1.4 Documenting your functions ([View Highlight](https://read.readwise.io/read/01hyazxbkkpbsrjcb9a78ftty2))
- 1 `def list_length(a_list):` 2   `"""Return the length of a list."""` 3   `length = 0` 4   `for item in a_list:` 5     `length = length + 1` 6   `return length` ([View Highlight](https://read.readwise.io/read/01hyfe1y3sp65j8cdm3v3jnq1y))
- it is good practice to always briefly record what each of your functions does ([View Highlight](https://read.readwise.io/read/01hyazy9wxe52r3vhjqepc35z3))
- docstrings ([View Highlight](https://read.readwise.io/read/01hyazyq8jet10hsv3y502rzcv))
- enclosed in a triplet of double quotes ([View Highlight](https://read.readwise.io/read/01hyazyz1hv3wjt61rjwxz2egm))
- same indentation as the rest of the function ([View Highlight](https://read.readwise.io/read/01hyb04ew9msb2bbt8mwyga1kt))
- can also be inspected in the shell, using `help(list_length)` ([View Highlight](https://read.readwise.io/read/01hyb051ap1ect7vp5azdt8gyb))
### 4.2 Function execution
#### 4.2.1 The Python interpreter and functions
- When the Python interpreter encounters a function definition, it reads this definition into memory for later use ([View Highlight](https://read.readwise.io/read/01hyb0as9w3yeazsqrfcve1mtf))
- where a function is called ([View Highlight](https://read.readwise.io/read/01hyb0fj77aeeejak44k4yw528))
- parameters are initialised ([View Highlight](https://read.readwise.io/read/01hyb0fnhqzpm7yhm6b4077r88))
- body are executed ([View Highlight](https://read.readwise.io/read/01hyb0frv5x1a6mvd312gkfms6))
- he keyword `return` ([View Highlight](https://read.readwise.io/read/01hyb0g18z8a7epv9ev08kaqwp))
- the function stops executing ([View Highlight](https://read.readwise.io/read/01hyb0g4hh6284y5kkmax06mqs))
- value of the expression following `return` is passed back ([View Highlight](https://read.readwise.io/read/01hyb0g9kgk29x07v08n1dcvzt))
#### 4.2.2 Executing the `list_length()` function
#### 4.2.3 Function execution: an animation and a description
#### 4.2.4 Reading Python error messages in the shell
- `Traceback …`) indicates that the program was executing when the error occurred and that execution was stopped as a result of the error ([View Highlight](https://read.readwise.io/read/01hyb5dja8jc4w5kj324547v4s))
- a typo, such as a missing parenthesis ([View Highlight](https://read.readwise.io/read/01hyb5ff0agxwfqvvqa8f2e2ma))
- would not have reached this point and a `SyntaxError` would have been reported ([View Highlight](https://read.readwise.io/read/01hyb5fqgh6s17g6k5vmtxz6ht))
- The next two lines identify the line and statement where the error occurred. ([View Highlight](https://read.readwise.io/read/01hyb5g3145s73cfq9ternqv6q))
### 4.3 Using functions: the benefits
- eliminate duplicate code ([View Highlight](https://read.readwise.io/read/01hyb5mbvyc3htx6rk5qsqndxn))
#### 4.3.1 Finding duplicate code
#### 4.3.2 Defining a function to replace duplicate code
- can make a program shorter and more readable ([View Highlight](https://read.readwise.io/read/01hyb638jdm7695wap5892rd3y))
- much easier to modify the code ([View Highlight](https://read.readwise.io/read/01hyb63beqfx0gjfb0x031fxsq))
- by hiding complexity, functions allow us to reflect our decomposition of the problem ([View Highlight](https://read.readwise.io/read/01hyb6639nq0hq3bf17bvhx3pq))
- shorter and consequently more readable ([View Highlight](https://read.readwise.io/read/01hyb68jjgpjj1tzz9e7a2xnn9))
- easier to change ([View Highlight](https://read.readwise.io/read/01hyb68n5e5r4znp40tj7tbgfa))
- mirrors the decomposition ([View Highlight](https://read.readwise.io/read/01hyb68t466bwx1040bah8cdpc))
#### 4.3.3 Reusing code
- once we have written a function for drawing a triangle, we can use this function not only in the current program, but also in other programs ([View Highlight](https://read.readwise.io/read/01hyb6b7p5dte596xyh8n7t4jy))
- Instead of copying a function into a new program, you can also put all your functions – say, for drawing figures – into a separate file ([View Highlight](https://read.readwise.io/read/01hyb6ccs0j9gss0twytp5vf16))
- Let’s call it `figure_drawing_functions.py`. At the beginning of your new program, you then simply add `from figure_drawing_functions import *` ([View Highlight](https://read.readwise.io/read/01hyb6g9metf4gen81158v4q8c))
- `figure_drawing_functions.py` is in the *same* folder ([View Highlight](https://read.readwise.io/read/01hyb6gjhtb54wv8xbtb54vp87))
#### 4.3.4 Generalising code
### 4.4 Testing code with functions
- We’ll use functions to test code automatically ([View Highlight](https://read.readwise.io/read/01hyb9tw50pndebae9y05gmj27))
#### 4.4.1 Why automate testing?
- Functions allow us to automate the testing of our code ([View Highlight](https://read.readwise.io/read/01hyb9y5n6m0qkj6npp8p920fb))
- the `assert` statement. ([View Highlight](https://read.readwise.io/read/01hyb9yb06zgg6b5myh8gm4bqq))
#### 4.4.2 Assert statements
- `assert` statement ([View Highlight](https://read.readwise.io/read/01hyba12fzv56jhaxc5r1z56gy))
- keyword `assert` ([View Highlight](https://read.readwise.io/read/01hyba177gg6ggw9nq7bf50gp5))
- followed by an expression ([View Highlight](https://read.readwise.io/read/01hyba1bxpfhfmeryz56hkc8pk))
- when the Boolean expression of an `assert` statement evaluates to `False` ([View Highlight](https://read.readwise.io/read/01hybadqnb55v439bbt7gdbat8))
- Execution of the statement stops ([View Highlight](https://read.readwise.io/read/01hybadm2rk1qd9qhttfcfh0my))
- An `AssertionError` error message is printed ([View Highlight](https://read.readwise.io/read/01hybadfc3abj2pjw9pdy2qad7))
#### 4.4.3 An algorithm for testing `list_length()`
#### 4.4.4 Implementing `test_list_length()`
- for functions that do have a return value, we recommend that you use a description of the output ([View Highlight](https://read.readwise.io/read/01hycv0fa7kejezptzvc8yc6gc))
- an `AssertionError` is *not* a return value; values can be passed on to other functions ([View Highlight](https://read.readwise.io/read/01hycv1t44pprbsyp6e29yj422))
- To use this test function `test_list_length()`, include it in the same program as the `list_length()` function itself. To call the tests, add at the end of the program: ([View Highlight](https://read.readwise.io/read/01hycvf5qa9yese7npptyw5myp))
- the fact that all tests were successfully passed does *not* prove that the program is correct ([View Highlight](https://read.readwise.io/read/01hycvg219rkdn9s97sqr0b9kv))
- When writing a function that has arguments and return values, it is good practice to think about a representative sample of arguments/return value pairs, and write the corresponding test function ([View Highlight](https://read.readwise.io/read/01hycvk3gdpc6hfpg35358vmhk))
- good practice to write your tests *before* you write the actual code ([View Highlight](https://read.readwise.io/read/01hycvwbkfqmqz567edrb6gh58))
- known as **test-driven development** ([View Highlight](https://read.readwise.io/read/01hycvwqs4xx17n9eveh4msyw5))
### 4.5 Expressions, objects and functions
#### 4.5.1 Data items as objects
- how the Python interpreter represents and processes data. ([View Highlight](https://read.readwise.io/read/01hycw8gsy1j93v0bfdj5ffcbk))
##### Expressions and objects
- In Python, data items are known as objects. ([View Highlight](https://read.readwise.io/read/01hycwdcqgzfq18jzvn7kb03vn))
- the programmer who enters expressions ([View Highlight](https://read.readwise.io/read/01hycwgbgkn78r6z5w2c7gdydm))
- objects that exist in the memory ([View Highlight](https://read.readwise.io/read/01hycwgkzhd7xxjdvrnhy2t25a))
- the Python interpreter is able to evaluate expressions to objects ([View Highlight](https://read.readwise.io/read/01hycwhgsxj60e86az4w0nxwag))
- In Python, each object consists of three components:
  • its id (identity)
  • its type
  • its **value**. ([View Highlight](https://read.readwise.io/read/01hycwv54xqwsq3zbf11pbg8f0))
##### The object’s id
- Each object has a unique number. This is the object’s id ([View Highlight](https://read.readwise.io/read/01hycz0975rjdq5eyp051drpps))
- `id()`: ([View Highlight](https://read.readwise.io/read/01hycz1d7vkdg2zdh5y2e4a3zv))
##### The object’s type
- type(a_number) ([View Highlight](https://read.readwise.io/read/01hycz3fb4db7pyrj6knjk3vb7))
##### The object’s value
- when we talk informally about an object, we are talking about its value ([View Highlight](https://read.readwise.io/read/01hycz448kyadtwm7pgc0em2wt))
- For the purpose of readability, in what follows we will suppress type and id of objects that are associated with literals ([View Highlight](https://read.readwise.io/read/01hyd7vcrk8m5wq241wvfbmkxd))
- Lists are known as containers ([View Highlight](https://read.readwise.io/read/01hyd7whv5rzmv84h2jesym8wa))
- zero or more references or labels. Each label is attached to an object ([View Highlight](https://read.readwise.io/read/01hyd7x5gfazb7p3gyrp18sbe4))
- Each of these indexes is attached to an element of the list ([View Highlight](https://read.readwise.io/read/01hyd846c35dq1zpkgvdxwhp76))
- The indexes tell us the position of the integer objects in the list ([View Highlight](https://read.readwise.io/read/01hyd84pzq1yzve91teg9y0vs1))
#### 4.5.2 Variables and assignments
- For Python, it is more appropriate to think of variables as labels or luggage tags. ([View Highlight](https://read.readwise.io/read/01hyd8802dj6pv7yfeajntwp32))
- a metaphor provides an intuitive mental aid for predicting how a variable will behave ([View Highlight](https://read.readwise.io/read/01hyd89h6epxkxdy3z5k4wpmwf))
##### The ‘variables as labels’ metaphor for Python
- the Python interpreter carries out the following two steps ([View Highlight](https://read.readwise.io/read/01hyd8e804f2kkqbkndp7b9s02))
- evaluates the expression on the right-hand side ([View Highlight](https://read.readwise.io/read/01hyd8ecnjg4avt6ny6gkq9p0d))
- checks whether there already is an object with the same label ([View Highlight](https://read.readwise.io/read/01hyd8epy21a0wngsqeta9serq))
- *If* the label is already in use: ([View Highlight](https://read.readwise.io/read/01hyd8esrxc2zkjag17zyhsrqb))
- this label is removed from its current bearer ([View Highlight](https://read.readwise.io/read/01hyd8ezge6sww9gm9p3axpcsj))
- this label is attached to the object ([View Highlight](https://read.readwise.io/read/01hyd8f3d3hev2pccgp5nvxft4))
- Otherwise ([View Highlight](https://read.readwise.io/read/01hyd8f6tx95cmfwx2kfzkfkmf))
- a new label is created and attached ([View Highlight](https://read.readwise.io/read/01hyd8fcksb2g2zdy83efw3zvt))
##### Using the same variable twice
#### 4.5.4 Assignments and functions
