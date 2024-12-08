# MST124 Unit 6

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/244923671/y6cBFx4EyXtqKG2t7quoG5SIF7iRkrQEbnaJDv33ai8-cove_9dZXDX1.png)

## Metadata
- Author: [[The Open University]]
- Full Title: MST124 Unit 6
- Category: #articles
- Summary: The gradient of a graph represents the rate of change at each point, and it varies for different values of x. This concept applies to both straight and curved graphs, where the derivative helps find the gradient. Additionally, the second derivative provides information about the shape of the graph, indicating whether it is concave up or down.
- URL: https://readwise.io/reader/document_raw_content/244923671

## Highlights
- Calculus provides away of solvingmany mathematical problems thatcan’t be solved using algebraalone.
- In essence, calculus allowsyou to work with situationswhere a quantity is continuously changing and itsrate ofchangeisn’tnecessarily constant
- Calculus appliesto all situationswhere one quantity changes smoothly with respect to anotherquantity.
- Basic calculus splitsinto two halves,known as diﬀerentialcalculus and integral calculus.
- in diﬀerential calculus, you start oﬀ knowing the values taken by a changing quantity throughouta periodofchange, andyou use thisinformation to ﬁndthe values taken by the rate ofchangeofthe quantity
- In integral calculus, you carry outthe opposite processto diﬀerential calculus.
- you’vemodelledthe man’s walk by ﬁnding aformulathatexpresseshis velocity
- Integral calculus allows you touse thisinformation to deduce hisdisplacement
- the precise mathematical ideasbehind calculus are coveredinthe subject areaknown as real analysis.You might study thissubject at Level2,
### 1 Whatisdiﬀerentiation?
#### 1.1Graphs of relationships
- If agraph thatrepresentsthe relationship between twoquantitiesiscurved, then there’s no single gradientvalue thatappliesto the whole graph.
- However, the graphhas agradient at each point on the graph
- in every graphinthese units, every value onthe horizontalaxiscorresponds to at mostone value onthe vertical axis.
#### 1.2Gradients of curved graphs
- To understand what’smeant by the gradient of a curved graphata particular point, considerthe pointonthe graphof y = x2 marked in Figure 7(a).Imaginethatyou’re tracingyourpen tipalongthe graph, but when itreaches the marked pointyou justcarry on moving it in the direction in which it’s been moving
- Thisstraightline‘justtouches’the graphatthe marked point, andiscalled the tangent
- The gradient of a graphata particular pointisthe gradient of the tangentto the graphatthatpoint.

