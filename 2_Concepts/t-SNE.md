---
aliases:
tags:
  - ai
  - "#dimensional_reduction"
related:
  - "[[PCA]]"
  - "[[UMAP]]"
---
## What is it? 🤔
It is a dimensional reduction technique which maps a high-dimensional vector into smaller dimensional for interpretation. It preserves local-structures so that neighborhood information is maintained at the cost of global distance. Distances are not very meaningful in this case. 

The way t-SNE is computed is by converting distances in high-D space into probabilities. Then, the points are scattered into low-D space randomly and then using gradient descent it tries to match the probability distribution of the high-D space using [[KL-divergence]] metric. 

Distances are converted into probabilities in high-D space using gaussians centered around each point and the gaussian width, called *perplexity* (slightly different from the information-theory concept) is a hyperparameter. Low values strongly preserve local neighborhood but global structure becomes less meaningful because the projected dimensions do not capture those structures. 

## Where I learnt this 🕶
[[Biological structure and function from learning sequences]]

## Example application 💡
To show visually how close embeddings are from a transformer architecture