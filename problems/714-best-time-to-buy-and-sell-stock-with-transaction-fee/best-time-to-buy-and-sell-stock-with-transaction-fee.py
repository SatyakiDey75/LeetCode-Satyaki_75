class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s=0
        h=-math.inf
        for i in prices:
            s=max(s,h+i)
            h=max(h,s-i-fee)
        return s
        