# MST124 Unit 8

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/254182331/Q1Pt4U93H-zYYha5iVLmnOTZ4L6PVMnA7IFu9HK5tEA-cove_ETMBCMy.png)

## Metadata
- Author: [[The Open University]]
- Full Title: MST124 Unit 8
- Category: #articles
- Summary: The fundamental theorem of calculus provides a quicker and more exact way to evaluate definite integrals compared to using subintervals. However, finding the necessary antiderivative for this method can sometimes be difficult or impossible. In this unit, you will learn various integration techniques, including integration by parts and how to use computer algebra systems for finding integrals.
- URL: https://readwise.io/reader/document_raw_content/254182331

## Highlights
### 1 Areas, signedareasand deﬁnite integrals


## New highlights added January 3, 2025 at 11:03 AM
- a continuous function is a function whose graphhas no breaks in it,overits wholedomain
#### 1.1Areas andsigned areas
- tasthe number of subintervals gets larger andlarger, the approximation obtained seemsto be getting closer andcloser to a particular number.Wesay thatthisnumberisthe limit of the approximationsasthe number of subintervals tends to inﬁnity.
- Youstart by dividing the interval [a, b]into a number,say n,ofsubintervals
- The widthofeach subintervalisthen (b − a)/n
- For each subintervalyou calculate the product
- u
- u addupall these products.
- The signedarea of the region is itsarea witha plus or minus sign according to whetheritliesabove or belowthe x-axis, respectively
- Strategy: To ﬁnd anapproximatevaluefor the signedarea between the graphofacontinuousfunction f and the x-axis, from x = a to x = b Divide the interval between a and b into n subintervals,eachof width(b − a)/n.For each subinterval, calculatethe product
- andadd up all these products.
- The value of b canalsobe equal to the value of a,and thisgives a signed area ofzero,
- Then the signedarea between the graphof f andthe x-axisfrom x = a to x = b is deﬁned to be the negative of the signed area between the graphof f andthe x-axisfrom x = b to x = a.
- Ifthere’s no mention of ‘from x = a to x = b’, then to decidewhetherthe signed area ispositive ornegativeyou justneed to considerwhetheritliesabove or belowthe x-axis. However, if the text is of the form ‘the signed areafrom x = a to x = b’, then to decidewhether the signed areaispositive or negativeyou alsohaveto considerwhether b is greater thanorlessthan a.
- The reason why itworksin cases where b is less than a is thatinthese cases the ‘width’ (b − a)/n of each subintervalis negative.
- normally youwould work outthe signed area from a to b,
#### 1.2Deﬁnite integrals
- If f is a continuousfunction and a and b are numbersinits domain
- the signed areabetween the graphof f andthe x-axisfrom x = a to x = b is calledthe deﬁnite integral
- read as ‘the integral from ato b of fofx,d x
- s a and b are calledthe lower and upper limitsofintegration,
- The symbol
  
  smaller form,
  
  is calledthe integral sign
- ,the ‘d’inthe notation fordeﬁnite integrals hasno independent meaning
- tyou must include
- also the dx at the end
- Standard properties of deﬁniteintegrals a f(x)dx =0 a a b c a f(x)dx = a f(x)dx = − b a b f(x)dx + c b f(x)dx f(x)dx
- the notation foradeﬁnite integral can be used withletters otherthanthe standard ones
- ,the input variable of the function in a deﬁnite integral is what’s known asa dummy variable
- We’ll denote (b − a)/n by w here,for conciseness.
- The endpoints nearest a of the subintervals are a +0w, a +1w, a +2w, ...,a+(n − 1)w.
- f(a +0w) ×w + f(a +1w) ×w + f(a +2w) ×w + ··· ··· + f(a +(n − 1)w) × w.
-  f(a +0w)+ f(a +1w)+ f(a + 2w)+ ··· + f(a +(n − 1)w) w.
  
