class Solution:
    def countAsterisks(self, s: str) -> int:
        
        ans = 0
        i = False

        for char in s:
            if char == '|':
                i = not i
            elif char == '*':
                if not i:
                    ans += 1

        return ans