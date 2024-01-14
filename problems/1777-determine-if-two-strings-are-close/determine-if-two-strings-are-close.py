class Solution(object):
    def closeStrings(self, word1, word2):
        dict1=Counter(word1)
        dict2=Counter(word2)
        return (
            len(word1)==len(word2) and Counter(dict1.values())==Counter(dict2.values())           and set(dict1)==set(dict2)
        )
        