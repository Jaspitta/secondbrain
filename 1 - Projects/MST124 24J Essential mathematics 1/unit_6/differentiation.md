
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
We can say that $f'(x)=\lim_{h\to\ 0}\frac{f(x+h)-f(x)}{h}$
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_6]]

This principle applies also to functions that are not [[differentiable]] in some particular points, you will observe that as h tends to 0 the number get larger and larger for a vertical tangent and that the number get closer to something different coming from positive or negative h for sharp corner.
It is important that even though you found the [[derivative]], that point still does not have a [[gradient]].

##### [[Leibniz notation]]

It differs from the usual $f'(x)$ in that you write $\frac{dy}{dx}$ and is red as the [[derivative]] of y in respect to the [[derivative]] of x.
It is important to note that d does not represent a [[factor]] and therefore must not be cancelled out, in the same way, even if the notation is one of the fraction, this is not a fraction.
To be precise, in [[Leibniz notation]] instead of using (x, f(x)) and (x+h, f(x+h)) you use $(x,y)\ \ (x+\delta x, y+\delta y)$ so in the end the $gradient=\frac{rise}{run}$ is $= \frac{\delta y}{\delta x}$ which is simplified to $\frac{dy}{dx}$ or sometimes $\frac{d}{dx}$

In example, if before you said the derivative of $x^2$ as $f'(x)=2x$ now you write $\frac{d}{dx}(x^2)=2x$

##### derivatives of functions with restricted domains

Not all functions have a [[domain]] that include all [[real numbers]], some have a limited domain. We said that [[function]]s that have a limited domain or similar are not [[differentiable]] in that point but that is not fully true.
A [[function]] that start from the origin and change with positive values but does not exist for negative values can have a tangent even in the point where it originates even if you can not get closer to it from values below. The reason is that you can get closer with values above, therefore we say that the point is [[right differentiable]] or [[left differentiable]] and the [[right derivative]] at that point is 0: 
![[right_derivative]]

Technically the definition works the other way around, saying a [[function]] is [[differentiable]] means that it has the same [[right derivative]] and [[left derivative]].
It is important to note that this is only possible because the point noted O is included in the [[domain]], if it were not included there would not be any [[derivative]]

##### [[derivative]] of power [[function]]s

You can see the previously calculated [[derivative|derivatives]] to notice that the [[derivative]] of a function $y=x^n$ is $\frac{d}{dx}(x^n)=nx^{n-1}$

This can be calculated by getting the value of $(x+h)^n$ but this can be difficult at time, also the rule stated above is not just for positive values but of all values (as long as they are in the [[domain]] of course).

![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_7]]

What happens however when you have a [[function]] with an exponent but also a constant in front? Normally, multiply a function by a constant, say from $f(x)=x^2$ to $f(x)=mx^2$ is called [[vertical scaling]] and it stretches the graph vertically or flip it for negative m.
To understand what happens to the [[derivative]] think of what happens to the gradient of a line graph when you [[vertical scaling|vertically stretch it]].

The answer is that it simply goes up by that amount, if you think of $f(x)=x$, the gradient is 1, when you [[vertical scaling]] it to say $f(x)=3x$ the gradient become 3.
We know that lines are also [[curve]]s so such rule apply not only for lines but for all curves.
Now that we know how the [[gradient]] changes, we know the [[derivative]] change the same way since it is in fact the [[gradient]]. This is called [[constant multiple rule]] and it states that $k(x)=af(x) \rightarrow k'(x)=af'(x)$ or $y=au \rightarrow \frac{dy}{dx}=a\frac{dy}{dx}$.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_9]]

You also saw that for a function that is a constant like $f(x)=1$ is the same as $f(x)=x^0$ which $f'(x)=0x^-1$ which is $f'(x)=0$. If you combine it with [[constant multiple rule]] you find that for every [[function]] that correspond to a constant you have a [[derivative]] of 0, which make sense because the [[straight-line graph]] is a horizontal line which has [[gradient]] 0.

##### [[sum rule]] of [[derivative|derivatives]]

To start, think about what happens to the values of y when you sum two [[function]]s together, the answer is that the values are simply the sum of the two [[function]]s.
The same thing happens to the [[gradient]] although it is harder to show or demonstrate, so in [[Lagrange notation]] $k(x)=f(x)+g(x) \rightarrow k'(x)=f'(x)+g'(x)$ or in [[Leibniz notation]] $y=u+v \rightarrow \frac{dy}{dx}=\frac{du}{dx}+\frac{dv}{dx}$.
This also works for subtraction, because in reality they can be reduced to a [[sum rule]] and a [[constant multiple rule]] because $f'(x)-g'(x)=f'(x)+(-g'(x))$.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_11]]

##### [[velocity]] of a fallen object

After knowing what a [[displacement]], [[speed]] and [[displacement-time graph]] are we can use what we know now to work further on such graph.
If we assume that there is no air resistance, we can plot the [[displacement-time graph]] of a falling object and realize that it is independent of the weight of the object itself.
Knowing the [[gravitational pull]] of the planet, we know that the relation described in the [[displacement-time graph]] of a falling object is $s=-4.9t^2$ (if time in seconds and [[displacement]] in meters)where s is the [[displacement]], t is the time and the negative sing is because we take as reference the point the object start to fall from, therefore moving down gives it a negative sign.

