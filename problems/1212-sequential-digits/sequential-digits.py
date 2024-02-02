class Solution(object):
    def sequentialDigits(self, low, high):
        l=[]
        for i in range(1,9):
            n=i
            for j in range(i+1,10):
                n=n*10+j
                if low<=n<=high:
                    l.append(n)
        return sorted(l)