## New highlights added December 8, 2024 at 1:53 PM
- . In general, if a graphhas a ‘sharp corner’ata point, then it hasno gradient at thatpoint.
- , if a graphhas a‘break’ (known as a discontinuity)at a particular point, then the graphhas no tangent, andhence no gradient, at thispoint.
- In general, if agraphhas a vertical tangentata point, then the graphhas no gradient at thatpoint.
#### 1.3Gradients of thegraph of y = x2
- The wayto ﬁnd the gradient at (1, 1) is to begin by thinking abouthow you could ﬁnd an approximate value for thisgradient
- Youchoose a second pointonthe graphof y = x2,fairlyclose to (1, 1),asillustrated in blue in Figure 11. The straightline thatpasses through both (1, 1) andthe second pointisan approximation forthe tangent
- The closer to (1, 1) youchoosethe second pointto be, the betterthe approximation will be
- althoughyou cantakethe second pointto be asclose to (1, 1) as youlike, either on the left or on the right, youcan’t take it to be actually equal to (1, 1)
- the closer the gradient of the line through (1, 1) and the second pointisto 2.So itlooks as if the gradient of the graphat(1, 1) mightbe exactly 2.
- youcan conﬁrmthatthe gradient is exactly 2 by using an algebraic version of the methodabove.
- Let’suse the variable h to denote the increase in the x-coordinatefrom the originalpoint(1, 1) to the second point. The value of h canbe either positive or negative, but notzero
- The x-coordinate of the second pointis1 + h,so, sincethe equation of the graphis y = x2, the y-coordinateofthe second pointis(1+ h)2
- Thegradient of the linethatpassesthrough the twopoints is rise run = (1 + h)2 − 1 (1 + h) − 1
- Thisexpression can be simpliﬁed
- =2+ h.
- thegradient of the linethatpassesthrough (1, 1) and(1+ h, (1 + h)2) is given by the expression 2+ h
- The fact that, as h gets closer andcloser to zero, the valueofthe expression 2+ h gets closer andcloser to 2isexpressedmathematically by saying that 2+ h tends to 2 as h tends to 0,
- the limit of 2+ h as h tends to zerois2.
- let’snow applythe algebraic methodto ﬁnd the gradient of the graph of y = x2 at the general pointwhose x-coordinateisdenoted by x
- The pointatwhich we want to ﬁnd the gradient is (x, x2). The second pointonthe graphis(x + h, (x + h)2),
- rise run = (x + h)2 − x2 (x + h) − x .
- =2x + h.
- As the second pointgetscloser andcloser to the originalpoint, the value of h gets closer andcloser to 0, andthe gradient of the line, 2x + h,gets closer andcloser to 2x.
#### 1.4Derivatives
- . If the graph of f hasa gradient at the point(x, f(x)), then we say that f is diﬀerentiable at x
- f(x)= |x| isn’tdiﬀerentiable at 0. Similarly,ifa function f isn’tevendeﬁned ata particular input value x,then it’snot diﬀerentiable at x.
- ,the gradient of the graphofa function f varies depending on which value of x you’re considering
- think of these gradientsasdeﬁning anew function,related to f.
- if the input value is x,thenthe outputvalue is the gradient of the graphof f at the point(x, f(x)).
- Thisnew function is calledthe derivative (or derivedfunction)
- and is denoted by f! (which is read as ‘f prime’or‘f dash’ or ‘f dashed’).
- The processofﬁnding the derivative ofa given function f is called diﬀerentiation,and when wecarry outthisprocess, we saythatwe’re diﬀerentiating
- The value of the derivativeofa function f at a particular input value x is calledthe derivative of f at x.
- t the algebraic methodthatyou sawinSubsection 1.3,where the formulafor the derivative ofthe function f(x)= x2 wasfound. It’s known as diﬀerentiation from ﬁrst principles.
##### Diﬀerentiationfromﬁrstprinciples
- Thisexpression is known as the diﬀerencequotient
- you need to ﬁnd, in terms of x,the limit of the diﬀerencequotientas h tendsto zero.
- Ifa function isn’tdiﬀerentiable at some values of x,thenyou canstill diﬀerentiateitfrom ﬁrst principles,but the processwon’t work forthe values of x at which it’s notdiﬀerentiable
- ifthe graphofa function f hasa sharp corner at (x, f(x)), then the diﬀerencequotientfor f at x will getcloser andcloser to a particular value when h is positive,but will getcloser andcloser to a diﬀerent value when h is negative.
- The methodofdiﬀerentiation from ﬁrst principles is summarised in the ’means ‘the limit as h tendsto zero of’.
  boxbelow.The notation ‘lim h→0
- Diﬀerentiationfromﬁrstprinciples Forany function f,the derivative f! of f is given by the equation f!(x)= lim h→0 f(x + h) − f(x) h foreach value of x in the domain of f forwhich thislimit exists.
- Of course,the idea of diﬀerentiation from ﬁrst principles is still needed,to ﬁnd the derivatives of the standard functions, to checkthatthe rulesfor combiningthemare valid,and to diﬀerentiate functionsthataren’t standard functionsorcombinationsofstandard functions.
##### Leibniz notation
- The notation thatwe’ve been using so far, in which the derivative ofa function f is denoted by f!,iscalled Lagrange notation or prime notation
- there’sanothernotation,called Leibniznotation,i
- ,Lagrange notation is used when you’re thinking in terms of a variable,and a function of thisvariable
- Leibniz notation is often usedwhen you’re thinking more of the relationship between twovariables.
- fthe equation y = x2 is gradient =2x. In Leibniznotation thisequation is writtenas dy dx =2x.
- the notation dy dx meansthe same as f!(x)
- althoughthe notation lookslike a fraction,it’simportanttorememberthatitisn’ta fraction!
- the change in the x-coordinatefrom the pointatwhich we want to ﬁndthe gradient to the second pointisdenoted by δx instead of h,
- The symbol δ is the lower-caseGreek letterdelta,and is read as ‘delta’.
- By convention,whenthe symbol δ is used asa preﬁx itindicates‘a small change in’
- The change in the y-coordinate
- tisdenoted in asimilar way, as δy
- Thegradient of the linethatpassesthrough the twopoints is then rise run = δy δx .
- As the second pointgetscloser andcloser to the ﬁrst point, the value of δy/δx gets closer andcloser to the gradient of the curveatthe point(x, y).
- Leibniznotation canbeusedina variety of ways.For example,the symbol d dx
- means‘the derivativewithrespect to x of’
- d dx (x2)=2x.
- if s = t2, then
- ds dt =2t
- Sometimes, particularly on a computeralgebrasystem, you mightsee dy/dx writtenas d dx y.
- Usually,ifa function is speciﬁed using function notation,then you use Lagrangenotation forits derivative, whereas if it’s speciﬁed using an equation thatexpressesone variable in terms of another, then youuse Leibniz notation
- For example,ifyou know that f(x)= x2,thenyou write f!(x)=2x,whereas if you knowthat y = x2,then you writedy/dx =2x.
- there are otheruseful notations, including one inventedbyIsaac Newton
##### Functionswhose domains include endpoints
- n f(x)= x3/2.The pointonits graphthatcorresponds to the endpoint0 of itsdomain is the origin.
- eitdoesn’thavea gradient at the origin; thatis, it’s not diﬀerentiable at x =0.
- However, the graphof f(x)= x3/2 does have a ‘tangentonthe right’
- Because of this, we saythatthe function f(x)= x3/2 is right-diﬀerentiable at x =0,and thatits right derivative at 0 is0.
  Similarly,a function can be left-diﬀerentiable at aparticular x-value, anditwill then have a leftderivative at that x-value.
