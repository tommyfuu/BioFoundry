# BioFoundry

BioFoundry Project at the HMC BioMakerspace. An automated workflow to design primers for circularised DNA and for [FastCloning](https://bmcbiotechnol.biomedcentral.com/articles/10.1186/1472-6750-11-92) experiments. This workflow supports fasta and genbank DNA file format as well as string format for plasmid sequence inputting to allow better user experience.

### Developmental Notes

Note that to design fastCloning primers with Phusion, you have to install selenium and have a (Macbook) with Chrome installed. Then, you have to install the chromedriver from [here](https://chromedriver.chromium.org/) for YOUR VERSION of chrome.

To run the webscrapper:

```
PATH=$(pwd):$PATH python3 NEBWebscraper.py
```

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

1. You can simply design primer3 primer pairs for simply isolating an area from a plasmid. The output will be a csv file. You can choose to have your primers to be outputted in a benchling acceptable format or not. Check out the sample outputs for this part in files `sampleOutputs/plasmidPrimerInfo.csv` and `sampleOutputs/benchlingPlasmidPrimerInfo.csv`.

You have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.

(1) If you input the plasmid sequence as a string,

```
plasmidPrimers(plasmidSeq, goalSeq, benchling=True, destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv', primerOptTm=PRIMER_OPT_TM, primerMinTm=PRIMER_MIN_TM, primerMaxTm=PRIMER_MAX_TM, primerMinSize=PRIMER_MIN_SIZE)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq)
# If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature), primerMinTem(the lowest acceptable melting temperature for primers), primerMaxTm(the highest acceptable melting temperature for primers), and primerMinSize (shortest acceptable primer length) are a few primer 3 parameters that you can adjust

## TEST INPUTS:
## plasmidPrimers(vectorPlasmidSeq1, vectorSeq1)
## plasmidPrimers(insertPlasmidSeq1, insertSeq1)
```

This gives you several primer pairs for isolating insertSeq1 from its plasmid insertPlasmidSeq1.

(2) If you input the plasmid sequence as a fasta/genbank file,

```
plasmidPrimersFile(plasmidSeqFile, goalSeq, benchling=True, destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv', primerOptTm=PRIMER_OPT_TM, primerMinTm=PRIMER_MIN_TM, primerMaxTm=PRIMER_MAX_TM, primerMinSize=PRIMER_MIN_SIZE)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq)
# If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature), primerMinTem(the lowest acceptable melting temperature for primers), primerMaxTm(the highest acceptable melting temperature for primers), and primerMinSize (shortest acceptable primer length) are a few primer 3 parameters that you can adjust

## TEST INPUTS:
## plasmidPrimersFile(vectorPlasmid1AddressFA, vectorSeq1)
## plasmidPrimersFile(insertPlasmid1AddressGB, insertSeq1)
```

2. You can design primer3 primer pairs for your fastCloning experiments. Check out the sample outputs for this part in files `sampleOutputs/fastCloningPrimerInfo.csv` and `sampleOutputs/benchlingfastCloningPrimerInfo.csv`.

Again, you have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.\
(1) If you input the plasmid sequences as strings,

```
fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq, maxTempDiff=MAX_TEMP_DIFF, destinationAddress='fastCloningPrimerInfo.csv', benchlingAddress='benchlingfastCloningPrimerInfo.csv', benchling=True, primerOptTm=PRIMER_OPT_TM, primerMinTm=PRIMER_MIN_TM, primerMaxTm=PRIMER_MAX_TM, primerMinSize=PRIMER_MIN_SIZE)
# Note that maxTempDiff, destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq)
# If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature), primerMinTem(the lowest acceptable melting temperature for primers), primerMaxTm(the highest acceptable melting temperature for primers), and primerMinSize (shortest acceptable primer length) are a few primer 3 parameters that you can adjust

## TEST INPUTS:
## fastCloningPrimers(vectorPlasmidSeq1, insertPlasmidSeq1, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

(2) If you input the plasmid sequences as fasta/genbank files (please make sure two plasmid files have the same format),

```
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq, maxTempDiff=MAX_TEMP_DIFF, destinationAddress='fastCloningPrimerInfo.csv', benchlingAddress='benchlingfastCloningPrimerInfo.csv', benchling=True, primerOptTm=PRIMER_OPT_TM, primerMinTm=PRIMER_MIN_TM, primerMaxTm=PRIMER_MAX_TM, primerMinSize=PRIMER_MIN_SIZE):
# Note that maxTempDiff, destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq)
# If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature), primerMinTem(the lowest acceptable melting temperature for primers), primerMaxTm(the highest acceptable melting temperature for primers), and primerMinSize (shortest acceptable primer length) are a few primer 3 parameters that you can adjust

## TEST INPUTS:
## fastCloningPrimersFile(vectorPlasmid1AddressFA, insertPlasmid1AddressFA, vectorSeq1, insertSeq1)
## fastCloningPrimersFile(vectorPlasmid1AddressGB, insertPlasmid1AddressGB, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

#### New features in the 11/15/2020 Update

1. Allow the users to manually decide primer3 parameters 'primerOptTm (optimal primer temperature), primerMinTem(the lowest acceptable melting temperature for primers), primerMaxTm(the highest acceptable melting temperature for primers), and primerMinSize (shortest acceptable primer length)'.
2. Allow outputs that are in Benchling readable format. If users would like to import the primer outputs from this workflow to benchling, simply click on `import Oligo` on benchling and upload the benchling compatible outputs this workflow provides.

#### Next steps

Next release will include the following:

1. The current algorithm uses primer3 default melting temperature calculator for Taq polymerase, but in our case we will need it for Phusion. We will try to figure that out.
2. Double checking primer feasibility to demonstrate our workflow's robustness.
3. More explanations on the algorithm that recircularizes linearized plasmid DNA for primer3.

### Acknowledgement

Developers:\
Tom Fu [(@tommyfuu)](https://github.com/tommyfuu)\
Richard Chang [(@richanghmc)](https://github.com/richanghmc)

Affiliation: Harvey Mudd College BioMakerspace (Polymerspace). \
Faculty advisor: Dr. Dan Stoebel.

This project is part of the intellectual property of the [Harvey Mudd College BioMakerspace](https://biomakerspace.com/). Please notify the space at **tfu@g.hmc.edu** for consent before using any of the materials in this repository. Please cite us if you use our repository for academic sharing purposes.

The funding support of the Harvey Mudd College BioMakerspace comes from Harvey Mudd College Office of Community Engagement and the college's Shanahan Fund.
