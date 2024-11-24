---
aliases:
  - python functions
---
They are a [[programming construct]] that make your code easier to understand, modify and reuse, all while also hiding potentially a lot of complexity underneath them.

They are defined by a name and arguments (potentially 0), the combination of these two gives a [[function expression]] which is a [[programming expression]] or in some languages a [[function signature]].

The goal of functions is to hide complexity away, you need to know the names, parameters (formal arguments), return and side effects but you do not need to know how the function does what it does.
All these together form what in [[python]] is called the [[function interface]], this create a separation between the interface and the [[implementation]] and it is a form of [[abstraction]].

Functions that do not return a value technically return a None.

By convention [[python function]] are defined with [[snake case]] and if they return a value the name should express that.
The first line of the function is known as the [[function header]] and take the shape of `def name_return(arguments):` and if the function return something the last line will have the shape of `return some_element`.
An optional but always recommended part of a function is the [[documentation]], in particular a comment that gives a brief description of what the function does, in the case of [[python]] we have the possibility of using [[docstrings]] which is a message in triple quotes just below the [[function header]] `"""Return the size of a list"""`. What you write as [[docstrings]] is also visible from the [[python shell]] with `help(your_function)`.

The [[python interpreter]] like any other [[interpreter]] read lines one by one and executes them as they come, however the [[function]] act differently, when a function is encountered it is loaded into [[RAM]] and kept for later use.

One of the main advantages of [[function]] is to avoid [[code duplication]] which makes the program shorter, more readable and potentially easier to change.
Another consequence of such approach is that the [[function]] will hide the complexity of some of the sub-problems away from you, resulting into a program that looks much more like your [[decomposing]] activity.
Avoiding [[code duplication]] also means introducing [[code reusability]], this is not only true of the single program you are writing but potentially you can reuse the same function in any other program by copy and paste. Of course there is an even better way, you can place your function into a `.py` file and add `from path_to_file import *` to [[import functions]].

It is not hard to see also that [[functions]] can be extremely beneficial also when performing [[code tests]], in particular in [[python]] we can perform such tests using the [[assert statement]].
The process involves writing a function that usually is named `test_tested_resource` and perform a bunch of [[assert statement]] after calling the tested resource to see if the expressions evaluate to True.