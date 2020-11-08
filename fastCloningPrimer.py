# -*- coding: utf-8 -*-

"""
Author      : Tom Fu
Date        : 2020 Nov 7
FileName    : fastCloningPrimer.py (for the BioFoundry Project at the HMC BioMakerspace)
Description : Find primer pairs for fast cloning
"""
import primer3
import pandas as pd

# test cases
primer3pySeq = 'GCTTGCATGCCTGCAGGTCGACTCTAGAGGATCCCCCTACATTTTAGCATCAGTGAGTACAGCATGCTTACTGGAAGAGAGGGTCATGCAACAGATTAGGAGGTAAGTTTGCAAAGGCAGGCTAAGGAGGAGACGCACTGAATGCCATGGTAAGAACTCTGGACATAAAAATATTGGAAGTTGTTGAGCAAGTNAAAAAAATGTTTGGAAGTGTTACTTTAGCAATGGCAAGAATGATAGTATGGAATAGATTGGCAGAATGAAGGCAAAATGATTAGACATATTGCATTAAGGTAAAAAATGATAACTGAAGAATTATGTGCCACACTTATTAATAAGAAAGAATATGTGAACCTTGCAGATGTTTCCCTCTAGTAG'


vectorPlasmidSeq1 = 'TTCGAGCTCGGTACCGGATCCGTCGACCTGCAGCCAAGCTTAATTAGCTGAGCTTGGACTCCTGTTGATAGATCCAGTAATGACCTCAGAACTCCATCTGGATTTGTTCAGAACGCTCGGTTGCCGCCGGGCGTTTTTTATTGGTGAGAATCCAAGCTAGCTTGGCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTTCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTTTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGGGTAATGACTCTCTAGCTTGAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCCTCTAGCAGCCCGGGCTGCggccgcTATTTCTCCTTTCGCGCAGTACGTGGTTCGCGGCTTAATCCTGCTGGCAGCGGTGATCTTCGACCGTTACAAGCAAAAAGCGAAACGCACTGTCTGATGCTTTTTTCTGCAACAATTTAGCGTTTTTTCCCACCATAGCCAACCGCCATAACGGTTGGCTGTTCTTCGTTGCAAATGGCGACCCCCGTCACACTGTCTATACTTACATGTCTGTAAAGCGCGTTCTGCGCAACACAATAAGAAAAGAGAAGGAGGAGAACCGGgtgACAGAACCGTTAACCGAAACCCCTGAACTATCCGCGAAATATGCCTGGTTTTTTGATCTTGATGGAACGCTGGCGGAAATCAAACCGCATCCCGATCAGGTCGTCGTGCCTGACAATATTCTGCAAGGACTACAGCTACTGGCAACCGCAAGTGATGGTGCATTGGCATTGATATCAGGGCGCTCAATGGTGGAGCTTGACGCACTGGCAAAACCTTATCGCTTCCCGTtCTAGATTTAAGAAGGAGATATACATATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCTACATACGGAAAGCTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTGACCTATGGTGTTCAATGCTTTTCCCGTTATCCGGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAACGCACTATATCTTTCAAAGATGACGGGAACTACAAGACGCGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATCGTATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTCGGACACAAACTCGAGTACAACTATAACTCACACAATGTATACATCACGGCAGACAAACAAAAGAATGGAATCAAAGCTAACTTCAAAATTCGCCACAACATTGAAGATGGATCCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCGACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGCGTGACCACATGGTCCTTCTTGAGTTTGTAACTGCTGCTGGGATTACACATGGCATGGATGAGCTCTACAAATAATGAATTCCAGCTGAGCGCCGGTCGCTACCATTACCAGTTGGTCTGGTGTCAAAAATAATAATAACCGGGCAGGCCATGTCTGCCCGTATTTCGCGTAAGGAAATCCATTATGTACTATTTAATTCTTGAAGACGAAAGGGCCTCGTGATACGCCTATTTTTATAGGTTAATGTCATGATAATAATGGTTTCTTAGACGTCAGGTGGCGATATCGGGCTAGCCGGCCCGACGCACTTTGCGCCGAATAAATACCTGTGACGGAAGATCACTTCGCAGAATAAATAAATCCTGGTGTCCCTGTTGATACCGGGAAGCCCTGGGCCAACTTTTGGCGAAAATGAGACGTTGATCGGCACGTAAGAGGTTCCAACTTTCACCATAATGAAATAAGATCACTACCGGGCGTATTTTTTGAGTTATCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTCCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTCTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGTGCTACGCCTGAATAAGTGATAATAAGCGGATGAATGGCAGAAATGACGGATATCGTCCATTCCGACAGCATCGCCAGTCACTATGGCGTGCTGCTAGCGCTTTTAGCCGCTTTAGCGGCCTTTCCCCCTACCCGAAGGGTGGGGGCGCGTGTGCAGCCCCGCAGGGCCTGTCTCGGTCGATCATTCAGCCCGGCTCATCCTTCTGGCGTGGCGGCAGACCGAACAAGGCGCGGTCGTGGTCGCGTTCAAGGTACGCATCCATTGCCGCCATGAGCCGATCCTCCGGCCACTCGCTGCTGTTCACCTTGGCCAAAATCATGGCCCCCACCAGCACCTTGCGCCTTGTTTCGTTCTTGCGCTCTTGCTGCTGTTCCCTTGCCCGCACCCGCTGAATTTCGGCATTGATTCGCGCTCGTTGTTCTTCGAGCTTGGCCAGCCGATCCGCCGCCTTGTTGCTCCCCTTAACCATCTTGACACCCCATTGTTAATGTGCTGTCTCGTAGGCTATCATGGAGGCACAGCGGCGGCAATCCCGACCCTACTTTGTAGGGGAGGGCGCACTTACCGGTTTCTCTTCGAGAAACTGGCCTAACGGCCACCCTTCGGGCGGTGCGCTCTCCGAGGGCCATTGCATGGAGCCGAAAAGCAAAAGCAACAGCGAGGCAGCATGGCGATTTATCACCTTACGGCGAAAACCGGCAGCAGGTCGGGCGGCCAATCGGCCAGGGCCAAGGCCGACTACATCCAGCGCGAAGGCAAGTATGCCCGCGACATGGATGAAGTCTTGCACGCCGAATCCGGGCACATGCCGGAGTTCGTCGAGCGGCCCGCCGACTACTGGGATGCTGCCGACCTGTATGAACGCGCCAATGGGCGGCTGTTCAAGGAGGTCGAATTTGCCCTGCCGGTCGAGCTGACCCTCGACCAGCAGAAGGCGCTGGCGTCCGAGTTCGCCCAGCACCTGACCGGTGCCGAGCGCCTGCCGTATACGCTGGCCATCCATGCCGGTGGCGGCGAGAACCCGCACTGCCACCTGATGATCTCCGAGCGGATCAATGACGGCATCGAGCGGCCCGCCGCTCAGTGGTTCAAGCGGTACAACGGCAAGACCCCGGAGAAGGGCGGGGCACAGAAGACCGAAGCGCTCAAGCCCAAGGCATGGCTTGAGCAGACCCGCGAGGCATGGGCCGACCATGCCAACCGGGCATTAGAGCGGGCTGGCCACGACGCCCGCATTGACCACAGAACACTTGAGGCGCAGGGCATCGAGCGCCTGCCCGGTGTTCACCTGGGGCCGAACGTGGTGGAGATGGAAGGCCGGGGCATCCGCACCGACCGGGCAGACGTGGCCCTGAACATCGACACCGCCAACGCCCAGATCATCGACTTACAGGAATACCGGGAGGCAATAGACCATGAACGCAATCGACAGAGTGAAGAAATCCAGAGGCATCAACGAGTTAGCGGAGCAGATCGAACCGCTGGCCCAGAGCATGGCGACACTGGCCGACGAAGCCCGGCAGGTCATGAGCCAGACCCAGCAGGCCAGCGAGGCGCAGGCGGCGGAGTGGCTGAAAGCCCAGCGCCAGACAGGGGCGGCATGGGTGGAGCTGGCCAAAGAGTTGCGGGAGGTAGCCGCCGAGGTGAGCAGCGCCGCGCAGAGCGCCCGGAGCGCGTCGCGGGGGTGGCACTGGAAGCTATGGCTAACCGTGATGCTGGCTTCCATGATGCCTACGGTGGTGCTGCTGATCGCATCGTTGCTCTTGCTCGACCTGACGCCACTGACAACCGAGGACGGCTCGATCTGGCTGCGCTTGGTGGCCCGATGAAGAACGACAGGACTTTGCAGGCCATAGGCCGACAGCTCAAGGCCATGGGCTGTGAGCGCTCTTCCGCTTCCTCGCTCACTGACTCGCTGCGCTCGGTCGTTCGGCTGCGGCGAGCGGTATCAGCTCACTCAAAGGCGGTAATACGGTTATCCACAGAATCAGGGGATAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCATAGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTGCACGAACCCCCCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCAACCCGGTAAGACACGACTTATCGCCACTGGCAGCAGCCACTGGTAACAGGATTAGCAGAGCGAGGTATGTAGGCGGTGCTACAGAGTTCTTGAAGTGGTGGCCTAACTACGGCTACACTAGAAGGACAGTATTTGGTATCTGCGCTCTGCTGAAGCCAGTTACCTTCGGAAAAAGAGTTGGTAGCTCTTGATCCGGCAAACAAACCACCGCTGGTAGCGGTGGTTTTTTTGTTTGCAAGCAGCAGATTACGCGCAGAAAAAAAGGATCTCAAGAAGATCCTTTGATCTTTTCTACGGGGTCTGACGCTCAGTGGAACGAAAACTCACGTTAAGGGATTTTGGTCATGAGATTATCAAAAAGGATCTTCACCTAGATCCTTTTAAATTAAAAATGAAGTTTTAAATCAATCTAAAGTATATATGAGTAAACTTGGTCTGACAGTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATACGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGAAGGGCCGAGCGCAGAAGTGGTCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTGCAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGTCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTAAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAACACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGAAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATACTCTTCCTTTTTCAATATTATTGAAGCATTTATCAGGGTTATTGTCTCATGAGCGGATACATATTTGAATGTATTTAGAAAAATAAACAAATAGGGGTTCCGCGCACATTTCCCCGAAAAGTGCCACCTGACGTCTAAGAAACCATTATTATCATGACATTAACCTATAAAAATAGGCGTATCACGAGGCCCTTTCGTCTTCAAGAA'
insertPlasmidSeq1 = 'GCTAAAGTTGGATACTTAAGAAATGCTTCATAATTCAGTAAGGCATTAGCATAATGGAAATAAAAGTGCAGAGACTATCTCTATGGATGATTAATACTGTCTTTTTATTGTCACCCATAAATAATCACCAGACTAATACTATCAACTTGATATTTGAAATGTGATCACTTGACTTTTGATACGTTATTTTATAACGGTTAACATATTTATAAAAACAACGGCCGTGCCACACGTCCGTTTCAATACTTAACGCACATGTATTTTGGTTTAGTCATCATCCGGTTATATGTATTTTAGCCAGGAACAGGTTAAATCATTCCTATATAACTCAAAAATTGAAACCTTATTCTCATGTCATGCTTATATTCATTATTATCGTTATATAAAAAGGCAACCATAATGTTTAGCAAATTGGCACAAAGTAGCATAAAGGCTATGTTTTAATTACAGGATGTTCAGTCATTTGAATGTATAACATTATAGCTAAACAAATCTAAAACGAAGTCAATAATTTATTGCTTTCACAAAATCTCATTTTGTTTAACATCCATTGAGATTCCTTGCTTTAAATTTTATTTTATATAAGCCATCATTTTAATTAATTTATTTTTTTGAGGGGGGGGTAATATACTCATATGCAAAATCAAGAAATAAACATCCTAATGAACCATATTAAATACCGTGGGATAAGACATAACAAatgAAGTGGATAGTAATTGACACGGTAATTCAACCTACATGTGGTATATCTTTTTCAGCCATATGGGGTAATATGAAAATGATCATCTGGTATCAATCTACTATATTTCTCCCTCCTGGCAGTATATTTACACCGGTTAAGTCTGGTATTATCCTTAAGGATAAAGAATATCCTATTACTATTTATCACATCGCACCATTCAACAAGGATTTATGGAGTTTACTCAAAAGCAGTCAAGAGTGTCCTCCAGGAGAAAGCAAAATAACAAATAAATGTTTACATAATAGTTGCATTATAAAAATATGCCCATATGGGCTCAAGtaa'
vectorSeq1 = 'CTAGATTTAAGAAGGAGATATACATATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCTACATACGGAAAGCTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTGACCTATGGTGTTCAATGCTTTTCCCGTTATCCGGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAACGCACTATATCTTTCAAAGATGACGGGAACTACAAGACGCGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATCGTATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTCGGACACAAACTCGAGTACAACTATAACTCACACAATGTATACATCACGGCAGACAAACAAAAGAATGGAATCAAAGCTAACTTCAAAATTCGCCACAACATTGAAGATGGATCCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCGACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGCGTGACCACATGGTCCTTCTTGAGTTTGTAACTGCTGCTGGGATTACACATGGCATGGATGAGCTCTACAAATAATGAATTCCAGCTGAGCGCCGGTCGCTACCATTACCAGTTGGTCTGGTGTCAAAAATAATAATAACCGGGCAGGCCATGTCTGCCCGTATTTCGCGTAAGGAAATCCATTATGTACTATTTAATTCTTGAAGACGAAAGGGCCTCGTGATACGCCTATTTTTATAGGTTAATGTCATGATAATAATGGTTTCTTAGACGTCAGGTGGCGATATCGGGCTAGCCGGCCCGACGCACTTTGCGCCGAATAAATACCTGTGACGGAAGATCACTTCGCAGAATAAATAAATCCTGGTGTCCCTGTTGATACCGGGAAGCCCTGGGCCAACTTTTGGCGAAAATGAGACGTTGATCGGCACGTAAGAGGTTCCAACTTTCACCATAATGAAATAAGATCACTACCGGGCGTATTTTTTGAGTTATCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTCCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTCTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGTGCTACGCCTGAATAAGTGATAATAAGCGGATGAATGGCAGAAATGACGGATATCGTCCATTCCGACAGCATCGCCAGTCACTATGGCGTGCTGCTAGCGCTTTTAGCCGCTTTAGCGGCCTTTCCCCCTACCCGAAGGGTGGGGGCGCGTGTGCAGCCCCGCAGGGCCTGTCTCGGTCGATCATTCAGCCCGGCTCATCCTTCTGGCGTGGCGGCAGACCGAACAAGGCGCGGTCGTGGTCGCGTTCAAGGTACGCATCCATTGCCGCCATGAGCCGATCCTCCGGCCACTCGCTGCTGTTCACCTTGGCCAAAATCATGGCCCCCACCAGCACCTTGCGCCTTGTTTCGTTCTTGCGCTCTTGCTGCTGTTCCCTTGCCCGCACCCGCTGAATTTCGGCATTGATTCGCGCTCGTTGTTCTTCGAGCTTGGCCAGCCGATCCGCCGCCTTGTTGCTCCCCTTAACCATCTTGACACCCCATTGTTAATGTGCTGTCTCGTAGGCTATCATGGAGGCACAGCGGCGGCAATCCCGACCCTACTTTGTAGGGGAGGGCGCACTTACCGGTTTCTCTTCGAGAAACTGGCCTAACGGCCACCCTTCGGGCGGTGCGCTCTCCGAGGGCCATTGCATGGAGCCGAAAAGCAAAAGCAACAGCGAGGCAGCATGGCGATTTATCACCTTACGGCGAAAACCGGCAGCAGGTCGGGCGGCCAATCGGCCAGGGCCAAGGCCGACTACATCCAGCGCGAAGGCAAGTATGCCCGCGACATGGATGAAGTCTTGCACGCCGAATCCGGGCACATGCCGGAGTTCGTCGAGCGGCCCGCCGACTACTGGGATGCTGCCGACCTGTATGAACGCGCCAATGGGCGGCTGTTCAAGGAGGTCGAATTTGCCCTGCCGGTCGAGCTGACCCTCGACCAGCAGAAGGCGCTGGCGTCCGAGTTCGCCCAGCACCTGACCGGTGCCGAGCGCCTGCCGTATACGCTGGCCATCCATGCCGGTGGCGGCGAGAACCCGCACTGCCACCTGATGATCTCCGAGCGGATCAATGACGGCATCGAGCGGCCCGCCGCTCAGTGGTTCAAGCGGTACAACGGCAAGACCCCGGAGAAGGGCGGGGCACAGAAGACCGAAGCGCTCAAGCCCAAGGCATGGCTTGAGCAGACCCGCGAGGCATGGGCCGACCATGCCAACCGGGCATTAGAGCGGGCTGGCCACGACGCCCGCATTGACCACAGAACACTTGAGGCGCAGGGCATCGAGCGCCTGCCCGGTGTTCACCTGGGGCCGAACGTGGTGGAGATGGAAGGCCGGGGCATCCGCACCGACCGGGCAGACGTGGCCCTGAACATCGACACCGCCAACGCCCAGATCATCGACTTACAGGAATACCGGGAGGCAATAGACCATGAACGCAATCGACAGAGTGAAGAAATCCAGAGGCATCAACGAGTTAGCGGAGCAGATCGAACCGCTGGCCCAGAGCATGGCGACACTGGCCGACGAAGCCCGGCAGGTCATGAGCCAGACCCAGCAGGCCAGCGAGGCGCAGGCGGCGGAGTGGCTGAAAGCCCAGCGCCAGACAGGGGCGGCATGGGTGGAGCTGGCCAAAGAGTTGCGGGAGGTAGCCGCCGAGGTGAGCAGCGCCGCGCAGAGCGCCCGGAGCGCGTCGCGGGGGTGGCACTGGAAGCTATGGCTAACCGTGATGCTGGCTTCCATGATGCCTACGGTGGTGCTGCTGATCGCATCGTTGCTCTTGCTCGACCTGACGCCACTGACAACCGAGGACGGCTCGATCTGGCTGCGCTTGGTGGCCCGATGAAGAACGACAGGACTTTGCAGGCCATAGGCCGACAGCTCAAGGCCATGGGCTGTGAGCGCTCTTCCGCTTCCTCGCTCACTGACTCGCTGCGCTCGGTCGTTCGGCTGCGGCGAGCGGTATCAGCTCACTCAAAGGCGGTAATACGGTTATCCACAGAATCAGGGGATAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCATAGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTGCACGAACCCCCCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCAACCCGGTAAGACACGACTTATCGCCACTGGCAGCAGCCACTGGTAACAGGATTAGCAGAGCGAGGTATGTAGGCGGTGCTACAGAGTTCTTGAAGTGGTGGCCTAACTACGGCTACACTAGAAGGACAGTATTTGGTATCTGCGCTCTGCTGAAGCCAGTTACCTTCGGAAAAAGAGTTGGTAGCTCTTGATCCGGCAAACAAACCACCGCTGGTAGCGGTGGTTTTTTTGTTTGCAAGCAGCAGATTACGCGCAGAAAAAAAGGATCTCAAGAAGATCCTTTGATCTTTTCTACGGGGTCTGACGCTCAGTGGAACGAAAACTCACGTTAAGGGATTTTGGTCATGAGATTATCAAAAAGGATCTTCACCTAGATCCTTTTAAATTAAAAATGAAGTTTTAAATCAATCTAAAGTATATATGAGTAAACTTGGTCTGACAGTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATACGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGAAGGGCCGAGCGCAGAAGTGGTCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTGCAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGTCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTAAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAACACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGAAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATACTCTTCCTTTTTCAATATTATTGAAGCATTTATCAGGGTTATTGTCTCATGAGCGGATACATATTTGAATGTATTTAGAAAAATAAACAAATAGGGGTTCCGCGCACATTTCCCCGAAAAGTGCCACCTGACGTCTAAGAAACCATTATTATCATGACATTAACCTATAAAAATAGGCGTATCACGAGGCCCTTTCGTCTTCAAGAATTCGAGCTCGGTACCGGATCCGTCGACCTGCAGCCAAGCTTAATTAGCTGAGCTTGGACTCCTGTTGATAGATCCAGTAATGACCTCAGAACTCCATCTGGATTTGTTCAGAACGCTCGGTTGCCGCCGGGCGTTTTTTATTGGTGAGAATCCAAGCTAGCTTGGCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTTCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTTTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGGGTAATGACTCTCTAGCTTGAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCCTCTAGCAGCCCGGGCTGC'
insertSeq1 = 'TCACTTGACTTTTGATACGTTATTTTATAACGGTTAACATATTTATAAAAACAACGGCCGTGCCACACGTCCGTTTCAATACTTAACGCACATGTATTTTGGTTTAGTCATCATCCGGTTATATGTATTTTAGCCAGGAACAGGTTAAATCATTCCTATATAACTCAAAAATTGAAACCTTATTCTCATGTCATGCTTATATTCATTATTATCGTTATATAAAAAGGCAACCATAATGTTTAGCAAATTGGCACAAAGTAGCATAAAGGCTATGTTTTAATTACAGGATGTTCAGTCATTTGAATGTATAACATTATAGCTAAACAAATCTAAAACGAAGTCAATAATTTATTGCTTTCACAAAATCTCATTTTGTTTAACATCCATTGAGATTCCTTGCTTTAAATTTTATTTTATATAAGCCATCATTTTAATTAATTTATTTTTTTGAGGGGGGGGTAATATACTCATATGCAAAATCAAGAAATAAACATCCTAATGAACCATATTAAATACCGTGGGATAAGACATAACAA'

