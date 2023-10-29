class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        for i in range(0,len(s)):
            sublen=1
            for j in range(i+1,len(s)):
                found=False
                for k in range(i,j):
                    if(s[j]==s[k]):
                        found=True
                if(found==True):
                    break
                else:
                    sublen=sublen+1
            if(sublen>max):
                max=sublen
        return max

