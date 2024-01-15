class Solution(object):
    def twoSum(self, n, t):
        l=0
        r=len(n)-1

        while l<r:
            s=n[l]+n[r]
            if s==t:
                return [l+1, r+1]
            if s<t:
                l+=1
            else:
                r-=1
                
        