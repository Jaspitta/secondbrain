## New highlights added January 27, 2025 at 4:07 PM
- y1 =4.
- If instead you choose to have the subscript n start from 0, then the closed form is yn = arn (n =0, 1, 2,...).
### 3 Graphs andlong-term behaviour
#### 3.1Graphs of sequences
- .You canthink of any sequence as a function whose domain is the set of natural numbers {1, 2, 3,...}.
- In general, the sequence(xn)∞ n=1 deﬁnesa function forwhich each input number n gives the output xn,
- , the graphofthe sequence consists of points thatlie on astraightline
- In each case,the graphconsists of points that lie on the graphofanexponential growthordecayfunction.
##### Plotting graphs of sequences with acomputer
#### 3.2Long-term behaviour of sequences
# MST124 Unit 10

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/263886445/HAR_16fbfD-n6cCJaA7fuiAjULGCgy-Id3ILU4bcG8o-cove_pTSvosU.png)

## Metadata
- Author: [[The Open University]]
- Full Title: MST124 Unit 10
- Category: #articles
- Document Tags: [[shortlist]] 
- Summary: A series is formed by adding the terms of a sequence, like 1 + 3 + 5 + 7 + 9. Sequences can be arithmetic, defined by a first term and a common difference, or geometric, defined by a first term and a common ratio. Understanding the behavior of these sequences helps in calculating their sums, even if they have infinitely many terms.
- URL: https://readwise.io/reader/document_raw_content/263886445

## Highlights
- sequence,which is the mathematical name fora listofnumbers arrangedina particular order.
- A closed form is a formulafor each term (individualnumber) in asequence
- recurrence systemindicateswhatthe ﬁrst term is andhow each subsequent term is related to the previousterm
### 1 Whatisa sequence?
#### 1.1Sequencenotation
- In mathematics, a listofnumbers is calleda sequence,and each number in the listiscalled a term of the sequence.
- A sequence thathas aﬁnite number of terms (and hencehas alasttermas well as aﬁrstterm) is calleda ﬁnite sequence, whereas asequence that hasan inﬁnite number of terms is calledan inﬁnite sequence.
- Manysequences have a structure, or pattern, thatallows us to givea concisedescription of the sequence
- . With a sequence, we representthe terms by using oneparticular letterwithanattached subscript
- Thisnotation is called subscriptnotation (or suﬃx notation).
- (an)17 n=1 denotesthe ﬁnite sequence a1,a2,a3,. .. ,a17 (an)∞ n=1 denotesthe inﬁnite sequence a1,a2,a3,. .. .
- The variable n in the notation fora sequence is sometimesreferred toas the indexvariable forthe sequence. It’s a dummy variable:
#### 1.2Closed forms forsequences
- o specify the inﬁnite sequence of perfect squares: 1, 4, 9, 16, 25,. .. .
- ,wehave sn = n2,which is aformulafor the general term, calledthe nth term,
- youneed to state the range of values of the subscript n.You do thisusing brackets, as follows: sn = n2 (n =1, 2, 3,... ).
- Aformulalike sn = n2,for deﬁning asequence in terms of the subscript n, is calleda closed form (ora closed-form formula)
- Closed form fora sequence A closed form fora sequence is a formulathatdeﬁnesthe general term an as an expression involving the subscript n.To specify a sequenceusing a closed form, two pieces of information are needed: • the closed form • the range of values forthe subscript n.
- If you’re given some terms of a particular sequence, then you may be able to spot aclosed form forthe sequence by recognisingthe patterninvolved. It’s helpful to considerquestionssuch asthe following.
  • Is the nth term aconstant multiple of n or of some ﬁxed powerof n?
  • Is the nth term aconstant multiple of the nth powerofsome ﬁxed number?
  • Do the terms alternate in sign?
