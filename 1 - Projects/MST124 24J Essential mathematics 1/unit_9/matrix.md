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
