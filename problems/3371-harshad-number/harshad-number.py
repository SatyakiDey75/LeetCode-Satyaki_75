class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        b = x
        s = 0
        while b > 0:
            s += (b % 10)
            b //= 10
        return s if x % s == 0 else -1