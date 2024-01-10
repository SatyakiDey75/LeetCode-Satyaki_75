class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        c=[0]*len(code)
        if k==0:
            return c
        s=list(accumulate(code+code, initial=0))
        for i in range (len(code)):
            if k>0:
                c[i]+=s[i+k+1]-s[i+1]
            else:
                c[i]+=s[i+len(code)]-s[i+k+len(code)]
        return c