- asthe value of n tendsto inﬁnity, is the exact value of b a f(x)dx.
- Algebraic deﬁnition ofadeﬁnite integral Suppose that f is a continuousfunction and a and b are numbersin itsdomain.Thenthe deﬁnite integral of f from x = a to x = b is given by the equation b a f(x)dx =lim n→∞  where w =(b − a)/n.
  If f is a particular continuous function,and a and b are numbersin its domain,thenyou cansometimescalculate anexact value for b f(a +0w)+ f(a +1w)+ f(a +2w)+ ··· ··· + f(a +(n − 1)w)  w
- ,ifyou want to evaluate a deﬁnite integral b a f(x)dx,then you have two main options.
- use acomputertocarry outthe calculations.
- usean algebraic methodthatarises from the fundamental theoremofcalculus,
- sometimesit’snot possibleornot practicable to use thismethod,
- the symbol  is an elongated ‘S’, which stands for ‘sum’.
- the verb ‘to integrate’ means‘to join together’.
- obtained by joiningtogether inﬁnitely manysigned areas,
- Fourier series.These are inﬁnite trigonometric series, which are now namedafterhim, andwhich arose inthe context of hiswork on heat
- Deﬁniteintegrals Suppose that f is a continuousfunction,and a and b are numbersin itsdomain.The signed area between the graphof f andthe x-axis from x = a to x = b is calledthe deﬁnite integral of f from a to b, andisdenoted by b a f(x)dx.
### 2 The fundamental theorem of calculus
- .The two areas of mathematicsare linkedby an importantfactknown as thefundamental theoremofcalculus.
#### 2.1Whatisthe fundamental theoremofcalculus?
- deﬁne, forany continuous function f,anew function whose values are signed areas between the graphof f andthe x-axis
- A(x)= signed area between the graphof f andthe x-axis, from s to x.
- e function A the signed-area-so-far function forthe function f,withstartingpoint s.
- A(x)= x s f(t)dt
- then the signed area between the graphof f andthe x-axis, from x = a to x = b,is given by A(b) −A(a).
  In otherwords, b f(x)dx = A(b) −A(a).
- let’s considerhow the value ofa signed-area-so-far function changes as the valueofthe input variable x changes.
- tfor anyconstant function f(x)= k,and any signed-area-so-far function A for f,the value of A(x)changes at the rate of k square units forevery unitbywhich x changes. In otherwords, the rate ofchangeof A(x)is k.
- sfor a function f thatisn’ta constant function.
- at anyvalue of x, the instantaneous rate ofchangeof A(x)is f(x),
- , the derivative ofthe function A is the function f,and so the function A is an antiderivative ofthe function f.
  Youcan seethatthiswill be true forany continuous function f andany signed-area-so-far function A for f.Thatis, we have the importantfact below. Because of itsimportance, it deserves to be calleda theorem.
- Theorem Supposethat f is a continuousfunction,and s is any numberinits domain.Let A be the signed-area-so-far function for f with starting point s.Then A is an antiderivative of f.
- let F be any antiderivativeof f.Then, since A and F are both antiderivatives of f,the value of F(b) −F(a)isthe same as the value of A(b) −A(a). That’sbecause,asyou sawinUnit7,the value of F(b) −F(a)isthe same no matterwhich a
- Fundamentaltheorem of calculus Suppose that f is a continuousfunction whose domain containsthe numbers a and b,and that F is an antiderivative of f.Then b f(x)dx = F(b) −F(a).
- The equation in the fundamental theoremofcalculus is true no matter whether the value a is less than, equal to or greater thanthe value b.
#### 2.2Using thefundamental theoremtoﬁnd signed areas
- Fundamentaltheorem of calculus(square bracket notation)
  Suppose that f is a continuousfunction whose domain containsthe
  numbers a and b,and F is an antiderivative of f.Then
  b
  f(x)dx = F(x) a.
  
  a
  b
- Anotheradvantage of using the fundamental theoremofcalculus is thatit gives youan exact answer,ratherthananapproximate one.However, remember thatyou canuse the fundamental theorem ofcalculus only when you can ﬁnd a formulafor the antiderivativethatyou need.
- As shown in the example,aconvenientway to carry outthese sortsof manipulationsisto manipulatethe expression inside the notation b a ... dx.Thisexpression is known asthe integrand.

