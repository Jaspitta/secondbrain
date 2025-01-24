# MST124 Unit 9

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/259327794/gasP0IhufG5bxmYw_18vYDgPM6XZWaVQk-qqB-gvxGo-cove_b0DFX4J.png)

## Metadata
- Author: [[The Open University]]
- Full Title: MST124 Unit 9
- Category: #articles
- Summary: This text discusses various operations that can be performed on matrices, such as addition, subtraction, and multiplication. It also introduces the concept of matrix inverses and their connection to systems of linear equations. The section emphasizes that while you can't divide matrices, there are methods that serve a similar purpose.
- URL: https://readwise.io/reader/document_raw_content/259327794

## Highlights
- , matrices are arrays of numbersused to hold information in an orderly way. In particular, they provide a useful way ofstoringdata thatcan be organised in rows andcolumns.
- arrays of numberscan be thought of as ‘multi-dimensional numbers’.For example,you canadd, subtractand multiply them,
### 1 Matrices andmatrix operations
#### 1.1Matrix notationand terminology
- In thismodule we’ll alwaysuse round brackets.
- We oftenuse capitalletters to denote matrices.For example,wemight write A = .
  12 −1 53 0 / , B = .
  1 3 2 1 / , C =   1 3 4 7 −6 22 0  .
- The numbersina matrix are calledits elements (or its entries,insome texts).
- Ahorizontallineofnumbers in amatrix is calleda row, and avertical line of numbersiscalled a column.
- Amatrix with the same number of rows as columnsiscalled a square matrix.
- .In general, the word vector is usedtomeanany matrix with asingle column,
- The elements of avector are often called its components,asinUnit5. Avector with n components is calledan n-dimensional vector.
- You can carry outoperationson matrices in asimilar waytonumbers.For example,you canadd, subtractand multiply them,asyou’llsee in this section.
#### 1.2Matrix addition and subtraction
- Youcan addtwo matrices only if they have the same size
- Matrix addition If A and B are m× n matrices,then A+B is the m× n matrix whose elementinrow i andcolumn j is aij + bij.
  Addition of two matrices of diﬀerent sizes is notdeﬁned.
- matrix addition is commutative.
- tmatrix addition is associative.
- Youcan alsosubtractmatrices of the same size
- .
- Matrix subtraction If A and B are m× n matrices,then A−B is the m× n matrix whose elementinrow i andcolumn j is aij − bij.
  Subtraction of two matrices of diﬀerent sizes is notdeﬁned.
- matrix subtraction is neither commutative nor associative
- Amatrix each of whose elements is zero iscalled a zeromatrix,
- ,if A is any matrix,thenthe matrix formedby changing each element of A to itsnegativeiscalled the negative of A,
#### 1.3Scalarmultiplicationofmatrices
- Any matrix canbe addedto itself, anda matrix sum A+A canbe writtenas2A
- ,adding A to itself n times, for any natural number n,gives a matrix in which each elementisthe corresponding elementin A multiplied by n.
- Scalarmultiplication If A is an m× n matrix and k is anyrealnumber, then kA is the matrix whose elementinrow i andcolumn j is kaij.
- The number k in a scalar multiple kA of a matrix A is sometimesreferred to as the scalar k
- (−1)A = −A,
- Properties of matrixaddition andscalarmultiplication Thefollowingproperties hold forall matrices A, B and C forwhich the sums mentioned are deﬁned, andfor all scalars m and n.
  1. A+B = B+A 2. (A+B)+C = A+(B+C) 3. A+ 0 = A 4. A+(−A)= 0 5. m(A+B)= mA+mB 6. (m+ n)A = mA+ nA 7. m(nA)= (mn)A 8. 1A = A (Inproperties 3 and 4, 0 is the zeromatrix of the same size as A.)
