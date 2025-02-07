They are born from the necessity of representing seemingly impossible numbers, the base of all the [[complex numbers]] is $i$ which is $+-\sqrt{-1}$ therefore $i^2=-1$.

They have very wide applications, much more than it seems, they are what made possible the creation of [[transistors]] and much more.

When working with the [[complex numbers]] $i$, sometimes it is referred to as $i=\sqrt{-1}$ but saying that $i^2=-1$ is more appropriate because the first interpretation leads to $\sqrt{-1}\sqrt{-1}=\sqrt{-1*-1}=\sqrt{1}=1$ which is of course wrong.

The term [[complex numbers]] refers in general to numbers in the form $a+bi$ where $a$ and $b$ are [[real numbers]]. Such notation express the [[real part]] as $a$ and the [[imaginary part]] as b also noted as $Re(z)=a$ and $Im(z)=b$. If a [[complex numbers]] has [[real part]] 0, it can be called an [[imaginary number]] or [[purely imaginary number]].

##### adding and subtracting [[complex numbers]]

In the simplest form, you treat $i$ as any variable like $x$ and sum the numbers with common factors.
![[activity_2_3]]

##### multiplying [[complex numbers]]

same concept as adding, just treat the $i$ as an $x$.

![[activity_4_5_6]]

##### [[complex conjugation]]

In general the [[complex conjugation]] of $a+bi$ is $a-bi$ and the notation is $\overline{z}$. This operation also follow the regular properties of arithmetics so:
- $\overline{z+-w}=\overline{z}+-\overline{w}$
- $\overline{z+-w}=\overline{z}+-\overline{w}$
- $\overline{zw}=\overline{z}\overline{w}$
- $\overline{z/w}=\overline{z}/\overline{w}$
Also, remember that $(a-b)^2=a^2-b^2$, so the property of [[complex conjugation]] make sure that $z*\overline{z}$ is a real number because $(a+bi)(a-bi)=a^2-(bi)^2=a^2+b^2$.
![[activity_8_9_10_11]]

##### [[dividing complex number]]s

The division of [[complex numbers]] involves in the essence writing the two numbers as a fraction so $\frac{a+bi}{c+di}$, now to simplify you can multiply both members by the [[complex conjugation]] of the denominator, this way you will have a [[real numbers]] at the bottom and you will be able to write the fraction without a [[complex numbers]] as denominator. This process is similar to [[surds]].
![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_12]]

##### [[geometry of complex numbers]]

To represent graphically [[complex numbers]] we used the [[complex plane]], numbers are analysed as their real and imaginary part, in the number $a+bi$ the coordinates are $(a,b)$, the horizontal axes is called the [[real axis]] and the vertical is called the [[imaginary axis]].

![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_13]]

The workings are similar to [[vector algebra]], if you sum two points you simply sum the single elements, if you multiply by a [[real numbers]] you multiply both parts by that number, and for [[complex conjugation]], you get the reflection on the [[real axis]].

The [[complex plane]] help us to get a representation of the [[magnitude|modulus]] of a [[complex numbers]], for [[real numbers]] it is defined as the distance from 0, that is the same for [[complex numbers]] but represented on the [[complex plane]]. To get the distance you have to use [[pythagoras theorem]] so $|z|= \sqrt{a^2+b^2}$

![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_15]]

The [[magnitude|modulus]] of [[complex numbers]] also has some additional properties, for example we saw that $z\overline{z}=a^2+b^2$ and $|z|=\sqrt{a^2+b^2}$ so $|z|^2=a^2+b^2=z\overline{z}$, so $|zw|^2=zw\overline{zw}=z\overline{z}w\overline{w}=|z|^2|w|^2$, therefore $|zw|=|z||w|$, and ultimately $|\frac{z}{w}|=\frac{|z|}{|w|}$.
![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_16]]

Now you can deduce that $z\overline{z}=|z|^2$ so $z=\frac{|z|^2}{\overline{z}}$, therefore $\frac{1}{z}=\frac{\overline{z}}{|z|^2}$.

![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_17]]

You can actually describe a [[complex numbers]] by it's [[magnitude|modulus]] and the direction as an angle in [[radian]], this is called the [[polar form]] and the direction part is called the [[argument]]. Since potentially there are an infinite number of angles that can describe a direction, the convention is that the angle should be described as $(-\pi,\pi]$ and is denoted as Arg(z).
A number in it's [[polar form]] is described by it's [[magnitude|modulus]] and the direction, if we imagine a number that lies on the [[unit circle]] ([[modulus]] 1) but has the same direction, it will have coordinates $cos\theta, sin\theta$  and form $cos\theta+isin\theta$, therefore our number will have the same structure but with a modulus that is a factor of the one on the [[unit circle]], overall it will have structure $r(cos\theta+isin\theta)$ .

Once you have the [[polar form]], all you need to do is calculate the values of sin and cos to get back the [[cartesian form]]

![[activity_20]]

Of course you can also go from [[cartesian form]] to [[polar form]] although it is a bit more difficult. First you get the modulus that will be your r. Than you understand in which quadrant your number lies based on the values of x and y, now you know it forms a triangle with two sides being the x and y coordinates, you can use the formula for the [[tangent]] to get the value of the angle with the [[real axis]] and finally use it to get the value of your [[argument]]
![[Pasted image 20250207191930.png]]
![[Pasted image 20250207192001.png]]
![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_21]]

While the [[cartesian form]] is more convenient for sums and subtraction the [[polar form]]  is better suited for multiplications and divisions.
The multiplication of two [[complex numbers]] in [[polar form]] is $zw=rs(cos(\theta+\sigma)+isin(\theta+\sigma))$, the reason is simply the multiplication of the two polar forms that is than simplified using [[angle sum identity]].

![[1 - Projects/MST124 24J Essential mathematics 1/unit_12/activity_22_23]]