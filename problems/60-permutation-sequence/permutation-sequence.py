class Solution(object):
    def getPermutation(self, n, k):
        r=""
        nu=[i+1 for i in range(n)]
        f=[1]*(n+1) 
        for i in range(2,n+1):
            f[i]=f[i-1]*i
        k-=1
        for i in range(n-1,-1,-1):
            j=k//f[i]
            k%=f[i]
            r+=str(nu[j])
            nu.pop(j)
        return r