#### 1.4Matrix multiplication
- Undercertain conditions, it is alsopossible tomultiplytwo matrices
- .Rememberthatthe elementinthe ﬁrst rowand ﬁrst column of the productmatrix in calculation (1)above wasobtained by multiplying each elementinthe ﬁrst row of the ﬁrst matrix by the corresponding elementinthe ﬁrst column of the second matrix,and adding the results:
- It waspossibletodothisbecause the number of columns in theﬁrstmatrix is thesame as thenumber of rows in thesecond matrix
- Whenitisnot possible to multiplytwo matrices,we sometimessay thattheir productis undeﬁned.
- Sothe productofan m× n matrix andan n × q matrix is a matrix of size m× q.
- Matrix multiplication Let A and B be matrices.Then the productmatrix AB canbe formedonlyifthe number of columnsof A is equal to the number of rows of B.
  If A hassize m× n and B hassize n × p,then the product AB has size m× p.
  The elementinrow i andcolumn j of the productmatrix AB is obtained by multiplyingeach element in the ith rowof A by the corresponding elementinthe jth column of B andadding the results.
  In elementnotation,if cij denotesthe elementinthe ith rowand jth column of AB,then cij = ai1b1j + ai2b2j + ··· + ainbnj.
- matrix multiplicationisnot commutative.
- , even in caseswhere both the products AB and BA are deﬁned, these twoproducts canbe diﬀerent matrices.


## New highlights added January 20, 2025 at 9:25 AM
- this property does hold in general: whenever A,B and C are matrices such thatthe products AB and BC are deﬁned, we have (AB)C = A(BC).
- , matrix multiplication is associative.
- ifthe matrix product AB exists, then, forany scalar k, A(kB)= (kA)B = k(AB).
- :ifthe matrix product A(B+C)can be formed, then A(B+C)= AB+AC.
- matrix multiplication is distributive over matrix addition.
- Some properties of matrixmultiplication Thefollowingproperties hold forall matrices A, B and C forwhich the products andsumsmentioned are deﬁned.
  • (AB)C = A(BC) • k(AB)=(kA)B = A(kB), for any scalar k • A(B+C)= AB+AC • (A+B)C = AC+BC
- Matrix multiplication isnot commutative • There are matrices A, B such thatthe product AB exists but the product BA does not.
  • Even when bothproducts are deﬁned, it canhappenthat AB '= BA
##### Matrix powers
### 2 Matrices andnetworks
- Matrices canbeusedtorepresent andanalyse variousﬂowsin networks
- A network is a collection of objectsconnected by links – eitherphysicalor abstrac
#### 2.1Networks
- a network diagram,
- The dots in a network diagram are called nodes,and the lines are called arcs
#### 2.2From networks to matrices
#### 2.3Combining networks
- Networkscan be combined by makingthe outputs from one network become the inputs to anothernetwork
- In general, we regard twonetworksofthe type considered inthissection as equivalent if they have the same input andoutput nodes, andall choices of inputs produce the same outputs in both networks.
- The conclusion of thisdiscussion is thatthe matrix thatrepresentsthe combined network in Figure 9 isthe productofthe matrices thatrepresent the originalnetworks.
- Notice thatthe matrix representing the top network is the second matrix in the productthatrepresentsthe combined network.
### 3 The inverse of amatrix
- it is notpossibleto divide a matrix by anothermatrix.However thereisa way to manipulatematrices thatincertain situationsplays the role of division.
#### 3.1Identitymatrices
- .Anidentity matrix is amatrix thatbehaves like the number 1, in the sensethatifa matrix A is multipliedby anidentity matrix of an appropriatesizethen the resultis again A
- • If A is anymatrix such thatthe product AI exists, then AI = A. • If A is anymatrix such thatthe product IA exists, then IA = A.
  Any matrix I with these two properties is calledan identity matrix.
- ,for everynatural number n,the n × n matrix thathas ones down the leading diagonal (the diagonal thatstartsatthe topleftelement and ends at the bottomrightelement), andzeros everywhere else,isan identity matrix.
- Identity matrices An identity matrix is a square matrix I such that • forany matrix A forwhich the product AI is deﬁned, AI = A • forany matrix A forwhich the product IA is deﬁned, IA = A. Each identity matrix hasthe form        10 0 ··· 0 01 0 ··· 0 00 1 ··· 0 ...
  ...
  ...
  . . .
  ...
        00 0 ··· 1  That is,ithas ones down the leadingdiagonal andzeros elsewhere.
  .
