### Before times

```mermaid
graph TD
    D[Central dogma\nsequence → structure → function]
    D --> P[Sequence databases\nUniProt · UniRef]
    D --> S[Structure databases\nPDB · AlphaFold]
    D --> F[Function databases\nInterPro · GO terms]
    P --> CASP[CASP\nbenchmarking structure prediction]
    S --> CASP
    CASP -->|decades of progress| pLM[Protein language models\nESM-2]
    P --> pLM
```

**Concepts in this diagram:** [[CASP]] · [[homology]] · [[protein families]] · [[intrinsic disorder]] · [[bioinformatics]] · [[SCOPe]]


### What the papers ask
```mermaid
graph TD
    P[Sequence] --> pLM[pLM\nESM-2]
    pLM --> E[Embeddings]
    E --> SAE[InterPLM\nSAE features]
    E --> U[Uncertainty\nRNS]
    SAE -.->|what did the model learn?| K[Known annotations\nInterPro - Uniprot]
    U -.->|can we trust this embedding?| K
```
**Concepts in this diagram:** 
[[ESM-2]] · [[embeddings]] · [[sparse auto encoders]] · [[random neighbor score (RNS)]] · [[mechanistic interpretability]]