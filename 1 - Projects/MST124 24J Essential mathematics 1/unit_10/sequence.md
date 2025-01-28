In mathematics a sequence is simply a series of numbers. It can be a finite amount of them making it a [[finite sequence]] or a infinite amount making it an [[infinite sequence]] .
Usually a [[sequence]] has a patter that describe it's [[term]]s, which are the single elements, but not necessarily.

A [[sequence]] uses a [[subscript notation]] where the elements are written as $a_1, a_2, a_3 ... a_{10}$.
The full way to denote a sequence is $(a_n)^{17}_n=1$ for a [[sequence]] of 17 elements or $(a_n)^{\infty}_n$ sometimes abbreviated to $(a_n)$ to represent an infinite [[sequence]] and $n$ is just a [[dummy variable]] called [[index variable]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_1]]


##### [[closed form sequence]]

I general you can define a [[sequence]] by stating the formula for the [[nth term]] and the range, for example for perfect squares you have $1,4,9,25...$ so $s_1=1^2,s_2=2^2,s_3=3^2...$
You can see that the general formula is $s_n=n^2$ and if you add the range $(1,2,3...)$ of the subscript you have the full specification of the [[sequence]].
This type of [[sequence]], the [[closed form sequence]], gives you a formula called [[closed form formula]] which allows you to get the [[term]] n directly.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_2]]

![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_3]]

![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_4]]
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_5]]

##### [[recurrence relation for sequence]]

Another way to describe a [[sequence]] is by defining the next value based on the previous. For example a sequence where each value is twice the one before we saw can be written as $a_n=2^n$ but can also be described as $a_n=2a_{n-1}$ where the range now is $(n=2,3,4....)$.
The second type of way to describe a sequence now is called [[recurrence relation]] and in particular a [[first-order recurrence relation]] since it involves only the previous value and one particularity is that they also need the first term, $a_1$, to be explicitly stated.
So the [[recurrence sequence]] is described by a [[recurrence system]] which is the combination of the [[recurrence relation]], the range of n and the first [[term]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_6]]

One particularity of [[recurrence system]] is that it can be used to describe some irrationals numbers to as many decimals of precision as you want

##### [[arithmetic sequence]]

It is simply a [[sequence]] that is defined by adding a fixed number to the previous [[term]], it can also be called [[arithmetic progression]]. The gap from one value to the other, or the fixed number, is called the [[common difference]].
It always require a starting value to be specified, usually denoted by a and together with the [[common difference]] they make the [[parameters]] of the [[arithmetic sequence]].

![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_8]]

If d is 0, each term is equal to the first and the sequence is called a [[constant sequence]].
When the [[arithmetic sequence]] described has a final term, you also need to find the last value of n that the [[sequence]] can accept. Because each step has distance d all you need to do is $N=\frac{last-first}{d}+1$ where N is the final value n can take and the +1 is because you also need to consider the first term.

Sometimes it is convenient to have an [[arithmetic]] sequence described with a [[recurrence relation]], but sometimes it might not be, luckily there is a way to describe such sequences as [[closed form formula]]. In general the form is $first+d(n-1)$ this is because the recurrence add d every time so starting from the first number we than add d for each step, the -1 is because the first element must not have d added.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_10]]

##### [[geometric sequence]]

It is a type of [[sequence]] where each number is obtained by multiplying for a constant each previous [[term]], exactly like [[arithmetic sequence]] but this time with multiplication and can also be called [[geometric progression]].
The number that you multiply by is called the [[common ration]] and is obtained by dividing a term $\frac{x_n}{x_{n-1}}$ and together with the first value a they make the [[parameters]] of the sequence.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_11]]

Just like [[arithmetic sequence]], a [[geometric sequence]] can be finite and sometimes you want to find the max value n can take knowing the last element of the [[sequence]]. We know that the last element is obtained with the first element multiplied with the [[common ration]] n-1 times so $last=first*r^{n-1}$. We can solve the equation $r^{n-1}=\frac{last}{first}\rightarrow (n-1)lnr=ln\frac{last}{first} \rightarrow n=1+\frac{ln\frac{last}{first}}{lnr}$.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_10/activity_13]]

Another way to describe a [[geometric sequence]] is with it's [[closed form formula]]. Since when we go from one [[term]] to the other we multiply, it means that at the term n we will have multiplied the [[common ration]] n-1 times (remove the first [[term]]) and we will have started from the initial term. So if the initial term is $a$ we have $x_n=a*r^{n-1}$

##### [[graphs of sequence]]

Since a sequence is simply a rule that gives a set of values starting from another it has much similarities with a [[function]].
For this reason, just like a [[function]] you can plot the graph of a [[sequence]].
In particular an [[arithmetic sequence]] will give you a [[straight-line graph]] since every point grows of the same amount and therefore the [[gradient]] remain constant, on the other hand a [[geometric sequence]] has a [[curve]] shaped graph because the graph of the [[derivative]] is a [[straight-line graph]].

##### [[long-term behaviour of sequences]]

Much like [[function]], when we analyse a [[sequence]] we can define it a [[increasing]] or [[decreasing]] based on if the next value is bigger or smaller than the previous. Some [[sequence]]s have a pattern that alternate in a range, we call those [[bounded sequence]].
We an also say that a [[sequence]] become [[arbitrary large]] if it grows with no bound or [[arbitrary small]] if gets closer and closer to 0, in particular we say that $x_n$ tends to $0$ as $n$ tends to infinity. This can be extended to any number say L, a [[sequence]] can be of the type that $x_n \rightarrow L\ \ as\ \  n \rightarrow \infty$.

Since [[arithmetic sequence]]s result in a [[straight-line graph]] their long term behaviour is easy to describe. They have form $x_n=b+dn$ with $b=a-d$ and therefore if d greather than 0 they $x_n \rightarrow \infty\ \ as\ \  n \rightarrow \infty$, if d 0 it'a a constant and if d less than 0 $x_n \rightarrow \infty\ \ as\ \  n \rightarrow -\infty$.

On the other hand [[geometric sequence]]s are more difficult to describe. They take the form $cr^n$ where $c=\frac{a}{r}$ so we can describe the behaviour of $r^n$. The are three special cases, when r is 0 the sequence is always 0, when 1 always 1 and when -1 it alternates between 1 and -1. When r is between 0 and 1 the sequence shrink slower and slower, when > 1 it grows steeper and steeper. Basically it behaves like the [[exponential function]].
