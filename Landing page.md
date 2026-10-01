
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

### All interesting bits!
```dataviewjs
const folder = "1_Literature";    // folder to search; "" = whole vault
const only = "interesting";     // label to find; "" = all code blocks

const re = /^(`{3,}|~{3,})[ \t]*([\w-]*)[^\n]*\n([\s\S]*?)^\1[ \t]*$/gm;
const pages = folder ? dv.pages(`"${folder}"`) : dv.pages();

for (const p of pages.sort(p => p.file.name)) {
  const text = await dv.io.load(p.file.path);
  const blocks = [...text.matchAll(re)]
    .filter(m => m[2] !== "dataviewjs" && (!only || m[2] === only));
  if (!blocks.length) continue;
  dv.header(3, p.file.link);
  for (const m of blocks) dv.paragraph("```" + m[2] + "\n" + m[3] + "```");
}
```