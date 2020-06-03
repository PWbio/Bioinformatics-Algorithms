import sys
sys.path.append("/Users/powang/Git/Bioinformatics-Algorithm/BA_Design_and_Implementation_in_Python")
from package import module4

def translation_codon(codon):
    """
    Translate a codon (Three letter) into an amino acid.
    by creating a dictionary for standard genetic code
    """
    codon_dict={
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "TGT":"C", "TGC":"C",
    "GAT":"D", "GAC":"D",
    "GAA":"E", "GAG":"E",
    "TTT":"F", "TTC":"F",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    "CAT":"H", "CAC":"H",
    "ATA":"I", "ATT":"I", "ATC":"I",
    "AAA":"K", "AAG":"K",
    "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "ATG":"M",
    "AAT":"N", "AAC":"N",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "TGG":"W",
    "TAT":"Y", "TAC":"Y",
    "TAA":"*", "TAG":"*", "TGA":"*"}
    if codon in codon_dict:
        return codon_dict[codon]
    else:
        return None

def translate_dna(dna_seq, pos=0):
    """Convert a DNA sequence into an amino acid sequence."""
    assert module4.check_DNA(dna_seq),"Invalid DNA sequence"
    dna_input=dna_seq.upper()
    aa_output=""
    for i in range (pos,len(dna_input)-2,3):
        codon=dna_input[i:i+3]
        aa_output += translation_codon(codon)
    return aa_output

def codon_usage(dna_seq, aa):
    """Summarize codon usage of a given amino acid"""
    assert module4.check_DNA(dna_seq),"Invalid DNA sequence"
    dna_input=dna_seq.upper()
    dic={}
    total=0
    for i in range(0,len(dna_input)-2,3):
        codon=dna_input[i:i+3]
        if translation_codon(codon) == aa:
            if codon in dic:
                dic[codon] += 1
            else:
                dic[codon] = 1
            total +=1
    if total >0:
        for j in dic:
            dic[j] /= total
    return dic