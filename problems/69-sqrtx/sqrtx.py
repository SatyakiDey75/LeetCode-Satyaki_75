class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = l + (r - l) // 2

            if m * m > x:
                r = m - 1
            else:
                l = m + 1

        return r