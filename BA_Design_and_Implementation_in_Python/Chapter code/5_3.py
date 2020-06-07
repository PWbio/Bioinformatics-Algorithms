"""Heuristic Algorithm: Boyer-Moore"""

class BoyerMoore:
    def __init__(self,alphabet,pattern):
        self.alphabet = alphabet
        self.pattern = pattern
        self.preprocess()

    def preprocess(self):
        self.process_bcr()
        self.process_gsr()
        #bcr, Bad-Character Rule
        #gsr, Good Suffix Rule

    def process_bcr(self):
        self.occurence = {}
        for char in self.alphabet:
            self.occurence[char] = -1
        for i in range(len(self.pattern)):
            c = self.pattern[i]
            self.occurence[c] = i
            # Give the offset of last character.

    def process_gsr(self):
        self.f = [0]*(len(self.pattern)+1)
        self.s = [0]*(len(self.pattern)+1)
        i = len(self.pattern)
        j = len(self.pattern)+1
        self.f[i] = j
        while i>0:
            while j <= len(self.pattern) and self.pattern[i-1] != self.pattern[j-1]:
                if self.s[j] == 0:
                    self.s[j] = j-i
                j = self.f[j]
            i -= 1
            j -= 1
            self.f[i] = j
        j = self.f[0]
        for i in range(len(self.pattern)):
            if self.s[i] == 0:
                self.s[i] = j
            if i == j:
                j = self.f[j]