- Ingeneral, no ﬁnite number of terms candescribea sequence without ambiguity, whereas a sequence described by a closed form with a subscriptrange is unambiguously deﬁned.
#### 1.3Recurrencerelations forsequences
- Some sequences have the property thateach term(afterthe ﬁrst) canbe obtained from thepreviousterm
- Note thatthe range of values of n here beginswith2 ratherthan1, because 2 isthe ﬁrst value of n forwhich the equation an = an−1 +7 applies.
- Aformulalike an = an−1 +7 or bn =2bn−1,which allowseach termofa sequence (afterthe ﬁrst) to be obtained from the previousterm, is calleda recurrencerelation. It’smore speciﬁcallya ﬁrst-order recurrence relation because it involves only the immediatelypreceding termofthe sequence.
- Notice thatifyou keep the same recurrencerelation but change the ﬁrst term, x1,then you obtain a diﬀerent sequence
- the speciﬁcation of aﬁrstterm, arecurrencerelation and the range of values of n forwhich the recurrencerelation appliesiscalled a recurrencesystem,and the resulting sequence is calleda recurrence sequence
- Recurrencesystemfor a sequence A recurrencerelation fora sequence is an equation thatdeﬁnes each term otherthanthe ﬁrst as an expression involving the previous term. To specify asequence using a recurrencesystem,three pieces of information are needed: • the value ofthe ﬁrst term • the recurrencerelation • the range of values forthe subscript n.
- sequences deﬁned by using recurrencesystems can sometimesbeusedto calculate approximationsto certain irrational numbersto asmanydecimal places as mayberequired.
- Threewaystospecifya sequence
- The values of the ﬁrst fewterms
- Aclosed form, an =expression in n,
- Arecurrencesystem, consisting of the value ofthe ﬁrst term, a recurrencerelation, an =expression involving an−1,
- Convention Theﬁrsttermofa sequence (an)istaken to be a1 unlessindicated otherwise.
### 2 Arithmeticand geometric sequences
#### 2.1Arithmetic sequences
- Any sequence with the structuredemonstrated above– the addition of a ﬁxed number to obtain the nextterm–iscalled an arithmetic sequence,oralternatively an arithmetic progression.
- xn = xn−1 + d
- , d is the diﬀerence xn − xn−1 between anypair of successive terms,usually calledthe commondiﬀerence
- we call a and d the parameters of the arithmetic sequence.
- whenthe common diﬀerence d is zero. In thiscase, each term of the sequenceisequal to the ﬁrst term.
  Such a sequence is calleda constant sequence
