As the name suggest, it is one of the basis of the whole discipline of [[calculus]] and it is also what links the concepts of [[signed area]] and [[rate of change]] in terms of [[derivative]] and [[integral]].

To understand [[the fundamental theorem of calculus]] we start with a [[continuous function]] $f$, we then define the [[signed area]] between $f$ and the [[x-axes]] as $A(x)$ starting from a point $s$ ending to a point $x$, in other words $\int_{s}^{x}f(t)dt=A(x)$ and we call this the [[signed area so far]]. Notice that by the rule of [[signed area]], we have that if we choose and interval from $x=a$ to $x=b$ and consider the [[signed area]] of such interval when the [[function]] is in the [[signed area so far]], we have that the [[signed area]] is $A(b)-A(a)$.
![[Pasted image 20250102095205.png]]



Now we can analyze how the [[signed area so far]] changes with respect to the changes of x. You start from a constant function where $f(x)=k$, if you plot the graph you see a horizontal line with height $k$, therefore if you consider an area from say $a=1$ to $b=5$, it will form a square with base $b-a$ and height $k$ with [[signed area so far]] $(b-a)*k$. What you find is that for every unit of $x$ the [[signed area so far]] changes by $k$, because the value of $(b-a)$ changes by 1.
If you do the same for a non constant function that is [[continuous function|continuous]] it becomes more difficult to understand the area between two points, however we can simplify by looking at the [[instantaneous rate of change]]. For the constant function, the height was always $k$, so at an interval infinitely small the [[rate of change]] of the [[signed area so far]] or the [[signed area]] for that matter was always $k$, now, if at any point of a [[continuous function]] we take the [[instantaneous rate of change]], that would be equivalent to the [[instantaneous rate of change]] of the function that is a constant [[function]] with $k$ equals to the current $f(x)$ in that moment, therefore the [[instantaneous rate of change]] is $f(x)$. If we understand [[derivative]] we can notice that the [[instantaneous rate of change]] is described exactly by the [[derivative]] of the function, therefore, if the [[instantaneous rate of change]] of the [[signed area]] is $f(x)$ as we said so far, the [[derivative]] of the [[signed area]] is $f(x)$ and as such, the [[antiderivative]] of $f(x)$ or the [[integral]] is $A(x)$, so the [[signed area]].

![[fundamental_theorem_calculus]]

Overall we say that for any [[continuous function]] $\int_{a}^{b}f(x)dx=A(b)-A(a)=F(b)-F(a)$ where $F(x)$ is the [[antiderivative]] of $f(x)$, and the [[signed area]] is therefore the difference in such [[antiderivative]].

It's worth mentioning that the [[signed area]] as the difference in the [[antiderivative]] can also be stated as $F(a)-F(b)=[F(x)]_{a}^{b}=\int_{a}^{b}f(x)dx$.

![[activity_8_9_10_11_12_13_14]]

Calculating the area of the function is not good only for itself but can also be used for problems related to [[rate of change]].