---
link:
  - https://www.nature.com/articles/s41592-026-03028-7
authors:
  - R. Prabakaran
  - Yana Bromberg
year: 2026
tags:
  - protein_language_models
  - 
architecture:
num_params:
dataset_size:
database_used:
---
## What we thought was most interesting

```interesting
AB : This paper presents probably the only method to measure the quality of an embedding from a protein language model. They find that not all embedding representations of protein are biologically meaningful and hence affects downstream tasks such as structure predictions. 

```

## Questions we have 

- [ ] AB

---

## The paper itself (reference)

### What it's about
	 What are the questions that the authors sought to answer? 
		- Is there a 'junkyard' of embedding space where low quality embeddings generally reside?  
		- Does embedding uncertainty affect downstream performance? 
		- 

	 What was known in the field before this paper?
		 - Some developments in natural language models studied embedding quality, but unclear how it was done.  

### Methods
#### RNS metric
The quality of an embedding vector (for a protein) is measured by which fraction of its neighbor correspond to a randomly shuffled protein structure. The core test of reliability of an embedding vector to predict downstream performance is to compare it to another embedding vector from a biologically implausible sequence. This is obtained by randomly shuffling amino acid sequences from a well curated [[Astral-40]] dataset. Each sequence in this dataset is shuffled four times to create an Astral-40R dataset from which embeddings are calculated using different PLMs. The metric is applicable to any protein language model which represents a single structure by a vector embedding. 


### Key results
##### Presence of a junkyard of protein embeddings
##### Embedding uncertainty predicts poor downstream performance: 

#### 


