In mathematics a sequence is simply a series of numbers. It can be a finite amount of them making it a [[finite sequence]] or a infinite amount making it an [[infinite sequence]] .
Usually a [[sequence]] has a patter that describe it's [[term]]s, which are the single elements, but not necessarily.

A [[sequence]] uses a [[subscript notation]] where the elements are written as $a_1, a_2, a_3 ... a_{10}$.
The full way to denote a sequence is $(a_n)^{17}_n=1$ for a [[sequence]] of 17 elements or $(a_n)^{\infty}_n$ sometimes abbreviated to $(a_n)$ to represent an infinite [[sequence]] and $n$ is just a [[dummy variable]] called [[index variable]].
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_1]]


##### [[closed form sequence]]

I general you can define a [[sequence]] by stating the formula for the [[nth term]] and the range, for example for perfect squares you have $1,4,9,25...$ so $s_1=1^2,s_2=2^2,s_3=3^2...$
You can see that the general formula is $s_n=n^2$ and if you add the range $(1,2,3...)$ of the subscript you have the full specification of the [[sequence]].
This type of [[sequence]], the [[closed form sequence]], gives you a formula called [[closed form formula]] which allows you to get the [[term]] n directly.
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_2]]

![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_3]]

![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_4]]
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_5]]

##### [[recurrence relation for sequence]]

Another way to describe a [[sequence]] is by defining the next value based on the previous. For example a sequence where each value is twice the one before we saw can be written as $a_n=2^n$ but can also be described as $a_n=2a_{n-1}$ where the range now is $(n=2,3,4....)$.
The second type of way to describe a sequence now is called [[recurrence relation]] and in particular a [[first-order recurrence relation]] since it involves only the previous value and one particularity is that they also need the first term, $a_1$, to be explicitly stated.
So the [[recurrence sequence]] is described by a [[recurrence system]] which is the combination of the [[recurrence relation]], the range of n and the first [[term]].
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_6]]

One particularity of [[recurrence system]] is that it can be used to describe some irrationals numbers to as many decimals of precision as you want

##### [[arithmetic sequence]]

It is simply a [[sequence]] that is defined by adding a fixed number to the previous [[term]], it can also be called [[arithmetic progression]]. The gap from one value to the other, or the fixed number, is called the [[common difference]].
It always require a starting value to be specified, usually denoted by a and together with the [[common difference]] they make the [[parameters]] of the [[arithmetic sequence]].

![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_8]]

If d is 0, each term is equal to the first and the sequence is called a [[constant sequence]].
When the [[arithmetic sequence]] described has a final term, you also need to find the last value of n that the [[sequence]] can accept. Because each step has distance d all you need to do is $N=\frac{last-first}{d}+1$ where N is the final value n can take and the +1 is because you also need to consider the first term.

Sometimes it is convenient to have an [[arithmetic]] sequence described with a [[recurrence relation]], but sometimes it might not be, luckily there is a way to describe such sequences as [[closed form formula]]. In general the form is $first+d(n-1)$ this is because the recurrence add d every time so starting from the first number we than add d for each step, the -1 is because the first element must not have d added.
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_10]]

##### [[geometric sequence]]

It is a type of [[sequence]] where each number is obtained by multiplying for a constant each previous [[term]], exactly like [[arithmetic sequence]] but this time with multiplication and can also be called [[geometric progression]].
The number that you multiply by is called the [[common ration]] and is obtained by dividing a term $\frac{x_n}{x_{n-1}}$ and together with the first value a they make the [[parameters]] of the sequence.
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_11]]

Just like [[arithmetic sequence]], a [[geometric sequence]] can be finite and sometimes you want to find the max value n can take knowing the last element of the [[sequence]]. We know that the last element is obtained with the first element multiplied with the [[common ration]] n-1 times so $last=first*r^{n-1}$. We can solve the equation $r^{n-1}=\frac{last}{first}\rightarrow (n-1)lnr=ln\frac{last}{first} \rightarrow n=1+\frac{ln\frac{last}{first}}{lnr}$.
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_13]]

Another way to describe a [[geometric sequence]] is with it's [[closed form formula]]. Since when we go from one [[term]] to the other we multiply, it means that at the term n we will have multiplied the [[common ration]] n-1 times (remove the first [[term]]) and we will have started from the initial term. So if the initial term is $a$ we have $x_n=a*r^{n-1}$

