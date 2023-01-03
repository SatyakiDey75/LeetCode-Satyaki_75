class Solution:
    def plusOne(self, l: List[int]) -> List[int]:
        p=len(l)-1
        s=0
        l1=[]
        for i in range (len(l)):
            s=s+(10**p)*l[i]
            p-=1
        s+=1
        while s>0:
            l1.append(s%10)
            s//=10
        return l1[::-1]