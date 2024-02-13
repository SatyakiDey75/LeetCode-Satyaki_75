class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        a,b,c=nums[0],nums[1],nums[2]
        if a+b<=c:
            return "none"
        else:
            if a==b and b==c:
                return "equilateral"
            if a==b or b==c:
                return "isosceles"
            else:
                return "scalene"
        