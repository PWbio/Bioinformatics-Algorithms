### check valid DNA sequence (ATCG only)
def check_DNA (dna_seq):
    seq=dna_seq.upper()
    dna_count=seq.count("A")+seq.count("T")+seq.count("C")+seq.count("G")
    if len(seq) == dna_count:
        return True
    else:
        return False

### count each component
def component (seq):
    index={}
    for i in seq.upper():
        if i in index:
            index[i] += 1
        else:
            index[i] = 1
    return index

### Full length GC content
def GC_content (seq):
    gc_count=0
    for i in seq:
        if i in "GCgc":
            gc_count +=1
    return gc_count / len(seq)
    # alternative: print(f"GC content: {gc_count/len(seq):.2%}")

### Interval GC content
def GC_content_interval(seq,k):
    result=[]
    for i in range(0,len(seq)-k+1,k):
        interval_seq= seq[i:i+k]
        gc=GC_content(interval_seq)
        result.append(gc)
    return result

### K-mer GC content, slide through seq
def GC_content_slide(seq,k):
    result=[]
    for i in range(0,len(seq)-k+1):
            # to slide along seq, do not specify step in range
        slide_seq= seq[i:i+k]
        gc=GC_content(slide_seq)
        result.append(gc)
    return result