---
year: 1948
tags:
  - ai
  - llm
link:
  - https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
---
#### Synopsis

This paper is Claude Shannon's most famous theory of language where he described basic theory of communication. 


## Choice, Uncertainty and Entropy
>Suppose we have a set of events (presumed independant) whose probabilities are p1, p2, .. pn. All we know are the probabilities of these events occuring. Can we quantify the "choice" involved in producing one event or another? 


If there is a metric H: what properties should it have? 
- H is a function of p1, p2, .. pn
- H is continuous with pi
- if pi is a equal to 1/n, H increases with n. With increased choices which are all equally likely then uncertainty increases with the number of choices. This kind of means, if there are many choices available and we have no preference then uncertainty increases with freedom. If we have some clear preference, then the probability distribution becomes less uniform and that *could* decrease uncertainty 
- If choices can be broken down to successive choices, then H should be a linear combination of the individual H involved in those two choices. 
  H = p1 H1 + p2 H2 . 

The only form for H is 
$$H = -K \sum_{i=1}^{n} p_i \cdot log(p_i)$$
*H* is called the entropy of the system 

