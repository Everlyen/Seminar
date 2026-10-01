---
tags:
  - protein_language_models
  - 
one_line: method to extract interpretable features from the embeddings of a language model
---
## What it is
It is a method to extract interpretable features from the embeddings of a language model. The embeddings from a language model learn through superposition, which is a method where a large number of features can be fit into a limited embedding space. 

Here a 'feature' can be thought of as a special direction in the embedding space which represent something meaningful that a language model has learnt. It could be that not all the features that a language model learnt is meaningful as it can be affected by the particulars of the dataset that are used in the training. 

In a Sparse Auto Encoder, we train a 1-layer neural network to learn the relevant features. The hidden layer is often extremely wide compared to the embedding dimension. The input and target vectors are the same. For each vector, the SAE learns to represent it as a combination of linear vectors. To keep the identified vectors minimal, the activations on the hidden layer are forced to be reduced through L1 regularisation. 

![[sae-figure.png]]
## Why it matters in our papers

SAEs are used in many atlases to identify residue level features and for function annotation tasks. The features identified by SAEs span a wide level of biologically relevant concepts from description of fold, to family, and function as explained in [[Language Modeling Materializes a World Model of Protein Biology]]
## Where it gets confusing
*Edge cases, places where the concept is used differently across papers, or things that tripped us up.*

Choosing this L1 weight decay parameter is not always robust and thus we need to be careful while interpreting the features. 

There is a difference between "features" identified by the SAE and the "concepts" that we use to describe those features through language. To match the concepts we need to align the said feature space to a common benchmarked databases. 

## Open questions
- [ ] **CP**: this concept also appears in [FoldSAE: learning to steer protein folding through sparse representations](https://openreview.net/pdf?id=4Nuy8EMu00) which applies SAE to [RFdiffusion](https://www.nature.com/articles/s41586-023-06415-8) (Baker lab). RFdiffusion used diffusion models to improve RoseTTAFold (structure prediction tool they had) shortly after Alphafold participated in [[CASP]]. I didn't read either link completely but it confused me because it seemed to be a tool you could use to "force" the model (RFdiffusion) towards a form of secondary structure or solvent accessibility. It may still be? 
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
