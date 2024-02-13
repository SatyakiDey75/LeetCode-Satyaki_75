class Solution(object):
    def triangleType(self, nums):
        a,b,c=nums[0],nums[1],nums[2]
        if not (a+b>c and b+c>a and c+a>b):
            return "none"
        else:
            if a==b and b==c:
                return "equilateral"
            if a==b or b==c or c==a:
                return "isosceles"
            else:
                return "scalene"
        