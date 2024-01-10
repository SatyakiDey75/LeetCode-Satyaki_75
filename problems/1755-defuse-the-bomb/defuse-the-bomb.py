class Solution(object):
    def decrypt(self, code, k):
        c=[0]*len(code)
        if k==0:
            return c
        for i in range (len(code)):
            if k>0:
                for j in range (i+1,i+k+1):
                    c[i]+=code[j%len(code)]
            else:
                for j in range (i+k,i):
                    c[i]+=code[(j+len(code))%len(code)]
        return c