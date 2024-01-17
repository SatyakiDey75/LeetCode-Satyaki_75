def gcd(i,j):
    if(j==0):
        return i
    else:
        return gcd(j,i%j)

class Solution(object):
    def countBeautifulPairs(self, nums):
        c=0
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    c+=1
        return c
        