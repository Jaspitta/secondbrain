The core concept is the need to describe an object in motion, to do so, in the real world for example, the [[speed]] is not enough, you need a [[direction]].
We saw a similar concept with [[displacement]] and the resulting dimension was called [[velocity]] of the object. The [[displacement]] is the combination of [[distance]] and [[direction]] so in general it works in every dimension, similarly, [[velocity]] is the combination of [[speed]] and [[direction]].

[[vector|Vectors]] are quantities that represent a [[size]] and a [[direction]] in general, they are called also [[vector|vector quantities]]. In [[vector|vectors]] the [[size]] is usually referred to as [[size|magnitude]]

The quantities we might be more used to only have a [[size]], such quantities are called [[scalar|scalars]] or [[scalar|scalar quantities]].

Vectors are often expressed with an arrow, the [[size|magnitude]] is the length of the arrow and the [[direction]] is where it points. Arrows can be used both in [[two dimensional coordinates]] systems or [[three-dimensional coordinates]] systems and the same arrow can represent two different things if you choose two different [[scales]]. However, once a scale is choose, two arrows or with the same length and direction represent the same [[vector]]

##### writing a vector

Vectors are typed as bold or handwritten as underlined so a vector v is written as **v** or <u>v</u>. Vectors that represent a [[displacement]] are called [[displacement vector]] and are represented as $\overrightarrow{PQ}$.
The magnitude of a vector **v** is represented as |**v**|

#####[[sum of vectors]]

The sum of vectors follows the rules of simply applying to an object the first and than the second vector which is called the [[triangle law for vector addition]]. 
![[Pasted image 20241121121347.png]]
It is typed simply as $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AB}$ ant the resulting [[vector]] is called [[resultant]] or [[resultant|resultant vector]].
An alternative is the [[parallelogram law for vector addition]]
![[Pasted image 20241121121451.png]]
![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_24]]


##### [[negative of a vector]]

Simply, given a [[vector]], the [[negative vector]] is the same with opposite [[direction]]. So what you have is that when you add a vector with it's [[negative vector]] the [[resultant]] is the [[zero vector]] you can say that $\textbf{a}+(\textbf{-a})=0$

The [[negative vector]] if what you use when you want to do [[subtraction of vectors]], you do the same as [[sum of vectors]] but you add the [[negative vector]] instead
![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_25]]

##### [[scalar multiple]]

A scalar multiple is the product of a [[vector]] and a [[scalar]]. Simply put, the resulting is the same [[vector]] with [[magnitude]] multiplied by the [[scalar]] given, if the [[scalar]] is positive the vector maintains the [[direction]], if negative it gets reversed and it is written as $m\textbf{a}$ where m is the scalar

![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_26]]
![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_27]]

##### [[vector algebra]]

It is the application of regular algebra to [[vector|vectors]] and [[scalar|scalars]]. For example the order of addition of [[vector|vectors]] does not matter $a+b+c=c+a+b$, therefore we say the addition is [[cumulative]], it is also [[associative]] because $(a+b)+c=a+(b+c)$.
Also multiplication holds similar rules as with [[real numbers]], adding two [[scalar|scalars]] and multiply the result for a [[vector]] is the same as multiplying the [[vector]] for each [[scalar]] and adding the results at the end so $(m+n)\textbf{a}=m\textbf{a}+n\textbf{a}$, this is called [[distributive]].

Multiplication of [[vector|vectors]] can be done in two different ways but it is a bit more complicated, and division of vectors is not possible, regardless the basic algebra rules that we have defined already allow us to work with [[equation|equations]] that contains vectors, these are called [[vector equation|vector equations]]

![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_28]]

##### working with [[vector|vectors]]

There are many ways of using [[vector|vectors]] for real life scenarios, of the most commons is to express the [[displacement]] or [[velocity]] of an object. To do this however we need a [[direction]], there are also many ways of expressing this but a common one is a [[compass bearing]], that is the angle of the direction compared to north measured clockwise (the north can be magnetic, true or on a map).

![[activity_30_31]]
![[activity_32_33]]

##### [[vector as component]]

[[vector component|vector components]] are an alternative way to represent [[vector|vectors]] that makes them easier to work with in many cases.
You start by choosing a [[two dimensional coordinates]] system or [[three-dimensional coordinates]] system and define the so called [[unit vector|unit vectors]], these are simply vector parallel to the axes with [[magnitude]] of 1.
The base concept is that every [[vector]] can be expressed as the sum of [[scalar multiple|scalar multiples]] of the [[unit vector|unit vectors]].
If you have a vector $\textbf{v}$, and unit vectors i and j (suppose a two dimensional system but it is the same for a three dimensional one), you can say that $\textbf{v}=a\textbf{i}+b\textbf{j}$, this is called the [[component form]] where a and b are the [[scalar multiple]] and are called the i component and j component respectively.
Since the [[unit vector]] are per definition made of a single unit and in the same direction of each axes they express the component of the original vector in each of the axes, hence the name [[vector component]].
There is a different way to write the [[component form]] of a vector $\begin{pmatrix}a \\ b\end{pmatrix}$
![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_34_35]]
Finally, you can also write [[vector component]] as [[column vector]] with the original letter and avoid the bold like this $\textbf{a}=a_1i+a_2j=\begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$.

When vectors are expressed as [[component form]], there is the possibility to carry out [[vector algebra]] in a different way.
For example, if you have 2 vectors **a** and **b**, and you want to get the vector **a+b**, you can simply add the components of the two [[vector|vectors]] $\textbf{a}+\textbf{b}=a_1i+a_2j+b_1i+b_2j=(a_1+b_1)i+(a_2+b_2)j$ represented by: 
![[sum_vec_components]]

