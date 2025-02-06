With complex [[derivative]] I mean all the rules that are used in [[calculus]] to deal with finding the [[derivative]] of [[function]] that include [[trigonometric raio]] and more, but at the end of the day, it is still [[differentiation]].

Remember that when dealing with [[derivative|derivatives]] of [[trigonometric function|trigonometric functions]], unless stated otherwise, the unit to consider are always [[radian|radians]].

##### [[derivative of sin]]

If you look at the [[sin graph]] you can start to have an idea of the behaviour of the gradient. The line [[tangent]] to the function seems to be 1 at the origin, than 0 at the peak of $\frac{\pi}{2}$ and than negative up to -1 on $\pi$, 0 at $\frac{\pi 3}{2}$ and back to positive.
Therefore in the end the graph looks something like:
![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_1]]

If you pay attention you notice that this is just the regular [[sin graph]] shifted to the left by $\frac{\pi}{2}$, and if you remember this is exactly the [[cos graph]] and in fact it is true that $f(x)=sinx \rightarrow f'(x)=cosx$. There is a more rigorous way to prove it mathematically but it is more complex and not necessary to remember even thought it is a good exercise [[proof_derivative_sin.pdf]]

##### [[derivative of cos]]

If you do a similar procedure to the [[derivative of sin]] to get the [[derivative of cos]] we notice that the graph looks almost like the [[sin graph]], however reflected on the [[y-axes]].
In fact $f(x)=cosx\rightarrow f'(x)=-sinx$.
Another way to deduce it is by the fact that you can obtain the graph of the [[cosine]] by translating the graph of the [[sine]] left by $\frac{\pi}{2}$ so the same can be said for the graph of the [[derivative of cos]].

##### [[derivative of tan]]

you have that $f(x)=tanx\rightarrow f'(x)=sec^2x$, remember that $sec^2x=(secx)^2$ and that $sec=\frac{1}{cos}$ so technically $f'(x)=\frac{1}{(cosx)^2}$.

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_2]]

This can be confirmed using the [[quotient rule]]:
$tanx=\frac{sinx}{cosx}\rightarrow f'(x)=\frac{cosx * cosx - sinx * (-sinx)}{cos^2x}=\frac{cos^2x+sin^2x}{cos^2x}$, from [[pythagoras theorem]] we know $cos^2x+sin^2x = 1$ so in the end $\frac{1}{cos^2x}$.

The same can be said for the other [[trigonometric ratio]]s and get:
- [[derivative of cosec]] $\frac{d}{dx}(cosecx)=-cosecx*cotx$
- [[derivative of sec]] $\frac{d}{dx}(secx)=secx*tanx$
- [[derivative of cot]] $\frac{d}{dx}(cotx)=-cosec^2x$

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_10]]

##### [[derivative of exp]]


Finding the [[derivative]] of $e^x$ is not super simple but not as bad, we can start with the more intuitive approach, working with the graph.

![[Pasted image 20241216094042.png]]
We know that by definition, e is that number that when has 0 as exponent the [[gradient]] of the graph is 1 so we can start there.
If we look at the structure of the graph and try to intuitively derive the gradient, we notice that it goes lower and lower getting close but never to 0 on the left and higher and higher on the right, which is exactly like the graph we already have, so maybe $f(x)=e^x\rightarrow f'(x)=e^x$.

Now we can try to get a more mathematical proof using the [[difference quotient]], if we apply for the [[exponential function]] we get $\frac{e^{x+h}-e^x}{h}$, we need to understand what happens as h gets closer to 0.
For starters, we know that $f'(0)=1$, so $\frac{e^{0+h}-e^0}{h}\rightarrow \frac{e^{h}-1}{h}$ so this expression gets closer to 1 as h gets closer to 0 because we know the gradient of that point is 1 by definition.
Now we can rearrange the initial [[difference quotient]] so $\frac{e^{x+h}-e^x}{h}\rightarrow \frac{e^{x}e^{h}-e^x}{h}\rightarrow e^{x}\frac{e^{h}-1}{h}$, we know that as h gets closer to 0 the second term gets closer to 1, so only the first term is relevant which is $e^x$ as we got intuitively before

##### [[derivative of natural logarithm|derivative of ln]]

We can start by acknowledging the fact that the [[function]] $f(x)=lnx$ is the inverse of $f(x)=e^x$ so the graph is the [[reflecting]] on the y=x axes:
![[Pasted image 20241216101412.png]]

Looking at the graph we can say that as x gets closer to 0 from the right, the [[gradient]] gets closer to infinity, so it comes down from infinity and gets slower and slower but never quite to 0.

We can prove this a bit better thought. Start again from the fact that $lnx$ is the inverse of $e^x$ so reflected on the $y=x$ axes, so each [[tangent]] on one graph corresponds to a [[tangent]] on the other reflected on the y=x axes.
If we take two of these linen and get the gradients, we have that the [[gradient]] of the [[tangent]] of the [[natural logarithm]] is the [[reciprocal]] of the [[gradient]] of the [[tangent]] of the [[exponential function]]:
![[ln_to_exp_gradients]]

