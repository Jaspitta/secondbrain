They are simply arrays of numbers, [[multi-dimensional array]]s to be precise, that can be used and treated as a single unit to facilitate some operations.
A [[matrix]] is made of rows and columns, and every single 'cell' is called an [[element]] where an m x n [[matrix]] is one that has m rows and n columns.

A [[vector]] is actually a [[matrix]] with a single column, and it is very clear when you use it the column notation to represent it.

##### [[matrix addition]]

You can add two [[matrix]] only if they have the same size and you do that by adding every respective number. A [[matrix]] can even be added to itself, every element is summed with itself and if the original [[matrix]] was called A the result will be 2A
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_2]]

##### [[matrix subtraction]]

Similar to [[matrix addition]], [[matrix subtraction]] can be done between two [[matrix]] of the same size and is done by subtracting every element of the second to the first. Unlike [[matrix addition]], the ordering here is important.

![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_3]]

##### [[scalar multiplication of matrix]]

We say that the double [[matrix]] is obtained when you sum to itself a [[matrix]] giving from A to 2A. This can be extended further where the 2 can be represented by a k and the final [[matrix]] is obtained by multiplying by $k$ every element in the matrix. In this context $k$ can be referred to as the [[scalar]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_4]]


##### [[matrix multiplication]]

In [[matrix multiplication]] you multiply each column of the first with each row of the first, in each of this multiplications you do a regular multiplication of each element and then sum the results.
$$
\begin{pmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{pmatrix}
*
\begin{pmatrix}
j\\
k\\
l
\end{pmatrix}
=
\begin{pmatrix}
a*j+b*k+c*l\\
d*j+e*k+f*l\\
g*j+h*k+i*l
\end{pmatrix}
$$

Of course, the same can be applied with more than one column, however the number of column of one must match the number of rows of the other [[matrix]], to be precise the second [[matrix]] must have as many rows as the columns of the first [[matrix]]. I case you had another column, the same thing would be repeated with the second column and another one would be added to the final [[matrix]]. So you can multiply a matrix only if they have sizes $m*n\ p*q$ where $n$ and $q$ are equal, and the final size of the [[matrix]] will be $m*q$.

Even thought [[matrix multiplication]] share some common characteristics with regular multiplication, they are not the same thing, for example [[matrix multiplication]] is not [[cummutative]] so $A*B$ is not the same as $B*A$, although it is true that $AB*C$ is the same as $A*BC$, so they are [[associative]].
Same holds for [[scalar multiplication of matrix]], so $k(AB)=A(kB)=(kA)B$. [[matrix multiplication]] is also [[distributive]] with [[matrix addition]] so $A(B+C)=AB+AC$, and therefore you can also [[factorising]] as the inverse operation.
![[activity_6_7_8_9_10]]

##### [[matrix power]]

Just like numbers, the power of a [[matrix]] is $A^2=AA$, however not all matrices can be raised to a power, this is because if the [[matrix]] has structure $m*n$, the $m=n$ is necessary for it to be possible to do [[matrix multiplication]].

##### [[matrices and networks]]

A [[network]] as we saw previously is a collection of objects interconnected physically or virtually, the biggest example today is the [[internet]].
A [[network]] can also be represented as a [[network diagram]] where [[node]]s represents the actors and the lines connecting them are called [[arc]]s. An example could be :
![[network_diagram_ex]]

This represent the relation between the top [[node]]s and the bottom once, the [[arc]]s are labeled with letters that represent the relation itself, so if you give one unit to input one it will be distributed as $1x$ to C, $1y$ to D and $1z$ to E.

This can also be represented as a [[matrix]] where we put in relation the input and output [[node]]s:
$$
\begin{array}{cc}
&A&B\\
C&x&u\\
D&y&m\\
E&z&n
\end{array}
$$
So, if we where to input value of 5 for A and 7 for B It would be a multiplication with the [[matrix]] $\begin{array}{cc} 5\\7\end{array}$.

A further thing you can do is combine two [[network]]s using [[matrix]], say you have another network represented by:
![[{F2A609A4-4241-4774-8654-792C38D3BDA1}.png]]
you get an overall result of :
![[{11C735DF-3AFB-4FE3-A8E9-8AE269FE6354}.png]]
however you can also simplify to the final network:
![[{5D0F9D52-8EE9-4F4B-9CED-D72F6B024BF0}.png]]

The second and third [[network]] are equivalent but we are missing the labels on the [[arc]]s so we need to get those. If you feed 1 unit to one of the top [[node]], you will get $1x$ to the middle node and than $(1x)y$ to the final one, where $x$ and $y$ are the labels of the arcs. There can be more than one route from one top node to the bottom one so you also need to sum the results together to get the final values you can write int he final version of the [[network]].
There is however a different way to get the [[matrix]] of the final network from the two starting once, if you assume the input vector is $\begin{array}{cc} a\\b\end{array}$ and the output is $\begin{array}{cc} c\\d\end{array}$, and finally the middle result of input and first [[network]] is $\begin{array}{cc} u\\v\\w\end{array}$ you can rewrite the network as:
$$
\begin{array}{cc} u\\v\\w\end{array}=\begin{array}{cc} x&e\\y&g\\w&i\end{array} * \begin{array}{cc} a\\b\end{array}
$$

because the first network times the input gives the middle result and than the middle result times the second network gives the output:
$$
\begin{array}{cc} c\\d\\\end{array}=\begin{array}{cc} h&f&l\\o&p&q\end{array} * \begin{array}{cc} u\\v\\w\end{array}$$

You can replace the middle node in the second equation with the first and solve to find that the result is simply the [[matrix multiplication]] of the two [[network]]s where the top network is the second matrix of the multiplication. When doing this always verify that each column has an output of 1 because if you put one on one side you should get a total of 1 on the other.
A simpler way to write is that, if the first [[network]] is identified by [[matrix]] A, the second by [[matrix]] B, the input by $x$, the output by $y$ and the middle output by $z$ we can write that $z=Ax$ and $y=Bz$, if we substitute the $z$ in the second equation $y=BAx$ (remember that order is important) so the output is equal to the input fed to the [[matrix multiplication]] of the two [[networks]].
![[activity_17_18]]


##### [[identity matrix]]

It is a [[matrix]] for which when another [[matrix]] is multiplied by, the result is the other matrix unchanged, just like multiplication of a number by 1. So, if you have a [[matrix]] A and one I, if AI is A and IA is A we say that I is an [[identity]] matrix.
An [[identity matrix]] has to be a [[square matrix]] because it has to have the same [[columns]] and [[rows]] of the other matrix in order to be multiplied in both ways
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_19]]

