---
tags:
  - ai
  - llm
  - protein_language_models
related:
  - "[[Log-likelihood|Entropy]]"
  - "[[Perpexity]]"
link:
---
Training language models requires us to have some solid grip on a few concepts. An important class of these concept relate to the performance of those language models. For classification and regression the performance measures are fairly common, like precision, recall, MAE etc. 

Language models have a certain objective. It tries to predict discrete tokens from context. These tokens could be the next-token in a sequence, or masked tokens within a sequence. But generally speaking, the tokens should be predicted by context. 

Now, if we have a method of predicting tokens at two missing locations, say position *i* and *j*, what is the joint probability? 

The joint probability should be the product of conditional probability (assuming the two predictions are independent). A working assumption, atleast from the [[Biological structure and function from learning sequences]] paper is that the conditional probability of the predictions for those missing tokens are independant from each other. That is if a model predicts an amino acid K at position *i* and another amino acid L at position *j*, then the working assumption is that the token probability at positions *i* and *j* are independent. That is the model makes prediction at *i* from the context independently from that of *j*. 

To make this joint prediction tractable, we compute the negative log of the cross entropy loss. This loss directly measures the [[Log-likelihood]] of the model given the data. The base of the logarithm is a choice. It can be either base-2 in which case the unit of this loss is in *bits*. It can be base-e (natural log), which makes the units of loss in *nats* or base-10 (for *dits*). Base-2 is a common choice for reporting because it is easier to interpret in the context of Shannon's information theory, while the natural log is easier to compute back-propagation so that is used in training. 

Choosing base-2, we can interpret the entropy loss as the number of yes/no questions that need to be asked to get the right question. Lower the better. Taking the exponent of this value gives us an interpretable quantity in terms of [[Perpexity]]. This term relates to the number of objects that a model has to choose from a uniform distribution. 

If a model needs to choose from 8 different objects, then it has a perplexity of 8. If I go to grocery store and need to decide which brand of chips I need to buy from, and there are 8 brands of chips. Then my perplexity measure is simply 8. Taking the log of that value, $$log(8)=3$$ gives me the value of entropy in bits (with base-2). 

So the performance of a language model can be meaningfully interpreted using the [[Perpexity]] score. 