To put it simply, it is the science of angles and is used to find sides or angles of triangles from other information about them.
In reality it is a much broader topic of which the rules apply also to many more scientific fields including sound and [[fourier series]].


##### [[radian]]s

They are a unit of measurement, an alternative to [[degrees]] and are extensively used because they are easier to work with.

To put it in words, one radian the [[angle]] made by an [[arc]] the length of the [[radius]] on the same [[circle]], so, if you take a length r that is the [[radius]] of the circle and use it to draw an arc on such circle, the angle you get is 1 radian (so we are talking about a ration between r length and angle made by an arc of r length).

In technical terms you say that one [[radian]] is the [[subtended angle]] of the [[arc]] of length equal to the [[radius]] of the circle
![[radian visual]]

Therefore, since the [[circumference]] of a circle is $2\pi r$ and an arc of one r makes a [[subtended angle]] of one [[radian]], to do a full circumference you need $2\pi r$ [[radian]]. So 360 degrees is the same as $2\pi r$ [[radian]].

If $360 = 2\pi \rightarrow \frac{360}{2\pi}=1 \rightarrow \frac{180}{\pi}=1$ we ca use this ratio to convert [[radian]] to [[degrees]] and vice versa


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 1.writing"
}
```
We can also now write the relationship between a [[subtended angle]] and it's arc in [[radian]]. Since we know that for arc with length r we have angle 1 [[radian]], if we have an angle in radian the arc is that angle times r, $arc\ len=r\theta$.

We can also calculate the [[area]] of a [[sector]] if we know it's angle. Since the area is $\pi r^2$, and the [[angle]] of such [[sector]] is $2\pi$ it means that $2\pi \ rad = \pi r^2$, so $1\ rad = \frac{\pi r^2}{2\pi} \rightarrow 1\ rad = \frac{1}{2}r^2$ and therefore for an angle of $\theta$ radian we have a sector with area $\theta rad = \theta\frac{1}{2}r^2$.


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 2.writing"
}
```
##### [[sine]], [[cosine]] and [[tangent]] of acute angles in right angled triangles

They are considered the basic of [[trigonometry]] and [[trigonometric ratio]]s.

If we consider a [[right angled triangle]], we can mark one of it's [[acute angle]]s as $\theta$, the side opposite to it as opp and the side next to it as adj.
The [[sine]] is $sin\theta=\frac{opp}{hyp}$
The [[cosine]] is $cosin\theta=\frac{adj}{hyp}$
The [[tangent]] is $tangent\theta=\frac{opp}{adj}$

For an angle $\theta$ of a right angled triangle, you always get the same values of [[sine]], [[cosine]] and [[tangent]]. This is because the sum of angles of a triangle is 180 deg or $\pi$, if one angle is necessarily $\frac{\pi}{2}$ and the other is $\theta$, the last must be always the same. Therefore, at most the sides can be scaled up or down


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 3.writing"
}
```

```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 4.writing"
}
```


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 6.writing"
}
```
Just like you can find the sides of a triangle by knowing a side and an angle using the [[trigonometric ratio]]s, you can use the inverse of these to find the angle if you no the [[ratio]] already.
The names are [[arcsin]], [[arccos]] and [[arctan]] which have notation of $sin^{-1}$ etc on your calculator.


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 9.writing"
}
```
##### [[special angle table]]

| radians         | degrees | sin                  | cos                  | tn                   | from              |
| --------------- | ------- | -------------------- | -------------------- | -------------------- | ----------------- |
| $\frac{\pi}{6}$ | 30      | $\frac{1}{2}$        | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$ | equilateral split |
| $\frac{\pi}{3}$ | 60      | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$        | $\sqrt{3}$           | equilateral split |
| $\frac{\pi}{4}$ | 45      | $\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | 1                    | square split      |
You can work out this values by imagining the shape in the from cell, give easy numbers to the known side lengths like one and 2, working out the [[hypotenuse]] with [[pythagoras theorem]].

##### [[trigonometric identity]]

This are [[identity]] that involve at least one [[trigonometric ratio]].
If you consider a [[right angled triangle]] with hypotenuse of 1, sides of a and b, when you consider the acute angle $\theta$ you have $sin\theta=\frac{a}{1}\ \ cos\theta=\frac{b}{1}\ \ tan\theta=\frac{a}{b} \rightarrow tan\theta=\frac{sin\theta}{cos\theta}$.
Remember that you can scale any triangle to have an hypotenuse of 1 and the [[trigonometric ratio]]s would not change so the above expression is an [[trigonometric identity]] since true for every $\theta$ .
You can continue with [[pythagoras theorem]] where $a^2+b^2=c^2 \rightarrow sin^2\theta + cos^2\theta = 1$.


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 10.writing"
}
```

