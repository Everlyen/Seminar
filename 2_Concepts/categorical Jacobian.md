---
tags:
  - protein_language_models
  - 
one_line:
---
## What it is
It is a way to represent structural information (what information? Aminoacid pairwise interactions?) from a general protein language model (need not be deep learning based, as long as it gives probability distribution per residue position)

## Why it matters in our papers


## Where it gets confusing
*Edge cases, places where the concept is used differently across papers, or things that tripped us up.*

**Initials**: Text 

## Open questions

- [ ] **AB**: How do the mutations matrixes with categorical jacobian work? What does it do to the input information? What does the final matrix mean? 
- [ ] **AB**: Is it already possible to visualise on a 3D structure the information within the Jakobian vs. Categorical Jakobian? Theoretically possible if the representation is an interaction between atoms involved in bond, and color bond with increasing value on likeleyhood? Requires atomic level information so a lot of work, or perhaps a script that searches the pdb for the shortest distance between the two residues presented and uses that bond? 


---
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
