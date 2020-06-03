import sys
sys.path.append("/Users/powang/Git/Bioinformatics-Algorithm/BA_Design_and_Implementation_in_Python")
from Package.module4 import *

class myseq:
    """define own biological sequence class"""
    def __init__(self, seq, seq_type= "DNA"):
        self.seq = seq.upper()
        self.seq_type= seq_type

    def __len__(self):
        return len(self.seq)

    def __getitem__(self,n):
        return self.seq[n]

    def __getslice__(self,i,j):
        return self.seq[i:j]

    def __str__(self):
        return self.seq

    def get_seq_biotype(self):
        return  self.seq_type

    def show_info_seq(self):
        print("Biotype:"+self.seq_type+"\n"+"Sequence:"+self.seq)

    def alphabet(self):
        """return the component of the sequence"""
        if(self.seq_type.upper()=="DNA"):
            return "ATCG"
        elif(self.seq_type.upper()=="RNA"):
            return "AUCG"
        elif(self.seq_type.upper()=="PROTEIN"):
            return "ACDEFGHIKLMNPQRSTVWY"
        else:
            return None

    def check(self):
        Char= self.alphabet()
        res= True
        i= 0
        while i < len(self.seq) and res:
            if self.seq[i] not in Char:
                res = False
            else:
                i += 1
        return res

    def transcription(self):
        if self.seq_type.upper()=="DNA":
            return myseq(self.seq.replace("T","U"),"RNA")
        else:
            return None

    def reverse_complement(self):
        if self.seq_type.upper() != "DNA":
            return "Not a DNA sequence"
        for i in self.seq.upper():
            if i not in "ATCG":
                print("Cotain non-DNA (ATCG) sequence")

        comp=""
        for i in self.seq.upper():
            if (i == "A"):
                comp = "T" + comp
            elif (i == "T"):
                comp = "A" + comp
            elif (i == "C"):
                comp = "G" + comp
            elif (i == "G"):
                comp = "C" + comp
        return myseq(comp,"DNA")

    def translate(self,frame=1):
        """ Translate an input DNA sequence to Protein.
        Specify the reading frame (1,2,3,-1,-2,-3),
        -1 means 'frame 1 in reverse complement sequence.' """
        if self.seq_type.upper() != "DNA":
            return "Not a DNA sequence (wrong seq_type)"

        aa_output=""
        dna_input=self.seq
        if frame == 0 or frame not in range(-3,4):
            return "Please specify a correct reading frame number. (+/- 1,2,3)"

        elif frame in range(-3,0):
            dna_input=reverse_complement(dna_input)

        for pos in range (abs(frame)-1,len(dna_input)-2,3):
            codon=dna_input[pos:pos+3]
            aa_output += translation_codon(codon)

        return myseq(aa_output,"Protein")

"""
x=myseq("atgtaataatgtTACcat","DNA")
x.seq_type
x.seq.upper()
x.show_info_seq()
print(x.translate(3))
print(x.reverse_complement().translate())
print(x.transcription())
print(x)
y=myseq("augcauaugcuagucugauguc","Rna")
y.seq_type
y.check()
print(y.alphabet())
"""