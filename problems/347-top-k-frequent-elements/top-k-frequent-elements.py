def key(d,t):
    for k,v in d.items():
        if v==t:
            return k

class Solution(object):
    def topKFrequent(self, nums, k):
        c=(Counter(nums))
        r=[]
        for i in range(k):
            s=max(c.values())
            p=key(c,s)
            r.append(p)
            del c[p]
        return r
        