##### Finitearithmetic sequences
- If youhavethe ﬁrst fewterms andthe lasttermofa particular ﬁnite arithmetic sequence, andyou want to ﬁnd a recurrencesystemthat speciﬁesthe sequence, then you need to ﬁndnot only the values of the parameters a and d,but alsothe subscriptofthe lastterm.
- number of terms = lastterm− ﬁrst term common diﬀerence +1.
#### 2.2Closed forms forarithmetic sequences
- To obtain a general term xn,you start with x1 = a andadd d exactly n − 1 times, so xn = a +(n − 1)d.
- Closed form foran arithmetic sequence The arithmetic sequence with recurrencesystem x1 = a, xn = xn−1 + d (n =2, 3, 4,...) hasthe closed form andsubscriptrange xn = a +(n − 1)d (n =1, 2, 3,...).
#### 2.3Geometric sequences
- Any sequence with the structuredemonstrated above– multiplication by a ﬁxed number to obtain the nextterm–iscalled a geometricsequence, or alternatively a geometricprogression
- That is, r is the constant ratio xn/xn−1 of any two successive terms,often called the commonratio of the sequence.
- Choosingthe values of the ﬁrst term a andcommon ratio r determines a particular geometric sequence; we call a and r the parameters
##### Finitegeometricsequences
- ,for a ﬁnite sequence you may need to ﬁnd how manyterms thereare,
#### 2.4Closed forms forgeometric sequences
- Closed form fora geometricsequence The geometric sequence with recurrencesystem x1 = a, xn = rxn−1 (n =2, 3, 4,...) hasthe closed form andsubscriptrange xn = arn−1 (n =1, 2, 3,...).
- If instead you choose to have the subscript n start from 0, then the closed form is yn = arn (n =0, 1, 2,...).
### 3 Graphs andlong-term behaviour
#### 3.1Graphs of sequences
- .You canthink of any sequence as a function whose domain is the set of natural numbers {1, 2, 3,...}.
- In general, the sequence(xn)∞ n=1 deﬁnesa function forwhich each input number n gives the output xn,
- , the graphofthe sequence consists of points thatlie on astraightline
- In each case,the graphconsists of points that lie on the graphofanexponential growthordecayfunction.
##### Plotting graphs of sequences with acomputer
#### 3.2Long-term behaviour of sequences
- Wenow investigatewhatcan be said aboutthe long-term behaviour of inﬁnite sequences,
##### Terminology forlong-termbehaviour
- we use the words increasing and decreasing for sequences in much the same wayaswas introduced forfunctionsinSubsection
- Next,supposethatall the terms of asequence (xn)lie withinsome interval [−A,A], where A is a ﬁxed positive number,asillustrated in Figure 9(e),for example.Thenwesay thatthe sequence (xn)is bounded.
- If there isno ﬁxed value of A, however large, forwhich all the terms of the sequence(xn)lie withinthe interval [−A,A], then we say thatthe sequence (xn)is unbounded,and alsothatthe terms of the sequence become arbitrarily large
- More generally,suppose thatthe terms of a sequence (xn)approacha particular number L more andmore closely, so they eventually lie within any interval[L − h,L + h], no matterhow small the positive number h is takentobe. Thenwesay that xn tends to L as n tends to inﬁnity
- We alsosay in such a case thatthe limit of the sequence(xn)is L,and thatthe sequence (xn) converges or is convergent to the limit L.
- If a sequence (xn)has the property that, whateverpositive number A youtake, no matterhow large, the terms of (xn)eventually lie in the interval [A,∞), then we say that xn tends to inﬁnity as n tends to inﬁnity,and we write
- ifa sequence (xn)has the property that, whateverpositive number A youtake, the terms of (xn)eventually lie in the interval (−∞, −A], then we say that xn tends to minus inﬁnity as n tends to inﬁnity,and we write
##### Long-term behaviour of arithmetic sequences
- d
- xn = b + nd (n =1, 2, 3,...), where b = a − d.
- when studying the long-term behaviourofarithmetic sequences,we’ll considersequences with the closed form xn = b + nd,
- Long-termbehaviour of arithmetic sequences Suppose that(xn)isanarithmetic sequence with common diﬀerence d.
  • If d> 0, then (xn)isincreasing and xn →∞ as n →∞.
  • If d< 0, then (xn)isdecreasing and xn →−∞ as n →∞.
  • If d =0,then (xn)isconstant.
##### Long-term behaviour of geometricsequences
- which is the same as xn = crn (n =1, 2, 3,...), where c = a/r.
- First, thereare three special cases. If r =0,then(rn)isthe sequence 0, 0, 0, 0,... .
  If r =1,then(rn)isthe sequence 1, 1, 1, 1,... . If r = −1, then (rn)isthe sequence − 1, 1, −1, 1,... .
- Recall thatthe graphofthe exponential function f(x)= bx,where b is positive but notequal to 1, is • increasing if b> 1, becoming steeper as x increases; • decreasing if 0 <b< 1, becoming lesssteep as x increases.
- The only diﬀerencebetween the sequence(rn)and the exponential function y = rx is thatthe domain of (rn)consists of all the natural numbers, whereas the domain of y = rx consists of all the real numbers.
- Forexample,considerthe sequence ((−2)n). The nth term of this sequence, (−2)n,can alsobe writtenas(−1)n × 2n,so the terms of the sequencehavethe same magnitude as the terms of the sequence(2n), but alternate in sign
- • If r< −1, then rn alternatesbetween positive andnegative values, and(rn)isunbounded.
  • If −1 <r < 0, then rn alternatesbetween positive andnegative values,and rn → 0as n →∞.
- Long-term behaviour ofthe sequence (rn) Value of r Behaviourof(rn) r>1Increasing, rn →∞ as n →∞ r =1 Constant:1, 1, 1,...
  0 <r <1Decreasing, rn → 0 as n →∞ r =0 Constant:0, 0, 0,...
  −1 <r <0Alternatesin sign, rn → 0 as n →∞ r = −1Alternatesbetween −1 and 1 r< −1Alternatesin sign,unbounded
- Nowrememberthatany geometric sequence hasthe form (crn). Youcan work outthe long-term behaviourofany sequence of thisform by thinking aboutthe long-term behaviourofthe sequence (rn)and using the fact that the terms of (crn)are obtained by multiplyingthe terms of (rn)by c.
