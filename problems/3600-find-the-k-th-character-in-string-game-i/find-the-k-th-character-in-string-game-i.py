class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        res = "a"
        while len(word) < k:
            for i in res:
                res = res + chr(ord(i)+1) 
            word = res

        return word[k-1]