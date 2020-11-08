# BioFoundry

BioFoundry Project at the HMC BioMakerspace. An automated workflow to design primers for fast cloning experiments.

### Next Steps

### Required libraries

1. Primer3-py (Download via terminal with `pip install primer3-py`)

### Usage

#### Installation

#### Primer design

So far, we can design primers given a plasmid sequence and a goal sequence (the sequence encapsulated by the plasmid sequence, which is also the sequence that we want to isolate from the plasmid sequence).

For example:

```
from fastCloningPrimer import *
plasmidPrimerDesign(insertPlasmidSeq1, insertSeq1)
```

#### Next steps

Functions to write are

```
def cleanPrimerInfo(primerInfo):
    """read primerInfo, the output of the previous function, and turn it into a more
    readable and analyzable data structure"""
    return


def tempDiffRestrict(primerInfo):
    """TODO: For Richard Chang to write"""
    return


def vectorPrimerDesign(vectorPlasmidSeq, vectorSeq):
    """Find the primers isolating vectorSeq from vectorPlasmidSeq; meanwhile
    getting two overhang sequences that need to be attached to the insert primer
    pairs"""
    return


def insertPrimerDesign(overhangSeq1, overhangSeq2, insertPlasmidSeq, insertSeq):
    """Find the primers isolating insertSeq from insertPlasmidSeq; meanwhile attaching
    the two overhang sequences to the insert primer pairs"""
    return


def fastCloningPrimers(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq):
    """Wrapper function that generates 2 primer pairs for the given circular
    raw vector and insert sequences

    Args:
        vectorPlasmidSeq ([str]): [description]
        insertPlasmidSeq ([str]): [description]
        vectorSeq ([str]): [description]
        insertSeq ([str]): [description]
    """
    return
```

The ones that are easy to write are (For Richard):

1. cleanPrimerInfo(primerInfo)
2. tempDiffRestrict(primerInfo)

THE CONTENT BELOW WILL BE ENABLED ONCE THE WHOLE THING IS DONE:

```
from fastCloningPrimer import *
fastCloningPrimersSeq(vectorPlasmidSeq, insertPlasmidSeq, vectorSeq, insertSeq)
```

vectorPlasmidSeq: sequence of the plasmid containing the vector sequence\
insertPlasmidSeq: sequence of the plasmid containing the insert sequence\
vectorSeq: sequence of the vector\
insertSeq: sequence of the insert

```
from fastCloningPrimer import *
fastCloningPrimersIndex(vectorPlasmidSeq, insertPlasmidSeq, vectorIndexPair, insertIndexPair)
```

vectorPlasmidSeq: sequence of the plasmid containing the vector sequence\
insertPlasmidSeq: sequence of the plasmid containing the insert sequence\
vectorIndexPair: a tuple containing the starting and ending indexes of the vector in the vectorPlasmidSeq, with indexes starting from 1 (instead of 0)\
insertIndexPair: a tuple containing the starting and ending indexes of the insert in the insertPlasmidSeq, with indexes starting from 1 (instead of 0)

### Acknowledgement

Developers:\
Tom Fu [(@tommyfuu)](https://github.com/tommyfuu)\

Affiliation: Harvey Mudd College BioMakerspace (Polymerspace). \
Faculty advisor: Dr. Dan Stoebel.

This project is part of the intellectual property of the [Harvey Mudd College BioMakerspace](https://biomakerspace.com/). Please notify the space at **tfu@g.hmc.edu** for consent before using any of the materials in this repository. Please cite us if you use our repository for academic sharing purposes.

The funding support of the Harvey Mudd College BioMakerspace comes from Harvey Mudd College Office of Community Engagement and the college's Shanahan Fund.