Now consider that, in a [[right angled triangle]], the two other angles together must be 180 deg so $\frac{\pi}{2}$. So if you know angle $\theta$ the other must be $\theta-\frac{\pi}{2}$ and vice versa.
Going back to the previous [[trigonometric identity]], and knowing that for the 2 different angles the opposite and adjacent are swapped we can say that $sin(\frac{\pi}{2}-\theta)=cos\theta$ and $cos(\frac{\pi}{2}-\theta)=sin\theta$

##### Trigonometric ratios of other angles

We start by considering the [[unit circle]] and imagining the point P as the point that is touched by our angle $\theta$.
The first things we could notice, is that different angles may have the same point P, this is because if you take an angle and add a full run to it you end up in the same point, whenever two angles differ by a multiple of $\frac{\pi}{2}$ they have the same point P.

Every P will land on a [[quadrant]] that is one of the four regions created by the x and y axis, counting anti-clockwise from right


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 12.writing"
}
```
Now, if we have a point P on the [[unit circle]] we can draw a line down or up until it touches the x axis and get a [[right angled triangle]]. We know this triangle has [[hypotenuse]] one so $sin=y \ \ cos=x\ \ tan=\frac{y}{x}$.
We can therefore say that the sin and cos of an angle $\theta$ are just the y and x values of the point P such angle make on the [[unit circle]]


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 13.writing"
}
```

```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 14.writing"
}
```

```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 15.writing"
}
```

##### graphs of [[trigonometric function]]s

Since the [[trigonometric ratio]]s are rules that takes an angle as input and give a number as output they can be defined as [[function]]s, in particular we call them [[trigonometric function]]s.

[[sin graph]]:

```handdrawn-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/sin graph.drawing"
}
```

[[cos graph]]
```handdrawn-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/cos graph.drawing"
}
```

[[tan graph]]


```handdrawn-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/tan graph.drawing"
}
```
##### inverse [[trigonometric function]]s

It is clear from the graph that all [[trigonometric function]]s are not 1 to 1 [[function]]s so they do not have an [[inverse function]]. However, as we saw in [[function]], we can sometimes get an [[inverse function]] by redefining the original one with a smaller domain. If we give the [[sine]] function a domain of $[-\frac{\pi}{2},\frac{\pi}{2}]$.
Now we have a 1 to 1 function that is always growing and has a inverse that we call $sin^{-1}$
and since we know [[inverse function]] are mirrored on the $y=x$ axes it is easy to imagine the graph as well.
Same thought can be applied to [[cosine]] with domain $[0,\frac{\pi}{2}]$, and [[tangent]] with domain again $[-\frac{\pi}{2},\frac{\pi}{2}]$


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 18.writing"
}
```

because we had to define bounds make the [[trigonometric function]]s have an [[inverse function]] not all values now fit in their domains.
However we can re-imagine the functions by looking at the graph of the inverse, for example even if $sin^{-1}{-x}$ is undefined, we can look at the graphs and understand that we can apply the rules that:
$$
\begin{aligned}
\sin^{-1}{-x}=-\sin^{-1}x \\
\cos^{-1}{-x}=\pi-\cos^{-1}x \\
\tan^{-1}{-x}=-\tan^{-1}x \\
\end{aligned}
$$


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 19.writing"
}
```
##### [[trigonometric equation]]s