testOutput1 = 'ggccgcTATTTCTCCTTTCGCGCAGTACGTGGTTCGCGGCTTAATCCTGCTGGCAGCGGTGATCTTCGACCGTTACAAGCAAAAAGCGAAACGCACTGTCTGATGCTTTTTTCTGCAACAATTTAGCGTTTTTTCCCACCATAGCCAACCGCCATAACGGTTGGCTGTTCTTCGTTGCAAATGGCGACCCCCGTCACACTGTCTATACTTACATGTCTGTAAAGCGCGTTCTGCGCAACACAATAAGAAAACTAGATTTAAGAAGGAGATATACATATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCTACATACGGAAAGCTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTGACCTATGGTGTTCAATGCTTTTCCCGTTATCCGGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAACGCACTATATCTTTCAAAGATGACGGGAACTACAAGACGCGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATCGTATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTCGGACACAAACTCGAGTACAACTATAACTCACACAATGTATACATCACGGCAGACAAACAAAAGAATGGAATCAAAGCTAACTTCAAAATTCGCCACAACATTGAAGATGGATCCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCGACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGCGTGACCACATGGTCCTTCTTGAGTTTGTAACTGCTGCTGGGATTACACATGGCATGGATGAGCTCTACAAATAATGAATTCCAGCTGAGCGCCGGTCGCTACCATTACCAGTTGGTCTGGTGTCAAAAATAATAATAACCGGGCAGGCCATGTCTGCCCGTATTTCGCGTAAGGAAATCCATTATGTACTATTTAATTCTTGAAGACGAAAGGGCCTCGTGATACGCCTATTTTTATAGGTTAATGTCATGATAATAATGGTTTCTTAGACGTCAGGTGGCGATATCGGGCTAGCCGGCCCGACGCACTTTGCGCCGAATAAATACCTGTGACGGAAGATCACTTCGCAGAATAAATAAATCCTGGTGTCCCTGTTGATACCGGGAAGCCCTGGGCCAACTTTTGGCGAAAATGAGACGTTGATCGGCACGTAAGAGGTTCCAACTTTCACCATAATGAAATAAGATCACTACCGGGCGTATTTTTTGAGTTATCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTCCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTCTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGTGCTACGCCTGAATAAGTGATAATAAGCGGATGAATGGCAGAAATGACGGATATCGTCCATTCCGACAGCATCGCCAGTCACTATGGCGTGCTGCTAGCGCTTTTAGCCGCTTTAGCGGCCTTTCCCCCTACCCGAAGGGTGGGGGCGCGTGTGCAGCCCCGCAGGGCCTGTCTCGGTCGATCATTCAGCCCGGCTCATCCTTCTGGCGTGGCGGCAGACCGAACAAGGCGCGGTCGTGGTCGCGTTCAAGGTACGCATCCATTGCCGCCATGAGCCGATCCTCCGGCCACTCGCTGCTGTTCACCTTGGCCAAAATCATGGCCCCCACCAGCACCTTGCGCCTTGTTTCGTTCTTGCGCTCTTGCTGCTGTTCCCTTGCCCGCACCCGCTGAATTTCGGCATTGATTCGCGCTCGTTGTTCTTCGAGCTTGGCCAGCCGATCCGCCGCCTTGTTGCTCCCCTTAACCATCTTGACACCCCATTGTTAATGTGCTGTCTCGTAGGCTATCATGGAGGCACAGCGGCGGCAATCCCGACCCTACTTTGTAGGGGAGGGCGCACTTACCGGTTTCTCTTCGAGAAACTGGCCTAACGGCCACCCTTCGGGCGGTGCGCTCTCCGAGGGCCATTGCATGGAGCCGAAAAGCAAAAGCAACAGCGAGGCAGCATGGCGATTTATCACCTTACGGCGAAAACCGGCAGCAGGTCGGGCGGCCAATCGGCCAGGGCCAAGGCCGACTACATCCAGCGCGAAGGCAAGTATGCCCGCGACATGGATGAAGTCTTGCACGCCGAATCCGGGCACATGCCGGAGTTCGTCGAGCGGCCCGCCGACTACTGGGATGCTGCCGACCTGTATGAACGCGCCAATGGGCGGCTGTTCAAGGAGGTCGAATTTGCCCTGCCGGTCGAGCTGACCCTCGACCAGCAGAAGGCGCTGGCGTCCGAGTTCGCCCAGCACCTGACCGGTGCCGAGCGCCTGCCGTATACGCTGGCCATCCATGCCGGTGGCGGCGAGAACCCGCACTGCCACCTGATGATCTCCGAGCGGATCAATGACGGCATCGAGCGGCCCGCCGCTCAGTGGTTCAAGCGGTACAACGGCAAGACCCCGGAGAAGGGCGGGGCACAGAAGACCGAAGCGCTCAAGCCCAAGGCATGGCTTGAGCAGACCCGCGAGGCATGGGCCGACCATGCCAACCGGGCATTAGAGCGGGCTGGCCACGACGCCCGCATTGACCACAGAACACTTGAGGCGCAGGGCATCGAGCGCCTGCCCGGTGTTCACCTGGGGCCGAACGTGGTGGAGATGGAAGGCCGGGGCATCCGCACCGACCGGGCAGACGTGGCCCTGAACATCGACACCGCCAACGCCCAGATCATCGACTTACAGGAATACCGGGAGGCAATAGACCATGAACGCAATCGACAGAGTGAAGAAATCCAGAGGCATCAACGAGTTAGCGGAGCAGATCGAACCGCTGGCCCAGAGCATGGCGACACTGGCCGACGAAGCCCGGCAGGTCATGAGCCAGACCCAGCAGGCCAGCGAGGCGCAGGCGGCGGAGTGGCTGAAAGCCCAGCGCCAGACAGGGGCGGCATGGGTGGAGCTGGCCAAAGAGTTGCGGGAGGTAGCCGCCGAGGTGAGCAGCGCCGCGCAGAGCGCCCGGAGCGCGTCGCGGGGGTGGCACTGGAAGCTATGGCTAACCGTGATGCTGGCTTCCATGATGCCTACGGTGGTGCTGCTGATCGCATCGTTGCTCTTGCTCGACCTGACGCCACTGACAACCGAGGACGGCTCGATCTGGCTGCGCTTGGTGGCCCGATGAAGAACGACAGGACTTTGCAGGCCATAGGCCGACAGCTCAAGGCCATGGGCTGTGAGCGCTCTTCCGCTTCCTCGCTCACTGACTCGCTGCGCTCGGTCGTTCGGCTGCGGCGAGCGGTATCAGCTCACTCAAAGGCGGTAATACGGTTATCCACAGAATCAGGGGATAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCATAGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTGCACGAACCCCCCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCAACCCGGTAAGACACGACTTATCGCCACTGGCAGCAGCCACTGGTAACAGGATTAGCAGAGCGAGGTATGTAGGCGGTGCTACAGAGTTCTTGAAGTGGTGGCCTAACTACGGCTACACTAGAAGGACAGTATTTGGTATCTGCGCTCTGCTGAAGCCAGTTACCTTCGGAAAAAGAGTTGGTAGCTCTTGATCCGGCAAACAAACCACCGCTGGTAGCGGTGGTTTTTTTGTTTGCAAGCAGCAGATTACGCGCAGAAAAAAAGGATCTCAAGAAGATCCTTTGATCTTTTCTACGGGGTCTGACGCTCAGTGGAACGAAAACTCACGTTAAGGGATTTTGGTCATGAGATTATCAAAAAGGATCTTCACCTAGATCCTTTTAAATTAAAAATGAAGTTTTAAATCAATCTAAAGTATATATGAGTAAACTTGGTCTGACAGTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATACGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGAAGGGCCGAGCGCAGAAGTGGTCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTGCAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGTCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTAAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAACACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGAAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATACTCTTCCTTTTTCAATATTATTGAAGCATTTATCAGGGTTATTGTCTCATGAGCGGATACATATTTGAATGTATTTAGAAAAATAAACAAATAGGGGTTCCGCGCACATTTCCCCGAAAAGTGCCACCTGACGTCTAAGAAACCATTATTATCATGACATTAACCTATAAAAATAGGCGTATCACGAGGCCCTTTCGTCTTCAAGAATTCGAGCTCGGTACCGGATCCGTCGACCTGCAGCCAAGCTTAATTAGCTGAGCTTGGACTCCTGTTGATAGATCCAGTAATGACCTCAGAACTCCATCTGGATTTGTTCAGAACGCTCGGTTGCCGCCGGGCGTTTTTTATTGGTGAGAATCCAAGCTAGCTTGGCGAGATTTTCAGGAGCTAAGGAAGCTAAAATGGAGAAAAAAATCACTGGATATACCACCGTTGATATATCCCAATGGCATCGTAAAGAACATTTTGAGGCATTTCAGTCAGTTGCTCAATGTACCTATAACCAGACCGTTCAGCTGGATATTACGGCCTTTTTAAAGACCGTAAAGAAAAATAAGCACAAGTTTTATCCGGCCTTTATTCACATTCTTGCCCGCCTGATGAATGCTCATCCGGAATTTCGTATGGCAATGAAAGACGGTGAGCTGGTGATATGGGATAGTGTTCACCCTTGTTACACCGTTTTCCATGAGCAAACTGAAACGTTTTCATCGCTCTGGAGTGAATACCACGACGATTTCCGGCAGTTTCTACACATATATTCGCAAGATGTGGCGTGTTACGGTGAAAACCTGGCCTATTTCCCTAAAGGGTTTATTGAGAATATGTTTTTCGTCTCAGCCAATCCCTGGGTGAGTTTCACCAGTTTTGATTTAAACGTGGCCAATATGGACAACTTCTTCGCCCCCGTTTTCACCATGGGCAAATATTATACGCAAGGCGACAAGGTGCTGATGCCGCTGGCGATTCAGGTTCATCATGCCGTTTGTGATGGCTTCCATGTCGGCAGAATGCTTAATGAATTACAACAGTACTGCGATGAGTGGCAGGGCGGGGCGTAATTTTTTTAAGGCAGTTATTGGTGCCCTTAAACGCCTGGGGTAATGACTCTCTAGCTTGAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCCTCTAGCAGCCCGGGCTGCGAGAAGGAGGAGAACCGGgtgACAGAACCGTTAACCGAAACCCCTGAACTATCCGCGAAATATGCCTGGTTTTTTGATCTTGATGGAACGCTGGCGGAAATCAAACCGCATCCCGATCAGGTCGTCGTGCCTGACAATATTCTGCAAGGACTACAGCTACTGGCAACCGCAAGTGATGGTGCATTGGCATTGATATCAGGGCGCTCAATGGTGGAGCTTGACGCACTGGCAAAACCTTATCGCTTCCCGTt'