##### [[graphs of sequence]]

Since a sequence is simply a rule that gives a set of values starting from another it has much similarities with a [[function]].
For this reason, just like a [[function]] you can plot the graph of a [[sequence]].
In particular an [[arithmetic sequence]] will give you a [[straight-line graph]] since every point grows of the same amount and therefore the [[gradient]] remain constant, on the other hand a [[geometric sequence]] has a [[curve]] shaped graph because the graph of the [[derivative]] is a [[straight-line graph]].

##### [[long-term behavior of sequences]]

Much like [[function]], when we analyse a [[sequence]] we can define it a [[increasing]] or [[decreasing]] based on if the next value is bigger or smaller than the previous. Some [[sequence]]s have a pattern that alternate in a range, we call those [[bounded sequence]].
We an also say that a [[sequence]] become [[arbitrary large]] if it grows with no bound or [[arbitrary small]] if gets closer and closer to 0, in particular we say that $x_n$ tends to $0$ as $n$ tends to infinity. This can be extended to any number say L, a [[sequence]] can be of the type that $x_n \rightarrow L\ \ as\ \  n \rightarrow \infty$.

Since [[arithmetic sequence]]s result in a [[straight-line graph]] their long term behaviour is easy to describe. They have form $x_n=b+dn$ with $b=a-d$ and therefore if d greater than 0 they $x_n \rightarrow \infty\ \ as\ \  n \rightarrow \infty$, if d 0 it'a a constant and if d less than 0 $x_n \rightarrow \infty\ \ as\ \  n \rightarrow -\infty$.

On the other hand [[geometric sequence]]s are more difficult to describe. They take the form $cr^n$ where $c=\frac{a}{r}$ so we can describe the behaviour of $r^n$. The are three special cases, when r is 0 the sequence is always 0, when 1 always 1 and when -1 it alternates between 1 and -1. When r is between 0 and 1 the sequence shrink slower and slower, when > 1 it grows steeper and steeper. Basically it behaves like the [[exponential function]]. Something stranger happens when you have r < 0, if you think about it $-r^n = -1^n*2^n$ therefore the result is that the points have the same [[magnitude]] as before but alternated sign

##### [[summing a finite sequence]]

We call the expression that express the sum of the [[term]]s in a [[sequence]] a [[series]], they can be a [[finite series]] or an [[infinite series]] if the corresponding [[sequence]] has a finite or infinite number of [[term]]s. 

Starting from adding an [[arithmetic sequence]], this is called an [[arithmetic series]], you. can start by imagining a simple $1+2+3$, if you flip it and add it to itself in columns you get $4+4+4$ so $4*3=12$, that is twice the original because we added it twice so $6$ is the final answer. This happens because with the original sequence you add to the initial term an amount on each step, with the reverse you remove such amount to each [[term]]. So. the final formula is $\frac{1}{2}*(number\ \ of\ \ term)(first+last)$. If we rewrite this we can say. $\frac{1}{2}n(a_1+a_1+(n-1)d)=\frac{1}{2}n(2a+(n-1)d)$
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_22_23]]

When you want to add a [[geometric sequence]] you have a [[geometric series]] and the process is similar but different. If. you take $1+2+2^2+2^3$ you can take the double of the sequence and get $2+2^2+2^3+2^4$,  assuming the first is $s$ and second is $2s$ you can subtract the second from the first and you get $s=2^4-1=15$. More in general we can say if $s=a+ar+ar^2....ar^{n-1}$ than $rs=ar+ar^2....ar^{n}$, if you subtract and simplify you get $s=\frac{a(1-r^n)}{1-r}$.
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_24]]

The [[sum of n squares]] is $1^2+2^2+3^2...n^2=\frac{1}{6}n(n+1)(2n+1)$
The [[sum of n cubes]] is $1^3+2^3+3^3...n^3=\frac{1}{4}n^2(n+1)^2$
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_25]]

##### [[sum of infinite series]]

Consider a [[series]] $s=a1+a2...an$, now consider $s1=a1+a2$, $s2=a1+a2+a3$ and so on. We call the smaller s [[partial sum]] and s the [[sequence of partial sum]]. If the [[sequence of partial sum]] converge to a limit we call that the [[sum]], if it does not converge but grow to infinity the [[series]] does not have a [[sum]].

