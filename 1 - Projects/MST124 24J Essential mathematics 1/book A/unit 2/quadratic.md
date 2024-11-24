A quadratic is either referred to a [[quadratic expression]] or a [[quadratic equation]].
The first has form $y = ax^2 + bx + c$ and the second $ax^2 + bx + c = 0$ where in both cases a, b and c are constants and a != 0.

No matter the [[equation]] if it follows the rules of a [[quadratic]] its graph will be a [[parabola]] which is a [[quadratic graph]].

To know how it changes compared to a, b and c you can look at the [applet](https://learn2.open.ac.uk/mod/oucontent/view.php?id=2296164) but in genera:
- a changes how tight or wide it is, if negative it is n shaped if positive u shaped
- c moves it up and down
- b moves the parabola compared to the [[y-interceps]], growing b will slide the whole parabola to the right if a positive or to the left if a negative. It does not move it simply horizontally, it **slides** the whole thing by keeping the [[y-intercepts]] and if negative the [[vertex]] of the [[parabola]] will be below the [[x-axes]]
![[b slide on parabola]]


The peak of a parabola is called a [[vertex]]. A [[parabola]] has zero, one or 2 [[x-intercepts]] but always one [[y-interceps]] because there is always at least one value of y for which x is 0.

A common way to work with a [[quadratic]] is [[factorising]], that is in this case writing it as the multiplication of 2 [[linear equation]] or expressions. While it is always technically possible to use [[factorization]] on a quadratic, it only make practical sense when the result are expressions with integers and not all [[quadratic]]s made of integers gives such expressions.
There are a few cases for such process:
- where $a = 1$: you start by knowing that they will have form $(x + n)(x + m)$, now you find 2 numbers that multiply to c and add to b. Usually you write the numbers that multiply to c and look for the pair that sum to b. If you can not find the solution it means that the numbers are not integers
- where a != 1: you can consider all the pairs that multiply to a and use the first method for each pair where the starting point will me $a=m*n => (mx+f)(nx+z)$. You also have to consider that for each pair you need to find the b to check if it matches with the starting one
- my strategy:
	- if $(ax+b)(cx+d)$ we known $acx^2 + adx + bcx + bd$
	- we can go back to the starting equation and solve it as a system of [[simultaneous equations]]
- if c = 0: you just take x out
- if b = 0: it might be a [[difference of two squares]] $a^2-b^2=(a+b)(a-b)$

One way to rearrange a quadratic is to express in [[completed-square form]] that is form $ax^2+bx+c$ to $a(x+r)^2+s$ where r and s are new constants.
When you meet a [[quadratic]] in the form $ax^2+bx$ all you need to do is find the equivalent $(x + )^2$ which of course will have an extra term c, that you need to subtract using s as it's negated value.
From this, moving to solve those in the form $ax^2+bx+c$ is simple, you do the same as before but than group the constants.
Very similarly, if a != 1, you can simply factor out the coefficient to get it to be in the form of a = 1 and than proceed normally like said before.


The grand daddy of them all, the [[quadratic formula]]: $x = \frac{-b+-\sqrt{b^2-4ac}}{2a}$ 

If we imagine a [[quadratic]] where a != 0, it is the discriminant under the square root that determines how many solutions the equation has, and as a consequence, how many [[x-intercepts]] the graph of the equation has, since they are in fact the solutions.
This portion is called [[discriminant]] and can lead to 3 scenarios:
- $b^2-4ac = 0$ one real solution
- $b^2-4ac > 0$ 2 real solutions
- $b^2-4ac < 0$ no real solutions


Other cases that are somewhat related are cases where an equation may be more than second grade but can be simplified to it.
Some [[cubic equations]] can be simplified by grouping for x and than solving the equation separately.
In some cases you can substitute, for example $x^4-5x^2+4=0$ can be solved by imagining $t=x^2$ and so $t^2-5t+4=0$

When you are [[sketching]] a parabola you want to find some key properties and plot them:
- find if it is u shaped or n shaped
- find it's [[x-intercepts]], y=0
- find it's [[vertex]]:
	- find the axe of symmetry:
		- the mean between any 2 point p and q with the same y so $(p+q)/2$
	- find the point where the curve meet the symmetry axe


