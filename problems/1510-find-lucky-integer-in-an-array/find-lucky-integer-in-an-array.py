from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        freq = Counter(arr)
        for i in arr:
            if freq[i] == i and  i > res:
                res = i
        return res