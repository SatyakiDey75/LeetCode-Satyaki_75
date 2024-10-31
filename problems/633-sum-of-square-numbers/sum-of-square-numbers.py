class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, math.isqrt(c)
        while l <= r:
            summ = l * l + r * r
            if summ == c:
                return True
            if summ < c:
                l += 1
            else:
                r -= 1
        return False