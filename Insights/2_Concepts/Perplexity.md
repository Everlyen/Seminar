---
aliases:
  - exponentiated cross entropy (ECE),
tags:
  - ai
  - protein_language_models
related: "[[Log-likelihood|Entropy]]"
---
## What is it? 🤔

It is a measure of uncertainty for discrete probability distribution
$$ \text{PPL} = b^{-\frac{1}{N}\sum_i \log_b q(x_i)} $$
It is related to entropy (E) through the exponential operation.

$$ \text{PPL} = b^{E} $$
## Where I learnt this 🕶
[[Biological structure and function from learning sequences]]

## Example application 💡
Measuring the amount of surprise in a generated sequence
