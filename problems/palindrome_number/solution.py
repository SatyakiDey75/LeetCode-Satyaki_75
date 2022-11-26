class Solution:
    def isPalindrome(self, x: int):
        b=x
        if x<0:
            return False
        else:
            d=0           
            while x>0:
                r=x%10
                d=d*10 +r
                x=x//10
            if d!=b:
                return False
            else:
                return True