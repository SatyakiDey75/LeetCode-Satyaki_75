class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        c=0
        l1=[]
        print(l)
        for j in l:
            if " " not in j and ""!=j:
                l1.append(len(j))
        print(l1)
        return l1[-1]