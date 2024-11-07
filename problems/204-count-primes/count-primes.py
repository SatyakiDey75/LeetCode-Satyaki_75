class Solution:
    def countPrimes(self, n: int) -> int:
        # pr = [True for i in range (n+1)]
        # i = 2
        # while (i*i <= n):
        #     if pr[i] == True:
        #         for j in range (i*i, n+1, i):
        #             pr[j] = False
        #     i += 1
        # ans = 0
        # for i in range(2, n):
        #     if pr[i]:
        #         ans += 1
        # return ans
        if n <= 1:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        cnt = 1

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    if primes[j]:
                        cnt += 1
                    primes[j] = False

        return n - cnt - 1