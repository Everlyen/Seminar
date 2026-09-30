---
tags:
  - protein_language_models
---
## What is it? 🤔
Also called: Exponentiated cross entropy

It is a measure of uncertainty for discrete probability distribution
$$ \text{PPL} = b^{-\frac{1}{N}\sum_i \log_b q(x_i)} $$
It is related to entropy (E) through the exponential operation.

$$ \text{PPL} = b^{E} $$
## Where I learnt this 🕶
[[Biological structure and function from learning sequences]]

## Example application 💡
Measuring the amount of surprise in a generated sequence

### Related concepts

```dataview
LIST
FROM [[]]
Where file.folder = "2_Concepts"
```

### Where this concept is discussed
```dataview
LIST
FROM [[]] AND "1_Literature"
```
