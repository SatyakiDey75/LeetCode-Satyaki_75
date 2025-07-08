class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for i in arr:
            if arr.count(i) == i:
              if  i > res:
                res = i
        return res