# default params (copied from primer3 with subtle changes according to our first primer designed)
SEQUENCE_ID = 'MH1000'
PRIMER_OPT_TM = 60.0
PRIMER_MIN_TM = 57.0
PRIMER_MAX_TM = 63.0
PRIMER_PRODUCT_SIZE_RANGE = [[100, 300], [150, 250], [301, 400], [
    401, 500], [501, 600], [601, 700], [701, 850], [851, 1000]]
MAX_TEMP_DIFF = 5.0


def pseudoCircularizePlasmid(plasmidSeq, goalSeq):
    """Reorder (pseudo-circularize) a plasmid sequence so that it is essentially
    still the same plasmid but contains the complete goalSeq. Note that there are two
    scenarios:
    (1) plasmidSeq = vectorPlasmidSeq; goalSeq = insertPlasmidSeq
    (2) plasmidSeq = vectorSeq; goalSeq = insertSeq
    We assume that the non-vector section will be longer than 2*17=34 bases.

    The first output will be a pseudo-circularized DNA sequence which is essentially the same as
    the input plasmidSeq, but will be prepared to be put into primer3. We also output the
    starting and ending indexes of the goalSeq in the pseudo-circularized DNA sequence.
    """
    # 1. get two segments of goalSeq separated by lineared plasmid seq
    finalPart1 = ''
    finalPart2 = ''
    for index in range(len(goalSeq)):
        currentPart1 = goalSeq[0:index]
        currentPart2 = goalSeq[index:]
        if (currentPart1 in plasmidSeq) and (currentPart2 in plasmidSeq):
            finalPart1 = currentPart1
            finalPart2 = currentPart2
            break
    # 2. get the indexes of the two parts in the plasmid seq
    part1StartInPlasmid = plasmidSeq.find(finalPart1)
    part1EndInPlasmid = part1StartInPlasmid + len(finalPart1)
    part2StartInPlasmid = plasmidSeq.find(finalPart2)
    part2EndInPlasmid = part2StartInPlasmid + len(finalPart2)
    # 3. generate pseudo-circularized plasmid
    # 3.1 part 1 is at the end of the plasmid sequence
    if part1EndInPlasmid == len(plasmidSeq):
        nonVectorSegment = plasmidSeq[part2EndInPlasmid:part1StartInPlasmid]
        arbitraryMiddleIndex = len(nonVectorSegment)//2
        output = nonVectorSegment[:arbitraryMiddleIndex] + finalPart1 + \
            finalPart2 + nonVectorSegment[arbitraryMiddleIndex:]
    # 3.2 part 2 is at the end of the plasmid sequence
    elif part2EndInPlasmid == len(plasmidSeq):
        nonVectorSegment = plasmidSeq[part1EndInPlasmid:part2StartInPlasmid]
        arbitraryMiddleIndex = len(nonVectorSegment)//2
        output = nonVectorSegment[:arbitraryMiddleIndex] + finalPart2 + \
            finalPart1 + nonVectorSegment[arbitraryMiddleIndex:]
    # 3.3 the plasmid sequence already contains the complete goalSeq
    else:
        output = plasmidSeq
    # figure out the starting and ending indexes of goalSeq in the output sequence
    outputStart = output.find(goalSeq)
    outputEnd = outputStart + len(goalSeq)
    return output, outputStart, outputEnd


