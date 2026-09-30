---
link:
  - https://www.nature.com/articles/s41592-025-02836-7
authors:
  - Elana Simon
  - James Zou
year: 2025
tags:
  - protein_language_models
---
## What we thought was most interesting

**Initials**:
## What confused us

**Initials**: 
## Questions we have/had
- [ ] AB: How does SAE actually work? Is there any risk of "seeing what you want to see?" involved here because you are using nonlinear functions on high dimensional data to project it down to small number of interpretable contents. 
- [ ] AB: How generalized is this exactly? What sort of limitations exist for this model? 
- [ ] AB: Can we just apply this model to any protein, for instance GBP to find relevant features? 
- [ ] AB: What are the features that it can detect? Are there "amphipathic helices" in there? 

---

## The paper itself (reference)

### What it's about
The authors demonstrate the application of mechanistic interpretability techniques developed for language models for protein language models. The tool, [[sparse auto encoders|Sparse AutoEncoder]] (SAE) can be used to extract relevant features for residues from a pLM. As a practical application, they claim that it can be used to identify missing features in databases for perhaps further curation. 

Questions the authors wanted to answer: 
- How do they identify conserved motifs from individual sequences? 
- What percentage of learned features actually focus on these conserved motif patterns? 
- How do they leverage these memorized patterns for accurate sequence predictions? 
- What additional computational strategies support these predictions?
### Methods

### Key results



