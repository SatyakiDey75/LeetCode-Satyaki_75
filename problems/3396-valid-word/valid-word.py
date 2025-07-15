class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 'aeiouAEIOU'

        def isConsonant(c: str) -> bool:
            return c.isalpha() and c not in vowels

        con, vow = 0, 0
        for c in word:
            if not c.isalnum():
                return False
            if isConsonant(c):
                con += 1
            if c in vowels:
                vow += 1
        if con == 0 or vow == 0:
            return False
        return True

# class Solution:
#   def isValid(self, word: str) -> bool:
#     VOWELS = 'aeiouAEIOU'

#     def isConsonant(c: str) -> bool:
#       return c.isalpha() and c not in VOWELS

#     return (len(word) >= 3 and
#             all(c.isalnum() for c in word) and
#             any(c in VOWELS for c in word) and
#             any(isConsonant(c) for c in word))