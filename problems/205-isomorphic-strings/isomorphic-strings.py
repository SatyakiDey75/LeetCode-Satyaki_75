class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for x,y in zip(s,t):
            if x not in d:
                d[x]=y
            if d[x]!=y:
                return False
        return len(set(d))==len(set(d.values()))
        
        # return [*map(s.index, s)] == [*map(t.index, t)]
        