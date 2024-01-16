class Solution(object):
    def detectCapitalUse(self, w):
        return w.isupper() or w.islower() or w==w.capitalize()

        