Starting from [[infinite geometric series]], we can take the [[sequence]] $a+ar^2+ar^3...$, that is the [[sum]] of it's [[partial sum]]s, so the formula for the [[partial sum]] at [[term]] n is $sn=\frac{a(1-r^n)}{1-r}$. you can solve this equation once you have r and in the end you will get a term with $n$ as exponent, you can study how that term behave with n growing, if it converges to a number and if it does use it to solve the equation and understand where the whole equation converges. In general you can notice that if $-1<r<1$ the term $r^n \rightarrow 0$ so the equation simplify to $\frac{a}{1-r}$
![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_26|activity_]]

##### [[sigma notation]]

It is just a fancy way to describe the [[series]] with a handy notation, what you write is $\sum_{k=p}^{m}n$ where $k=p$ is the first [[term]], $m$ is the number of [[term]]s (n) and $n$ is the [[closed form formula]] of the [[sequence]].
For example something like $3^3+4^3+5^3....9^3$ is $\sum_{n=3}^{9}n^3$.
Can be used to express [[sum formula]]s:
- $\sum_{k=1}^{n}1=n$
- $\sum_{k=1}^{n}k=\frac{1}{2}n(n+1)$
- $\sum_{k=1}^{n}k^2=\frac{1}{6}n(n+1)(2n+1)$
- $\sum_{k=1}^{n}k^3=\frac{1}{4}n^2(n+1)^2$

You can also use this notations to works with multiple [[sum]]:
- $\sum_{k=p}^{m}cn=c\sum_{k=p}^{m}n$ if $c$ is a constant
- $\sum_{k=p}^{m}(n+-g)=\sum_{k=p}^{m}n+-\sum_{k=p}^{m}g$
- $\sum_{k=p}^{m}(n)=\sum_{k=1}^{m}n-\sum_{k=1}^{p-1}n$ if $1<p<=q$

![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_30]]


when it come to [[infinite series]] the concept is exactly the same, instead of a number on $n$ you will have a $\infty$

##### [[binomial theorem]]

It is a formula to expand a [[power of a binomial]] so $(a+b)^n$. We know that $(a+b)^2=a^2+2ab+b^2$ so $(a+b)^3=(a+b)(a^2+2ab+b^2)=a^3+3a^2b+3ab^2+b^3$.
You can notice that at every new $n$ you are multiplying the previous number by $(a+b)$ once more. Since every time you multiply by $a$ and than by $b$, you increase the power by 1, so each term will always have sum of the exponents equal to n, starting from $a^n$ than $a^{n-1}b$ up to $b^n$.

![[4 - Archive/MST124 24J Essential mathematics 1/unit_10/activity_35_36]]

We can write the formula for the [[power of a binomial]] as the [[binomial expansion]] $(a+b)^n=C_0^na^n+C_1^na^{n-1}b....C_{n-1}^nab^{-1}+C_n^nb^n$.
You now know how to deduce the [[power index]] quickly but what about the [[coefficient]]s $C$?.
A [[factorial]] is the product of a number up to that number so $5!=1*2*3*4*5$ and $0!=1$. In general $n!=n(n-1)!$, written as a [[sequence]] we have $c_0=1$, $cn=nc_{n-1}$. The formula for a [[coefficient]] $k$ of the [[binomial]] $n$ is $C_k^n=\frac{n!}{k!(n-k)!}$, as long as $0<=k$.
The reason for the formula is that, we can check it works for the edge values because when $k=0$ is evaluates to $1$ and when $k=n$ then $n-k=0$ so again it evaluates to 1. The other reason to check is that it is the sum of the two values above in the [[pascal triangle]], the two values above are $C^{n-1}_{k-1}$ and $C^{n-1}_k$, so we need to check that $C^n_k=C^{n-1}_{k-1} + C^{n-1}_k$, you can use the initial formula and simplify to in the end get the proof.

![[activity_37_38]]
The full [[binomial theorem]] can also be stated as [[sigma notation]]
$(a+b)^n=\sum^n_{k=0}C^n_ka^{n-k}b^k=\sum^n_{k=0}\frac{n!}{k!(n-k)!}a^{n-k}b^k$
![[activity_39_40_41_42]]




