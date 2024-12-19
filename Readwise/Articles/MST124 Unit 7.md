## New highlights added December 19, 2024 at 9:40 AM
- The diﬀerence quotient for f(x)= ex is f(x + h) − f(x) h = ex+h − ex h .
- by using the fact thatyou alreadyknowwhathappens in the particular case when x =0,since youknowthat f"(0)= 1.
  When x =0,the diﬀerencequotientis e0+h − e0 h = eh − 1 h .
- t the diﬀerencequotientfor ageneral valueof x.You can rearrange it as follows: ex+h − ex h = exeh − ex h = ex ) eh − 1 h - .
- f"(x)= ex.
- So the derivativeofthe exponential function is the exponential function!
- The exponential function,and itsconstant multiplessuchasthe function f(x)=3ex,are the only functionsthatare equal to theirown derivatives
- . It’s thisproperty thatmakes the constant e sucha special number.
##### Derivative of ln
- f(x)=ln x.Since this function is the inverseofthe exponential function f(x)= ex,its graphis the reﬂection of the graphof f(x)= ex in the line y = x,
- So the gradientsofthe twographs are related,
- Whenyou meet thisrule, you’ll seethat the formulafor the derivativeof f(x)=lnx turns outtobe f"(x)= .
  1 x
- Derivativesofexp andln d dx (ex)= ex d dx (ln x)= 1 x
### 2 Finding derivatives of more complicated functions
#### 2.1 Productrule
- Suppose thatyou know the formulas forthe derivatives of twofunctions, andyou want to know the formulafor the derivativeoftheir product.
- Productrule(Lagrange notation) If k(x)= f(x)g(x), then k"(x)= f(x)g"(x)+ g(x)f"(x), forall values of x at which both f and g are diﬀerentiable.
- Productrule(Leibniznotation) If y = uv,where u and v are functionsof x,then dy dx = u dv dx + v du dx , forall values of x at which both u and v are diﬀerentiable.
- Productrule(informal) ) derivative of product - derivative of ﬁrst function  . =(ﬁrst) × ) derivative of second - +(second) × ) derivative of ﬁrst - .
- remembertosimplifyyour ﬁnalanswers, where possible. Youshouldalwaysdothiswhenyou diﬀerentiatefunctions.
- Productrule(Lagrange notation) If k(x)= f(x)g(x), then k"(x)= f(x)g"(x)+ g(x)f"(x), forall values of x at which both f and g are diﬀerentiable.
##### Aproof of the productrule
- The expression in the ﬁrst pair of largebrackets is the diﬀerencequotient for f
- the expression in the secondpair of large brackets is the diﬀerencequotientfor g
- Hencethe whole expression gets closer andcloser to f"(x)g(x)+ f(x)g"(x); thatis, f(x)g"(x)+ g(x)f"(x). So k"(x)= f(x)g"(x)+ g(x)f"(x),
#### 2.2 Quotient rule
- (Remember thata quotient of twofunctionsisobtained by ‘dividingone by the other’.)
- Quotientrule(Lagrange notation) If k(x)= f(x)/g(x), then k"(x)= g(x)f"(x) − f(x)g"(x) (g(x))2 , forall values of x at which both f and g are diﬀerentiable and g(x) )=0.
- Quotientrule(Leibniznotation) If y = u/v,where u and v are functionsof x,then dy dx v = du dx − u v2 dv dx , forall values of x at which both u and v are diﬀerentiable and v )=0.
- Quotientrule(informal) ) derivative of quotient - (bottom) × = (bottom)2 .
  ) derivative of top - − (top) × ) derivative of bott
- Youcan alsouse the quotient rule to ﬁndthe derivatives of the trigonometric functionscosec, secand cot
- Derivativesofcosec, sec andcot d dx d dx d dx (cosec x)= −cosec x cot x (sec x)= sec x tanx (cot x)= −cosec2 x
#### 2.3 Chain rule
- k(x)= sin(x2). Thisfunction isn’ta sum,a productora quotient of functionsthatyou candiﬀerentiate.
  However, it’s still madeupoffunctionsthatyou candiﬀerentiate
