# BioFoundry

BioFoundry Project at the HMC BioMakerspace. An automated workflow to design primers for fast cloning experiments.

### Next Steps

### Required libraries

1. Primer3-py (Download via terminal with `pip install primer3-py`)

### Usage

#### Installation

#### Primer design

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
