class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        pal=""
        for i in range(0,len(s)-1):
            for j in range (1,len(s)):
                if s[i]==s[j]:
                    l.append(s[i:j+1])
        m=0
        for i in l:
            if len(i)>0 and i==i[::-1] and len(i)>m:
                m=len(i)
                pal=i
        if len(s)<2 or (len(s)==2 and s[0]!=s[1]):
                pal=s[0]
        return pal