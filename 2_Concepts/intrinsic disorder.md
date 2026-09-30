Sequence prediction tools: 

https://metapredict.net/
https://iupred3.elte.hu/

- **IUPred3 / metapredict / PONDR** — sequence-only disorder predictors. Run the isoform sequence through one of these independent of any structure prediction. Alternative measure of intrinsic disorder within protein from sequence (how do these work?)
- **Uversky charge-hydropathy plot** — plots net charge against mean hydropathy; IDPs cluster in a well-defined region of that plot. Purely compositional, no model involved, easy to compute by hand from the sequence.
- **Short MD relaxation** from the predicted coordinates — does the structure hold, or does the "patch" region become mobile almost immediately? [[AWSEM-MD: Protein Structure Prediction Using Coarse-Grained Physical Potentials and Bioinformatically Based Local Structure Biasing]] ?? 
- **Resampling the structure prediction from ESM2** with different seeds — if the model is well-calibrated about a disordered region, you should see the predicted conformation vary run to run rather than converge on one confident answer.