As you can imagine, they are [[equation]]s that contains at leas one [[trigonometric function]] it it.
Simple once can be solved using the [[inverse function]] but for more complex once there are possibly infinite solutions as we saw from the [[trigonometric function]]s above so what you do is find the solutions between for example $[0, 2\pi]$ which are always 2 and state all the others solutions as adding multiples of $2\pi$ integers.
So for any angle we have an equivalent +- solutions possible, much like [[quadratic]].


```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 20.writing"
}
```

```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 21.writing"
}
```

##### [[sine rule]]

Imagine a triangle with no right angled angles, you name the [[vertices]] (and angles) from A to C and the opposite sides as a to c.
Even if you do not have a [[right angled triangle]], you can draw a line from a vertex to one the opposite sides and have 2 different [[right angled triangle]] with the new vertex h:
![[basic not right triangle]]

Now we can use what we know to define the sin of c and b:
$sinC = \frac{h}{b} \rightarrow h=bsinC$
$sinB=\frac{h}{c} \rightarrow h=csinB$

Therefore we can rewrite it saying $bsinC=csinB \rightarrow \frac{b}{sinB}=\frac{c}{sinC}$
In fact this can be done with any of the angles, and if we do the same for A at the end we get the [[sin rule]] that $\frac{b}{sinB}=\frac{c}{sinC}=\frac{a}{sinA}$
![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 23]]

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 24]]

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 25]]

##### [[cosine rule]]

The concept of the [[cosine rule]] is very similar to the [[sine rule]] but it has a different ending and can be used where the [[sine rule]] can not.
We always start with the same concept of the non [[right angled triangle]] and draw h
![[basic not right triangle]]

However this time we proceed differently, we know that if the segment from C to h has a length and we call it y, therefore the other segment must be a - y and if we apply the [[pythagoras theorem]] we ca say that $b^2=y^2+h^2$ and $c^2=h^2+(a-y)^2 \rightarrow c^2=h^2+a^2+y^2-2ay$.
We can replace the value of the first equation into the second since it contains the [[rhs]] and get $c^2=b^2+a^2-2ay$.
Considering that $cosC=\frac{y}{b} \rightarrow y=bcosC$ and substituting into the previous [[equation]] we get $c^2=b^2+a^2-2abcosC$.

The letters used normally are not the same that we have in this triangle but they do not matter as long as they are respected, the final rule is $a^2=b^2+c^2-2bccos A$.
If in the rule A is a [[right angle]], the cos is 0 so you get the [[pythagoras theorem]] so the [[cosine rule]] is a more general rule.

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 27]]

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 28]]

##### decision making

At this point we know four main rules to work with angles and sides of triangles:
- [[pythagoras theorem]]
- [[trigonometric ratio]]s
- [[sine rule]]
- [[cosine rule]]

which one you should use can be described in a tree:
![[triangle rules decision tree]]

##### [[area of triangle]]

The classic formula for the area of a triangle is $b = \frac{1}{2} * b * h$.
Now that we saw [[trigonometric raio]]s and more we can also solve the case in which we have only 2 sides and the angle between them:
![[Pasted image 20241110160213.png]]
It might be difficult in words but it is easy looking at the drawing, we know that $sin\theta=\frac{h}{a} \rightarrow h=asin\theta$.
We can rewrite the classic formula as $\frac{1}{2}*b*asin\theta$

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 29]]

##### [[angle of inclination]]

The angle of inclination of a line is the angle that it makes with the x axes measured anti clock wise.
If we have a [[straight-line equation]] we know that it has a [[gradient]] and that changes the inclination of the line so there must be a relation between the [[gradient]] and the [[angle of inclination]].

If we try to draw the [[unit circle]] on a graph and consider a point P on it, connecting it with the origin will give you a [[straight-line equation]].
Since the point P have coordinates x, y and the line touches the origin the [[gradient]] has formula $gradent = \frac{y}{x}$.
Not coincidentally this is the same as [[tangent]], so for a straight line with [[angle of inclination]] $\theta$ we have $gradient = tan\theta$ 

##### more [[trigonometric identity]]

