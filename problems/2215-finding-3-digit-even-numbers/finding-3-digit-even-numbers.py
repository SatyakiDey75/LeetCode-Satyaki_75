class Solution(object):
    def findEvenNumbers(self, digits):
        a=[]
        c=collections.Counter(digits)
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 9, 2):
                    if c[i]>0 and c[j]>(j==i) and c[k]>(k==i)+(k==j):
                        a.append(i*100+j*10+k)
        return a