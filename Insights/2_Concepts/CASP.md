---
aliases:
tags:
  - ai
---

## What is it? 🤔
Critical Assesment of Structure Prediction - [CASP](https://en.wikipedia.org/wiki/CASP)
Ranking of current protein structure prediction methods. A.I. models like Alphafold have won since 2018 (CASP13) when Alphafold1 participated for the first time. In 2020 (CASP14) Alphafold 2 was introduced and scored 90/100 points of accuracy (what does accuracy measure here exactly?) in the category of moderately difficult protein targets (interpretation of quote from wiki from CASP cofounder and the graph in wikipedia article. But no source.)

Source: [[High-accuracy refinement using Rosetta in CASP13]] 
There are different categories in CASP, one of them is model refinement where predictors attempt to use an energy minimization function and conformational search to find the lowest energy conformation of a protein structure.  

AlphaFold2 criticism: 
It did not reveal the underlying mechanism or rules of protein folding for the protein folding problem. 
 - source: https://www.chemistryworld.com/opinion/behind-the-screens-of-alphafold/4012867.article
## Where I learnt this 🕶
Background recollection and wikipedia curation for accuracy - Cecilia
First encountered: [[Protein language models learn evolutionary statistics of interacting sequence motifs]]
Appears again in the work of David Baker 


### History
source: https://predictioncenter.org/index.cgi with some extra digging: 
Starting from a primary sequence how does one determine the protein tertiary structure? 
There have been mainly two approaches: 
1. Anfinsen's thermodynamics
	1. Native structure is *global* free-energy minimum for that sequence under physiological conditions. Based on a physics based forcefield (minimize free energy), as long as you sample the conformational space well enough you should find the native structure of the sequence by finding the lowest energy state. This is the idea behind ab initio modeling. 
2. Evolutionary conservation
	1. Structure is far more conserved through evolution than sequence is. Distantly related proteins keep the same fold long after their sequences have diverged past recognition. Instead of searching the physical space (like ab initio does), search the known structure space for something comparable. This is the idea behind template-based modeling. 
		1. Template based modeling or comparative modeling can be divided into two approaches: 
			1. homology modeling - clear sequence similarity to a solved structure. Align directly and copy the structure 
			2. Fold recognition/threading - no sequence similarity. Place the primary sequence within known folds/known structures and score the fit based on side-chain burial, contacts, secondary-structure compatibility. Useful when sequence identity is below 25%.  

CASP4 (2000) - Ab initio modeling takes a big leap. Rosetta (Baker lab) used fragment assembly, Monte Carlo energy search, multi-homolog folding (what is this really, seeing as it should be a model free method?) and all-atom relaxation. Comparative modeling is already established at this point (eg. MODELLER, THREADER - May be interesting to look into these a bit?).

CASP5 - 10 (2002 - 2012) - No ab initio models for sequences above 100 residues with [[GDT_TS]] above 50. I-TASSER and HHpred lead in threading, RaptorX (multi-template threading server). Correlated-mutation contact prediction exists but stays under 20% precision.  In what way does it exist? 

CASP11 (2014) - DCA-based contact prediction (MSA coevolution used by CONSIP2/MetaPSICOV - 27% precision now). Baker group builds a 256-residue, <5% sequence-identity target with no template. 4 ab-initio targets over 100 residues cross GDT_TS 50. Template-based modeling is among others: Zhang server (I-TASSER), BAKER-ROSETTASERVER, QUARK (also a Zhang group predictor). 

CASP12 (2016) - Template-based modeling (TBM) improves due to better multi-template alignment and model-accuracy estimation. Contact prediction precision nearly doubles from 27% to 47%, with 21 of 23 methods using deep/machine learning. Half of ab initio targets over 100 residues now exceed GDT_TS 50. 

CASP13 (2018) - Best-model ab-initio GDT_TS rises 52.9 → 65.7 (>20% backbone-accuracy improvement). Contact precision jumps again, 47% → 70% (RaptorX, MULTICOM deep ResNets). Rosetta, UNRES, and MULTICOM all use restraint-guided energy search using deep-learning-derived distances rather than plain contacts. TBM leaders (excluding AlphaFold/A7D): Zhang > MULTICOM > Seok-refine > McGuffin — with best TBM-hard results now coming from deep-learning methods that barely use an explicit template at all. 

CASP14 (2020) - AlphaFold2: ~2/3 of 96 targets reach GDT_TS >90, competitive with experimental accuracy. TBM average reaches ~92 GDT_TS. MULTICOM2 (Cheng lab) still ranks among top server predictors, getting correct topology on nearly all TBM and most FM targets. No further gain in raw contact-prediction precision between CASP13 and 14.

MULTICOM and trROSETTA (Yang group) are interesting - outperform the default AF models in CASP15 and 16. 

How this leads back to ESM? The coevolutionary statistics that DCA/AF2 extract _explicitly_ from a MSA at prediction time get baked _implicitly_ into ESM-2's weights during pretraining across the whole protein dataset. 

Question: So really is AF2 is a natural extension on what the field was already doing and ESM2 is the next step. (Analogy: if aminoacids are tokenized as words are, instead of looking for similar sentences -MSA/DCA to find the fold, they consume all books -Databases, train on that and find similarities?)
## Example application 💡