# BioFoundry

BioFoundry Project at the HMC BioMakerspace. An automated workflow to design primers for circularised DNA and for [FastCloning](https://bmcbiotechnol.biomedcentral.com/articles/10.1186/1472-6750-11-92) experiments. This workflow supports fasta and genbank DNA file format as well as string format for plasmid sequence inputting to allow better user experience. For designing FasctCloning Primers, we thank [NEB Tm Calculator](https://tmcalculator.neb.com/#!/batch) for making their primer melting/annealing temperature tools publicly available.

### Dependencies

Install dependencies with

```
pip install -r requirements.txt
```

In addition, you need to have a [Google Chrome browser](https://www.google.com/chrome/) installed on your device (preferrably a Macbook). Check the version of your Chrome browser by clicking on `Help>About Google Chrome`, then download the Chrome webdriver [here](https://chromedriver.chromium.org/) that corresponds to your own Chrome version. Move the Chrome webdriver you installed to the Biofoundry repository, and you should be ready to go.

If you would like to install them manually:

1. [Primer3-py](https://libnano.github.io/primer3-py/index.html) (Download via terminal with `pip install primer3-py`)
2. [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) (Download via terminal with `pip install pandas` or `conda install pandas`)
3. [selenium](https://selenium-python.readthedocs.io/installation.html) (Download via terminal with `pip install selenium`)

### Usage

#### Tutorial Video

[Here](https://drive.google.com/file/d/1XiwsN5Bmk_Z4w-_1xH6apJqvr7TNc6kV/view?usp=sharing) is a super short tutorial video for this repo, especially on how to corroborate the primers designed by the workflow. Note that Benchling crashed in the middle of the video ahaha :-)......

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

Alternatively, you can enter the following in the terminal:

'''
python3 -i fastCloningPrimer.py
'''

If you do not prefer to use ipython, you can instead directly do the following in the terminal:
(1) enter the Biofoundry directory, type `python` to enter python mode
(2) type `from fastCloningPrimer import *` to import all functions.

This repository enables two types of primer designs. You can either design primer pairs for PCR on a plasmid; or you can design primer pairs for [FastCloning](https://bmcbiotechnol.biomedcentral.com/articles/10.1186/1472-6750-11-92) experiments.

1. You can simply design primer3 primer pairs for PCR on a plasmid. The output will be a csv file. You can choose to output your primers in a benchling acceptable format or not. Check out the sample outputs for this part in files `sampleOutputs/plasmidPrimerInfo.csv` and `sampleOutputs/benchlingPlasmidPrimerInfo.csv`.

You have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.

(1) If you input the plasmid sequence as a string,

```
plasmidPrimers(plasmidSeq, goalSeq, benchling=True, destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv', primerOptTm=PRIMER_OPT_TM, primerMinSize=PRIMER_MIN_SIZE, enzyme="Taq", maxTempDiff=MAX_TEMP_DIFF)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq). The outputs can be found at the default addresses (destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv').
# Outputs friendly for Benchling will be automatically generated. If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature) and primerMinSize (shortest acceptable primer length) are the two primer3 parameters that you can adjust, along with the maxTempDiff, which is the maximum melting temperature difference between two primers in each primer pair.
# You can choose which enzyme you are using. Currently we support Taq polymerases OR NEB phusion polymerase. You can input that as either `enzyme="Taq"` or `enzyme="phusion"`.

## TEST INPUTS:
## plasmidPrimers(vectorPlasmidSeq1, vectorSeq1)
## plasmidPrimers(insertPlasmidSeq1, insertSeq1)
```

This gives you several primer pairs for isolating insertSeq1 from its plasmid insertPlasmidSeq1.

(2) If you input the plasmid sequence as a fasta/genbank file,

```
plasmidPrimers(plasmidSeqFile, goalSeq, benchling=True, destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv', primerOptTm=PRIMER_OPT_TM, primerMinSize=PRIMER_MIN_SIZE, enzyme="Taq", maxTempDiff=MAX_TEMP_DIFF)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq). The outputs can be found at the default addresses (destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv').
# Outputs friendly for Benchling will be automatically generated. If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature) and primerMinSize (shortest acceptable primer length) are the two primer3 parameters that you can adjust, along with the maxTempDiff, which is the maximum melting temperature difference between two primers in each primer pair.
# You can choose which enzyme you are using. Currently we support Taq polymerases OR NEB phusion polymerase. You can input that as either `enzyme="Taq"` or `enzyme="phusion"`.

## TEST INPUTS:
## plasmidPrimersFile(vectorPlasmid1AddressFA, vectorSeq1)
## plasmidPrimersFile(insertPlasmid1AddressGB, insertSeq1)
```

2. You can design primer3 primer pairs for your fastCloning experiments. Check out the sample outputs for this part in files `sampleOutputs/fastCloningPrimerInfo.csv` and `sampleOutputs/benchlingfastCloningPrimerInfo.csv`.

Again, you have two options. You can either input the plasmid sequence as a string or as a fasta/genbank file. Note that only fasta/genbank formats are supported for now.\
Note that the goal sequence (goalSeq), or the sequence you would like to isolate from the plasmid, always needs to be inputted as a string.\
(1) If you input the plasmid sequences as strings,

```
fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq, maxTempDiff=MAX_TEMP_DIFF, destinationAddress='fastCloningPrimerInfo.csv', benchlingAddress='benchlingfastCloningPrimerInfo.csv', benchling=True, primerOptTm=PRIMER_OPT_TM, primerMinSize=PRIMER_MIN_SIZE)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq). The outputs can be found at the default addresses (destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv').
# Outputs friendly for Benchling will be automatically generated. If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature) and primerMinSize (shortest acceptable primer length) are the two primer3 parameters that you can adjust, along with the maxTempDiff, which is the maximum melting temperature difference between two primers in each primer pair.
# You can choose which enzyme you are using. Currently we support Taq polymerases OR NEB phusion polymerase. You can input that as either `enzyme="Taq"` or `enzyme="phusion"`.

## TEST INPUTS:
## fastCloningPrimers(vectorPlasmidSeq1, insertPlasmidSeq1, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

(2) If you input the plasmid sequences as fasta/genbank files (please make sure two plasmid files have the same format),

```
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq, maxTempDiff=MAX_TEMP_DIFF, destinationAddress='fastCloningPrimerInfo.csv', benchlingAddress='benchlingfastCloningPrimerInfo.csv', benchling=True, primerOptTm=PRIMER_OPT_TM, primerMinSize=PRIMER_MIN_SIZE)
# Note that destinationAddress, benchlingAddress, and benchling are unnecessary.  You can choose to change the input. If you choose not to, you can simply do the following:
fastCloningPrimersFile(vectorPlasmidAddress, insertPlasmidAddress, vectorSeq, insertSeq). The outputs can be found at the default addresses (destinationAddress='plasmidPrimerInfo.csv', benchlingAddress='benchlingPlasmidPrimerInfo.csv').
# Outputs friendly for Benchling will be automatically generated. If you prefer to not output benchling format files, please set the benchling boolean to False.
# primerOptTm (optimal primer temperature) and primerMinSize (shortest acceptable primer length) are the two primer3 parameters that you can adjust, along with the maxTempDiff, which is the maximum melting temperature difference between two primers in each primer pair.
# You can choose which enzyme you are using. Currently we support Taq polymerases OR NEB phusion polymerase. You can input that as either `enzyme="Taq"` or `enzyme="phusion"`.

## TEST INPUTS:
## fastCloningPrimersFile(vectorPlasmid1AddressFA, insertPlasmid1AddressFA, vectorSeq1, insertSeq1)
## fastCloningPrimersFile(vectorPlasmid1AddressGB, insertPlasmid1AddressGB, vectorSeq1, insertSeq1)
```

Check out your destinationAddress for your primers.

#### Uploading your primers to Benchling

#### New features in the 11/15/2020 Update

1. Allow the primer design with phusion for plasmid primer designs and fastCloning primers design, using [Serenium](https://selenium-python.readthedocs.io/installation.html) webscraping of the [NEB Tm Calculator](https://tmcalculator.neb.com/#!/batch).
2. Allow the users to manually decide primer3 parameters 'primerOptTm (optimal primer temperature) and primerMinSize (shortest acceptable primer length)'.
3. Allow outputs that are in Benchling readable format. If users would like to import the primer outputs from this workflow to benchling, simply click on `import Oligo` on benchling. Copy paste the primer information in your benchling-compatible output files and paste them into the textbox in benchling.

#### Next steps

Next release and updates will be announced here.

1. Enable the support for more operating systems.
2. Enable the support for more browsers.

### Acknowledgement

Developers:\
Tom Fu [(@tommyfuu)](https://github.com/tommyfuu)\
Richard Chang [(@richanghmc)](https://github.com/richanghmc)

Affiliation: Harvey Mudd College BioMakerspace (Polymerspace). \
Faculty advisor: Dr. Dan Stoebel.

This project is part of the intellectual property of the [Harvey Mudd College BioMakerspace](https://biomakerspace.com/). Please notify the space at **tfu@g.hmc.edu** for consent before using any of the materials in this repository. Please cite us if you use our repository for academic sharing purposes.

The funding support of the Harvey Mudd College BioMakerspace comes from Harvey Mudd College Office of Community Engagement and the college's Shanahan Fund.

We also thank [Zhengyao Lin](https://github.com/rod-lin) for his assistance on the web scraping part of the project.
