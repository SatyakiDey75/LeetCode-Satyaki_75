class Solution:
    def isValid(self, word: str) -> bool:
        # if len(word) < 3:
        #     return False
        # vowels = 'aeiouAEIOU'

        # def isConsonant(c: str) -> bool:
        #     return c.isalpha() and c not in vowels

        # con, vow = 0, 0
        # for c in word:
        #     if not c.isalnum():
        #         return False
        #     if isConsonant(c):
        #         con += 1
        #     if c in vowels:
        #         vow += 1
        # if con == 0 or vow == 0:
        #     return False
        # return True

        if len(word) < 3: 
            return False
        v, c = False, False
        for x in word:
            if not x.isdigit() and not x.isalpha(): 
                return False
            if x.lower() in 'aeiou':
                v = True
            elif not x.isdigit():
                c = True

        return v and c