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

## New highlights added December 26, 2024 at 1:24 PM
- 1. Identify the quantity thatyou canchange, andrepresent it by a variable,notingthe possiblevalues thatitcan take.Identifythe quantity to be maximised or minimised, andrepresent it by a variable.These variablesare the independent anddependent variables, respectively.
  2. Find aformulafor the dependent variable in terms of the independent variable.
  3. Usethe techniques of diﬀerential calculus to ﬁnd the valueofthe independent variable thatgives the maximum/minimum valueof the dependent variable.
  4. Interpretyouranswer in the context of the problem.
#### 3.2 Diﬀerentiationusing acomputer
#### 3.3 Derivatives of inversefunctions
- Then x is alsoa function of y.Asyou know,the derivativeof x with respect to x is 1, andwecan writethisfactas dx dx =1.
- dx dx = Therefore dx dy dx dy dy dx dy dx =1.
  Hence, forvalues of x forwhich dx/dy exists andisnon-zero, dy dx 1 = dx/dy
- Inversefunction rule(Leibniznotation) If y is an invertible function of x,then dy dx 1 = dx/dy , forall values of x suchthat dx dy exists andisnon-zero.
- d dx d dx d dx (sin−1 x)= √ 1 1 − x2 (cos−1 x)= −√ 1 1 − x2 (tan−1 x)= 1 1+ x2
##### Theinversefunction rule in Lagrange notation
- Inversefunction rule(Lagrange notation) If f is afunction with inversefunction f−1,then (f−1)"(x)= 1 f"(f−1(x)) , forall values of x suchthat f"(f−1(x))exists andisnon-zero.
- Iftwo straightlines (drawnonaxes with equal scales) are reﬂectionsofeachother in the line y = x,thentheir gradients are reciprocals of each other
#### 3.4 Table of standard derivatives
### 4 Reversing diﬀerentiation
- We’ll considersituationswhere youknowthe values takenbythe rateof change of acontinuouslychangingquantitythroughouta periodofchange, andyou want to ﬁndthe values takenbythe quantity throughoutthe same period.
- A continuous function is onewhose graphhas no discontinuities
#### 4.1 Antiderivatives andindeﬁniteintegrals
- In integral calculus youusually start with afunction f,and youwantto ﬁnd anotherfunction,say F,whose derivativeis f.Sucha function F is calledan antiderivative
- The processofﬁnding an antiderivativeofa function is called antidiﬀerentiation,or, more commonly, integration.
- So theformula F(x)= x2 + c describes the complete family of antiderivatives of the function f(x)= 2x.Wecall the general function F(x)= x2 + c the indeﬁnite integral
##### Functionsthataren’tcontinuous
#### 4.2 Antiderivatives of powerfunctions
- d dx ) 1 7 x7 - = 1 7 × 7x6 = x6.
- e the indeﬁnite
  integral of f(x)= x6 is
  F(x)= 1
  7x7 + c
- dx ) 1 n +1 xn+1 - 1 = n +1 × (n +1)xn = xn.
- Indeﬁniteintegral of apowerfunction Forany number n except n = −1, the indeﬁnite integral of xn is 1 n +1 xn+1 + c.
- To ﬁnd an antiderivativeofa powerfunction (exceptthe power function f(x)= x−1), ﬁrst increase the powerby1,thendividebythe newpower.
  As usual, to obtain the indeﬁnite integral, addthe arbitrary constant c.
#### 4.3 Constantmultipleruleand sum rule for antiderivatives
- Constant multiple rulefor antiderivatives If F(x)isanantiderivativeof f(x), and k is aconstant,then kF(x)is an antiderivativeof kf(x).
- Indeﬁniteintegral of aconstantfunction Theindeﬁnite integral of the constant a is ax + c.
### 5 Particularantiderivatives
#### 5.1 Finding particular antiderivatives
- Youcan work outwhich of the inﬁnitely manyantiderivatives of afunction is the rightone if youhavesome appropriateextra information.Usually the extra information thatyou have is the valuetaken by the antiderivativeatsome valueofthe input variable.
#### 5.2 Using integration to workwithrates of change
- The calculation in Example 20 is the sort of calculation thatintegral calculus allowsyou to carry out: if youknowthe values takenbythe rate of change of aquantitythroughouta periodofchange, then youcan use integration to ﬁndthe values takenbythe quantity
- Yousaw thatifanobject falls from rest underthe inﬂuenceof gravity,and the eﬀectsofair resistanceare negligible,thenits displacement s (inmetres) at time t (inseconds) afteritbegan fallingis modelledbythe equation s = −4.9t2.
- n,9.8ms−2,isknown as the accelerationdue to gravity.
  70
#### 5.3 Changes in thevalues of antiderivatives
- theamount of thechange is the same forall theantiderivatives of f.
- Consider anyantiderivative F of f.Then F is of the form F(x)= x2 + c,where c is some constant.The valueof F when x =1 is F(1)=12 + c, andthe valueof F when x =2 is F(2)=22 + c.
  So the change in the valueof F as x changesfrom x =1 to x =2 is F(2) −F(1)=(22 + c) − (12 + c) =4+ c − 1 − c =3.
- Supposethat f is afunction thathas an antiderivative, and f is continuous. If a and b are numbersinthe domain of f,thenall the antiderivatives of f change by the same amount as x changesfrom x = a to x = b.Inother words, the valueof F(b) −F(a)isthe same forevery antiderivative F of f.
#### 6 Antiderivatives of furtherstandard functions
#### 6.1 Anantiderivativeofthe reciprocal function
- d dx (lnx)= .
  1 x
- the formuladoestellyou thatanantiderivativeofthe function
- g(x)= is G(x)= ln x.
  Thisfactisillustrated in Figure 40. The graphof g(x)=1/x (x> 0),in Figure 40(a),gives the gradientsofthe graphof G(x)= ln x,in Figure 40(b).
  1 x (x> 0)
- To deal with the ‘otherhalf’ofthe function f(x)=1/x,you canuse the fact thatequation (1), together with the chain rule,gives
- d dx (ln(−x)) = 1 −x × (−1) = .
  1 x
- dx (ln(−x)) = 1 −x × (−1) = .
  1 x
- h(x)=1/x (x< 0) is H(x)=ln(−x).
- The formulafor the antiderivativeof f(x)=1/x foundabove canbe writtenas F(x)= / ln(−x)(x< 0) ln x (x> 0).
- canbewrittenconcisely as F(x)=ln |x|.
- F(x)=ln |x| + c.
- Indeﬁniteintegral of the reciprocalfunction Theindeﬁnite integral of 1 x is ln |x| + c.
  (If x takesonlypositivevalues,thenthe indeﬁnite integral of simply ln x + c.)
#### 6.2 Table of standard indeﬁnite integrals
- Youcan use all of the derivatives of standard functionsthatyou metin Unit 6and in the ﬁrst three sectionsofthisunittodeduceantiderivatives,

