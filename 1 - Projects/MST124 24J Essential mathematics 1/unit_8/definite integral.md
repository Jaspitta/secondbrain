
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