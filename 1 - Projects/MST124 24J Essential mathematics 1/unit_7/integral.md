[[integral]] or [[integral calculus]] is that area of [[calculus]] that deals with the reverse process of the [[derivative]].
With [[differentiation]] you have the definition of the change of a quantity and you can get the definition of the rate of change, with [[integral|Integrals]] you do the reverse process, from the definition of a rate of change you want to get the definition of the change of the quantity.

The process of finding [[integral|integrals]] is also called [[integration]] or [[antidifferentiation]] because you start with a [[function]] $f$ and you want to find a [[function]] $F$ whose [[derivative]] is $f$.

The first problem is that any [[function]] like $f(x)=x^2+b$ will result in $f'(x)=2x$, no matter the value of b, so how can I deduce from the [[derivative]] which is the original function? First of all, we know that this situation happens because the member $+b$ represent a [[vertical translation]] which does not affect the [[gradient]], but this also means that the derivative $2x$ is represented only by this type of [[functions]] so we could way $F(x)=x^2+c$, and this is called the [[complete family of antiderivatives]] or [[indefinite integral]] and c is called [[arbitrary constant]] or [[arbitrary constant|constant of integration]].

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_26_27]]

##### [[antiderivative of power]]

The working of an [[antiderivative]] is basically the reverse of the [[derivative]]. You know that for a [[function]] $f(x)=x^c$ the [[derivative]] is $f'(x)=cx^{c-1}$, so now you need to do the reverse.
If you have a function $f(x)= x^c$, the [[antiderivative]] must be $F(x)=\frac{1}{c+1}x^{c+1}$, this way, if you have $f(x)=x^6 \rightarrow F(x)=\frac{1}{7}x^7$, in fact the [[derivative]] of the second gives the first and therefore the [[indefinite integral]] is $F(x)=\frac{1}{c+1}x^{c+1}+a$.
One special case is where you have $f(x)=1$, the [[antiderivative]] is simply $x$ and the [[indefinite integral]] is $x+c$, this is because we saw that $x^0=1$ and therefore $f(x)=1=x^0\rightarrow F(x)=\frac{1}{0+1}x^{0+1}=x$
![[activity_28_29]]

##### [[constant multiple rule for antiderivatives]]

Since the [[constant multiple rule]] allow for a constant to simply be carried over, the same can be done in reverse, so $kf(x) \rightarrow kF(x)$.

##### [[sum rule for antiderivatives]]

Since the [[sum rule]] simply state that the [[derivative]] is the sum of the [[derivative|derivatives]] of the single [[functions]], the same can be said in reverse, therefore $k(x)= f(x)+g(x)\rightarrow K(x)=F(x)+G(x)$.

![[activity_30]]

##### finding one specific [[antiderivative]]

Working out the [[indefinite integral]] is something that we already covered, however, it is common when modeling real life situations that you need a specific [[antiderivative]] and not the generic one.
You can work out such [[function]] when you have the value taken by it at a specific point.

![[activity_31]]

![[activity_32]]
![[activity_33_34]]

##### change in [[antiderivative]]

One peculiar thing to notice about the [[indefinite integral]] of a [[function]] is that it is true that it can be any function due to the constant c, however, if you consider the change from one point to the other, it does not matter which constant you choose, the result is the same.
This can be proved mathematically also $f(x)=x \rightarrow F(x)=\frac{1}{2}x^2+c$ and if you analyze a change, $F(a)-F(b)=\frac{1}{2}a^2+c-\frac{1}{2}b^2-c$, as you can see the c cancels out 


![[activity_35_36]]

##### [[antiderivative of reciprocal]]

We saw that the formula for [[antiderivative of power]] does not work for $x^{-1}$ because the function that has such [[derivative]] is $ln(x)$.
We can however say that the [[antiderivative]] of $\frac{1}{x}$ is $ln(x)$, but only when $x>0$ because we know $ln(x)$ has [[domain]] $x>0$.
To get the [[antiderivative]] for the negative portion we can use a little trick, we can define $ln((-x))$ and solve it with the [[chain rule]] which gives $-1\frac{1}{-x}=\frac{1}{x}$. So we have that also for $x<0$ the [[antiderivative]] is $\frac{1}{x}$.
Overall the result can be written as:

$$
 F(x)=
 \begin{cases} 
      ln(-x) & (x< 0) \\
      ln(x) & (x> 0)
\end{cases}
$$
However, you saw that for negative values, the result is still positive x, so we can say that $-x=|x|$ and $x=|x|$ so the final [[function]] can also be written as $ln|x|$ and the [[indefinite integral]] is $ln|x|+c$, where the graph is
![[Pasted image 20241223125103.png]]

![[activity_37]]