- Saying thata function is diﬀerentiable at a particular x-valueisthe same as saying thatithas both a leftand arightderivative atthat x-value,and the left andrightderivatives are equal.
- If f is a function whose domain includesone or more endpoints, then we adjustthe deﬁnition of itsderivative f!
- We include in the domain of f! notjust the values of x at which f is diﬀerentiable,but alsothe values of x thatare endpoints of the domain of f andatwhich f is left- or right-diﬀerentiable.The value of f! at each of these endpoints is the appropriateleftorrightderivative.
- Derivatives The derivative (or derivedfunction)ofa function f is the function f! such that f!(x)= gradient of the graphof f at the point(x, f(x)).
  The domain of f! consists of the values in the domain of f at which f is diﬀerentiable (thatis, the x-valuesthatgivepoints at which the gradient exists).
  If y = f(x), then f!(x)isalsodenoted by The derivative f! is given by the equation f!(x)= lim h→0 f(x + h) − f(x) h .
  The procedure ofusing thisequation to ﬁnda formulafor the derivative f! is called diﬀerentiation from ﬁrst principles. dy dx .
### 2 Finding derivatives of simple functions
#### 2.1Derivatives of powerfunctions
- The formulas thatyou sawfor the derivatives of the three powerfunctions abovecan be stated asfollows, using Leibniz notation: d dx (x2)=2x, d dx (x3)=3x2, d dx (x4)=4x3.
  Notice thatthey all followthe same pattern.
