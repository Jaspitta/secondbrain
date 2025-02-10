
##### [[signed area]]

Suppose that you have a house with a rounded roof, you want to know the area taken by that roof until the flat portion of the house.

![[{F07DCCDB-8C0A-4B1E-B29B-EE8980D1EF43}.png]]

What you can do is divide the colored part into rectangles and get an approximation of the area:

![[1 - Projects/MST124 24J Essential mathematics 1/unit_8/activity_1]]

If you keep dividing the shape into smaller and smaller rectangles, you notice that the value of the area get closer and closer to a number. This number is called the [[limit]] of the approximation as the number of squares [[tends to infinity]].

This concept works when trying to calculate the area of any [[continuous function]].

It can happens that the shape is below the [[x-axes]], in such cases you notice that you end up with a negative area. If what you care is simply the area, you can ignore the minus sign, however it is worth making the distinction.
We call the [[signed area]] the area with the sign included, which shows weather it lays above or below the [[x-axes]]

The definition of the area of a [[continuous function]] up until know has been defined from a to b where a is less than b, however, the full definition says that the same area from b to a is the negative of the area from a to b.
This means that when calculating the [[signed area]], if there is no mention of a and b you can simply consider whether it lies above or below x, but if there is a mention and b is smaller than a you will need to flip the sign at the end.

##### definition of [[definite integral]]

Now that you know what the [[signed area]] is it is easy to define the [[definite integral]], that is the [[signed area]] for a [[continuous function]] between the graph of the [[function]] and the x axes from a to b, written as $\int_{a}^{b} f(x)dx$ where a and b are the lower and upper [[limit of the integration]] (the symbol $\int$ is called the [[integral sign]]).
![[1 - Projects/MST124 24J Essential mathematics 1/unit_8/activity_6_7]]

Remember that $f(x),\ a$ and $b$ are all [[dummy variable]], you can replace them with any letter you like as long as you coherent when you use them in a problem.

What the [[definite integral]] express is the [[signed area]], so for $\int_{a}^{b}f(x)dx$ we have that when we apply the formula of the [[signed area]] we have n rectangles with base $(b-a)/n$ which we denote as $w$. The endpoints nearest to a are $a+0w,\ a+1w,\ ...,\ a+(n-1)w$ and therefore the value of the signed area is $f(a+0w)*w+f(a+1w)*w,\ ...,\ f(a+(n-1)w)*w \rightarrow (f(a+0w)+f(a+1w),\ ...,\ f(a+(n-1)w))w$.
As n gets larger, w gets smaller because there are more rectangles and the value therefore gets closer to the actual [[definite integral]] $\int_{a}^{b}f(x)dx$ in total we say $\int_{a}^{b}f(x)dx=\lim_{x\to\infty}(f(a+0w)+f(a+1w),\ ...,\ f(a+(n-1)w))w$

##### [[integration by substitution]]

At the core, it is the reverse of the [[chain rule]] for [[derivative]], so since the chain rule works with $\frac{dy}{dx}f(t) = (\frac{dy}{dx}f(t))*(\frac{dy}{dx}t)$, if you can recognize $t$ or a [[integral]] that has such form, you can deduce the result. To make it simpler the form of the [[integral]] should be $f(something)*derivative\ of\ something$ since that is the result of the [[derivative]].
Once you recognize the something, you can rewrite the [[integral]] as $f(something)$ where something becomes say $u$ so $\int f(u)du$, now you find the [[integral]] of this [[function]] and lastly you replace the $u$ with the $something$, the opposite of what you do with the [[chain rule]].

The reason we can say that $\int f(u)\frac{du}{dx}dx=\int f(u)du$ is the following, say that we have $F(u)$ which is an [[antiderivative]] of $f(u)$, it means that $F'(u)=f(u)$, and in the same way $\int f(u)du=F(x)+c$. By the [[chain rule]] (because $u$ is a [[function]], say $g(x)$) $\frac{d}{dx}(F(u))=F'(u)*\frac{d}{dx}u$, and so $\frac{d}{dx}(F(u))=f(u)*\frac{d}{dx}u$. If we integrate both sides $\int \frac{d}{dx}(F(u))dx=\int f(u)*\frac{d}{dx}u\ dx$, $\int$ and $\frac{d}{dx}$ cancels out and so it become  $F(u)+c=\int f(u)*\frac{d}{dx}u\ dx$. We already saw before that $\int f(u)du=F(x)+c$ so we can replace to get the final answer $\int f(u)*\frac{d}{dx}u\ dx=\int f(u)du$

![[activity_21_22_23_24_25_26_27_28_29_30]]

Of course, this is not limited to [[indefinite integral]] but it can be used for [[definite integral]] as well in the same exact way.

![[1 - Projects/MST124 24J Essential mathematics 1/unit_8/activity_32]]

Sometimes you can use [[integration by substitution]] even when there is an extra factor outside the main one and it looks like the form is not $f(something)*\frac{d}{dx}something$. For example if you have $\int (x+1)(ax+1)^n$, where $a$ and $n$ are constants it may look like there is no way to use [[integration by substitution]] because there is an extra $x$.
Sometimes however you can rewrite the term in $u$, so if $u=(ax+1)$, the [[derivative]] is $a$ and you can rewrite $x$ in terms of $u$ as $x=\frac{1}{a}(u-1)$, because the initial factor had $x+1$ you also have to add the +1. Now you can rewrite the initial [[integral]] in $u$, $\frac{1}{a}\int (\frac{1}{a}(u-1)+1)au^ndu$, the $a$ is added because it needs to satisfy the form of [[integration by substitution]] and the bigger part before is the $x+1$ expressed as u. Now you can multiply and solve the [[integral]] normally.

![[1 - Projects/MST124 24J Essential mathematics 1/unit_8/activity_33]]

##### [[integration by parts]]

Like the [[integration by substitution]] is the reverse of the [[chain rule]] the [[integration by parts]] is the reverse of the [[product rule]].
Suppose you have a function f and g where G is the [[antiderivative]] of g, if you apply the product rule to f and G you get $\frac{d}{dx}(f(x)G(x))=f(x)(\frac{d}{dx}G(x))+f'(x)G(x)$, we know that $\frac{d}{dx}G(x)$ can be written as $g(x)$ since we established it is the [[antiderivative]].
If you adjust the initial equation now we get $f(x)g(x)=-f'(x)G(x)+\frac{d}{dx}(f(x)G(x))$, now if we integrate both sides we get  $\int f(x)g(x)dx=f(x)G(x))-\int f'(x)G(x)dx$.
Basically it moves the problem to integrating $\int f'(x)G(x)dx$, so it makes sense only when you can find a $G(x)$ from $g(x)$ and the product is easier to integrate.
When integrating with this method, be very careful to $f'(x)$ and $G(x)$, sometimes getting one of these may require more complex methods like [[chain rule]] or [[integration by substitution]] in itself, you can see the mistake I did below, sometimes it can even happen that in the [[integral]] you get into [[integration by parts]] you need to use again complex [[integral]] procedures.
![[activity_34_35_36_37_38_39_40_41_42_43_44_45]]

