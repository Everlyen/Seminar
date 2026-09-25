---
year: 2025
tags:
  - ai
  - esm
  - protein_language_models
link:
  - https://www.nature.com/articles/s41592-025-02836-7
architecture_class:
  - transformers
training_size:
dataset:
architecture_params:
---
#### Synopsis
The authors demonstrate the application of mechanistic interpretability techniques developed for language models for protein language models. The tool, Sparse AutoEncoder (SAE) can be used to extract relevant features for residues from a pLM. As a practical application, they claim that it can be used to identify missing features in databases for perhaps further curation. 

Questions I have before reading the paper: 
- How does SAE actually work? Is there any risk of "seeing what you want to see?" involved here because you are using nonlinear functions on high dimensional data to project it down to small number of interpretable contents. 
- How generalised is this exactly? What sort of limitations exist for this model? 
- Can we just apply this model to any protein, for instance GBP to find relevant features? 
- What are the features that it can detect? Are there "amphipathic helices" in there? 

Questions they ask themselves: 
- How do they identify conserved motifs from individual sequences? 
- What percentage of learned features actually focus on these conserved motif patterns? 
- How do they leverage these memorized patterns for accurate sequence predictions? 
- What additional computational strategies support these predictions?
## Concepts
- [[Sparse Auto Encoders]]
- 
## Methods

#### Method - 1 
- 

##### Method - 2

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