class Solution(object):
    def maxCount(self, banned, n, maxSum):
        s,c=0,0
        for i in range(1,n+1):
            if i not in banned and s+i<=maxSum:
                s+=i
                c+=1
            elif s+i>maxSum:
                break
        return c
        