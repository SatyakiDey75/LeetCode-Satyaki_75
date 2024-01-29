class Solution(object):
    def getLucky(self, s, k):
        a=""
        for i in s:
            a+=str(ord(i)-96)
        print(a)
        while k>0:
            a=sum(int(i) for i in str(a))
            k-=1
        return a