- Derivative of a powerfunction Forany number n, d dx (xn)= nxn−1.
- .Ingeneral, forthe powerfunction f(x)= xn,the processinvolves multiplying out the expression (x + h)n
- the formulaholdsnot justfor values of n thatare positive integers,but for all values of n,
- Rememberinparticular thatfor a function to be diﬀerentiable at a particular value of x, itmust alsobe deﬁned there. For example,the function f(x)= √ x isn’tdiﬀerentiable at x = −3, sinceit isn’tevendeﬁned there.
- the formulafor the derivative ofa powerfunction tells you thatthe function f(x)= x (which is the same as f(x)= x1) hasderivative f!(x)=1× x0;thatis, f!(x)= 1
#### 2.2Constantmultiplerule
- you alreadyknowthe formulafor the derivativeofthe function f(x)= x2,but suppose thatyou want to know the formulafor the derivative ofthe function g(x)=3x2.
- When youmultiplya function by a constant,the eﬀect
- sare called vertical scalings.
- considerwhathappens to the gradient of a straightlinewhen you scale it vertically by a particular factor, say a.The scaledline will go up by a times
- The samething happensfor anygraph: if you scale it vertically by a particular factor,
- Constant multiple rule(Lagrange notation) If the function k is given by k(x)= af(x), where f is afunction and a is aconstant,then k!(x)= af!(x), forall values of x at which f is diﬀerentiable.
- taking a negativeisthe same as multiplyingby −1. It’s useful to remember in general thatif f and k are functionssuch that k(x)= −f(x), then, by the constant multiple rule, k!(x)= −f!(x),
- Constant multiple rule(Leibniznotation) If y = au,where u is a function of x and a is aconstant,then dy dx = a du dx , forall values of x at which u is diﬀerentiable.
- Yousaw in the previoussubsection thatthe function f(x)=1 hasderivative f!(x)=0. Thisfact, together with the constant multiple rule,tells youthatif a is any constant,then the function f(x)= a (which is the same as f(x)= a × 1)
- Forexample,the function f(x)=3 hasderivative f!(x)=0.
- Derivative of a constantfunction If a is aconstant,then d dx (a)=0.
- Constant multiple rule(Lagrange notation) If the function k is given by k(x)= af(x), where f is afunction and a is aconstant,then k!(x)= af!(x), forall values of x at which f is diﬀerentiable.
##### Aproof of the constantmultiplerule
- Considerthe function k given by k(x)= af(x).
- k(x + h) − k(x) h
- af(x + h) − af(x) h
- a  , f(x + h) − f(x) h  .
#### 2.3Sum rule
- suppose thatyou know the formulas forthe derivatives of two functions, andyou want to know the formulafor the derivativeoftheir sum
- When youadd twofunctions, the y-coordinates of the points on the two graphs are added
- The eﬀect thatadding the functionshas on the gradientsisquite complicated to think about, butinfactit’sjust whatyou mightexpect: if youadd twofunctions, thenthe gradient of the sumfunction at any particular x-value isthe sum of the gradientsof the twooriginal functions at that x-value.
- Sumrule(Lagrange notation) If k(x)= f(x)+ g(x), where f and g are functions, then k!(x)= f!(x)+ g!(x), forall values of x at which both f and g are diﬀerentiable.
- if k(x)= f(x)+ g(x)+ h(x), then k!(x)= f!(x)+ g!(x)+ h!(x),
- It alsofollowsfrom the sumrule, together with the constant multiple rule, thatif k(x)= f(x) − g(x), then k!(x)= f!(x) − g!(x),
- thisby writingthe equation k(x)= f(x) − g(x)as k(x)= f(x)+ (−g(x)).
- Sumrule(Leibniznotation) If y = u + v,where u and v are functionsof x,then dy dx = du dx + dv dx , forall values of x at which both u and v are diﬀerentiable.
- Likethe constant multiple rule,the sum rule can be formally proved by using the idea of diﬀerentiation from ﬁrst principles,
- Everypolynomial function (withdomain R)isdiﬀerentiable at every value of x.
- Sumrule(Lagrange notation) If k(x)= f(x)+ g(x), where f and g are functions, then k!(x)= f!(x)+ g!(x), forall values of x at which both f and g are diﬀerentiable.
- Aproof of the sumrule
- k(x)= f(x)+ g(x)
- k(x + h) − k(x) h
- f(x + h)+ g(x + h) − f(x) − g(x) h
-  f(x + h) − f(x) h  +  , g(x + h) − g(x) h 
### 3 Rates of change
- tthe gradient of astraight-linegraphisthe rateof change of the variable on the vertical axis with respect to the variable on the horizontalaxis
- Of course,unlikeinFigure 29(a), in Figure 30 the variable y doesn’t actually increase by two units for every unitthat x increases. Thisrate of change is an ‘instantaneous’ value
- Sincethe gradient of anygraphofthe variable y against the variable x is given by the derivativedy/dx,anotherway to think aboutthe derivative dy/dx is thatitisthe rate ofchangeof y with respect to x.
#### 3.1Displacementand velocity
- tifthe displacementofanobject alongastraightlineis plottedagainst time,thenthe gradient of the resulting graphisthe rate of change of the object’s displacementwithrespect to time,which is calledits velocity.
- In each of the twographs in Figure 32, the quantity on the horizontalaxis (time)ismeasured in hours, andthe quantity on the vertical axis (distance)ismeasured in kilometres,sothe gradient is measured in kilometres perhour.
- incethe gradient of the displacement–time graph of any object thatmoves alonga straightline isthe velocity of the object,wehavethe following importantfact.
- Relationship between displacementand velocity Supposethatanobject is moving alonga straightline. If t is the time thathas elapsed since some chosen pointintime, s is the displacementofthe object from some chosen referencepoint, and v is the velocity of the object,then v = ds dt .
- Thisisthe sort of calculation thatdiﬀerential calculus allows you to carry out: if you knowthe values taken by a changing quantity throughouta periodofchange, then you can use diﬀerentiation to ﬁndthe values taken by the rate ofchangeofthe quantity throughoutthe same period.
- Youmightﬁnd it enlightening to think aboutwhatthe processof diﬀerentiation from ﬁrst principles meanswhen itisappliedto a displacement–time graph. In thiscasethe diﬀerencequotientata particular time value representsthe averagevelocity over atime interval startingorending at thattime value
- If the eﬀect of air resistanceisnegligible (which it is if the object is fairly compactand the fall is fairly short), then the distance fallenbythe object isn’taﬀected by howheavy it is,for example,but depends only on the time thatithas been falling
- the total distancefallen is proportional to the square of the time
- If time is measured in seconds anddistance is measured in metres, then the constant of proportionality is about4.9,
- ,ifwealsotakethe referencepointto be the pointfrom which the object startsto fall,
- is given by the equation s = −4.9t2.
#### 3.2Total cost and marginalcost
### 4 Finding wherefunctions are increasing, decreasingorstationary
#### 4.1Increasing/decreasing criterion
- Informally,a function is increasing on an interval if itsgraphslopes up on thatinterval, andisdecreasing on an interval if itsgraphslopes down on the interval
- you can’ttellfrom the graphalonethatthisfunction stops increasing andstartsdecreasing when x is exactly −2, or thatitstops decreasingand startsincreasingwhen x is exactly 3.
- Increasing/decreasingcriterion If f!(x)ispositive for all x in an interval I,then f is increasing on I.
  If f!(x)isnegativefor all x in an interval I,then f is decreasing on I.
