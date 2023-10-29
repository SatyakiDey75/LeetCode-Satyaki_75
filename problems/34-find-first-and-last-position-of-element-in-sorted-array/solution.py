class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
        c=[]
        for i in range(0,len(n)):
            if n[i]==t:
                c.append(i)
        if c==[]:
            c=[-1,-1]
        elif len(c)==1:
            c.append(c[0])
        elif len(c)>2:
            l=[]
            l.append(c[0])
            l.append(c[-1])
            c=l
        return c