"""
Modified from original source of code (add CountNode):
Lecture for 9/25/2013 in EN 600.439/639: Computational Genomic
,Ben Langmead
https://www.youtube.com/watch?v=hLsrPsFHPcQ
"""
class SuffixTrie():

    def __init__(self, t):
        """ Make suffix trie from t """
        t += '$' # special terminator symbol
        self.root = {}
        for i in range(len(t)): # for each suffix
            cur = self.root
            for c in t[i:]: # for each character in i'th suffix
                if c not in cur:
                    cur[c] = {} # add outgoing edge if necessary
                cur = cur[c]

    def followPath(self, s):
        """ Follow path given by characters of s.  Return node at
            end of path, or None if we fall off. """
        cur = self.root
        for c in s:
            if c not in cur:
                return None
            cur = cur[c]
        return cur

    def hasSubstring(self, s):
        """ Return true iff s appears as a substring of t """
        return self.followPath(s) is not None

    def hasSuffix(self, s):
        """ Return true iff s is a suffix of t """
        node = self.followPath(s)
        return node is not None and '$' in node

def CountNode(self):
    """ Count total nodes of suffix tries """
    def Flatten(self):
        """ Recursive loop to count dictionary type """
        count = 0
        for keys in self.keys():
            if isinstance(self[keys], dict):
                count +=1
                c = Flatten(self[keys])
                count += c
        return count
    return Flatten(self) + 1 # plus 1 root node


strie = SuffixTrie('ATA')
strie.root
CountNode(strie.root)
strie.hasSubstring('would have been')
strie.hasSubstring('nope')
strie.hasSuffix('such a word')
