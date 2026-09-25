---
year: 2024
tags:
  - ai
  - protein_language_models
  - esm
link:
  - https://doi.org/10.1073/pnas.2406285121
architecture_class:
  - transformers
training_size:
dataset:
architecture_params:
---
## Synopsis

The paper investigates the mechanisms driving the protein language models. These are the three hypothesis that they are testing. 

![[Pasted image 20260804143350.png]]

### Why? 
Why are they doing these studies at all? 
- MSA are useful to infer structure because there are a lot of homologous proteins that have been determined experimentally. If a similar sequence has been determined, it's easier to infer that a closely related sequence will share that fold. However, the most useful situation would be a language model which has learnt the biophysics that underlies protein folding. This would make it useful for proteins that share very little sequence [[Homology|homology]] with known/determined structures, [[isoforms]], etc. It would also provide scientists with more knowledge on this process which is currently generally well understood, but which clearly lacks identification of certain factors to describe the process that happens biologically. (The clear improvement of protein structure folding at [[CASP]] from CASP 13 to CASP 14). 
## Concepts
- [[Categorical Jacobian]]: 
## Methods

#### Method - 1 
- Does the model predict unphysical structures from [[isoforms]]? 

##### Method - 2

## Evidence


### Structure prediction tools predicts unphysical structures from isoforms

- Spatial Aggregation Propensity (SAP) : how easily does the structure aggregate? (more is bad) - this aggregation happens because of the types of (hydrophobic) residues that are left exposed in the predicted structure (more is bad)
- Predicted local distance difference test ([[pLDDT]]): AI model confidence score from 0-100. Higher means higher confidence. 
- RMSD to reference: how different are the predicted models to the reference. higher means less similar. 
![[Pasted image 20260804173712.png]]


### Progressive unmasking quickly from adjoining context is more efficient at recovering structure than random unmasking

#### Flanking is better at recovering structure than random unmasking
![[Pasted image 20260804174026.png]]
#### Flanking produces sharp jump in recovery by the addition of a single residue
![[Pasted image 20260804174115.png]]
This tells us that there is a certain "memory" of the structure associated with a particular fragment of sequence. This memory gets triggered by progressive unmasking through flanks. There is a sharp jump in recovery. 

### Categorical Jacobians can recover structure information almost as good as supervised training with a contact head

#### Method of extracting categorical jacobian
![[Pasted image 20260804174459.png]]

#### Catogorical jacobian to contact prediction
![[Pasted image 20260804174552.png]]
#### Bigger models produce more accurate contact signals
![[Pasted image 20260804174411.png]]
Subfigure (E) shows how correlation of the contact predictions wrt Linear models increase with model size. B, C and D uses ESM-2 3B model. 

Contact prediction is estimated through precision @ top L/2. 

| Method                                        | P@L/2 |
| --------------------------------------------- | ----- |
| Linear model                                  | 0.67  |
| pLM (categorical jacobian)                    | 0.8   |
| pLM (w/ supervised training for contact head) | 0.87  |

## Conclusion
- pLM learns to connect fragments of sequences into structural signal. 
- pLM or even AlphaFold have not learnt protein biophysics 
- categorical jacobian is a useful way to extract structural signal from pLM without additional supervised head. Just the pLM signal alone gets almost all the structure prediction. 
- "A model that segments a protein into common motifs, as our work suggests pLMs are doing, offers a clear route to [[compression]]. A downside of such compression is that within- family evolutionary effects such as multiple stable conformations are inaccurately predicted by ESM-2 (SI Appendix - Supporting Information Text), a clear area for future improvement" - look at the examples presented in the SI text to better understand what is meant by: "multiple stable conformations are inaccurately predicted by ESM-2" - this conclusion is essentially that the motifs and coevolution data is stored within the model. So hypothesis 3 is the closest to correct? 

