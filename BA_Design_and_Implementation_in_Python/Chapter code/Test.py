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

x={}
x[1]=2
y=["ATC"]*2
y


# Python3 program for Boyer Moore Algorithm with
# Good Suffix heuristic to find pattern in
# given text string

# preprocessing for strong good suffix rule
def preprocess_strong_suffix(shift, bpos, pat, m):
    # m is the length of pattern
    i = m
    j = m + 1
    bpos[i] = j

    while i > 0:

        '''if character at position i-1 is 
        not equivalent to character at j-1, 
        then continue searching to right 
        of the pattern for border '''
        while j <= m and pat[i - 1] != pat[j - 1]:

            ''' the character preceding the occurrence 
            of t in pattern P is different than the 
            mismatching character in P, we stop skipping 
            the occurrences and shift the pattern 
            from i to j '''
            if shift[j] == 0:
                shift[j] = j - i

            # Update the position of next border
            j = bpos[j]

        ''' p[i-1] matched with p[j-1], border is found. 
        store the beginning position of border '''
        i -= 1
        j -= 1
        bpos[i] = j

    # Preprocessing for case 2


def preprocess_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):

        ''' set the border position of the first character 
        of the pattern to all indices in array shift 
        having shift[i] = 0 '''
        if shift[i] == 0:
            shift[i] = j

        ''' suffix becomes shorter than bpos[0], 
        use the position of next widest border 
        as value of j '''
        if i == j:
            j = bpos[j]


'''Search for a pattern in given text using 
Boyer Moore algorithm with Good suffix rule '''


def search(text, pat):
    # s is shift of the pattern with respect to text
    s = 0
    m = len(pat)
    n = len(text)

    bpos = [0] * (m + 1)

    # initialize all occurrence of shift to 0
    shift = [0] * (m + 1)

    # do preprocessing
    preprocess_strong_suffix(shift, bpos, pat, m)
    preprocess_case2(shift, bpos, pat, m)

    while s <= n - m:
        j = m - 1

        ''' Keep reducing index j of pattern while characters of 
            pattern and text are matching at this shift s'''
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1

        ''' If the pattern is present at the current shift, 
            then index j will become -1 after the above loop '''
        if j < 0:
            print("pattern occurs at shift = %d" % s)
            s += shift[0]
        else:

            '''pat[i] != pat[s+j] so shift the pattern 
            shift[j+1] times '''
            s += shift[j + 1]

        # Driver Code


if __name__ == "__main__":
    text = "ABAAAABAACD"
    pat = "ABA"
    search(text, pat)

# This code is contributed by
# sanjeev2552

t="1234567"
x=[]
x.append((t[1:3], 0))
t[1:3]