def primer3ShortCut(seq, goalStart, goalEnd, primerOptTm=PRIMER_OPT_TM, primerMinTm=PRIMER_MIN_TM, primerMaxTm=PRIMER_MAX_TM):
    """Take in three outputs of pseudoCircularizePlasmid, call primer3 to create primers,
    with parameters if needed"""
    goalLen = goalEnd - goalStart
    sequenceMap = {
        'SEQUENCE_ID': SEQUENCE_ID,
        'SEQUENCE_TEMPLATE': seq,
        'SEQUENCE_INCLUDED_REGION': [goalStart, goalEnd]
    }
    paramMap = {
        'PRIMER_OPT_TM': primerOptTm,
        'PRIMER_MIN_TM': primerMinTm,
        'PRIMER_MAX_TM': primerMaxTm,
        'PRIMER_PRODUCT_SIZE_RANGE': [goalLen, goalLen+100]
    }
    return primer3.bindings.designPrimers(sequenceMap, paramMap)


def plasmidPrimerDesign(plasmidSeq, goalSeq):
    """Uses the primer3-py api to find the primer info for isolating the current
    goalSeq from the plasmidSeq"""
    preppedPlasmidSeq, goalSeqStart, goalSeqEnd = pseudoCircularizePlasmid(
        plasmidSeq, goalSeq)
    primerInfo = primer3ShortCut(
        preppedPlasmidSeq, goalSeqStart, goalSeqEnd)
    return primerInfo


