def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

class Solution(object):
    def findGCD(self, nums):
        return gcd(max(nums),min(nums))
        