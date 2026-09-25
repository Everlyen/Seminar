---
year: 2026
tags:
  - ai
link:
  - https://www.biorxiv.org/content/10.64898/2026.06.03.729735v1.full
architecture_class:
training_size:
  - 2.8 billion [sequences]
dataset:
  - "[UniRef](https://www.uniprot.org/uniref)"
  - (156 million) 
  - "[JGI](https://genome.jgi.doe.gov/portal/)"
  - (2.029 billion)
  - "[MGnify](https://www.ebi.ac.uk/metagenomics/)"
  - (621 million)
architecture_params:
  - 300 [million]
  - 600 [million]
  - 6 [billion]
---
#### Synopsis
ESM-Cambrian is the latest iteration of the ESM series of protein language models. The paper claims foundational breakthrough in the ability to characterization of protein biology. Their method is to apply language modelling to unify representations across protein biology. This representation is useful to perform diverse structure tasks like structure predictions and interactions. In addition they also study the conceptual space of the language model to reveal a structured representation of concepts. The organisation of these concepts was used to explore the connections across known and unknown protein biology, and they present an atlas of billions of proteins across evolutionary timescales. 

## Concepts
[[Enzyme Classification (EC) numbers]]

## Methods

#### Method - 1 
- 

##### Design of binders with high-affinity
- p(x,s) = p(s | x,t) p(x)
- p(x) prior sequence probability from ESMC
- p(s | x,t) probability of the structure x conditioned upon a target sequence t and candidate sequence x
- generate many candidate binders -> predict each target-bound complex with multiple ESMFold2 replicas -> and rank candidates by their average ipTM, a confidence score for the predicted interface
## Evidence

### Result 1
- 
### Result 2
#### Sub-result 1


## Conclusion


### Useful blocks
```mermaid
graph LR
  A[A] --> B[B] --> C[C]
```
- $$y = f(W \cdot x + b)$$