If we consider the point P on the [[unit circle]] and we draw the usual triangle, we know that the y is the [[sine]] and the x is the [[cosine]].
If this is the case, we can define the hypothenuse in them, since the length of it is one we get $(sin\theta)^2+(cos\theta)^2 = 1^2$ and this is a new [[trigonometric identity]].

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 32]]

We can look at the graphs of [[sine]], [[cosine]] and [[tangent]] to deduce a few extra [[trigonometric identity]].
First of all the [[trigonometric function]]s are periodic so we can say that:
$sin(\theta+2\pi)=sin\theta$
$cos(\theta+2\pi)=cos\theta$
$tan(\theta+\pi)=tan\theta$

Also from the graph we can easily notice that:
$sin(-\theta)=-sin(\theta)$
$cos(-\theta)=cos(\theta)$
$tan(-\theta)= -tan(\theta)$

In a similar way, you can [[translate]] the graph of [[cosine]] to the left by $\frac{\pi}{2}$ and reflect it on the y axes to get the graph of [[sine]], so we can say that:
$cos(-\theta+\frac{\pi}{2})=sin\theta$
therefore
$sin(-\theta+\frac{\pi}{2})=cos\theta$
(I do not understand why the textbook does it so weirdly, the same thing can be obtained by simply [[translate]] to the right by $\frac{\pi}{2}$).

##### [[cosecant]], [[secant]] and [[cotangent]]

guess what they are, the [[inverse]] or [[reciprocal]] to their regular counter parts so $ratiocant=\frac{1}{otherRatio}$...
$sec\theta=\frac{hyp}{adj}, \ \ \ \ cosecant\theta=\frac{hyp}{opp}, \ \ \ \ cotangent\theta=\frac{adj}{opp}$

And the graphs are the reflection on the y=x axes which is weird: 
![[Pasted image 20241111172024.png]]

![[1 - Projects/MST124 24J Essential mathematics 1/book A/unit 4/activity 33]]

We can also start form the identity $sin^2\theta+cos^2\theta=1$ and manipulate it by dividing for $cos^2\theta$ or $sin^2\theta$ to get respectively:
$tan^2\theta+1=sec^2\theta$
$1+cot^2\theta=cosec^2\theta$

##### [[angle sum identity]]
![[angle sum in sin identity proof.excalidraw]]

Start with 2 [[right angled triangle]]s, assume they have a base of 1, hypothenuse of p and q and angle of A and B.
Now smoosh them together and get the area of each individually with the formula in [[area of triangle]].
We know that the area of the two together is the area of the whole, so we can write the equation:
$\frac{1}{2}pqsin(A+B)=\frac{1}{2}p1sin(A)+\frac{1}{2}q1sin(B)$
we can now multiply everything by 2 and divide by pq to get:
$sin(A+B)=\frac{1}{q}sin(A)+\frac{1}{p}sin(B)$

going back to the triangles, we can get the [[cosine]]s of A and B which give $cos(A)=\frac{1}{p}$ and $cos(B)=\frac{1}{q}$.
If we substitute these in the original equation we get the final form of:
$sin(A+B)=cos(B)sin(A)+cos(A)+sin(B)$

This is our new [[trigonometric identity]], even thought we worked out the proof for only [[acute angle]]s it works for every angle, the proof is just a bit more complicated.

This does not stop here, we can use the previous identities to rewrite it in the [[cosine]] form, in particular we want to replace A with $\frac{\pi}{2}-A$ and B with $-B$ (This because we know the rule works for all angles):
$sin(\frac{\pi}{2}-A-B)=cos(-B)sin(\frac{\pi}{2}-A)+cos(\frac{\pi}{2}-A)sin(-B)$
if we use the [[trigonometric identity]] we defined earlier:
![[Pasted image 20241111202110.png]]
in the end we get:
$cos(A+B)=cos(A)cos(B)+sin(A)sin(B)$
And this is a new [[trigonometric identity]] again.

If you notice, we can now divide the first by the second, adjust the equation and we get the same [[trigonometric identity]] for the [[tangent]]:
$tan(A+B)=\frac{tanA+tanB}{1-tanAtanB}$

You can replace in these identities B with -B and use the previously defined [[trigonometric identity]] to get also the same rules for the differences