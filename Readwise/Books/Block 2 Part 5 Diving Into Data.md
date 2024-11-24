# Block 2 Part 5 Diving Into Data

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/177691990/U6e1K1FC5AczzBbi0vh75vA8E24SmYt4AJRA-MqdrrI-cove_P8Rm5yA.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 2 Part 5 Diving Into Data
- Category: #books
- Summary: The text explores measuring happiness using data collected by the UK government. It demonstrates how Python can be used to analyze and summarize happiness data over multiple years. The focus is on understanding trends in happiness levels through data analysis.
- URL:

## Highlights
### Introduction
- Data analysis consists of taking a set of data and computing something from it – ‘crunching the numbers’ – to extract information ([View Highlight](https://read.readwise.io/read/01hyts65nqtpawa67vy7aenwgp))
- calculating an average ([View Highlight](https://read.readwise.io/read/01hyts828dt4a8xdrwwnghzgdv))
- Jacob Köbel ([View Highlight](https://read.readwise.io/read/01hyts9vnq4hdgqm7m56c5pabm))
- His clever solution was to get 16 volunteers to stand in a line as shown in Figure 5.1, find the overall distance, then split it into 16 equal parts. ([View Highlight](https://read.readwise.io/read/01hyts9k3q0da5gc0efvevda5b))
- in the modern world, datasets can be huge ([View Highlight](https://read.readwise.io/read/01hytsakn2zbjkszb281m9w1ap))
- Python is well suited for data analysis ([View Highlight](https://read.readwise.io/read/01hytsay63kzzyb3h0w5cgsgv2))
- Before starting, we need to decide what questions we hope to answer ([View Highlight](https://read.readwise.io/read/01hytsba7ynne0dvdttv9g4m85))
- before diving into the data analysis, we’ll take a deeper look at creative problem solving and introduce the idea of heuristics – ‘rules of thumb’ ([View Highlight](https://read.readwise.io/read/01hytsebcb8339fb4baf7g73aw))
### 5.1 The creative problem solver
#### 5.1.1 Problem solving as a process
- for most of our human history, problem solving was just something people did ([View Highlight](https://read.readwise.io/read/01hytsjnf4hapxrh255fzk65t3))
- very recently have people thought about problem solving itself as a process that can be studied ([View Highlight](https://read.readwise.io/read/01hytsk29q9xbvq3wma4kyqda7))
- One of the pioneers was the Hungarian mathematician George Pólya ([View Highlight](https://read.readwise.io/read/01hytska6d2c1xzyfpqcsn8n99))
- in a ground-breaking book *How to Solve It* ([View Highlight](https://read.readwise.io/read/01hytske9c615menctv3zsfp3v))
- problem solving is a process with four stages ([View Highlight](https://read.readwise.io/read/01hytsm5t8xc7a5rjq3m0x63xq))
- Pólya’s interest was in mathematical problems, but we have adapted his ideas ([View Highlight](https://read.readwise.io/read/01hytsn6v3wgz4ma860j55sdxk))
- Understand the problem ([View Highlight](https://read.readwise.io/read/01hytsnefajrpa3ztry3q1a2hf))
- clear idea of where we are starting from and what we want to get out of it ([View Highlight](https://read.readwise.io/read/01hytt0ejz1rwxntj3s3t1m4nq))
- Make a plan ([View Highlight](https://read.readwise.io/read/01hytsnh0dg93fck1c555vhmpb))
- devising an appropriate algorithm ([View Highlight](https://read.readwise.io/read/01hytt1r4k736gsy9664dem7cq))
- very useful guidelines, generally called heuristics ([View Highlight](https://read.readwise.io/read/01hytt31ntvzrtgzptd1eymv1n))
- Carry out the plan ([View Highlight](https://read.readwise.io/read/01hytsnk9j5nczth66skgdg576))
- Write and test code ([View Highlight](https://read.readwise.io/read/01hytt3mv5z8pykcyyvr1xdprt))
- Look back ([View Highlight](https://read.readwise.io/read/01hytsnsg5e54f8zxy4w1p6e0h))
- Heuristics are methods of discovery and invention ([View Highlight](https://read.readwise.io/read/01hytt4w2pn51fsz73twgm3bay))
- rules of thumb that we can use to help us solve problems ([View Highlight](https://read.readwise.io/read/01hytt6cd0x790k9y0jaj6qc2p))
#### 5.1.2 Heuristics in action
- learn to recognise when it can be applied ([View Highlight](https://read.readwise.io/read/01hyttc85cae6zabvvtbqrv737))
- This idea, of bootstrapping from a small beginning, occurs often ([View Highlight](https://read.readwise.io/read/01hyttg2chxy2m5mpbgrfcysb6))
### 5.2 A data analysis project
- we have chosen to look at some questions about happiness and well-being, as measured by data from the Office for National Statistics ([View Highlight](https://read.readwise.io/read/01hywaaztaazf6wweccg8xx6sd))
#### 5.2.1 Working with data in Python
- Between each number and the next is a separator, which is a comma, and this way of representing data is known as comma-separated values (CSV). ([View Highlight](https://read.readwise.io/read/01hywbb1cbhzbhex0hha7z5y0w))
#### 5.2.2 Getting started on the data
- Opening a file in Python ([View Highlight](https://read.readwise.io/read/01hywmsdrschv75kd87z9p67rv))
- file = open('happ_1.txt', 'r') ([View Highlight](https://read.readwise.io/read/01hywms8y1294tjmsmccq97pz8))
- The second argument `'r'` tells Python we want to read from the file. (To write to it, we would use `'w'`.) ([View Highlight](https://read.readwise.io/read/01hywmsye9rqf4z89ns9kf4t1z))
- A file consists of a series of lines ([View Highlight](https://read.readwise.io/read/01hywmtkx58g32fvf80jwdcj6g))
- file = open('happ_1.txt', 'r') 
  for line in file: 
  print(line) ([View Highlight](https://read.readwise.io/read/01hywmtvm0ggwhsq52k3s981gr))
#### 5.2.3 Working out an average
- we will work out the average for each year and compare the results ([View Highlight](https://read.readwise.io/read/01hywn52a9hsqnx35w4fkwmr0s))
- There is more than one kind of average ([View Highlight](https://read.readwise.io/read/01hywn5fvdjwb3pf73ec5s8186))
- we find the mean by summing the numbers, then dividing by how many numbers there are ([View Highlight](https://read.readwise.io/read/01hywn6anqpn7wkfww99cp600r))
- We can’t just average the percentages; we have to take the ratings into account as well ([View Highlight](https://read.readwise.io/read/01hywncr1626fvxf96v0ak4ga0))
##### Averaging star ratings
- For simplicity, let’s imagine exactly 100 people rated Book A. Then out of those 100 people, 9 awarded 0 stars, 27 awarded 1 star, 26 awarded 2 stars, and so on. ([View Highlight](https://read.readwise.io/read/01hywns9tyhn6ch07tdqkt62q8))
- There were a total of 219 stars and 100 people, so the average rating is 219 ÷ 100 = 2.19. ([View Highlight](https://read.readwise.io/read/01hywntvs8j6sbexwtt1zqj0g8))
##### Implementing the algorithm
- If we think of the table as a series of rows, with every row being a list, then we can represent the table as a *list of lists* ([View Highlight](https://read.readwise.io/read/01hyxamz6c2cprtfyj97hr47tk))
#### 5.2.4 Getting the data in the form we want
- but it turns out each row is actually a string, not a list at all ([View Highlight](https://read.readwise.io/read/01hyxb3tw41hv51r4fvtvbe8qg))
- convert each row into a list of separate values ([View Highlight](https://read.readwise.io/read/01hyxbc6f8vb9bpp0kenxvw6yk))
- use the Python CSV reader, which is in a Python module `csv` ([View Highlight](https://read.readwise.io/read/01hyxbchry55vzge3b6agxcnea))
- import csv ([View Highlight](https://read.readwise.io/read/01hyxbd8c4ekzt4znnfx1mdp6f))
- table =[] ([View Highlight](https://read.readwise.io/read/01hyxbe06fqrsmkjh0gcnpm7f1))
- reader = csv.reader(file) ([View Highlight](https://read.readwise.io/read/01hyxbdrn4gmbedwmppxh4g162))
- for row in reader: ([View Highlight](https://read.readwise.io/read/01hyxbe5997nfc6731w05f0hv1))
- table.append(row) ([View Highlight](https://read.readwise.io/read/01hyxbe7adnacd5311a327q9m1))
- A CSV reader automatically splits a string of comma-separated values ([View Highlight](https://read.readwise.io/read/01hyxbf97pcd2jrkxrtzxd22f3))
##### Introducing `table_utils`
- a well-known library for data analysis in Python called `pandas` ([View Highlight](https://read.readwise.io/read/01hz1gyfjt52fjcyeys3jjeb79))
- instead we have written our own small library `table_utils` ([View Highlight](https://read.readwise.io/read/01hz1gzw69yykew6h85cvxbjzj))
- `rows()` takes three arguments: a table, a start row and an end row ([View Highlight](https://read.readwise.io/read/01hz1h04nxpj4madhn56418mmp))
- returns a new table containing just the rows ([View Highlight](https://read.readwise.io/read/01hz1h0jbqqcw9v0t6q6zpf05b))
- `cols()` takes three arguments: a table, a start column and an end column ([View Highlight](https://read.readwise.io/read/01hz1h0sz8syg3cq4wgfyzwp1m))
- returns a new table containing just the columns beginning ([View Highlight](https://read.readwise.io/read/01hz1h100wzsfj9zp9r23w76c3))
- `flip()` takes one argument, a table ([View Highlight](https://read.readwise.io/read/01hz1h1d9scjaj6srazptkjfbw))
- returns a new table like the original but with the rows and columns interchanged ([View Highlight](https://read.readwise.io/read/01hz1h1jpfqnew5xw1an2qrryd))
- `to_float()` function takes a table as argument and returns a new table with all the strings in the table converted to their equivalent floating-point values, where possible ([View Highlight](https://read.readwise.io/read/01hz1h3cfrdta0bsvwngcq3jmw))
#### 5.2.5 More on summarising data
- we should only use the mean when the data measures a quantity such as weight or height ([View Highlight](https://read.readwise.io/read/01hz1hds49n2b6wga993jppe3f))
- points on an arbitrary scale (such as happiness) don’t represent a real quantity ([View Highlight](https://read.readwise.io/read/01hz1hdzb669yhrsbhmzd4xby3))
- We can’t really say that someone who rates their happiness as 10 is twice as happy as someone who rates theirs as 5. ([View Highlight](https://read.readwise.io/read/01hz1he8p852z8bpwbnef09cet))
- there is another form of average we could use: the median ([View Highlight](https://read.readwise.io/read/01hz1hf3ckp11xxbcqcwktqw1v))
- The median is just the middle value when the data are sorted ([View Highlight](https://read.readwise.io/read/01hz1hxsxxvqn1rm00qkdq800m))
- If the number of data is even, so there are two middle values, we take the value halfway between them (their mean, in fact) ([View Highlight](https://read.readwise.io/read/01hz1hy6m5rdmrm3q0vwmbx2b4))
- The median and the mean are both measures of central tendency. They summarise where the centre of a dataset lies. ([View Highlight](https://read.readwise.io/read/01hz1j3q36tx9mt3mzstvf8x58))
##### Dispersion
- how spread out the data are ([View Highlight](https://read.readwise.io/read/01hz1j6hvawzfejrxda81xe0p4))
- One measure of dispersion that goes naturally with the median is the interquartile range ([View Highlight](https://read.readwise.io/read/01hz1j6w7z7tgn16rh7g60r9pt))
- the values that split the data into quarters ([View Highlight](https://read.readwise.io/read/01hz1jbx4vpjjw6gzyz3t82vqv))
##### Skew
- A dataset is skewed if the values are distributed unevenly about the average ([View Highlight](https://read.readwise.io/read/01hz415xfbe9mj0ds77p2j1gpw))
- there is quite a long tail off to the right. (The distribution is described as right-skewed ([View Highlight](https://read.readwise.io/read/01hz417b1kctsnt7hw5f1w44eb))
- to the left (also known as negative skew) or right (also known as positive skew) ([View Highlight](https://read.readwise.io/read/01hz417vdfcqw3b17qds4bea1k))
- When data is skewed, the median is often preferred to the mean ([View Highlight](https://read.readwise.io/read/01hz4183hfnm17sjskhrgjbzgb))
- if the median is used as the average, then by definition exactly 50% will be on or above the average ([View Highlight](https://read.readwise.io/read/01hz41cgkxw84zyqy88h2ek26m))
##### What about happiness?
##### 5.3 The geography of happiness
- 5.3.1 Understanding the data ([View Highlight](https://read.readwise.io/read/01hz42zwqw2aa2fs92bf8kxvbk))
#### 5.3.2 Extracting geographical information
- `table2 = filter_by('.92', 0, table1)` 
  `print(table2)` ([View Highlight](https://read.readwise.io/read/01hz4770b0qrgmtt8ymz49zpq0))
    - Note: keep values containing 92 from table1 column 0
- Python (and other languages) compares strings in a different way from numbers, using something called lexicographic order: the same rule as used to sort words in a dictionary ([View Highlight](https://read.readwise.io/read/01hz47bk7rgjnb2vjxqbey5tag))
- It compares strings by the first character – or if they have the same first character, by the second character ([View Highlight](https://read.readwise.io/read/01hz47c37xm6tbsxmkmj3b8k1x))
- if we have numbers represented as strings but want to sort them into normal numerical order, we must convert them to numbers first ([View Highlight](https://read.readwise.io/read/01hz47hrq45a5c44re6ggg0t6n))
- The algorithmic pattern for filtering a table on a given *condition* looks like this, with *table0* being the input and *table1* the output. ([View Highlight](https://read.readwise.io/read/01hz47rnx34m2qj4p76vkapz0x))
- initialise an empty table *table1*
  for each *row* in *table0*
  if *row* satisfies *condition*
  append *row* to *table1* ([View Highlight](https://read.readwise.io/read/01hz47rr1wx8brg945xwmq9frh))
- Sometimes our code doesn’t work and we just can’t figure out why.
  A very useful strategy in these circumstances is to find someone else to tell the problem to, because often stating a problem as clearly as possible will suggest its solution. ([View Highlight](https://read.readwise.io/read/01hz47w0ewwk2t6pwaj7bjmerw))
### 5.4 Correlation and all that
- finding the mean and the median are examples of aggregation problems. Finding the happiest location is an example of a retrieval problem ([View Highlight](https://read.readwise.io/read/01hz4ffb755e228vh0w8m98gqd))
- correlation, which describes a relationship between two datasets ([View Highlight](https://read.readwise.io/read/01hz4fjys9bqvfh8b80p67fgjj))
- form of aggregation problem ([View Highlight](https://read.readwise.io/read/01hz4fmt7vhh35hvrv11xkt5m9))
#### 5.4.1 Visualising and measuring correlation
- When the values in two datasets seem to change together, we say they are correlated ([View Highlight](https://read.readwise.io/read/01hz4fqrfkwzc1yvm9h2fvxws7))
- A good way of visualising a correlation is to use a scatterplot ([View Highlight](https://read.readwise.io/read/01hz4fqtgm00s8575wqg3vh32w))
- the one we will use is the correlation coefficient ([View Highlight](https://read.readwise.io/read/01hz4fttaa3n3ztq3eycw9w63n))
- a number calculated from the two datasets and always takes a value between +1 and –1. It is usually denoted by the letter *r* ([View Highlight](https://read.readwise.io/read/01hz4fv0yrp70hmw2pf26nadn0))
- +1 indicates the points all lie on or near a line with positive slope ([View Highlight](https://read.readwise.io/read/01hz4fy42mhacvngx8fjkevdz6))
- –1 indicates the points all lie on or near a line with negative slope ([View Highlight](https://read.readwise.io/read/01hz4fy97d0xkrdcbd7zxnxnrv))
- 0 indicates that the correlation between the variables is weak or non-existent ([View Highlight](https://read.readwise.io/read/01hz4fyjehrakxyky4v60q915n))
- For anyone who is blind or who has very low vision, an alternative way of representing the relationship between the variables is via the medium of sound. Rendering graphical information as sound is called sonification. ([View Highlight](https://read.readwise.io/read/01hz4g41p01h78c9s9cxth09pd))
##### Calculating and interpreting correlation coefficients
- `corr_coef()` takes two lists of numbers, which must be of equal length, and returns the correlation coefficient between them. ([View Highlight](https://read.readwise.io/read/01hz4ga6y9m45mpk5sqjsfbed4))
- The value of *r* is sometimes described as a way of measuring the ‘size of an effect’ ([View Highlight](https://read.readwise.io/read/01hz4gbz1njf47t49g8c2x6783))
#### 5.4.2 May you live long and prosper!
##### Mortality data
- Note that if greater happiness is associated with longer life, that corresponds to lower mortality. So we are looking for a negative correlation. ([View Highlight](https://read.readwise.io/read/01hz4gqadehce6nwqxwj55e2qy))
#### 5.4.3 Correlation is not causation
- When we say A *causes* B, we mean that A has somehow brought about B. The cause A is responsible for the effect B. ([View Highlight](https://read.readwise.io/read/01hz51mnr9rqx0w8hfdjy3aqhy))
