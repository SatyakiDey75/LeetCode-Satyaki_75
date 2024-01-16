class Solution(object):
    def validPalindrome(self, s):
        def vp2(a,b):
            return all(s[i]==s[b-i+a] for i in range(a,b))
        n=len(s)
        for i in range(n//2):
            if s[i]!=s[~i]:
                return vp2(i+1,n-1-i) or vp2(i,n-2-i)
        return True
        