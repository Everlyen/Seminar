
link: https://amigo.geneontology.org/amigo/landing


description: https://geneontology.org/docs/ontology-documentation/

The Gene Ontology (GO) is a structured, standardized representation of biological knowledge. GO describes concepts (also known as terms, or formally, _classes_) that are connected to each other via formally defined [relations](https://geneontology.org/docs/ontology-relations/). The GO is designed to be species-agnostic to enable the annotation of gene products across the entire tree of life. The computational framework of the GO enables consistent gene annotation, comparison of functions across organisms, and integration of knowledge across diverse biological databases. 

GO is divided into three aspects: 
	Molecular function (MF)
		Individual molecule (protein, RNA) task (example: [[Catalysis]] or transcription regulator activity) 
	Biological Process (BP)
		 The biological task (example: [[DNA repair]] and [[Signal transduction]]). 
	Cellular component (CC) 
		The cellular location (example: [[Plasma membrane]])

Overview: 
https://amigo.geneontology.org/amigo/dd_browse
Very dense annotation. GoSlim is a selected number of relevant nodes
https://docs.omicsbox.biobam.com/latest/GO-Slim/

Data: https://current.geneontology.org/ontology/subsets/goslim_generic.obo - Curated
https://geneontology.org/docs/download-go-annotations/


Eg: 
[Term]
id: GO:0000228
name: GO CC.1 - nuclear chromosome
namespace: [[GO 1 - cellular_component]]
def: "A chromosome that encodes the nuclear genome and is found in the nucleus of a eukaryotic cell during the cell cycle phases when the nucleus is 

synonym: "nuclear interphase chromosome" NARROW []
is_a: GO:0005694 ! chromosome
intersection_of: GO:0005694 ! chromosome
intersection_of: part_of GO:0005634 ! nucleus
relationship: part_of GO:0005634 ! nucleus