class Solution:
    def countPrimes(self, n: int) -> int:
        pr = [True for i in range (n+1)]
        i = 2
        while (i*i <= n):
            if pr[i] == True:
                for j in range (i*i, n+1, i):
                    pr[j] = False
            i += 1
        ans = 0
        for i in range(2, n):
            if pr[i]:
                ans += 1
        return ans