## Questions
- How did they select those "fragments" to test? Did they choose fragments of aa with known contact or was it randomly selected? 
- If we select blindly certain fragments, can we know if there is a contact or not just by looking at the categorical jacobian contact maps? 
- Is that all that pLMs learn? Are there any "useless" bits of correlations that they learn which are not really relevant? What percentage of learned patterns are actually useful? 
- Quote: "unsupervised task of masked language modeling" - what does this learn on? Only on the tokens/aminoacids from the sequence? Whats masked?
- CP thought: the text assumes that the structures are incorrect because the form found in cells is as an aggregate or am I interpreting this incorrectly? Its possible that they've studied the isoform of the proteins that give rise to aggregates and they know that it's a different structure? But then they should compare those two structures as representations of the final state (proteins go through defined steps/phases of unfolding between being folded and being misfolded and then unfolded).  
- Quote: "If state-of-the-art protein structure prediction approaches predict such isoforms as either unfolded or alternately structured, it would imply an intrinsic understanding of the biophysics of protein folding" - proteins that have such exposed patches, aren't these the kinds of structural determinants (properties of the structure determined by the properties of the residues available for interaction in a solvent exposed state) that lead to aggregation. If that all follows then my question is, is this the right metric to be using? Because to an extent it could be an accurate representation of the diseased form of the protein exactly because it is a semi stable form of a protein that does tend to aggregate. (It actually would then hold the biophysical properties that are in the intermediate step - between healthy and native protein and the bowl of spaghetti at the end of the process.)
- Quote: "A clue for how ESM-2 might be storing coevolutionary information came via a consistent error we encountered in the predicted structures of isoforms, which we found were consistently predicted to fold to fragments matching their structure context within the full-length proteins, but which left nonphysical patches of hydrophobic residues exposed. We figured whether the model learned protein folding and not simply looked up evolutionary statistics, it should be able to model a more-likely unfolded conformation." The aggregated form of a protein has a lower energy than a protein with a hydrophobic patch exposed. Why is the unfolded conformation the most likely? Is it not trained on folded proteins? How would it even learn what unfolded is in it's training data/weights? If anything, if it learned the biophysics behind protein folding I would expect to see different folds of the protein where those patches are minimized. Perhaps they already are? Maybe this is the lowest possible energy state for this sequence? It would make sense, it has to be somewhat stable, but high potential energy? Not in the energy well like we're used to, but the transient high energy state we cannot see?  
- From figure 2: What does the structure of the wt and the models predict for IL4 and HER1 isoforms? 
	- Left: full type prediction(CHS.43898.1_IL4), middle: isoform (CHS.43898.5_IL4), right: wild type (PDB: 2B8U)
  ![[image3.png|199]]![[image4.png|189]]![[image5.png|193]]
- What about [[de novo genes]]? This is maybe a side track but these are proteins that don't share much homology with others genes. 
### Limitations: 
By authors: 
- "A clear limitation of this study is that we do not have experimental evidence for the actual in vitro structure landscapes of these isoform examples." - example: Myoglobin isoform HS.35702.2 from [[CHESS]]
- "Our analysis does not completely rule out that pLMs have learned the concept of full folds, since the continuous segment unmasked in the flanking region might have helped the model to match to full proteins. " 
- "A downside of such compression is that within- family evolutionary effects such as multiple stable conformations are inaccurately predicted by ESM-2 (SI Appendix), a clear area for future improvement.". Examples from SI: 
	- ESM2 predicted same fold for two KaiB sequences with different experimental structures. KaiB adopts two distinct states as part of its function. (...) While experimental results showed that each sequence favors one state over another, ESM2 predicted that both sequences fold to the thermodynamically unfavorable fold-switched (FS) state. 
	- ESM2 predicted the same interchain contacts for bacterial response regulator subfamilies with diverse interchain contacts. Three bacterial response regulator subfamilies were shown to have diverse interchain contacts between their homomeric interfaces despite having similar intrachain contacts. Method: We calculated the interchain contacts from experimental structures of the three different families (contact defined as < 12 Å between alpha carbons) and predicted contact maps for them using the sequence of the domain and the ESM255 contact head. The outputs of the ESM2 contacts on the different aligned using US-align, removing all gap positions. We consider the top 300 contacts predicted by ESM2 which are >5 positions off the diagonal. Interchain contacts which are unique to each structure are colored according to the family they belong to in the distogram.