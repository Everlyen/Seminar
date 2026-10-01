---
tags:
  - protein_language_models
  - biology
  - deep_learning
one_line: A model trained to learn the conditional probability distribution of amino acid residues from a large sequence database.
---
## What it is

It is a deep learning model trained to learn the pattern of amino acid residues found in sequence databases. Conceptually, it is similar to Large Language Models, with amino acid residues forming the unit of tokenisation and is therefore another example of the [[distributional hypothesis]] 
This is accomplished by masking out a certain percentage of amino acids in a given input sequence (typically, around 15%) and training a transformer based neural network model to predict the masked residues. It has been found that such a masked language modelling objective results in a model whose internal representations can be used to extract meaningful biologically relevant signals. 

You can think of a protein language model like a series of parallel residual streams (shown below), sort of like different lanes in a swimming pool. Each token "swims" in its lane, but gets affected by other tokens in the input (this is where the analogy fails!)

The manner in which the embeddings get transformed at each layer is shown below for the protein language model. 

![[residual-stream-plm.gif|521]]

In a large language model, only the early tokens are allowed to affect the later tokens and thus have a unidirectional causal flow. This is represented in the following animation. 
![[residual-stream-llm.gif|520]]
## Why it matters in our papers

The learned embeddings from a protein language model are increasingly being used as a prior to guide structure prediction or function annotations. Learning how these models are trained, and to understand how the embeddings can be extracted is useful to develop new tools for structure prediction or protein design. 

## Where it gets confusing
*Edge cases, places where the concept is used differently across papers, or things that tripped us up.*

A common source of confusion is in developing intuitions for high-dimensional geometry. Many papers use reduced dimensionality through t-SNE, UMAP or PCA projections. It is useful in these plots to understand the assumptions built in, especially regarding local and global distance measures. 

It is also easy to trip up which embeddings are being referred to in different places. You can have one embedding per residue, or pool from all residues of a protein to have one embedding per protein structure. It would be important to identify which representation is being talked about while reading papers about it. 

## Open questions

- [ ] 
### Related concepts

```dataview
LIST
FROM [[]] AND "2_Concepts"
```

### Where this concept is discussed
```dataview
LIST
FROM [[]] AND "1_Literature"
```
