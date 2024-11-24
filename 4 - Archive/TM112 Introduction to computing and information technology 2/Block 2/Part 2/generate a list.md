[[list generation]] is a [[computational problem]] that can be solved in many ways, the two main once are generating a sequence and storing each value in the list and the second is transforming an existing list into a new one.

The [[list generation]] topic also is related to [[coding pattern|coding patterns]] that involves list in general, first of all the [[sequence generation problem]] which involves generating a sequence in general and also the [[list generation]] pattern.
As usual, the boundaries between the two [[coding pattern]] are not always clear, some problems can fall in both the patterns and in those cases unless there is a specific reason both are valid solutions.

In general computing, lists are represented as \[n, n, n\] where each n is an element. Usually, but not always, the element's indexes start at 0 ([[0 indexed array]]) all the way to length - 1 and the size of the list is defined as length.
It is also very common to have a [[function]] called [[range]](begin, end) to cycle the elements in a list where begin is inclusive and end is exclusive.

Programs and patterns that include lists, like all others needs to tested with [[code tests]]. In this programs there are two types of tests to perform, tests on the values in the list, which are the regular once already addressed in the [[code tests]] and [[test driven development]] sections and also [[test]] on the list itself. For [[list tests]], borderline values usually include the case where the list has 0, 1 or the max number of items if there is a max (usually there isn't).

