import bisect
a = [1,3,3,6,9,10,14]
bisect.bisect_left(a,3)
bisect.bisect_left(a,9)
bisect.bisect_left(a,11)

class Index(object):
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k + 1):
            """Create index of t in kmer"""
            self.index.append((t[i:i+k],i)) # Tuple
        self.index.sort()

    def query(self, p):
        """Search and return offsets where first kmer of p matches index of t"""
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1)) # -1 is larger than the number of index. Therefore, the offset retrieved will be at the leftmost position.
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer: # If mismatch, the p is definitely not existed in t. Return empty list.
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def queryIndex(p, t, index):
    """Function use class Index's method to align sequence"""
    k = index.k
    offsets = []
    for i in index.query(p):
        if p[k:] == t[i+k:i+len(p)]: # check rest of sequence outside kmer
            offsets.append(i)
    return offsets

class Index_v2(object):
    def __init__(self, t, k):
        self.k = k
        self.index = {}
        for i in range(len(t) - k + 1):
            self.index[i] = t[i:i+k]

    def query(self, p):
        kmer = p[:self.k]
        hits= []

        for i in range(len(self.index)):
            if self.index[i] == kmer:
                hits.append(i)
            i += 1
        return hits

class Index_v3(object):
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k + 1):
            """Create index of t in kmer"""
            self.index.append((t[i:i+k],i)) # Tuple
        self.index.sort()

    def query(self, p):
        """Search and return offsets where first kmer of p matches index of t"""
        kmer = p[:self.k]
        hits = []
        for i in range(len(self.index)):
            if self.index[i][0] == kmer: # If mismatch, the p is definitely not existed in t. Return empty list.
                hits.append(self.index[i][1])
            i += 1
        return hits

t="ATGATGTAACGATCGTACGTACGTGACGTCATCGAGGCAGCTGATGGGTA"
p="ATGATGTAA"
A= Index(t,3)

Linear_dict = Index_v2(t, 3)
Linear_tuple = Index_v3(t, 3)
Log_tuple = Index(t, 3)
Linear_dict.query(p)
Linear_tuple.query(p)
Linear_tuple.query(p)

import timeit
def time():
    X= timeit.timeit('Linear_dict.query(p)', 'from __main__ import Index_v2, t, p, A, Linear_dict', number=100000)
    Y= timeit.timeit('Linear_tuple.query(p)', 'from __main__ import Index_v3, t, p, A, Linear_tuple', number=100000)
    Z= timeit.timeit('Log_tuple.query(p)', 'from __main__ import Index, t, p, A, Log_tuple', number=100000)
    print(X, Y, Z)
time()