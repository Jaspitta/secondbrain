Solving a coding problem is a step based process that start with the overall problem to arrive to a final [[code implementation]].

The first step is to identify the problem and split it into [[sub-problem|sub-problems]]. This is a process that can take more than one step as the single sub-problems may need to be split further.
In practical terms, this may means starting to write a [[code comments|code comment]] with the description of the problem at the top, and slowly the single decomposed steps below.
Keep in mind that if there are steps that have common elements (like same input) they should be [[aggregating common instructions|aggregated]] into one or omitted in the second occurrence.

Once we have the sub-problems described, we can now start to identify [[problem type|problem types]] and [[coding pattern|coding patterns]] that can be applied to the single case. This will probably mean describing further the sub problems into [[pseudo code]] and further [[aggregating common instructions]].

Once all the problems, inputs/outputs and patterns have been described we can finally move to the actual [[code implementation|algorithm implementation]]. This should follow the description we have created, include the necessary [[code comments|code comments]] and the related [[code tests|tests]] for the problem to be considered fully completed (unless specified otherwise).

Remember that [[code tests]] could also be required to write at the beginning of the process in the case of [[test driven development]]


### Restaurant Example:

Consider a restaurant that adds a service charge to the bill if there are more than six people in the party. Compute the bill correctly, given the number of people.

Decompose the problem:
- > Compute bill
- >> compute bill for the case the charge is added
- >> compute bill for the case the charge is not added

Here we can identify 2 patterns already, the [[formula problem]] pattern for calculating the bill and the [[cases pattern]] for the 2 different cases:
- initialize inputs
- if inputs follow first case
	- compute output for first case
- otherwise:
	- compute output for second case
- print result

At this point we have the patterns clear and we can fill in them:
- initialize inputs
- if inputs follow first case
	- initialize inputs -> can be omitted [[aggregating common instructions]]
	- set output to the formula with the input applied
- otherwise:
	- initialize inputs -> can be omitted [[aggregating common instructions]]
	- set output to the formula with the input applied
- print result

Finally we can further elaborate with the cases described:
- initialize inputs
- if people > 6
	- set output to the formula with the input applied
- otherwise:
	- set output to the formula with the input applied
- print result

Next, before writing the code we could start thinking about the [[code tests|tests]]. We need to identify normal and border values, than testing those. The most obvious once should be 6 and 7 since they are at the edge of the 2 cases.
Than for more normal values we could test 1 (since 0 and 0.5 are not acceptable)




