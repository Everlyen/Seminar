---
link:
  - https://www.nature.com/articles/s41592-025-02836-7
authors:
  - Elana Simon
  - James Zou
year: 2025
tags:
  - protein_language_models
architecture:
dataset_size:
training_size:
database_used:
---
## What we thought was most interesting

```interesting
AB: Embeddings from a protein language model provide a rich source of biologically meaningful information, but it is often hard to interpret through concepts. It is known that such embeddings represent concepts in superposition, which allows a language model to squeeze large number of near-independant features into a finite embedding dimension. This paper uses a method called Sparse Auto Encoders to identify these features. Further, they intepret these features through biologically relevant concepts by aligning the features to human-curated database such as Swiss-Prot, which contains residue-level concepts. 

```


## Questions we have/had
- [ ] AB: How generalizable are the concepts mapped on to the feature space? Do we know any particular test case for such a method to validate? 
- [ ] AB: How useful is the automated annotation method? Unclear if there is any validation done on that. 
- [ ] 

---

## The paper itself (reference)

### What it's about
The authors demonstrate the application of mechanistic interpretability techniques developed for language models for protein language models. The tool, [[SAE|Sparse AutoEncoder]] (SAE) can be used to extract relevant features for residues from a pLM. As a practical application, they claim that it can be used to identify missing features in databases for perhaps further curation. 

Questions the authors wanted to answer: 
- How do they identify conserved motifs from individual sequences? 
- What percentage of learned features actually focus on these conserved motif patterns? 
- How do they leverage these memorized patterns for accurate sequence predictions? 
- What additional computational strategies support these predictions?
### Methods

### Key results



