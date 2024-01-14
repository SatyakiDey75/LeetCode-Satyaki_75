class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!=len(word2):
            return False
        c1=collections.Counter(word1)
        c2=collections.Counter(word2)
        if sorted(c1.keys())!=sorted(c2.keys()):
            return False
        return sorted(c1.values())==sorted(c2.values())
            