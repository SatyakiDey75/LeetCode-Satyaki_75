class Solution(object):
    def digitCount(self, num):
        res=[1]*len(num)
        for i in range(len(num)):
            if int(num.count(str(i)))==int(num[i]):
                res[i]=0
        return sum(res)==0