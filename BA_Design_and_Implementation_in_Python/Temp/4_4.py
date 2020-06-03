import sys
sys.path.append("/Users/powang/Git/Bioinformatics-Algorithm/BA_Design_and_Implementation_in_Python")
from package.module4 import *

def reading_frame(dna_seq):
    """Find six ORFs of a given DNA sequence"""
    assert check_DNA(dna_seq),"Invalid DNA sequence"
    result=[]
    result.append(translate_dna(dna_seq,0))
    result.append(translate_dna(dna_seq,1))
    result.append(translate_dna(dna_seq,2))
    rc=reverse_complement(dna_seq)
    result.append(translate_dna(rc,0))
    result.append(translate_dna(rc,1))
    result.append(translate_dna(rc,2))
    return result

def protein_orf (aa_seq):
    """Return all possible ORF from an amino acid sequence."""
    aa_seq = aa_seq.upper()
    temp_prot = []
    result_prot = []
    for aa in aa_seq:
        if aa == "*":
            if temp_prot:
            #Return true if the list is not empty. This is to prevent append only a stop codon into [result_prot]
                for p in temp_prot:
                    result_prot.append(p)
                    #Add aa seq from [temp_prot] to [result_prot]
                temp_prot = []
                #Reset [temp_prot] to empty
        else:
            if aa == "M":
                temp_prot.append("")
                #make a new element in [temp_prot]
            for i in range(len(temp_prot)):
                temp_prot[i] += aa
                #len(temp_prot) return 1 when "M" is found. Or >1, when more than a "M" is found before stop codon.
                #Otherwise, it return 0 and no aa is added to [temp_prot]
    return result_prot

def all_protein_orf(dna_seq):
    """Detect all ORFs from a DNA sequence."""
    assert check_DNA(dna_seq),"Invalid DNA sequence"
    read_frame = reading_frame(dna_seq)
    result_orf = []
    for seq in read_frame:
        temp_orf = protein_orf(seq)
        for i in temp_orf:
            result_orf.append(i)
    return result_orf

def all_protein_orf_order(dna_seq,threshhold=0):
    """Detect all ORFs from a DNA sequence. Print in order and Set the minimum amino acid length."""
    def insert_protein_order(orf,result_orf):
        i = 0
        while i < len(result_orf) and len(orf) < len (result_orf[i]):
            i += 1
        # If current orf is shorter, add into latter position in list
        # (repeat comparison until the length of orf is equal or shorter than the existed orf)
        result_orf.insert(i,orf)
        # If current orf is longer, add into former position[0] in list
    assert check_DNA(dna_seq),"Invalid DNA sequence"
    read_frame = reading_frame(dna_seq)
    result_orf = []
    for seq in read_frame:
        temp_orf = protein_orf(seq)
        for orf in temp_orf:
            if len(orf) > threshhold:
                insert_protein_order(orf,result_orf)
    return result_orf

x=["1","2","3"]
x.insert(1,"*")
x

reading_frame("ATGGTGACATAACTCGTGATGAGGTGGTTTCCCATAGTATAG")
all_protein_orf_order("ATGGTGACATAACTCGTATGGATGAGGTATGGGATGTTTCCTAACAATGTAGTATAG")
all_protein_orf("ATGGTGACATAACTCGTATGGATGAGGTATGGGATGTTTCCTAACAATGTAGTATAG")
protein_orf("MSADASD*AMSD*MASD*MASDASDMasdsd*")