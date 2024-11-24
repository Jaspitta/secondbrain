# Block 1 Part 2: Introduction to [[problem solving]] in [[Python]]

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/153302623/wSYx2X6JF1nJg4wKXULB6FES6SI_Zdlbm0qp7SqxC3k-cove_w31KWDX.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 1 Part 2: Introduction to [[problem solving]] in [[Python]]
- Category: #books
- Summary: Block 1 Part 2 introduces [[Python]] [[programming]], highlighting it as a problem-solving process that requires thinking about a problem, [[decomposing]] it, and then writing code. [[Algorithms]] play a crucial role in [[programming]], providing a clear sequence of steps to follow. The text discusses the importance of decomposition in solving problems and the translation of [[algorithms]] into [[computer code]]. It also explains how to use iteration and loops to simplify program design and implementation in [[Python]], focusing on drawing shapes like squares and triangles.

## Highlights
- [[Programming]] is about solving problems ([View Highlight](https://read.readwise.io/read/01hsaqtrs85x39kg0yzbbr0nb6))
- closely related to many things we do every day ([View Highlight](https://read.readwise.io/read/01hsaqtzwpy8jh8t4235j54g36))
- In general, we solve problems by [[decomposing]] them ([View Highlight](https://read.readwise.io/read/01hsaqv6f44mzrmch7xpk2xrj7))
- [[Python]] is a great language for beginner programmers as small programs can be quickly and easily written ([View Highlight](https://read.readwise.io/read/01hsaqvjhhxs3n1g70396a807m))
#### Strategies for success
- [[Programming]] is an activity where it is sometimes assumed that success is highly dependent on an innate ability ([View Highlight](https://read.readwise.io/read/01hsar00hysfnvdmd8knp8rfmv))
- the approach taken to learning is key ([View Highlight](https://read.readwise.io/read/01hsar078h9m378vv8y4htwx8x))
- [[Deep learning]] is more concerned with understanding material and making connections ([View Highlight](https://read.readwise.io/read/01hsaqz2hdt58646yjk9j2mkt6))
- the study found evidence that [[deep learning]] was a more successful strategy ([View Highlight](https://read.readwise.io/read/01hsaqz8mx6qpmj70ph4yr4kg7))
- one of the key determinants of success in that domain is if students believe the brain is plastic ([View Highlight](https://read.readwise.io/read/01hsar1dp394jr7qj37baz6kjk))
- the brain essentially has two modes: a [[focused mode]], where attention is on very particular aspects; and a [[diffuse mode]], where attention is much less focused ([View Highlight](https://read.readwise.io/read/01hsar28qdynk7jxxcd0bwnrsc))
- the diffused mode where connections are made ([View Highlight](https://read.readwise.io/read/01hsar2f9gmxdt62k070z5ajej))
- three points (preference for [[deep learning]], belief that learning can occur, need for focused and [[diffuse thinking]] ([View Highlight](https://read.readwise.io/read/01hsar3fvynajk2vbtvrgyyzvd))
- focused learning requires concentrated work. So when it is going well, keep going – but if you are struggling, do not lose belief in your ability to learn ([View Highlight](https://read.readwise.io/read/01hsar57f5r5kbxzqzj5tjj962))
- a good strategy is regular study with short breaks within a study session ([View Highlight](https://read.readwise.io/read/01hsara43d9yyh482j0p9t03c5))
- combined with reviewing earlier material ([View Highlight](https://read.readwise.io/read/01hsarapy8sr4n5nkpjkcdjr85))
- discussing issues with others. ([View Highlight](https://read.readwise.io/read/01hsarbaem1kzeb4ezng3vc5cs))
- the [[Pomodoro Technique]] ([View Highlight](https://read.readwise.io/read/01hsarcpfs0xxtvcfg5nawhbp2))
- If you cannot achieve a goal in 25 minutes, no problem; the good thing is you now have a goal carried over for tomorrow ([View Highlight](https://read.readwise.io/read/01hsare75bddmtrn3s8ssg2fbb))
- you are learning how much you can get done in 25 minutes ([View Highlight](https://read.readwise.io/read/01hsarf1am0mbvkm2q6trvj5q0))
#### Strategies for [[problem solving]]
- Often when solving a problem, I can adapt a solution to one solved earlier ([View Highlight](https://read.readwise.io/read/01hsarvxyngkw7nzxkv5vm1s8a))
- This ability to reuse solutions is key ([View Highlight](https://read.readwise.io/read/01hsarweyptjt9aew17jajqxn7))
- a key aspect of software construction ([View Highlight](https://read.readwise.io/read/01hsarxeada2f5sn1jjbg26f3j))
- thrown up many tools and ideas ([View Highlight](https://read.readwise.io/read/01hsarxzeda1m8jhzj8vq0yfek))
### 2.1 [[problem solving]] using decomposition
#### 2.1.1 [[Algorithms]]
- An [[algorithm]] tells us or a [[computer]] how to carry out a task ([View Highlight](https://read.readwise.io/read/01hsas18h5xyap2fbs9nqtyv66))
- self-contained ([View Highlight](https://read.readwise.io/read/01hsas1wx6qe3vn221vfvsgpzx))
- allows anyone following the algorithm to organise their work ([View Highlight](https://read.readwise.io/read/01hsas2begfej37jsgx9mxbec8))
- Algorithm ([View Highlight](https://read.readwise.io/read/01hsasaff13v0p4qnnfmp78m8y))
- an odd word ([View Highlight](https://read.readwise.io/read/01hsasan61jetxte1wnhftmfws))
- derived from Arabic ([View Highlight](https://read.readwise.io/read/01hsasar0xqvcxdgfj5cmdgm3z))
- It honours [[Muhammad ibn Musa al-Khwārizmī]] ([View Highlight](https://read.readwise.io/read/01hsasb03qy14fr0raeyn5fzew))
- profound insights into algebra (another Arabic word, of his invention ([View Highlight](https://read.readwise.io/read/01hsasb4w0x95pregj9csbbbqp))
- the idea of using a step-by-step approach to solving mathematical problems long pre-dates his work ([View Highlight](https://read.readwise.io/read/01hsasdtk2ey1qvcs7g2zss1sm))
- [[algorithms]] we meet in everyday life – such as recipes or instructions ([View Highlight](https://read.readwise.io/read/01hsasrdc16qw39txbser93q5q))
- brief recap of material covered in TM111 ([View Highlight](https://read.readwise.io/read/01hsda1w53460x3smvcpjgshw6))
- simple rules ([View Highlight](https://read.readwise.io/read/01hsda2cb5zy69nashhpwnnfe8))
- only perform one action at a time ([View Highlight](https://read.readwise.io/read/01hsda2j93jbswv0a3yryax4p6))
- new action once we have completed the current action ([View Highlight](https://read.readwise.io/read/01hsda2wf85sa0npp6fak4h7wa))
- we can only go to the next action in the sequence. ([View Highlight](https://read.readwise.io/read/01hsda39f1t497hgc5efmv9n47))
- cannot return to an earlier action after we have completed it ([View Highlight](https://read.readwise.io/read/01hsda3jkppfyj7b21tym2v19z))
- finished the last action, we have completed ([View Highlight](https://read.readwise.io/read/01hsda43xrwjzk3kvt7xp7nj2j))
- the outcome of performing an action is dependent on the outcome of previous steps ([View Highlight](https://read.readwise.io/read/01hsda9aykpbwx3wdr7x0wqzcj))
- while English is easy to understand and familiar, it has many ambiguities ([View Highlight](https://read.readwise.io/read/01hsdaag2c4aysdhj9w1c4fgmd))
- language, containing a restricted number of words and a precise structure (known as its syntax), is needed. ([View Highlight](https://read.readwise.io/read/01hsdab15pnx8wnpfb4nczc6ey))
#### 2.1.2 Make life simple: [[algorithms]] in simple English
- Rather than settle on writing our [[algorithms]] in one particular [[programming language]], we will write our [[algorithms]] by expressing them in simple English. Our goal is to represent [[algorithms]] clearly, allowing a reader to trace the order in which steps are executed and test that an algorithm produces the intended result. Such [[algorithms]] can later be translated into our [[computer language]] of choice – in other words, implemented on the [[computer]]. ([View Highlight](https://read.readwise.io/read/01hsdahceqtanznhvdg7nfb89f))
- goal is to represent [[algorithms]] clearly ([View Highlight](https://read.readwise.io/read/01hsdajvvh4vmra4ezz7k7qz7t))
- trace the order ([View Highlight](https://read.readwise.io/read/01hsdak3fv7g370e0s3vkv5mt4))
- test ([View Highlight](https://read.readwise.io/read/01hsdak79f04f67z94cx0p0cmv))
- Such [[algorithms]] can later be translated into our [[computer language]] of choice ([View Highlight](https://read.readwise.io/read/01hsdakem0kjh16x12g2ase07k))
##### How we write [[algorithms]]
- series of steps expressed largely in ordinary natural language ([View Highlight](https://read.readwise.io/read/01hsdarzjjt165g6yx10c9eagn))
- in a structured way ([View Highlight](https://read.readwise.io/read/01hsdas704mnwe0d6cqnyr8jq1))
- solve a problem by [[decomposing]] (dividing) it into steps that solve it ([View Highlight](https://read.readwise.io/read/01hsdasbwex5ge5xy0ja3njk77))
- we may first decompose it into sub-problems ([View Highlight](https://read.readwise.io/read/01hsdasp4ewqks4k4v35mg5hq6))
- key thing is that by dividing up problems, we either solve them or express them as simpler sub-problems. ([View Highlight](https://read.readwise.io/read/01hsdb04q654scp6y7tnyb5jve))
- The key thing is that a task can be broken into steps. Somebody who knows how to do the individual steps can make a cup of tea by following the algorithm ([View Highlight](https://read.readwise.io/read/01hsdb2j6ktft2aab01vzwtjpt))
- 2.1.3 [[Programming]] and robotic turtles ([View Highlight](https://read.readwise.io/read/01hsdbchqxj2j7t08ec9pbb4j1))
- we need to keep [[decomposing]] until the steps of our algorithm are simple enough to translate into single lines of a [[programming language]]. ([View Highlight](https://read.readwise.io/read/01hsdbdq6axsee2tf5axyx0kb0))
- the language we are using is [[Python]] ([View Highlight](https://read.readwise.io/read/01hsdbekw8eg8w6t5jc3v3q7t6))
- we will program a robotic turtle. This is a turtle that can be instructed to move around a two-dimensional space, leaving a trace of its movement using a coloured pen ([View Highlight](https://read.readwise.io/read/01hsdbhf3ra7v9ngq9y16wjmdc))
- nice thing about learning to program by writing programs to draw things is that you will quickly be able to see any mistakes you have made ([View Highlight](https://read.readwise.io/read/01hsdbjp2ryzm1t79sq61cf7g5))
- line starting with a `#` symbol is known as a comment ([View Highlight](https://read.readwise.io/read/01hsdbn2182xhjwsnnbc8jfdbd))
- from turtle import * ([View Highlight](https://read.readwise.io/read/01hsdbrnpsbsw2yjc47rnpzhhf))
- you can think of the next line as saying we want to be able to work with turtles ([View Highlight](https://read.readwise.io/read/01hsdbrcqjjqamqasv5wntd5cm))
- forward(40) ([View Highlight](https://read.readwise.io/read/01hsdbrvrgye1fvdzgtfj9zrdq))
- move forward by 40 units. ([View Highlight](https://read.readwise.io/read/01hsdbsc8jtndbrkqqj58mmsky))
- The turtle always starts pointing horizontally to the right ([View Highlight](https://read.readwise.io/read/01hsdbsskm49pmgtr26y7k3etx))
- [[Python]] is very strict on layout ([View Highlight](https://read.readwise.io/read/01hsdc1g2nb7wc54a6bjqve7rb))
- Our first line uses a ‘>’ symbol, which shows that the first line is a heading ([View Highlight](https://read.readwise.io/read/01hseberc9eq6nkqf3p3wxy54h))
- in general, such an algorithm can be used to produce our original program by translating each line ([View Highlight](https://read.readwise.io/read/01hsebjpg35136srhx6xxd9ybk))
- We will refer to this translation process as implementing the algorithm ([View Highlight](https://read.readwise.io/read/01hsebkyz3tqjw96wsrra8w4tx))
- operations seen so far have a name and, in brackets, a number ([View Highlight](https://read.readwise.io/read/01hsebwvzav1dqh2q0qcrvwwzr))
- The number in brackets is a parameter – it allows us to specify in more detail what we want the operation to do ([View Highlight](https://read.readwise.io/read/01hsebx4k3b0mnxv70syne7c69))
- This ability to parametrise operations is one of the things that makes a [[programming language]] a powerful ([View Highlight](https://read.readwise.io/read/01hsebxdtake177wc0dkr7ge5x))
#### 2.1.4 Drawing some simple shapes through decomposition
- our solutions to problems are a sequence of steps ([View Highlight](https://read.readwise.io/read/01hsfwbgdrd3rys4jz918ysmph))
- we are saying how to solve a problem by carrying out simple steps ([View Highlight](https://read.readwise.io/read/01hsfwbmp7tgkbwx4e86qmyv09))
- the steps are ones that are either trivial or easy ([View Highlight](https://read.readwise.io/read/01hsfwbvyn3eycvz6htmbcm4g4))
### 2.2 Iteration
#### 2.2.1 Everyday problems that need repetition
- walk 10 000 steps per day to stay fit ([View Highlight](https://read.readwise.io/read/01hsfwnyn739ajzbrsgrmc5pzx))
- The next three lines are a decomposition of the line above, which start to achieve the task it sets out. ([View Highlight](https://read.readwise.io/read/01hsfwqq53k18m1vgn7sxs3zk8))
- I want a way of writing down something that repeats a number of times ([View Highlight](https://read.readwise.io/read/01hsfwr6kpw4tyz8pf66s4avf2))
- We will have a variable called ‘step-counter’, ([View Highlight](https://read.readwise.io/read/01hsfwszp9h26z7sj4apv4s24p))
- increasing the value. We also need to stop after 10 000 ([View Highlight](https://read.readwise.io/read/01hsfwt4fbhdksnymd1ab0xgvs))
- use the keyword ‘for’ to show that we want to do something for a number of times ([View Highlight](https://read.readwise.io/read/01hsfwth7bv95m2m2zpks89m2f))
- start, the value of step-counter is set to 1 ([View Highlight](https://read.readwise.io/read/01hsfwvn9qa4xajttw1svwxage))
- take a step and increase the value ([View Highlight](https://read.readwise.io/read/01hsfwvvs67pz4c7819nqrn99z))
- We ask whether the step-counter has exceeded 10 000 ([View Highlight](https://read.readwise.io/read/01hsfww164say1bkjmb8df3qt0))
- continues until after we have done 10 000 steps ([View Highlight](https://read.readwise.io/read/01hsfx11b2sc0chjb86mb1f78f))
- For step-counter from 1 to 10 000 ([View Highlight](https://read.readwise.io/read/01hsfx180vvnpvegjzhztwwem4))
- we have a line in our algorithm, ‘Walk a step’, that will be carried out 10 000 times ([View Highlight](https://read.readwise.io/read/01hsfx28nt4pqw0vg7x5990s8n))
- This is an example of iteration: something gets carried out a number of times ([View Highlight](https://read.readwise.io/read/01hsfx5w7yhr9nt7vnvy35ved2))
- Another way used to refer to this is to say that we have a [[loop]] ([View Highlight](https://read.readwise.io/read/01hsfx6086s1y6f630aryvmjxs))
#### 2.2.2 Making choices
- we can see that we want to click every time the value in our steps variable gets to a multiple of 10 ([View Highlight](https://read.readwise.io/read/01hsfxcb8f1sn6k7wm9zwzcqay))
- This is an example of a conditional statement ([View Highlight](https://read.readwise.io/read/01hsfxda4wwqapme9w4yh5ee6y))
- Notice that the if keyword is indented at the same level as ‘Walk a step’ ([View Highlight](https://read.readwise.io/read/01hsfxf67y6r2d7tjnp2tjyw9n))
- The click step is indented further, to show it is conditional on the condition expressed by the if statement ([View Highlight](https://read.readwise.io/read/01hsfxfxncwznsabkk2rqyx778))
#### 2.2.3 [[Programming]] for repetition
- [[Python]] has a [[programming]] construct that corresponds to the way we have done iteration before ([View Highlight](https://read.readwise.io/read/01hsfxtdsgj9ptgtkavnjze382))
- By [[programming]] construct, I mean a keyword – for – and a way of structuring code that [[Python]] recognises as having a particular meaning ([View Highlight](https://read.readwise.io/read/01hsfxtypc3gp5m11cr4ykv0pg))
- `range(1, 11)` means that the range of numbers starts at 1, counts upwards by 1 and stops just before 11. ([View Highlight](https://read.readwise.io/read/01hsfy087jx13gyxp9bj24teny))
- Note also the colon at the end of the line `for section in range(1, 11):` ([View Highlight](https://read.readwise.io/read/01hsfy1d60g3293m6bcatb7p6m))
- the colon is, in effect, an extra hint that this is about to happen ([View Highlight](https://read.readwise.io/read/01hsfy6ekafrch20h5xv9v6d3b))
- we will use four spaces when indenting in [[Python]]. ([View Highlight](https://read.readwise.io/read/01hsfy6pv16j294wcqvczd1kvg))
- [[Python]] is particular about this layout, as the layout is used to indicate the structure of the code ([View Highlight](https://read.readwise.io/read/01hsfy92j8y8hxyn3pz43yw45w))
- In [[Python]], when we specify a range using just one number, then the range starts at 0. In this case, when using `range(10)`, we get a range of whole numbers from 0 to 9 ([View Highlight](https://read.readwise.io/read/01hsfyan6a4pc0vpgsbt4z65fn))
- shorter and clearer ([View Highlight](https://read.readwise.io/read/01hsfyb4rcsts669wsm2ggeak4))
- In later parts, we will use `range(n)` where we want something done *n* times, and where starting at 0 is not a problem. ([View Highlight](https://read.readwise.io/read/01hsfydzz867rrpt85mcg6fv3v))
#### 2.2.4 A more powerful approach to design
- we can think about a more powerful approach to design ([View Highlight](https://read.readwise.io/read/01hsgzjaq1p6aqbbgjhrvce778))
- design and implement a program to draw two squares, one below the other, with a gap in between ([View Highlight](https://read.readwise.io/read/01hsgzjqnqpg59r09d7ydxyqww))
- previously ([View Highlight](https://read.readwise.io/read/01hsgzke2pbv5se6qgr95d5170))
- we mostly translated it into appropriate [[Python]] on a statement-by-statement basis ([View Highlight](https://read.readwise.io/read/01hsgzmta8m1q741y9y56404y4))
- now decomposed my problem into sub-problems, rather than steps. ([View Highlight](https://read.readwise.io/read/01hsgzphrcd5gkj1v1y3trwh2t))
- reusing solutions is a mature approach to program design ([View Highlight](https://read.readwise.io/read/01hsgzr4f4103ftqm2343q0mjj))
- cutting and pasting code does allow for errors to slip in ([View Highlight](https://read.readwise.io/read/01hsgzsdbmdffgm6t86je7x0np))
- we will see better of ways of reuse ([View Highlight](https://read.readwise.io/read/01hsgzt2md0fz0arf6ebd341v0))
- I have decomposed the sub-problems ([View Highlight](https://read.readwise.io/read/01hsgztd2q9ryskqypa3jyy1a2))
- I have also decomposed the problem ([View Highlight](https://read.readwise.io/read/01hsgztpx73atebq4ajx6fxxdp))
- I have indicated the sub-problems being decomposed ([View Highlight](https://read.readwise.io/read/01hsgztv4dqyvhajs1972hy2rr))
### 2.3 Problems
#### 2.3.1 A triangle problem
- iteration where we need to do things *several* times ([View Highlight](https://read.readwise.io/read/01hsh0aer4g1rtq61j1axrdjmf))
#### 2.3.2 A three-triangle problem
#### 2.3.3 Drawing a stick person
#### 2.3.4 Drawing a house
### 2.4 Using lists for flexibility
#### 2.4.1 Drawing a graph of a fixed number of points
- how to draw a line graph ([View Highlight](https://read.readwise.io/read/01hsh0yaj9a3sj760s217ss6fs))
- we will use variables to hold the sales of gloves for each quarter ([View Highlight](https://read.readwise.io/read/01hsh14nh6g8hkn4vdctxhcsgq))
- [[Python]] has, like many [[programming]] languages, a construct called assignment. ([View Highlight](https://read.readwise.io/read/01hsh14bxz3s047tc21a3p0npn))
#### 2.4.2 Working with simple lists
- we would like a way of holding the glove data together and being able to access it in a flexible way. ([View Highlight](https://read.readwise.io/read/01hsh1q3mjhnjs1empn5vt96bg))
- We are now working with a variable that refers to a list of numbers ([View Highlight](https://read.readwise.io/read/01hsh1qge5wtmwza318m90150k))
- [[Python]] allows me to access a position in the list by saying:
  gloves[0] ([View Highlight](https://read.readwise.io/read/01hsh1r3pg3dm56k2kv4h0fnq8))
- The value in the square brackets is known as an index ([View Highlight](https://read.readwise.io/read/01hst5knwm2kq4we4k9z493rzk))
- first value in the list has index 0 ([View Highlight](https://read.readwise.io/read/01hst5kygxtpjwvawkqg2qmh1y))
- refer to the values in the list as its elements ([View Highlight](https://read.readwise.io/read/01hst5n5twamkpvxhk1q76g4yq))
- often useful to be able to find the size of a list. [[Python]] allows us to do this by writing, in our case, `len(gloves)` ([View Highlight](https://read.readwise.io/read/01hst5p9y78bk0sndmfd9cgk61))
- when I combine lists and loops. I can write in [[Python]]:
  total = 0for index in range(0, len(gloves)):  total = total + gloves[index] ([View Highlight](https://read.readwise.io/read/01hst5pxac37xmy4nx6e84dp88))
- combining the use of lists and a [[loop]] allows us to write programs that deal with a varying number of items in a very flexible way ([View Highlight](https://read.readwise.io/read/01hst5vadqmww670g24dndq363))
#### 2.4.3 Practical work with lists
- In order to produce numerical outputs, we will use a new feature of [[Python]]: its `print` statement ([View Highlight](https://read.readwise.io/read/01hst5yxcs04rx9gg872z9syak))
#### 2.4.4 Another example of the power of using lists and loops
### 2.5 [[Nested iteration]]
#### 2.5.1 Independent [[nested loops]]
- use looping as a way of concisely expressing the solution to a problem where something needs to be done several times ([View Highlight](https://read.readwise.io/read/01hst6ctamsbwfs1kx2bajgeyh))
- Sometimes we use loops within loops (embedded loops) to solve more complex problems ([View Highlight](https://read.readwise.io/read/01hst6daazzqamem8g7k03wcfj))
- Consider the problem of producing a ‘times table’: a table showing all the possible multiplications of two numbers between 1 and 12, in order ([View Highlight](https://read.readwise.io/read/01hst6ga3qn2zvk4nnanh3f19t))
- we have used a variable (Set *size* to 12) to specify the total number of times around the [[loop]]. This is good practice as it makes our design much easier to change ([View Highlight](https://read.readwise.io/read/01hst6mnfwygbz1trsgvwjtwze))
- try to avoid having loops that contain actual numerical values, since that is inflexible ([View Highlight](https://read.readwise.io/read/01hst6n9s756jdahxb3mk18af0))
- We want the numbers from the inner [[loop]] to appear in a single ([View Highlight](https://read.readwise.io/read/01hst6vzmfyw11wprqyteg6j3q))
- `print` allows us to specify what should follow whatever is being printed ([View Highlight](https://read.readwise.io/read/01hst6wba905vqaddavepfhw0b))
- We need to include `end = ...` any time we don’t want `print` to move to a new line ([View Highlight](https://read.readwise.io/read/01hst6wzd64cqqgbjdjxm6qdr7))
- 2.5.2 [[Programming]] the turtle using [[nested loops]] ([View Highlight](https://read.readwise.io/read/01hst783vv3gqhjr3qf79xdbfe))
#### 2.5.3 Dependencies between [[nested loops]]
- the index of the inner [[loop]] is dependent on the outer [[loop]] ([View Highlight](https://read.readwise.io/read/01hst7pyyy2dy8pj26rnkrjjrb))
- 2.5.4 More turtle programs using [[nested loops]] ([View Highlight](https://read.readwise.io/read/01hst7xgj7q27k58pk49gf1z98))
