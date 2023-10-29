class Solution:
    def removeElement(self, l: List[int], n: int) -> int:
        for i in range (len(l)):
            if l[i]==n:
                l[i]='_'
        for i in range(len(l)):
            if l[i]=='_':
                l.remove(l[i])
                l.append('_')
        i,b=0,0
        try:
            while l[i]!='_':
                b+=1
                i+=1
        except:
            pass
        return b