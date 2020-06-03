"""Modules from chapter 4"""

##### Chapter 4.1

def check_DNA (dna_seq):
    """Check valid DNA sequence (ATCG only)"""
    seq=dna_seq.upper()
    dna_count=seq.count("A")+seq.count("T")+seq.count("C")+seq.count("G")
    if len(seq) == dna_count:
        return True
    else:
        return False

def component (seq):
    """Count each component of a given sequence"""
    index={}
    for i in seq.upper():
        if i in index:
            index[i] += 1
        else:
            index[i] = 1
    return index

def GC_content (seq):
    """Full length GC content"""
    gc_count=0
    for i in seq:
        if i in "GCgc":
            gc_count +=1
    return gc_count / len(seq)

def GC_content_interval(seq,k):
    """Interval GC content"""
    result=[]
    for i in range(0,len(seq)-k+1,k):
        interval_seq= seq[i:i+k]
        gc=GC_content(interval_seq)
        result.append(gc)
    return result

def GC_content_slide(seq,k):
    """K-mer GC content, slide through seq"""
    result=[]
    for i in range(0,len(seq)-k+1):
            # to slide along seq, do not specify step in range
        slide_seq= seq[i:i+k]
        gc=GC_content(slide_seq)
        result.append(gc)
    return result

##### Chapter 4.2

def transcription(dna_seq):    
    """transcribe DNA to RNA, input is sense strand"""
    assert check_DNA(dna_seq), "Invalid DNA sequence"
    return dna_seq.upper().replace("T","U")

def reverse_complement(dna_seq):
    """Reverse complement"""
    assert check_DNA(dna_seq), "Invalid DNA sequence"
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

##### Chapter 4.3

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
    assert check_DNA(dna_seq),"Invalid DNA sequence"
    dna_input=dna_seq.upper()
    aa_output=""
    for i in range (pos,len(dna_input)-2,3):
        codon=dna_input[i:i+3]
        aa_output += translation_codon(codon)
    return aa_output

def codon_usage(dna_seq, aa):
    """Summarize codon usage of a given amino acid"""
    assert check_DNA(dna_seq),"Invalid DNA sequence"
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

##### Chapter 4.4

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