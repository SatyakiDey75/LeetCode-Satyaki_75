class Solution(object):
    def isIsomorphic(self, s, t):
        # if len(s)!=len(t):
        #     return False
        # d={}
        # for x,y in zip(s,t):
        #     if x not in d:
        #         d[x]=y
        #     if d[x]!=y:
        #         return False
        # return len(set(d))==len(set(d.values()))
        return len(set(zip(s,t)))==len(set(s))==len(set(t))
        