class Solution(object):
    def maxCount(self, banned, n, maxSum):
        s,c,i=0,0,1
        while i<n+1 and not s>maxSum:
            
            if i not in banned:
                s+=i
                if not s>maxSum:
                    c+=1
            i+=1
        return c

        