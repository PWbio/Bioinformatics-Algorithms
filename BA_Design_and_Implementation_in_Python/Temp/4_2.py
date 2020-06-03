# import previous coded functions 
import sys
sys.path.append("/Users/powang/Git/Bioinformatics-Algorithm/BA_Design_and_Implementation_in_Python/package")
import module4

### transcribe DNA to RNA, input is sense strand
def transcription(dna_seq):    
    assert module4.check_DNA(dna_seq), "Invalid DNA sequence"
    # alert the input is not DNA seq
    return dna_seq.upper().replace("T","U")

### Reverse complement
def reverse_complement(dna_seq):
    assert module4.check_DNA(dna_seq), "Invalid DNA sequence"
    result=""
    for i in dna_seq.upper():
        if i == 'A':
            result = "T" + result
        if i == 'T':
            result = "A" + result
        if i == 'C':
            result = "G" + result
        if i == 'G':
            result = "C" + result
    return result