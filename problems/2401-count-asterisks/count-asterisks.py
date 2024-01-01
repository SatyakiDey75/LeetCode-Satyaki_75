class Solution:
    def countAsterisks(self, s: str) -> int:
        c1,c=0,0
        for i in s:
            if i=='|':
                c1+=1
            elif i=='*' and c1%2==0:
                c+=1
        return c