#### 3.2Matrix inverses
- in the arithmetic of numbers, dividing by anumberisthe same as multiplyingbyits reciprocal
- Let A be a square matrix.Ifthere is anothermatrix B of the same size with the property that AB = I and BA = I,
- thenwesay that A is invertible andthat B is an inverse of A.
- If amatrix A is invertible,thenithas exactlyone inverse
- We usually write the inverseofaninvertiblematrix A as A−1.Sothe following factshold
- Inverseofamatrix If A is an invertible matrix,then AA−1 = I and A−1A = I, where I is the identity matrix of the same size as A.
- t follows from the deﬁnition of the inverseofa matrix thatif A is an invertible matrix,then not only is A−1 the inverseof A,but also A is the inverseof A−1.Inother words, A and A−1 are inverses of each other.
- Inverses of 2 × 2matrices
- Determinantofa2 × 2matrix Let A = .
  ab cd / .Thenthe number ad − bc is calledthe determinant of A,and writtenasdetA.
  If the determinantof A is notzero, then A is invertible.
  If the determinantof A is zero, then A is notinvertible.
- Amatrix thatdoesnot have an inverseiscalled a non-invertible
- In some texts, non-invertible matrices are called singular matrices,
- invertible matrices are called non-singular
##### Determinantsand inverses of larger matrices
### 4 Simultaneous linearequations and matrices
#### 4.1Solving simultaneous linearequations in two unknowns
- The 2 × 2 matrix thatappears in thisequation is calledthe coeﬃcient matrix of the simultaneous linearequations
- Matrix form of simultaneous linearequations Thesimultaneouslinearequations ax + by = e cx + dy = f canbewrittenasthe matrix equation .
  ab cd /. / x y The matrix .
  = ab cd / . / e f .
  is calledthe coeﬃcient matrix.
## New highlights added January 25, 2025 at 12:05 AM
- Strategy: To solvea pair of simultaneous linearequationsintwo unknownsusingmatrices Write the simultaneous linearequationsinmatrix form Ax = b, where A is the coeﬃcientmatrix, x is the corresponding vector of unknowns, and b is the vector whose components are the corresponding right-hand sides of the equations.
  If the matrix A is invertible,thenthe solution is given by x = A−1b.
#### 4.2Non–invertible coeﬃcientmatrices
- . If it hasexactly one solution,then wesay thatithas a unique solution.
- So,inconclusion,ifthe coeﬃcientmatrix hasdeterminantzero, then the equationshaveeithernosolution or inﬁnitely manysolutions.
- Forapair of simultaneous linearequationsintwo unknowns: • if the determinantofthe coeﬃcientmatrix is non-zero, then this matrix is invertible andthe equationshavea uniquesolution • if the determinantofthe coeﬃcientmatrix is zero, then this matrix is notinvertible and the equationshaveno solution or inﬁnitely manysolutions.
#### 4.3Simultaneous linearequations in more than two unknowns
- canbe used toﬁnd a solution formore thantwo simultaneous equationsinmore thantwo unknowns
- We’ll referto a collection of linearequationsin a given setofunknowns as a system of linearequations.
- A solution to a systemoflinearequationsisanassignment of values to the unknowns thatmakes all the equationshold simultaneously.
- Any systemof n linearequationsin n unknowns canbe writtenasa single matrix equation Ax = b,
- where A is an n × n coeﬃcientmatrix, x is an n-dimensional vector whose components are the unknowns, and b is an n-dimensional vector
- In fact using matrix inverses is notusually the mosteﬃcient way to solve systems of linearequations, but the methodhas theoreticalimportance.
- if the determinantofthe coeﬃcientmatrix of a systemof n equations is non-zero, then thismatrix is invertible