In [[column notation]] you have $\textbf{a}=\begin{pmatrix}a_1 \\ a_2 \end{pmatrix}$ $\textbf{b}=\begin{pmatrix}b_1 \\ b_2 \end{pmatrix}$ and $\textbf{a}+\textbf{b}=\begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \end{pmatrix}$
The best part is that, regardless of the notation you use, the rule stated above apply to a [[sum of vectors]] for as many [[vector|vectors]] as you want.

You can immagine a very similar situation when it comes to [[subtraction of vectors]]. At the end of the day you simply add the [[negative vector]] so $\textbf{a}-\textbf{b}=a_1i+a_2j-b_1i-b_2j=(a_1-b_1)i+(a_2-b_2)j$
In [[column notation]] you have $\textbf{a}=\begin{pmatrix}a_1 \\ a_2 \end{pmatrix}$ $\textbf{b}=\begin{pmatrix}b_1 \\ b_2 \end{pmatrix}$ and $\textbf{a}-\textbf{b}=\begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \end{pmatrix}$
![[1 - Projects/MST124 24J Essential mathematics 1/unit 5/activity_36_37]]

Using the properties of [[vector algebra]] it is easy to deduce how [[multiplication of vector by scalar]] might work when you are dealing with [[vector component|vector components]]. You simply multiply each component for the scalar so $m\textbf{a}=m(a_1i+a_2j)$

##### [[position vector]]

If you have any point P, the [[position vector]] is defined as $\overrightarrow{OP}$ where 0 is the origin. We can also describe the [[vector component|vector components]] and quickly realise that they are simply the coordinates of P, to be precise $\overrightarrow{OP}=x\textbf{i}+y\textbf{j}=\begin{pmatrix}x\\ y\end{pmatrix}$. If you have any [[vector]], it can be expressed as the sum of the [[position vector]] that makes it up, for a vector $\overrightarrow{AB}$ you have the two [[position vector|position vectors]] $\overrightarrow{OA}$  and $\overrightarrow{OB}$, since the direction is importante we have $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$ because:
![[vec_as_origins]]

You can also use this strategy to get a new way to find the [[midpoint]]. In the example above we can say the midpoint is the vector $\overrightarrow{AM}$ and has associated the [[position vector]] $\overrightarrow{OM}$, which is $\overrightarrow{OA}+\overrightarrow{AM}$ we know that $\overrightarrow{AM} = \frac{1}{2}\overrightarrow{AB}= \frac{1}{2}(\textbf{b}-\textbf{a})$, finally we can say $\overrightarrow{OM}=\textbf{a}+\frac{1}{2}(\textbf{b}-\textbf{a})=\frac{1}{2}a+\frac{1}{2}b=\frac{1}{2}(x_1i+y_1j+x_2i+y_2j)=\frac{x_1i+x_2i}{2}+\frac{y_1i+y_2i}{2}$ which is the formula we got  with the previous procedure of finding the [[midpoint]].

![[activity_41_42]]

##### from [[vector component]] to [[magnitude]]

When you have a two dimensional vector and it's components, you know such components are its x and y properties. Therefore, you can easily deduce that they are usable to draw a right angle triangle with the actual [[vector]] and getting the [[magnitude]] is a matter of [[pythagoras theorem]] and this actually hold also for a [[three-dimensional coordinates]].

![[activity_44_45]]

The reverse is fairly similar, sketch the vector, find an angle and use [[trigonometry]] to find the rest
![[activity_46_47]]

It is easy to deduce the formula of the [[vector component]] from the [[magnitude]], that is $v=|v|cos\theta i+ |v|sin\theta j$. It is easy to deduce it by drawing the [[right angled triangle]], or imagining the [[vector]] inside the [[unit circle]], in this case the x and y are necessarily [[cosine]] and [[sine]], how you only need to scale them back (the [[unit circle]] measure 1) by the [[magnitude]].

![[activity_49_50]]

##### [[scalar product of vectors]]

The [[scalar product of vectors]] is as the name say a scalar so has no [[direction]]. The formula to calculate it is $a \bullet b=|a||b|cos\theta$.
Due to the notation it is also called the [[scalar product of vectors|dot product]] and it is obtained as $|a|(magnitude\ of projection\ of\ a)$ or $|a|(magnitude\ of\ projection\ of\ a)$ when the [[angle]] is an [[acute angle]] and the negative when it is an [[octuse angle]]:

![[scal_prod]]

![[activity_52_53]]

This works even better with [[vector component|vector components]], in fact the scalar product of $a \bullet b$ where  $a=a_1i+a_2j$ and $b=b_1i+b_2j$ can be calculated as $a \bullet b = (a_1i+a_2j) \bullet (b_1i+b_2j)=a_1b_1(i \bullet i)+a_2b_2(j \bullet j)+a_1b_2(i\bullet j)+a_2b_1(j\bullet i)$, however, we know the [[unit vector]] i and j measure 1 and are perpendicular so $a_1b_1(1)+a_2b_2(1)+a_1b_2(0)+a_2b_1(0)=a_1b_1+a_2b_2$
![[activity_52_53]]
You can see that the formula of [[scalar product of vectors]] gives you a relation between such value, the [[magnitude]] of the [[vector|vectors]] and the [[angle between vectors]], this also means that if we have the scalar we can get the angle as a consequence and with [[vector component]] we can easily get that, to be precise $cos\theta=\frac{a\bullet b}{|a||b|}$
![[activity_54_55]]