#### 4.2Stationary points
- there are points at which the gradient of the graphiszero, as shown in Figure 39. Apointatwhich the gradient of a graphiszero iscalled a stationary point.
- The term ‘stationary point’ is used torefer to the x-coordinateofa stationary point, as well as to the pointitself
- At the left-hand stationary pointinFigure 39,the value taken by the function is larger thanatany otherpointnearby, so we say thatthe function hasa localmaximum at thispoint. Similarly,atthe right-hand stationary point, the value taken by the function is smaller thanatany otherpointnearby, so we say thatthe function hasa localminimum at thispoint.
- Apointwhere afunction hasa localmaximum or localminimum is called a turningpoint
- Astationary pointofeitherofthe typesshown in Figure 40 is calleda horizontal pointofinﬂection
- Notice thatthe tangentto a curveata horizontalpointof inﬂection crossesthe curveatthatpoint.
- Strategy: To ﬁnd the stationary points of a function f Solvethe equation f!(x)=0 .
- the following useful test fordeterminingthe nature ofa stationary point. It’s known asthe ﬁrstderivativetes
- First derivative test (for determiningthe nature of a stationary pointofafunction f) If thereare open intervals immediatelyto the left andrightofa stationary pointsuch that • f!(x)ispositive onthe left interval andnegativeonthe right interval, then the stationary pointisa localmaximum • f!(x)isnegativeonthe left interval andpositive onthe right interval, then the stationary pointisa localminimum • f!(x)ispositive onbothintervals or negativeonbothintervals, then the stationary pointisa horizontalpointofinﬂection.
- Strategy: To applythe ﬁrst derivative test by choosingsample points
- Choose two points (thatis, two x-values) fairly close to the stationary point, one oneach side.
- Check thatthe function is diﬀerentiable at all points between the chosen points andthe stationary point,
- Find the value ofthe derivativeofthe function at the two chosen points.
- If the derivativeispositive atthe left chosen pointand negativeatthe rightchosen point, then the stationary point is alocal maximum.
  • If the derivativeisnegativeatthe left chosen pointand positive at the rightchosen point, then the stationary point is alocal minimum.
  • If the derivativeispositive atbothchosen points or negative at both chosen points, then the stationary pointisa horizontalpointofinﬂection.
#### 4.3Usesofﬁnding stationary points
##### Finding the vertex of aparabola
- An alternative methodisto use the fact thatthe vertex of a parabola is a stationary point
##### Sketching the graphofa function
- Finding the greatest andleast valuesofa function on an interval of the form [a, b]
- when you want to ﬁndthe greatestorleast value thata function takesona particular interval
- Strategy: To ﬁnd the greatest or least valueofafunction on an intervalofthe form [a, b] (Thisstrategyisvalidwhenthe function is continuous on the interval, anddiﬀerentiable at all values in the interval exceptpossiblythe endpoints.) 1. Find the stationary points of the function.
  2. Find the values of the function at anystationary points inside the interval, andatthe endpoints of the interval.
  3. Find the greatestorleast of the function values found.

