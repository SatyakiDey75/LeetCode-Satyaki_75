def sod(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s%2
    # return s
class Solution(object):
    def countEven(self, num):
        # return (sum(1 for i in range(2,num+1) if sod(i)%2==0))
        return (num-sod(num))//2
        