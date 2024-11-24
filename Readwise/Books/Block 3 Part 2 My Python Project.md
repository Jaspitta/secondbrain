# Block 3 Part 2 My Python Project

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/194377274/QEPRc-PEyMBzuW-vNKKer35IPknrsnM0Ep6yoxhzElA-cove_AkYEQys.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 3 Part 2 My Python Project
- Category: #books
- Summary: The text discusses learning Python concepts like dictionaries and interactive loops through activities and discussions.
It guides you through creating algorithms and implementing them in Python for tasks like showing flashcards and interactive loops.
The activities help you practice writing code and testing programs to enhance your Python skills.

## Highlights
### Introduction
- Python mini-project
- develop a flashcard algorithm
### 2.1 From lists to dictionaries
- Python dict, also known as the Python dictionary
#### 2.1.1 Lists revisited
##### The list object
- It differs from strings and numbers in that its value consists of zero or more labels or indexes
#### 2.1.2 Introducing Python dictionaries
- Python dictionaries have
- a key-value pair and is written as follows:
  `key: value`
- consist of zero or more `key: value` pairs
- {key1: value1, key2: value2, ...}
#### 2.1.3 Dictionary objects versus list objects
- dictionaries – just like any other data items – are objects with an id, type and value
- The keys can be, among other things, strings and numbers. However, lists and dictionaries themselves *cannot* be keys
- labels (indexes or keys) are *unique*
- The dictionary’s values are not to be confused with the dictionary object value. The latter is the collection of labels
#### 2.1.4 Using Python dictionaries
##### Creating Python dictionaries
- It is also possible to create a dictionary with no values: an empty dictionary
##### Adding items to a Python dictionary
- a_dict[key] = value
##### Accessing dictionary values
##### Amending a dictionary
- If you want to change the value for a key, all you need to do is assign the key to the new value.
- the following Boolean expression evaluates to `True` if the key is in the dictionary, and `False` otherwise:
  `key in a_dict`
##### Checking for a key
### 2.2 Random dictionary key selection
- picking a random key from a dictionary involves breaking it into two problems:
  1. turning the dictionary into a list of its keys, then
  2. picking a random item from that list
#### 2.2.1 Converting a dictionary into a list
- the function `list()` is applied to a dictionary, it returns the keys of that dictionary as a list
#### 2.2.2 Selecting a random item from a list
- To select a random item from a list in Python, you can use the function `choice()` (after importing the `random` module)
- >>> from random import * 
  >>> choice([1,2,3,4,5,6])
- the interactive loop pattern
- is ‘interactive’ because it relies on user input
#### 2.3.1 Getting user input
### 2.3 Interactive loops
- To get input from the user, we use the function `input()`
- one argument, which is a string. When `input()` is called, this string is displayed on the screen
#### 2.3.2 The interactive loop pattern
- When we write up an algorithm, the Python code
  `user_input = input('How shall I greet you? ')`
  will be expressed as follows in English:
  Set the variable *user_input* to the response to 'How shall I greet you? '
- 1 set the variable *exit* to false 2 while *exit* is equal to false:  2a  set the variable *user_input* to the response to ‘Type your input here: ’  2b  if the *user_input* is ‘quit’, set the variable *exit* to true  2c  otherwise if *user_input* has some value(s) do something  2d  otherwise if *user_input* has some other value(s) do something else  2e  ...  2f  otherwise do something else
##### Pattern 2.1 The interactive loop
#### 2.3.3 Implementing the pointless interactive loop
- Python provides the Boolean expressions `True` and `False`. So, instead we can write
  `exit = False`
- there is another shorter more elegant way to implement the condition using the Boolean operator `not`:
  `while not exit:`
#### 2.3.4 The echo chamber interactive loop
### 2.4 From the flashcard problem to an algorithm
#### 2.4.1 The problem and its decomposition
##### The problem
#### 2.4.2 Setting up the glossary
#### 2.4.3 The interactive loop
#### 2.4.4 Showing a flashcard
### 2.5 Implementation
- Four steps for producing ideas
- write down any partial or tentative ideas
- you may get tired working out the puzzle. Try to give it one other go
- realise you aren’t making any progress
- drop the whole subject
- Out of nowhere the Idea will appear
#### 2.5.1 Getting started with the implementation
##### Creating a `.py` file
- declare any module that we are importing
##### Setting up the glossary
#### 2.5.2 Showing a flashcard
#### 2.5.3 The interactive loop
#### 2.5.4 And now with the TM112 glossary
##### Using the TM112 glossary
