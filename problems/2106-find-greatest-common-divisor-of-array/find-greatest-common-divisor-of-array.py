# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

class Solution(object):
    def findGCD(self, nums):
        # return gcd(max(nums),min(nums))
        mi,ma=min(nums),max(nums)
        for i in range (mi,0,-1):
            if mi%i==0 and ma%i==0:
                return i
        