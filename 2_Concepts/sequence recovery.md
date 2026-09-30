---
aliases:
tags:
  - ai
  - protein_design
---

## What is it? 🤔

It is a metric to validate the performance of a protein design neural network. It measures the percentage of residues in the predicted sequence that perfectly match the sequence identity in the native structure that is experimentally determined. The network would be given just the backbone of a protein structure by removing all the side chains. The task of the model is to predict the side chain residues. 
## Where I learnt this 🕶
[[Protein design using ProteinMPNN]]

## Example application 💡
Sequence recovery of predicted structure is 54% means 54% of predicted residues match the native structure. It may also mean that certain predicted sequence might still be stable, but just does not match what is experimentally determined. 