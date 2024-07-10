class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i!="../" and i!="./":
                c+=1
            elif i=="../":
                c-=1 if c>0 else 0
        return c