They all have the same structure, a diagonal 1 from top left to bottom right:
$$
\begin{array}{cc} 1&0\\0&1\end{array}
$$
$$
\begin{array}{cc} 1&0&0\\0&1&0\\0&0&1\end{array}
$$
etc..

##### [[matrix inverse]]

In regular [[arithmetic]] a reciprocal of number $a$ is the number $b$ such that $ab=1$, this concept is often used also for divisions because dividing by a number is the same as multiplying by the [[reciprocal]].
In [[matrix]] if you have a matrix $A$ and there is a [[square matrix]] such that $AB=I$ and $BA=I$ where I is the [[identity matrix]] we call B the [[matrix inverse]] of A, the same concept a the [[reciprocal]] of a number since I has very similar properties to number 1.
Remember also that if a [[matrix]] has an inverse, it has only 1 and is noted as $A^{-1}$

To find the [[matrix inverse]] of a 2x2 matrix you can use the formula where the original matrix is $\begin{array}{cc} a&b\\c&d\end{array}$:$\frac{1}{ad-bc}\begin{array}{cc}d&-b\\-c&a\end{array}$ 
which is possible only when $ad-bc \neq 0$, this term is called the [[determinat]] and when it is 0 the [[matrix inverse]] does not exist.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_22]]

You can also get the proof for the formula by multiply the [[matrix]] in it:
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_22]]




##### matrices for [[linear equation]]

surprisingly, a [[matrix]] can also be used as an alternative method to [[substitution method]] or [[elimination method]] for solving [[linear equation]].

You start by converting the equations into a [[matrix]], if you have $ax+by=e$ and $cx+dy=f$ you can write $\begin{array}{cc}ax&+by\\cx&+dy\end{array}=\begin{array}{c}e\\f\end{array}$  or $\begin{array}{cc}a&b\\c&d\end{array}*\begin{array}{cc}x\\y\end{array}=\begin{array}{c}e\\f\end{array}$.
So the first [[matrix]] in the second form is called the [[coefficient matrix]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_9/activity_25]]

