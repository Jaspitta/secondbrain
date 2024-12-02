
Start by imagining a [[two dimensional coordinates]] system with a graph that represent the [[displacement]] of someone walking. If we imagine that the person get more tired the more it walks it means it will go slower an slower, therefore the graph will be a curve.

There is not [[gradient]] in a [[curve]], however, there is a [[gradient]] at each point of the [[curve]] and it changes continuously.
We saw how to calculate the [[gradient]] of a [[straight-line graph]] as $g=\frac{rise}{run}$  and this require two points on the [[x-axes]] and two points on the [[y-axes]]. But in the case of a curve we need to find the [[gradient]] of a single point so how? The answer is that you find the [[gradient]] of the [[tangent]] of the curve in such point, so the line that touches the curve only in that point and that you would obtain if you kept moving in the same direction of the gradient the origin curve had there:
![[gradient_tangent_curve]]

There are some exceptions to consider, for example in $f=|x|$, at the [[origin]] you have a [[sharp corner]] where the [[gradient]] changes as soon as you go to the left or right, in this cases there is no [[gradient]] at that point, same goes for graphs that have a [[discontinuity]] so a break and also for points where the [[gradient]] is vertical.

##### [[find the gradient of a tangent]]

Let's start with the example of the graph $y=x^2$, and finding the gradient at (1,1). We know that to find the [[gradient]] we need two point, but the second can not be the point itself or we would get zero.
So you try to get an [[approximation]] of the point by getting the [[gradient]] of the line that passes through two point of the curve, one is you (1,1), the other is a point as close as possible to it, this way the line is as close as possible to the actual [[tangent]].
You can do this with different points that get closer and closer and notice that the [[gradient]] looks like it get closer and closer to 2, however you can not state for sure that it is 2.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_3]]

You can however use some algebraic expressions to demonstrate that is is in fact 2. You define the distance from the first point to the second as h, so the value of y in h will be $y=(1+h)^2$ (1+h is the distance h plus the starting point 1) and you can use this to calculate the gradient as $g=\frac{(1+h)^2-1}{(1+h)-1}$ which simplify to $g=2+h$.
At this point, since we know h is the distance, if it is 0 the [[gradient]] must be 2, so we demonstrated that that is the [[gradient]], you say that 2+h tends to 2 as h tends to 0 or the [[limit]] of 2+h is 2 as h tends to 0.

We can now extend this definition to any point, we take the first to be (x, y) which become (x, x^2), and the second to be (x+h, (x+h)^2), the [[gradient]] therefore is $g=\frac{(x+h)^2-x^2}{(x+h)-x}$ which simplify to $g=h+2x$ . Now we can be happy and say that for $y=x^2$ the [[gradient]] of a point is $2x$. This process of finding the [[derivative]] is called [[differentiation from first principles]]
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_5]]

As we said, not all points have a [[gradient]], but the once that do are said to be [[differentiable]].

##### [[derivative]]

We said that every point of a [[function]] f that has a gradient at (x, f(x)) is said to be [[differentiable]], however, we also sow that the [[gradient]] at each point of the function can be different. So it is possible to define a new [[function]] that given a point x will give the gradient at (x, f(x)), such function is called [[derivative]] or [[derivative|derived function]] and is denoted with $f'$ read as [[f prime]].
So the process of finding the [[derivative]] is what we call [[differentiation]] and the action is called [[differentiation|differentiating]]. 

##### [[differentiation from first principles]]

This works exactly as we demonstrated with $f=x^2$, so in general:
$(x, f(x))\ \ (x+h, f(x+h))$

$gradient=\frac{f(x+h)-f(x)}{x+h-x}=\frac{f(x+h)-f(x)}{h}$

We call this expression the [[difference quotient]] of the [[function]].