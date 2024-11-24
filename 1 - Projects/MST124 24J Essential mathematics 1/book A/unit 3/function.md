this is intended as a mathematical function, not a programming function, although the concepts are very related of course.

At the very core, when one quantity is dependent on another, the first quantity is a [[function]] of the second.

The part that transform input in output values is called a [[processor]], the [[set]] of possible input values is called [[domain]] and the [[set]] of possible output values is called [[codomain]].
Because they are represented by the input and output it means that if you plot a [[function graph]] you can visualize the [[domain]] (x axis) and [[image set]] (y axis):
![[image set and domain on graph]]

A function is described using [[function notation]] so if there is a function that for the [[input variable]] x gives $x^2$ you can write:
$f(x)=x^2$

Every input value of a function **must** have an output value, for example in a function $f(x)=\sqrt{x}$ negative numbers can not be in the [[domain]] of the function. However, not every value of the [[codomain]] has to be an output value for the function, it is common to consider a [[codomain]] that contains much more numbers.
The set of values that correspond to exactly all the possible output values id called the [[image set]].
On the other hand, every input value in the [[domain]] **must** have exactly **one** value as output in the [[codomain]]

Functions whose [[domain]] and [[codomain]] are the [[real numbers]] are called [[real functions]].

It is very important to remember that to state a function the [[domain]] must be explicit, two functions with same [[function rule]] but different [[domain]] are different functions. In some occasions the function is defined only by the [[function rule]] but that is because the [[domain]] should be the largest possible [[set]] of [[real numbers]].

Sometimes, [[function]]s can be defined simply by an [[equation]], for example, $C=2\pi r$ is considered a [[function rule]] and if we assume the [[domain]] it is an actual function.

Functions can also be defined as [[piecewise function]]s, so for different parts of its domain it will have different [[function]] rules:
$$
 f(x)=
 \begin{cases} 
      x^2 & (x\geq 0) \\
      x+5 & (x< 0)
\end{cases}
$$


Of course, functions can also be represented as [[function graph]]s, this simply means plotting the images of x under f for every element in the [[domain]]. Remember in this cases the graph is of the equation $y=f(x)$ which is the same as transforming the function in an [[equation]].

It is important to remember that a [[function]] maps [[domain]] and [[image set]] one to one, so if the graph has more than one x for a y it is not a [[function graph]]:
![[Pasted image 20241020174309.png]]

[[function]] are related to the equivalent [[equation]]:
- $f(x)=mx+c$ is a [[linear function]] because it is a [[linear equation]]
- $f(x)=ax^2+bx+c$ is a [[quadratic function]] because the [[equation]] is a [[quadratic]]

Both of these are technically [[polinomial function]] because they come from a [[polinomial expression]]. 
Another thing to keep in mind is that no matter the [[polinomial function]], if you plot it and consider the domain R, it will always tend to infinity or -infinity. The term with the [[polinomial degree]] will tell you if it tends to infinity or -infinity.

One particular type of [[function]] is the [[modulus function]] described as $f(x)=|x|$. As we saw, the [[modulus]] of a number is it's distance from 0 and the graph is a smooth graph except one corner.
This function is the same as:
$$
f(x)=
\begin{cases}
	x, & if\ \ \ x >= 0 \\
	-x, & if\ \ \ x<0
\end{cases}
$$
and the resulting graph is simply a V

Another is the [[reciprocal function]], where remember the [[reciprocal]] is 1/x for x. The domain is all the real numbers except 0 of course:
![[Pasted image 20241022150446.png]]
The property of the y-exes in this image is what is an [[asymptote]] so a line to which the graph gets closer and closer but never touch.

Every [[polinomial function]] is a type of [[rational function]] which has the structure of $f(x)= \frac{p(x)}{g(x)}$ where p and q are polynomial functions

You can [[translate]] a vertically the graph of a [[function]] by changing the constant c at the end. Remember that translating means moving it without distorting it in any way.
You can do the same horizontally by adding a constant to each x term, so for $f(x)=x^2$ you want to make it $f(x)= (x+c)^2$.
Why this work is simpler than it sounds, imagine your [[function graph]] if you need to shift it by c, it means that for each y, the resulting x should be x+-c, so you do exactly that. It is a bit counter intuitive but the translation require $x-c$ and not $x+c$ , if c is a negative number it will became a + but the graph will be translated to the left. So positive numbers translate to the right and negative to the left, but the equation require the opposite sign because you are technically moving the y not the x:
![[horizontal translation]]

Another type of [[translate]] is when a [[function]] is scaled and it is called [[scaling]],.
Mathematically, it means multiply the function by a constant ([[vertical scaling]])and graphically it stretches the graph such that every point $m$ that is distant $n$ from the x-axis will be distant $cn$.
If the constant $c$ is negative it can also change the orientation of the graph.
Same type of concept can be applied to [[horizontal scaling]], this time however the terms $x$ are divided by a constant $c$, this means that the distance between the original x and the y-axes will increase to $cn$.
Remember that in both cases, there is a change at the number 1, since 1 would leave the $x$ unchanged, above that will stretch it out and below stretch it in. Because of this, for every function, if you scale it horizontally of vertically by -1 you get the graph reflected on the y-axes or x-axes
It is also important to remember the difference in applying [[horizontal scaling]] and [[vertical scaling]]. With [[vertical scaling]] you multiply outside the x, so $y = x^2$ would be $y = cx^2$, with [[horizontal scaling]] you replace all the x arguments so $x^2$ become $(\frac{x}{c})^2$.

Knowing [[translate]] and [[scaling]] of [[function graph]] can be an amazing too to have a better idea of what a curve will look like by imagining the standard one and than applying such techniques one by one to get to your curve.

