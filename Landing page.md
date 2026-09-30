
### Progression
```mermaid
graph TD
    D[Central dogma\nsequence → structure → function]
    D --> P[Sequence\nUniProt · UniRef]
    D --> S[Structure\nPDB · SCOPe]
    D --> Dom[Domains & families\nInterPro]
    D --> F[Function\nGO terms]
    P & S & Dom & F --> CASP[CASP\nbenchmark tracking progress]
    CASP -->|decades of progress| pLM[Protein language models\nESM-2]
    P --> pLM
```
### What the papers ask
```mermaid
graph TD
    subgraph Input
        P[Sequence only]
    end
    subgraph Model
        P --> ESM[ESM-2\ntrained on sequence alone]
        ESM --> E[Embeddings]
    end
    subgraph Questions
        E --> SAE[InterPLM\nWhat did it learn?]
        E --> RNS[Quantifying Uncertainty\nCan I trust this?]
    end
    subgraph Validation
        SAE & RNS -.-> DB[Known biology\nInterPro · GO terms · SCOPe]
    end
```

# Papers 
[[InterPLM discovering interpretable features using Sparse AutoEncoders]]
[[Quantifying Uncertainty of protein representations]]

### All concepts
```dataview
TABLE without ID 
	file.link AS "Concept",
	one_line AS "One line definition"
FROM "2_Concepts"
SORT tags ASC
```

