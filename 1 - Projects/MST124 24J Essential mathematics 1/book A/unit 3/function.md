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
Don't be fooled though, even [[vertical scaling]] can look like a multiplication, for example if $c=0.5$ than such vertical scaling will take the shape of $2x$ so $y=f(2x)$, the key is that the change is made **inside** the x not outside.

Knowing [[translate]] and [[scaling]] of [[function graph]] can be an amazing too to have a better idea of what a curve will look like by imagining the standard one and than applying such techniques one by one to get to your curve.


There are of course also ways to combine more functions together, in particular sum, minus, product and quotient.
The resulting [[domain]] is the [[intersection]] of the two, except for the two quotient in which you also have to exclude the points that would make the [[denominator]] 0.
We define the [[rule]] of these [[function]]s as the result of combining the two and simplifying.

Functions can also be combined into [[composite function]]s where one [[function]] is chained to the other by feeding the result of the first to the second, assuming that the [[image set]] of the first and the [[domain]] of the second allows it.
These functions have a special syntax that is $g \circ f$ where the order is reversed so here the result of $f$ is fed into $g$. In total you write $(g \circ f)(x)=g(f(x))$.

There also exist the [[inverse function]] of a [[function]], called also [[inverse]] which is the reflection of the original where the [[domain]] become the [[image set]] and the [[image set]] become the [[domain]] compared to the starting one. This functions are denoted as $f^{-1}$ if for $f$ given x you get y, if you give y to $f^{-1}$ you get back x, therefore $f^{-1}$ undoes $f$.
Remember that [[functions]] must map only one y to every x, therefore some functions do not have an [[inverse]], for example $x^2$ inverted might look like $\sqrt{x}$ but in the original function there are 2 x for every y (positive and negative squared) and therefore the [[inverse]] is not a [[function]] anymore.
[[function]]s that do have an [[inverse]] are called also [[one-to-one function]].
One of the easiest ways to find the inverse is to either deduce it by head or to simply write the $f$ function in y so $x=...y...$ . and than rewrite it in form $f^{-1}(x) = ...x...$, remember also that functions that are always increasing or always decreasing for their domain are always [[one-to-one function]] and therefore [[invertible]].
For [[quadratic function]]s it can be a bit trickier, what you need to do is keep in mind the domain, rearrange the function by finding the [[perfect square form]] and rooting everything. Once you have the term with $\pm$ you can try to see what fits better based on the domain.
One way to verify that a function if the inverse of the other is by feeding the result of one into the other, since $f^{-1}$ gives x for $f(x)$ you can to $f^{-1} \circ f$ and you should get x (like walking in circle).
From a graph point of view, the [[inverse function]] appear as a reflection of the original one on the axes $y = x$ because for their properties if you give the output of one to the others you should get x, so if you give calculate y of $f$ and give it to $f^{-1}$ as x you will get a y that is equal to the x of $f$, it simple terms it means that if you have a point of $f$ and swap the x and y you get the corresponding point of $f^{-1}$.

Remember that $f^{-1}$ is not the same as $f(x)^{-1}$, this is called a [[reciprocal]] and is the same as $\frac{1}{f(x)}$.

[[function]]s that are not [[one-to-one function]] do not have an [[inverse]], but we can still take some actions to write an approximation of it.
We can take the original function, use a [[domain]] in which it is a [[one-to-one function]] and take the inverse of that. Such functions are called [[restriction]]s and the process is called [[function restriction]].

Another type of [[function]]s are [[exponential function]]s which for is $f(x)= b^x$ where b is a positive constant not 1. b is called the [[base]] of the exponential function. Remember that $b^0$ is always 1, so all [[function]] of this type will have to pass by (0,1). In relation to [[logarithm]]s, $f(x)=b^x$ can also be written as $f(x)=e^{kx}$ where $k=\ln{b}$ because $e^{\ln{b}}=b$ and therefore $b^x=e^{{(\ln{b}})^x}$.
This means that the resulting function id $f(x)=e^x$ with [[horizontal scaling]], given by $f(kx)$ with $c=\frac{1}{k}$, this is because we said that the base function for [[horizontal scaling]] is $f(\frac{x}{c})$ so $f(kx)=f(\frac{x}{c}) \rightarrow kx=\frac{x}{c} \rightarrow ckx=x \rightarrow ck=1 \rightarrow c=\frac{1}{k}$.
The closer b get to 1, the flatter the [[curve]] will be because at 1 you get a flat line, since every [[exponential function]] passes by (0, 1) and the curvature change with b, there is b at which in (0,1) the [[gradient]] is exactly 1. Such number is $e$ and the [[function]] $f(x)=e^x$ is called [[the exponential function]] which has [[gradient]] of exactly 1 and (0,1).
Remember that $e$ is an irrational number like $\pi$.
Related to [[exponential function]] there are [[logarithmic function]]s which have the form $f(x)=\log_{b}x$ where $b$ is the [[base]] and a positive constant different from 1. If you put them into relation, the [[logarithmic function]] is the [[inverse function]] of the [[exponential function]] (and vice versa of course).
Being [[inverse function]]s, the graph of one is the reflection on $y=x$ of the other so:
![[Pasted image 20241026133417.png]]

#### Growth or Decay factor in exponential functions

An interesting property of [[exponential function]]s is that if you have such a function and you get the result for x and than for x + c where c is a constant, $f(x) \rightarrow f(x+c)$ the second function will be the first one multiplied by a factor independent from x but only dependent on $c$. So if for example $f(1) = 5\ \  and\ \  f(5) = 15$ it means that $f(20)$ will be $f(16) * 3$ because it is the same gap c. This factor is called [[growth factor]] or [[decay factor]].
Using this logic we can define a number p that $e^{kp} = 2$, so p is the number that if added to x double or halves the value of the function depending if it represent growth of decay. This number is also called the [[doubling period]] or [[halving period]] and when the function refers to time it can be called [[half-life]]