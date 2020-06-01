def check_DNA (dna_seq):
    seq=dna_seq.upper()
    dna_count=seq.count("A")+seq.count("T")+seq.count("C")+seq.count("G")
    if len(seq) == dna_count:
        return True
    else:
        return False
check_DNA("atcgcgtatatat")
check_DNA("atcgaaax")

def component (seq):
    index={}
    for i in seq.upper():
        if i in index:
            index[i] += 1
        else:
            index[i] = 1
    return index
component("atcgcgtatatat")
component("MVQILVSKKK")