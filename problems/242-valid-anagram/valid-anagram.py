class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        ss = set(s)
        for i in ss:
            if s.count(i) != t.count(i):
                return False

        return True