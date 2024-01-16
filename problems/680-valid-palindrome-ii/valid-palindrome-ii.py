class Solution(object):
    def validPalindrome(self, s):
        if s==s[::-1]:
            return True
        for i in range(len(s)):
            if s[i]!=s[len(s)-1-i]:
                t=s[:i]+s[i+1:]
                t2=s[:len(s)-1-i]+s[len(s)-i:]
                return t==t[::-1] or t2==t2[::-1]
        