- k is a composite of the functions f(x)= x2 and g(x)= sinx
- f(x)= x2 and g(x)=sin x are functionsthatyou can diﬀerentiate
- chainrule,which allowsyou to diﬀerentiatefunctionsthatare composites of functions
- sometimescalled the composite rule or the functionofa functionrule.
- , supposethatyou have an equation thatspeciﬁes y as afunction of x.Ifthe equation is of the form y =a function of ‘something’,
- where the ‘something’isa function of the input variable x,thenthe originalfunction is acompositefunction.Todecomposeitintoits two constituent functions, youset the ‘something’equal to u.Inother words, youwrite y as afunction of u,where u is afunction of x.
- Chain rule(Leibniznotation) If y is afunction of u,where u is afunction of x,then dy dx = dy du du dx , forall values of x where y as afunction of u,and u as afunction of x, are diﬀerentiable.
- Supposethat y is afunction of u,where u is afunction of x,asinthe statement of the chain rule.Supposethatfor aparticular valueof x,the valueofdu/dx is 2, andfor the valueof u thatcorresponds to this particular valueof x,the valueofdy/du is 3. Since y is increasing at the rateof3 units forevery unitthat u increases, and u is increasing at the rateof2 units forevery unitthat x increases, you’dexpect y to be increasing at the rateof3 ×2= 6units forevery unitthat x increases.
- w here’s an explanation of where the name ‘chain rule’comesfrom.
- function that’sa compositeof three functions.
- dy dx = dy du du dv dv dx .
#### 2.4 Diﬀerentiatingfunctions of linearexpressions
- Youcan seethattodiﬀerentiatea compositefunction in which the ‘something’is ax,where a is aconstant,you diﬀerentiatewithrespect to ax,and thenmultiplyby a.
- Derivative of afunction of the form k(x)= f(ax) If k(x)= f(ax), where a is anon-zeroconstant,then k"(x)= af"(ax),
- If k(x)= f(ax + b), where a and b are constantswith a non-zero, then k"(x)= af"(ax + b),
- Remember thatanexpression of the form ax + b,where a and b are constants, is calleda linear expression in x.
#### 2.5 Using thediﬀerentiationrules together
- Checklistfor diﬀerentiatinga function 1. Is it astandard function (isits derivativegiven in the Handbook)?
  2. Canyou use the constant multiple rule and/or sum rule?
  3. Canyou rewriteittomakeiteasiertodiﬀerentiate? For example,multiplying outbrackets mayhelp. 4. Is it of the form f(ax)or f(ax + b), where a and b are constants and f is afunction?Ifso, use the rule fordiﬀerentiatinga function of alinearexpression.
  5. Canyou use the productrule(is it of the form f(x)=something × something)?
  6. Canyou use the quotient rule (isitofthe form f(x)=something/something)?
  7. Canyou use the chain rule (isitofthe form f(x)=a function of something)?
  When youuse adiﬀerentiation rule,you usually have to ﬁndthe derivatives of simplerfunctions. Youcan applythe checklistabove to each of these simplerfunctionsinturn.
- Notealsothatwhenyou need to applymore thanone rule to diﬀerentiate afunction,the ﬁrst rule thatyou shouldapplyisthe onethatappliesto the overall structureofthe rule of the function
##### Aproof of the quotient rule
##### Aproof of the formulafor the derivative of apower function
- d dx (xn)= d dx =(en ln x) (en ln x) d dx =(en ln x) × n × =(en ln x) × n × (n ln x) (by the chain rule) d dx 1 x = xn × n × = nxn−1, 1 x
### 3 Morediﬀerentiation
- ehow to usediﬀerentiation to solvea type of problemthatoccurs frequentlyinapplicationsofmathematics,
#### 3.1 Optimisationproblems
- , it’s oftenhelpful to solveproblems thatinvolveidentifying the best possibleoption from achoiceofsuitable possibilities. Problems of thistypeare knownas optimisation problems.
- Strategy: To ﬁndthe greatest or least valueofafunction on an intervalofthe form [a, b]

