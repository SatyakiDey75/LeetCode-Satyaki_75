class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        s=sorted(Counter(words).items(),key=lambda x:(-x[1],x[0]))
        res=s[0:k]
        t=dict(res)
        return ([x for x in (t.keys())])
        