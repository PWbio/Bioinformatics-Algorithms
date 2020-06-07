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
            self.index.append((t[i:i+k]), i)