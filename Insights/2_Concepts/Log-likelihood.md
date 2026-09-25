---
aliases:
  - Entropy
tags:
  - ai
related: "[[Perpexity]]"
---

## What is it? 🤔
It is a common way to measure the performance of a model. We are talking about any model that aims to learn from data through some parameters. We want the model to maximise the term Likelihood. This is the probability that we observe some data, *D* for a given set of parameters *theta*. The model tunes the parameter to fit the data. 

$$Likelihood =  P(D | \theta) $$
We take the logarithm of this likelihood function because it is much easier to work with. In case of language models, the likelihood is the product of conditional probabilities of all the missing tokens. Taking logarithms make the product into a sum which is much easier to work with. For machine learning applications, it is generally the convention that we multiply that by -1 to minimise that objective. 

$$ Log-likelihood = -1 \cdot log[P(D | \theta)]
$$
## Where I learnt this 🕶
This is a general concept. It is widely used in many applications

## Example application 💡