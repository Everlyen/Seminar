---
aliases:
tags:
  - ai
  - protein_language_models
---

## What is it? 🤔
It is a way to represent structural information (what information? Aminoacid pairwise interactions?) from a general protein language model (need not be deep learning based, as long as it gives probability distribution per residue position)

## Question
How do the mutations matrixes with [[Categorical Jacobian]] work? What does it do to the input information? What does the final matrix mean? 
## Where I learnt this 🕶
[[Protein language models learn evolutionary statistics of interacting sequence motifs]]



## Example application 💡
Is it already possible to visualise on a 3D structure the information within the Jakobian vs. Categorical Jakobian? Theoretically possible if the representation is an interaction between atoms involved in bond, and color bond with increasing value on likeleyhood? Requires atomic level information so a lot of work, or perhaps a script that searches the pdb for the shortest distance between the two residues presented and uses that bond? 