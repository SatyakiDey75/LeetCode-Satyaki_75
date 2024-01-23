# def fact(h):
#     if h==0:
#         return 1
#     return h*fact(h-1)

# class Solution(object):
#     def trailingZeroes(self, n):
#         s=str(fact(n))
#         return len(s)-len(s.rstrip('0'))

class Solution(object):
    def trailingZeroes(self, n):
        return 0 if n==0 else n//5+self.trailingZeroes(n//5)