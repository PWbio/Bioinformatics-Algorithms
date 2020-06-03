from Bio.Seq import Seq

Test_seq=Seq("ATTGTCAGTATGCGTCAGTCGTCAT")
Test_seq
print(Test_seq)
Test_seq.alphabet

from Bio.Alphabet import IUPAC

a_seq= Seq("GTACGTACGTACTTGCAT",IUPAC.unambiguous_dna)
a_seq
a_seq.alphabet
help(a_seq.alphabet)
IUPAC.unambiguous_dna.letters
IUPAC.ambiguous_dna.letters
IUPAC.IUPACAmbiguousDNA.letters
IUPAC.IUPACProtein.letters
IUPAC.
for i in a_seq:
    print(i)
from Bio.Alphabet import generic_nucleotide
help(generic_nucleotide)
help(Seq.Alphabet)
b=Seq("ACTGACGTACTGATGC")
b.alphabet
b_rc=b.reverse_complement()
b_rc.alphabet
b.transcribe()

from Bio import SeqFeature
from Bio.Seq import Seq
from Bio.SeqFeature import *
example_seq = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTT")
example_feat = SeqFeature(FeatureLocation(5, 18), type="gene", strand=-1)
feature_seq = example_feat.extract(example_feat)
print (feature_seq)
x=SeqFeature.location_operator