So if for $e^x$ the gradient is $\frac{a}{b}$ for $lnx$ the gradient is $\frac{b}{a}$. Now we can consider a point on the [[logarithmic function]], that has coordinates $(x,lnx)$, by definition the [[reflecting]], which in this case is the [[inverse function]], so the [[image set]] of one become the [[domain]] of the other and vice versa, will have coordinates $(lnx,x)$. We know that the derivative for $f(x)=e^x$ is $e^x$ so the [[gradient]] is $e^x$ so at the x $lnx$ it is $e^{lnx}$ which is x. We know the [[gradient]] of the [[logarithmic function]] is the [[reciprocal]], therefore the gradient is $\frac{1}{x}$.
In fact we have that $f(x)=lnx\rightarrow f'(x)=\frac{1}{x}$.
However, the domain of the [[logarithmic function]] is $[0,\infty)$ , so the same has to be stated for the [[derivative]] which is admissible for $x>0$.
![[Pasted image 20241216110435.png]]

##### [[product rule]]

Unfortunately it is not as easy as multiply the [[derivative]], but it is also not that bad.
$k(x)=f(x)g(x)\rightarrow k'(x)=f(x)g'(x)+f'(x)g(x)$

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_4_5]]

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_6_7]]

The proof start from the [[difference quotient]] again, if $k(x)=f(x)g(x)$ than $\frac{k(x+h)-k(x)}{h}$ so we can say $\frac{f(x+h)g(x+h)-f(x)g(x)}{h}$.
At this point you can add and subtract $f(x)g(x+h)$ which is the difference of the two quotient and you get:
$\frac{f(x+h)g(x+h)+f(x)g(x+h)-f(x)g(x+h)-f(x)g(x)}{h}$, which can become $(\frac{f(x+h)-f(x)}{h})g(x+h)+f(x)(\frac{g(x+h)-g(x)}{h})$
Now, the first bracket is the [[difference quotient]] for $f(x)$ so as h gets closer to 0 it become $f'(x)$, the second big brackets does the same for $g'(x)$, $f(x)$ stay the same and $g(x+h)$ gets closer to $g(x)$.
If you consider this the overall quotient gets closer to $f'(x)g(x)+f(x)g'(x)$.

##### [[quotient rule]]

The rule comes out to be $k'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}$ where $k(x)=\frac{f(x)}{g(x)}$.
A way to get the proof is that if you have a function $k(x)=\frac{g(x)}{f(x)}=g(x)f(x)^{-1}$, you can differentiate this using the [[product rule]] $g'(x)f(x)^{-1}+g(x)\frac{d}{dx}(f(x)^{-1})$, you can now use the [[chain rule]] to get $g'(x)f(x)^{-1}+g(x)(-1f(x)^{-2})f'(x))$ and $\frac{g'(x)}{f(x)}-\frac{g(x)f'(x)}{f(x)^2}$ and arrange to the final formula.

Remember to be careful about the order here because you have a - in the middle so the first term must be the [[derivative]] of the top with the bottom and the second must be the [[derivative]] of the bottom with the top

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_8_9]]

[[chain rule]]

The [[chain rule]], also called [[chain rule|composite rule]] or [[chain rule|function of a function rule]] is a rule that allows you to get the [[derivative]] of a [[function]] that is made of more functions inside.
The first thing you need to do however is, recognize when this is the case and [[decompose]] the original [[function]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_11]]

At this point you have the actual rule:
	$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$

The proof is outside the scope but a concept is that, if you have a function made of two functions, the first grows of n every unit ([[gradient]]) and the second grows by m every unit ([[gradient]]), the resulting final function grows for both on every unit so $mn$.

![[activity_12_13_14]]


The reason why this is called the [[chain rule]] rule is that it is not limited to two functions but potentially can be done for n functions one inside the other where $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dv}\frac{dv}{dx}$ .

##### combining [[differentiation]] rules

Overall, you can now combine the [[differentiation]] you have met so far, remember that you should always differentiate from the outside to the inside, so when you apply the rule, you always apply them to the bigger structure first and only than to the inner one

![[activity_17_18_19]]

##### [[optimization problems]]

These are problems that involves choosing the best option among a suite of possibilities, they can be [[maximization problems]] or [[minimisation problems]] if you are looking for the max or min value.

- find the [[stationary point]]
- find the value of the [[function]] at the [[stationary point]] and the end points of the domain
- find the greatest or least

![[1 - Projects/MST124 24J Essential mathematics 1/unit_7/activity_20_21]]

When it comes to more real applications like those, the general strategy to solve should be:
- identify the final quantity to measure and the formula that leads to it
- identify the variable that can change and how they change
- identify how those variable fit in the formula
- deduce the equation that describe your quantity
- get derivative and stationary points
- work out which are [[local maximum]] or [[local minimum]]


##### [[derivative of an inverse function]]

if we suppose that y is [[inverse function]] of x it means that x is also a [[function]] and the [[derivative]] of a x to x is 1:
$\frac{dx}{dx}=1$
However, we can use the [[chain rule]] to rewrite it to say that $\frac{dx}{dx}=\frac{dx}{dy}\frac{dy}{dx}$ so it is equal to 1 so $\frac{dy}{dx}=\frac{1}{\frac{dx}{dy}}$.

In words, we know that the [[derivative]] is the gradient of the function or the change in the [[gradient]] to be precise. If y is an [[invertible]] [[function]] of x, x is also a [[function]] of y, so if for every y increase, x increase by 2, you would expect that for every value of x, y increase by $\frac{1}{2}$.	

What this rule express, is the same as what we saw with the [[derivative of natural logarithm]], where it is plotted against the [[exponential function]] as it's inverse and therefore the [[rise]] and [[run]] are inverted, so the two [[gradient]] are the [[reciprocal]] of each other


