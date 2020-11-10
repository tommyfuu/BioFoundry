# BioFoundry

BioFoundry Project at the HMC BioMakerspace. An automated workflow to design primers for circularised DNA and for [FastCloning](https://bmcbiotechnol.biomedcentral.com/articles/10.1186/1472-6750-11-92) experiments. This workflow supports fasta and genbank DNA file format as well as string format for plasmid sequence inputting to allow better user experience.

### Dependencies

Install dependencies with

```
pip install -r requirements.txt
```

If you would like to install them manually:

1. [Primer3-py](https://libnano.github.io/primer3-py/index.html) (Download via terminal with `pip install primer3-py`)
2. [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) (Download via terminal with `pip install pandas` or `conda install pandas`)

### Usage

#### Installation

Clone or download this repository, enter the local directory where the repo is located. If you haven't already, install the dependencies with

```
pip install -r requirements.txt
```

More accessible installation methods to come later.

#### Primer design

Enter ipython in your terminal before you design your primer. Then do the following:

```
run fastCloningPrimer.py
```

This repository enables two types of primer designs. You can either design primer pairs for simply isolating an area from a plasmid; or you can design primer pairs for [FastCloning](https://bmcbiotechnol.biomedcentral.com/articles/10.1186/1472-6750-11-92) experiments.

1. You can simply design primer3 primer pairs for simply isolating an area from a plasmid. The output will be a python dictionary with really readable data structure, for example, for the sample output below, for each primer pair, we have two primers, with their annealing temperatures and sequences clearly outputted.

```
{'primerPair0': [['left', 60.10745937656958, 'GGAGAGGGTGAAGGTGATGC'],
  ['right', 59.96383622575223, 'ATCACTTGCGGTTGCCAGTA']],
 'primerPair1': [['left', 60.10745937656958, 'GGAGAGGGTGAAGGTGATGC'],
  ['right', 59.899496813039036, 'CGGGATGCGGTTTGATTTCC']],
 'primerPair2': [['left', 60.10745937656958, 'GGAGAGGGTGAAGGTGATGC'],
  ['right', 60.108991841923455, 'TATTGTCAGGCACGACGACC']],
 'primerPair3': [['left', 59.808935902916005, 'AGTGGAGAGGGTGAAGGTGA'],
  ['right', 59.96383622575223, 'ATCACTTGCGGTTGCCAGTA']],
 'primerPair4': [['left', 59.808935902916005, 'TCAGTGGAGAGGGTGAAGGT'],
  ['right', 59.96383622575223, 'ATCACTTGCGGTTGCCAGTA']]}
```

You have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.

(1) If you input the plasmid sequence as a string,

```
primer3Only(plasmidSeq, goalSeq)

## TEST INPUTS:
## primer3Only(vectorPlasmidSeq1, vectorSeq1)
## primer3Only(insertPlasmidSeq1, insertSeq1)
```

This gives you several primer pairs for isolating insertSeq1 from its plasmid insertPlasmidSeq1.

(2) If you input the plasmid sequence as a fasta/genbank file,

```
primer3OnlyFile(plasmidSeqFile, goalSeq)

## TEST INPUTS:
## primer3OnlyFile(vectorPlasmid1AddressFA, vectorSeq1)
## primer3OnlyFile(insertPlasmid1AddressGB, insertSeq1)
```

2. You can design primer3 primer pairs for your fastCloning experiments. Sample outputs can be seen at `sampleOutput-fastCloningPrimerInfo.csv`.

Again, you have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.\
(1) If you input the plasmid sequences as strings,

```
fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq, maxTempDiff, destinationAddress)
# Note that maxTempDiff, destinationAddress are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq)

## TEST INPUTS:
## fastCloningPrimers(vectorPlasmidSeq1, insertPlasmidSeq1, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

(2) If you input the plasmid sequences as fasta/genbank files (please make sure two plasmid files have the same format),

```
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq, maxTempDiff, destinationAddress)
# Note that maxTempDiff, destinationAddress are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq)

## TEST INPUTS:
## fastCloningPrimersFile(vectorPlasmid1AddressFA, insertPlasmid1AddressFA, vectorSeq1, insertSeq1)
## fastCloningPrimersFile(vectorPlasmid1AddressGB, insertPlasmid1AddressGB, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

#### Next steps

Next release will include the following:

1. Potentially including more primer3 parameters to be adjusted by users.
2. The current algorithm uses primer3 default melting temperature calculator for Taq polymerase, but in our case we will need it for Phusion. We will try to figure that out.
3. Double checking primer feasibility to demonstrate our workflow's robustness.
4. More explanations on the algorithm that recircularizes linearized plasmid DNA for primer3.

### Acknowledgement

Developers:\
Tom Fu [(@tommyfuu)](https://github.com/tommyfuu)\
Richard Chang [(@richanghmc)](https://github.com/richanghmc)

Affiliation: Harvey Mudd College BioMakerspace (Polymerspace). \
Faculty advisor: Dr. Dan Stoebel.

This project is part of the intellectual property of the [Harvey Mudd College BioMakerspace](https://biomakerspace.com/). Please notify the space at **tfu@g.hmc.edu** for consent before using any of the materials in this repository. Please cite us if you use our repository for academic sharing purposes.

The funding support of the Harvey Mudd College BioMakerspace comes from Harvey Mudd College Office of Community Engagement and the college's Shanahan Fund.
