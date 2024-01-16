class Solution(object):
    def detectCapitalUse(self, w):
        if w.isupper():
            return True
        elif w.islower():
            return True
        elif w[0].isupper() and w[1:].islower():
            return True
        return False

        