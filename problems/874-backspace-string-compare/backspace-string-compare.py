class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ''
        t1 = ''

        for i in s:
            if i=="#":
                s1=s1[:-1]
            else:
                s1 += i
        for i in t:
            if i=="#":
                t1=t1[:-1]
            else:
                t1 += i
        return s1 == t1