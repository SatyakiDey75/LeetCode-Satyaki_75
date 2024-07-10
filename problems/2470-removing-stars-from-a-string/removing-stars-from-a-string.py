class Solution:
    def removeStars(self, s: str) -> str:
        ans = ''
        for i in s:
            if i != "*":
                ans += i
            else:
                ans = ans[:-1]
        return ans