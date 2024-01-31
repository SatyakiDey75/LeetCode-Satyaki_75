class Solution(object):
    def maxCount(self, banned, n, maxSum):
        s,c=0,0
        ban=set(banned)
        for i in range(1,n+1):
            if i not in ban and s+i<=maxSum:
                s+=i
                c+=1
            elif s+i>maxSum:
                break
        return c
        