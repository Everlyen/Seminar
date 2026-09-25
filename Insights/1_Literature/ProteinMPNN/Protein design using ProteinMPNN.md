---
year: 2022
tags:
  - ai
  - generative_biology
  - protein_design
  - graph_neural_network
link:
  - https://www.science.org/doi/10.1126/science.add2187
architecture_class:
  - Graph Neural Network
training_size:
  - 19700 [high-res single-chain structures]
dataset:
  - PDB
architecture_params:
  - 1.381 [million]
  - 1.678 [million]
---
#### Synopsis
The goal of this paper is to design a sequence which fits the desired protein backbone. The authors claim that they used graph neural networks to predict the sequence for a given protein backbone. They measured the performance using something called [[Sequence recovery]]. They also performed experiments on the predicted sequence. So I am expecting they obtained the gene vector, purified that protein and observed the structure experimentally. 

## Concepts
- [[CATH]] classification scheme for protein structure (Class, Architecture, Topology, Homology)
#### Performance metrics: 
- [[Sequence recovery]]: what percentage of predicted sequences actually matches native structure from test structures
- Relative AF success rate: 
- 

## Takeaways
#### Locally connected graph network suitable for structure-sequence prediction
>Unlike the protein structure prediction problem, locally connected graph neural networks can accurately model the structure-to-sequence mapping problem because the *optimality of an amino acid at a particular position is largely determined by the immediate protein environment*.

So a locally connected network has as its edges the nearest residues connected to a particular residue. This is an input to the network, therefore the network has to find residues which can fit into this connective network, sort of like a jigsaw puzzle. 

#### Network prediction done auto-regressively one residue at a time
>We began from a previously described message-passing neural network (MPNN) with three encoder and three decoder layers and 128 hidden dimensions that predicts protein sequences *in an autoregressive manner from the N to C terminus using protein backbone features*—distances between Cα-Cα atoms, relative Cα-Cα-Cα frame orientations and rotations, and backbone dihedral angles—as input ([_1_](https://www.science.org/doi/10.1126/science.add2187#core-collateral-R1)).

The network has as its inputs the backbone features of a protein (baseline: c-alpha to c-alpha distances, relative frame orientation and backbone dihedral angles). From this, the network has to predict one residue at a time. I guess the output is some kind of embedding vector that can be decoded as a residue? 

## Methods

#### Architecture
- Graph Neural Network (Message Passing Neural Network) + 3 encoder layer + 3 decoder layer + 128 hidden dimensions 
- They used 16, 24, 32 and 48 nearest neighbour connected graph network and found performance saturated after 32
- Output of architecture is one embedding vector corresponding to a residue (I guess) because it predicts residues autoregressively
- 19,700 structures used for training/val/test divided based on [[CATH]]
- [[Sequence recovery]] used as performance metric

#### Input and architectural details
The input features are edge features. There are 5 atoms per residue that they consider and between two residues you have 5 x 5 = 25 distances that you need to compute. 

They use radial basis functions to split the scalar distance into a vector. 16 functions between 2 and 22 A. So for each edge, they have 400 numbers encoding distances. Additionally, they use one hot encoding for relative positional encoding for max sequence distance of 32. That vector is of size 16. Therefore we have in total 416 dimensional vector that is input. That input is squished into 128 (hidden_dim) vector which actually goes into the network. 

- Encoder
The encode takes the edges. The nodes are zero vectors. The steps followed are as follows: 
for node i 
for all node j
- Message: Concatenate: node vector i, node vector j, edge feature E_ij and pass through MLP (3 layers)
- Aggregate message: Sum(message) (in the code it is also normalised by length so it is a mean)
- Update the node feature (along with some fancy layer norm + FFN)
- Use the updated node features to also update the edge feature (saw in Experiment 3 that it improves)

- Decoder: Takes the updated node and edge features from encoder. Updates only the node features. 
	- for node i, 
		- Message: concatenate node feature from i, j and edge feature Eij and pass it through MLP 
		- Aggregate: take mean of the messages recieved from all neighbors
		- Update the new node feature and layer norm that 
	- You also get a sequence vector S and a mask. The mask tells you which sequence positions that the decoder is allowed to look at for each prediction. 
	- 

![[Pasted image 20260610114631.png]]
#### Experimental design: Progressive improvement of performance: 
They conduct small improvements from a baseline model to test whether they produce meaningful improvement in performance. 


>[!How are these features encoded? ] How are these features encoded?

- Baseline model: only has protein backbone features. 
	- $c-\alpha$ to $c-\alpha$ distances
	- frame orientation of residues (I guess that is what they mean by ca-ca-ca relative frame orientation)
	- dihedral angles

- Experiment 1: Include additional positional feature; N, Ca, C, O and virtual C-beta
	- What is virtual C-beta? calculated from baseline features?
	-  interatomic distances evidently provide a better inductive bias to capture interactions between residues than dihedral angles or N-Cα-C frame orientations?

- Experiment 2: Include edge-update along with node update
- Experiment 3: Combine Experiment 1 and Experiment 2
- Experiment 4: Experiment 3 with random decoding
	- Decoding order is not fixed from N to C, but is randomly sampled 



## Evidence

### In silico experiments show better sequence recovery
![[Pasted image 20260611104251.png]]
#### Alphafold predicts the same structure that the sequence intended to design 
- Adding noise to the training data helps because it relaxes the constraints imposed by X ray data
![[Pasted image 20260611104317.png]]


### Experimental validation of the designed sequences
#### ProteinMPNN recovers the failed Alphafold designs
- Better soluble proteins recovered
-![[Pasted image 20260611104410.png]]
- Recovered soluble proteins have the expected mass distribution according to chromatography
![[Pasted image 20260611104426.png]]
- Recovered soluble proteins have secondary structures which are stable until 95C 
![[Pasted image 20260611104440.png]]
#### Recovered proteins have the expected structure through X ray crystallography
![[Pasted image 20260611104505.png]]

#### Designed proteins can bind to a desired target showing protein function capability

![[Pasted image 20260611104530.png]]

## Conclusion
The authors show that graph neural network which is locally constrained is capable of producing stable design sequences. The sequences produced match that of native structures better than Rosetta. AlphaFold also predicts that the ProteinMPNN sequence folds into the right conformation, although that required training the model with some (but not a lot) of gaussian noise. 

The authors also show that the predicted sequences are soluble, have the right mass distribution and hte secondary structure are stable at high temperatures. The structure observed through X ray crystallography also matches the desired structure, which is somewhat unique to those found in the PDB (TM =0.56, but the sequence is quite novel HHBlits E-value = 2.3)

They also show that designed proteins can also perform the expected function by designing a scaffold for a polyproline peptide. This scaffold was stable and it also was able to bind to the target protein. Mutating the sequence failed to perform the function and the peptide binder did not bind. 