def cleanPrimerInfo(primerInfo):
    """read primerInfo, the output of the previous function, and turn it into a more
    readable and analyzable data structure"""
    primerPairDict = {}
    for key in primerInfo:
        if key[-8:] == 'SEQUENCE':
            if key[:11] == 'PRIMER_LEFT':
                primerNum = key[12]
                leftOrRight = 'left'
                primerTM = primerInfo[key[:13]+'_TM']
                primerPairKey = 'primerPair' + primerNum
                if primerPairKey not in primerPairDict:
                    primerPairDict.update(
                        {primerPairKey: [(leftOrRight, primerTM)]})
                else:
                    primerPairDict[primerPairKey].append(
                        (leftOrRight, primerTM))
            else:
                primerNum = key[13]
                leftOrRight = 'right'
                primerTM = primerInfo[key[:14]+'_TM']
                primerPairKey = 'primerPair' + primerNum
                if primerPairKey not in primerPairDict:
                    primerPairDict.update(
                        {primerPairKey: [(leftOrRight, primerTM)]})
                else:
                    primerPairDict[primerPairKey].append(
                        (leftOrRight, primerTM))
    return primerPairDict


def primer3Only(plasmidSeq, goalSeq):
    """A quick wrapper for non-fastCloning specific primer design"""
    primerInfo = plasmidPrimerDesign(plasmidSeq, goalSeq)
    return cleanPrimerInfo(primerInfo)


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
