Code testing is something that should be always done, regardless of how simple you think the program is with in mind the idea of catching any errors.
Generally speaking, testing a program means writing a series of inputs and expected outputs, running the program and verify if the outputs match the expected one.

On this note, some [[development methodologies]] advocate for writing tests before starting to write the program and it is called [[test driven development]].

Remember from the [[code comments]] section that we write as comment the admissible values so you only have to write tests for those, anything else is considered to cause an error by default ([[garbage in, garbage out]]).
Generally speaking you want to test some normal values and [[borderline values]] like the smallest and largest admissible values, 0, 1 and -1.
For 3 inputs you generally should expect 3^2 tests.
If one of your tests fail you have to fix the error and always starts the tests over to make sure there are no [[regressions]].

Remember that tests by nature can not cover all input values and therefore we say that they show the presence of errors but not the absence of them ([[Edsger Dijkstra]]).
