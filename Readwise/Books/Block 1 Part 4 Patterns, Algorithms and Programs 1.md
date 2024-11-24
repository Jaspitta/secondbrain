# Block 1 Part 4 Patterns, Algorithms and Programs 1

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/158789745/z3Xadn5pMzPthxkqT3c-bs5Qe2EulRegY-qXX69r9TY-cove_BvUeSsr.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 1 Part 4 Patterns, Algorithms and Programs 1
- Category: #books
- Summary: The text explains how to solve problems using patterns and algorithms, specifically focusing on formula problems and case analysis. It demonstrates translating algorithms into Python code and emphasizes the importance of thorough testing before writing code. The text also discusses nested 'if' statements and provides examples of problem-solving techniques for computational challenges.
- URL:

## Highlights
##### Introduction
- you saw examples of how to go from a problem to its solution ([View Highlight](https://read.readwise.io/read/01htkts0qdsz1xbzmkhcycdhww))
- The problem is decomposed into sub-problems, which are solved by refining a high-level algorithm into the detailed sequential or iterative steps ([View Highlight](https://read.readwise.io/read/01htktsbch1bn84vpyrrrze6wr))
- Many of the problems that need to be solved daily are very similar to previous problems ([View Highlight](https://read.readwise.io/read/01htktstpgqckd0ty3wjnd33yk))
- A group of similar problems can be viewed as belonging to a common problem *type* ([View Highlight](https://read.readwise.io/read/01htktt7kzkcbck3kdcy38k40v))
- a group of similar solutions (for similar problems) can be viewed as particular cases of a solution *pattern* ([View Highlight](https://read.readwise.io/read/01htktv4f7b1sty4s0recctn89))
- I will show you several types of problems and the corresponding patterns that you can use to solve them ([View Highlight](https://read.readwise.io/read/01htktz27jvb2gttz9ew4c8t14))
- if you recognise the type of the problem, you can then use the corresponding pattern to create a concrete algorithm for the given problem ([View Highlight](https://read.readwise.io/read/01htkv347kjczm983g9dyx3ctk))
### 4.1 Calculate
- The aims of this section are to recap and summarise some concepts you already came across in Part 2 and possibly in TM111 ([View Highlight](https://read.readwise.io/read/01htkw45685rbww0awtkm71n11))
#### 4.1.1 Numeric expressions
- Unlike other programming languages, Python integers can be arbitrarily large (for both positive and negative integers). ([View Highlight](https://read.readwise.io/read/01htkwav842d28cx5qmnj30zda))
- since Python 3.6, you can use underscores for grouping digits (so you can write, for instance, 100_000 ([View Highlight](https://read.readwise.io/read/01htkwcaq3eygt8wj662mby058))
- Python has no thousands separator and uses the point as the decimal mark, so the same number is written as `1000000.5` ([View Highlight](https://read.readwise.io/read/01htkwdjydmr2behgjbe6z1fft))
- Having seen some of the numbers and arithmetic operators Python provides, let’s solve a numeric problem ([View Highlight](https://read.readwise.io/read/01htpcgmcmhh1b2azreb1bm2rq))
##### Decompose the problem
#### Identify the sub-problems’ types
- I realise the sub-problems look like many of the problems I faced in the past ([View Highlight](https://read.readwise.io/read/01htpcmwkxwxed5b50y7wkvwtf))
- One or more values are given (the problem’s inputs), one value is sought (the problem’s output), and it can be computed by applying a formula (a numeric expression) to the inputs. ([View Highlight](https://read.readwise.io/read/01htpcn0c234454djt35n84qjt))
- I will refer to these problems, where a single output can be directly computed from one or more inputs, as ‘formula problems’. ([View Highlight](https://read.readwise.io/read/01htpcxtqskdnr1qg59g9v3cvh))
- the pattern is not an algorithm (or it is a very vague one, if you prefer): it doesn’t tell us the precise variables and values to use ([View Highlight](https://read.readwise.io/read/01htpd0se2rg0t2ab43f6c2eeg))
- Therefore I will also use the verb ‘instantiate’ to mean ‘fill in’ ([View Highlight](https://read.readwise.io/read/01htpd1j8srmhdwqw6zvwwx2tz))
- 4.1.3 Formula problems: algorithm ([View Highlight](https://read.readwise.io/read/01htpd90fmbtat4abzdag1cmg2))
##### Instantiate the pattern
#### 4.2.1 Documentation
- it’s not immediately clear from the code what are the allowed types, values and units of the input variables ([View Highlight](https://read.readwise.io/read/01htpqy0m6zq40gskszypxsz4q))
- The solution is to document the code, by adding comments. ([View Highlight](https://read.readwise.io/read/01htpqyr1cm90s90r1paxs4cng))
- Comments should also be used to explain the inputs and outputs, in what units the values are, and any constraints – for example, not being negative ([View Highlight](https://read.readwise.io/read/01htpqz7bvwb11fkv6kw40nky4))
- a complicated or unfamiliar formula that is not easy to explain, you may consider pointing the comment to a source (e.g. Wikipedia) ([View Highlight](https://read.readwise.io/read/01htpqzsjxxedsqsbsy2e43r6k))
- Comments should be used to explain the non-obvious ([View Highlight](https://read.readwise.io/read/01htpr12e8zwqr5kryz6nx03sp))
- I will, however, always start programs with a comment that describes the problem, i.e. what the program does. ([View Highlight](https://read.readwise.io/read/01htpr3dj5g3a6sc2kzn70tf4f))
#### 4.2.2 Tests
- you should get into the habit of testing it to catch any errors ([View Highlight](https://read.readwise.io/read/01htpr4gy2b7n3n6rp3w8a69k8))
- Testing a program consists of writing down several pairs of inputs and the corresponding expected outputs, running the program for those inputs, and checking whether the actual outputs match the ones you expected ([View Highlight](https://read.readwise.io/read/01htpr68djemyejfx3dnf8s89j))
- Many people advocate writing down the tests even *before* ([View Highlight](https://read.readwise.io/read/01htpr6gvvze241rps652t48w7))
- You only have to test your program for admissible input values and document in the code which values are not. ([View Highlight](https://read.readwise.io/read/01htpr72hbbgfcfz1nt86ame8m))
- garbage in, garbage out. ([View Highlight](https://read.readwise.io/read/01htpr7sfwz2gexny6hk29cpsh))
- You will have to run your program for *each* test, so think lazy ([View Highlight](https://read.readwise.io/read/01htpran1v1pv5msvm9tzqnkwd))
- Test all borderline values and also a ‘normal’ one. ([View Highlight](https://read.readwise.io/read/01htprd918dmse5t77jbpm6xh4))
- smallest and largest possible admissible values ([View Highlight](https://read.readwise.io/read/01htprdkh3q7h6ykvf5qay29r6))
- 0, because it is the border between negative and positive ([View Highlight](https://read.readwise.io/read/01htprdr3s2yk4j1nyvdq34kyr))
- 1, because it is at the border between positive and non-positive integers ([View Highlight](https://read.readwise.io/read/01htprdz74n44w5p2fwgcf6zaq))
- –1, because it is at the border between negative and non-negative integers. ([View Highlight](https://read.readwise.io/read/01htpre8ka27wm0knk6nsfx3kq))
- Once you have the values to be tested for each input, each test will be a combination of those values ([View Highlight](https://read.readwise.io/read/01htprfykwt6c3pwc4r5ny6pes))
- If one of your tests fails, i.e. the actual outputs don’t match the expected ones, then you have to find the source of the error and fix it. After doing that, you must restart testing from the first test ([View Highlight](https://read.readwise.io/read/01htprht9wb0h9pp0s4h42hc5z))
### 4.3 Analyse two cases
- but the sub-problem doesn’t state what the values of the width and length are. Usually the algorithm would ask the user to type in some values on the keyboard, but to keep things simple I choose the values myself ([View Highlight](https://read.readwise.io/read/01htpdene4nsaxn1mg5szkgzvy))
- a single line of the pattern became two lines of the algorithm ([View Highlight](https://read.readwise.io/read/01htpdhw0yaetgx3rdvtcrp1nq))
- use specific and descriptive variable names that capture the problem at hand ([View Highlight](https://read.readwise.io/read/01htpdj0s5s7m80rc0q8306c8b))
#### 4.1.4 Formula problems: program
##### Implement the algorithm
### 4.2 Document and test
- Even the smallest programs may be hard to understand and have errors. It is therefore best to document and test your programs, no matter how trivial they seem. ([View Highlight](https://read.readwise.io/read/01htpdnvfr1sgrfwabjaw9qhvk))
- Python provides several numeric operators ([View Highlight](https://read.readwise.io/read/01htmvkxk3qkb4p2ranmd76m9n))
- addition (`+`), subtraction (`-`) and multiplication (`*`) ([View Highlight](https://read.readwise.io/read/01htmvm3txtmyb6ghwweeys030))
- single division sign (`/`) represents exact division, i.e. the result is always a floating-point number, whereas a double division sign (`//`) represents floor division ([View Highlight](https://read.readwise.io/read/01htmvmdzphts5qapfzwhspbvt))
- Python also provides the remainder (modulus) operator, confusingly written as the percentage sign (`%`). The operator calculates the remainder of the floor division of the first number by the second ([View Highlight](https://read.readwise.io/read/01htmvrpdy93att8khv2bqfwx4))
- The remainder operator is useful to check if a number *n* is a multiple of another number *m* ([View Highlight](https://read.readwise.io/read/01htmw2ke11cfkdgm5wrjnfmch))
- Python follows the usual convention of doing multiplications, remainders and divisions before additions and subtractions ([View Highlight](https://read.readwise.io/read/01htmw54fhxf91n894nyr8m5sq))
- Multiplications and divisions are done from left to right, and so are additions and subtractions ([View Highlight](https://read.readwise.io/read/01htmw5bf3svebtvgwe91n38hw))
#### 4.1.2 Formula problems: pattern
##### Fill in the pattern
- The copying of Pattern 4.1 into Pattern 4.2 led to duplicate initialisation and printing. I’ll omit them in the next version of the algorithm. ([View Highlight](https://read.readwise.io/read/01htyfcbhm82sp20xqa16p8cz8))
- to start filling the pattern, you need to identify the outputs and inputs ([View Highlight](https://read.readwise.io/read/01htyfe1mt2dp529hr4ezpe7eg))
#### 4.3.2 Tests
- we need at least one input value for each possible case ([View Highlight](https://read.readwise.io/read/01htyvnspsgyqfdwhfd84mmkam))
#### 4.3.3 Program: Boolean expressions
- The selection of which case ([View Highlight](https://read.readwise.io/read/01htyw5nn59nndfhc5nm5d1wmh))
- is always based on a Boolean expression, i.e. an expression that has a true or false value ([View Highlight](https://read.readwise.io/read/01htyw5cdzv0tdm2t324jtc376))
- two equal signs is a Boolean operator that means ‘is equal to’, whereas one equal sign is the assignment operator that means ‘becomes equal to’. ([View Highlight](https://read.readwise.io/read/01htyw9xznc3e9qkbvryhas2w3))
### 4.4 Analyse multiple cases
#### 4.4.1 Pattern and algorithm
#### 4.4.2 Program: Boolean operators
- most programming languages provide Boolean operators to write more complicated Boolean expressions ([View Highlight](https://read.readwise.io/read/01htywt2sr4z9ak01nk0avsk19))
- With the new pattern, when a case is checked we know that all previous ones have failed, and so we may simplify the conditions ([View Highlight](https://read.readwise.io/read/01htz4v2xm979780mmn2dan29r))
- Boolean operators also have an order ([View Highlight](https://read.readwise.io/read/01htywww0gjw2vmwghh85d7sgq))
- negations are evaluated first, then conjunctions, and finally disjunctions ([View Highlight](https://read.readwise.io/read/01htywx0d6dyj9hh36794q165a))
- the simplification done depends on the order in which the cases are checked ([View Highlight](https://read.readwise.io/read/01htz4x0rd3vqe2kfht34desmm))
- always use parentheses in expressions with more than one Boolean operator ([View Highlight](https://read.readwise.io/read/01htyx5v0728qkt6ya8dz0h7g4))
- whilst there are many algorithms to solve the same multiple-case problem, it’s best to check cases in a systematic order ([View Highlight](https://read.readwise.io/read/01htz58hs3fhqddq5ybr5hy9wr))
### 4.5 Generate a sequence
#### 4.4.3 Program: nested ‘if’ statements
#### 4.5.1 Initialise and generate
- The disadvantage of Pattern 4.3 is that *all* cases are always checked, even though only *one* will be handled ([View Highlight](https://read.readwise.io/read/01htz1v2ypqprm7tt6p2mpmg86))
- A sequence generation problem involves generating values, one by one, until some termination condition that stops the generation occurs. ([View Highlight](https://read.readwise.io/read/01htz5f2ecv4t6w8kp7j07wzjn))
- A more efficient algorithm doesn’t check any further cases as soon as it detects which case the input falls into. The trick is to ‘nest’ the cases inside each other ([View Highlight](https://read.readwise.io/read/01htz1w1xreanjg1ymabwt3dyy))
- The repeat-until loop provided in TM111 Block 2 Part 4 first does one iteration and then checks the termination condition, whereas a while loop first checks the condition and then does one more iteration or not ([View Highlight](https://read.readwise.io/read/01htz5y55fxbsc7bchjm49y898))
- ‘Otherwise if’ can be directly translated to Python’s `elif` ([View Highlight](https://read.readwise.io/read/01htz2bs9d4cbq732bpnf1syeb))
- The pattern assumes that the sequence isn’t empty, i.e. at least one value has to be generated. It also assumes that the next value is based on the current value, and therefore a single variable suffices ([View Highlight](https://read.readwise.io/read/01hv0psmcpx2ndffwy9w767the))
- There can be at most one `else` part, and it has to be the last part of the `if` statement, serving as a ‘catch-all’ for when the input doesn’t fall into any of the previous cases ([View Highlight](https://read.readwise.io/read/01htz2djakw0ddrmqjjs7fn0q4))
#### 4.5.2 Terminate
#### 4.5.3 Infinite loops
