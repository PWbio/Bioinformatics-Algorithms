import sys
sys.path.append("/Users/powang/Git/Bioinformatics-Algorithm/BA_Design_and_Implementation_in_Python")
from package.module4 import *

def read_seq_from_file(filename):
    """Read a sequence file and covert multiple lines to one line"""
    files = open(filename,"r")
    lines = files.readlines()
    seq=""
    for l in lines:
        seq += l.replace("\n","")
    files.close()
    return seq

def write_seq_to_file(seq, filename):
    """Write input sequence to a file"""
    files=open(filename,"w")
    files.write(seq)
    files.close()
    return None

# Program receive a input DNA seq and output its GC content, RNA and ORFs
file_input = input ("Please input file directory:")
seq_input = read_seq_from_file(file_input)
if check_DNA(seq_input):
    print("Valid DNA sequence")
    print("Reverse complement (DNA sequence):",reverse_complement(seq_input))
    print("GC content (global)",GC_content(seq_input))
    print("Transcription (RNA sequence):", transcription(seq_input))
    print("Direct translation (Protein sequence)",translate_dna(seq_input))
    orf_input=all_protein_orf_order(seq_input,25)
    i = 1
    for orf in orf_input:
        write_seq_to_file(orf,"ORF-"+str(i)+".fasta")
        i += 1
    print("ORFs from all 6 frames (>25 amino acids) are output as filename: ORF-#.fasta")
else: print ("DNA sequence is no valid, please check again.")