At this point we know the definition of [[derivative]] and that it is basically the [[rate of change]] of the [[rate of change]] of a graph or the [[rate of change]] of the [[gradient]] of a graph. Since the [[gradient]] describe how the y changes with the changes of x, in a [[displacement-time graph]] it means knowing how the [[displacement]] change in relation to the time, which is called the [[velocity]] as we say previously.
Knowing the [[derivative]] of a [[displacement-time graph]] means that we know the [[velocity]] at any infinitely small point and therefore we can calculate the [[speed]] at any moment. Calculating the [[derivative]] of the equation above gives us $v=\frac{ds}{dt}=-9.8t$ which is the equation of the [[velocity]] of a free falling object ignoring air drag

![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_12]]

##### finding where [[function|functions]] are [[increasing function|increasing functions]] or [[decreasing function|decreasing functions]]

We already met the definition of an [[increasing function]] or [[decreasing function]], and that is a [[function]] for which every point successive to another follow the defined increasing or decreasing rule.
This can be deduced approximately by a graph, but never exactly. Since the [[derivative]] is nothing else than the [[gradient]] of the curve at any specific point, this can tell us if the [[function]] is [[increasing function]] or [[decreasing function]].
So for an interval in which $f'$ is positive $f$ is increasing and vice versa
![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_14]]

![[activity_15]]

Some functions, namely the once that are not always [[increasing function]] or [[decreasing function]], are likely to have a point where the [[gradient]] change and therefore in that specific point it has to be 0, these points are called [[stationary point|stationary points]].
![[stationary_point]]

Each [[stationary_point]] represent likely a change in the [[gradient]], therefore the part that comes before and after has to have an increasing or decreasing gradient opposite to the other. This means that such point is at the top or bottom of those two regions, depending on this we call it a [[local maximum]] or [[local minimum]], in the case of the graph above, the point on the right is a [[local minimum]] and the point on the left is a [[local maximum]]. A point where a [[function]] has a [[local maximum]] or [[local minimum]] is also called a [[turning point]].
![[Pasted image 20241206120754.png]]
These for example are not [[turning point|turning points]] but are [[stationary point|stationary points]] and in these cases they are also called [[horizontal point of inflection]].

Since a [[stationary point]] is a point at which the [[gradient]] is 0 by definition, it is easy to find it with the tools we have now, all we need is to solve $f'(x)=0$
![[activity_16]]

In total, we can find the nature of a [[stationary point]] by following the [[first derivative test]] which states that:
- if there is an open interval at which $f'$ is positive to the right and negative to the left, such point is a [[local minimum]]
- if there is an open interval at which $f'$ is positive to the left and negative to the right, such point is a [[local maximum]]
- if there is an open interval at which $f'$ is positive or negative to both left and right, such point is a [[horizontal point of inflection]]
![[activity_17]]

There is another way of finding [[stationary point]]s, [[local maximum]]s and [[local minimum]]s, once you find a [[stationary point]] you choose two points before and after, fairly close, with no other [[stationary point]] in the middle and where the [[function]] is [[differentiable]].
Then you find the value of the [[derivative]] of the [[function]] and you know that:
- if the [[derivative]] of the points is positive on the left and negative on the right it is a [[local maximum]]
- if the [[derivative]] of the points is negative on the left and positive on the right it is a [[local minimum]]
- If the [[derivative]] of the points is positive or negative at both points it is a[[horizontal point of inflection]]
![[activity_18]]

##### [[second derivative]]

Up to this point we saw the functioning and uses of getting the [[derivative]] of a [[function]], however, the result is also a [[function]] and as such it is [[differentiable]].
When you get the [[derivative]] of the [[derivative]] it is called [[second derivative]] or [[second derivative|second derived function]] (technically the [[derivative]] is the [[derivative|first derivative]] but for convention it is called just [[derivative]]).
The [[Lagrange notation]] is $f''(x)$ and the [[Leibniz notation]] is $\frac{d^2y}{dx^2}$, where the [[second derivative]] is possible the point is defined as [[twice-differentiable]].
Technically you can keep going and get the [[third derivative]], [[forth derivative]] and so on, a [[function]] can even be infinitely [[differentiable]].
![[activity_26_27]]


One big connection that can be drawn between the [[second derivative]] and the original [[function]] is if the original [[function]] is concave up (u shaped) or concave down (n shaped). If you think about the [[derivative]], it tells us the gradient of the [[function]], when this is negative the function is decreasing and vice versa, the [[second derivative]] is the [[gradient]] of the [[gradient]], so when the [[second derivative]] is negative, the [[derivative]] is decreasing so the [[gradient]] of the function is decreasing making it a [[concave down]] or [[concave]], vice versa we say the [[function]] is [[concave up]] or [[concave up|convex]].

##### [[second derivative test]]

This knowledge can be used in the [[second derivative test]], we know that a [[function]] can be deduced to be [[concave up|convex]] or [[concave down|concave]] based on the [[second derivative]], and it is easy to imagine why at a [[stationary point]] the function is one of the two, if it is [[concave up|convex]] it is a [[local minimum]] and if it is [[concave down|concave]] it is a [[local maximum]].

![[1 - Projects/MST124 24J Essential mathematics 1/unit_6/activity_28]]
