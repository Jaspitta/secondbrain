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


