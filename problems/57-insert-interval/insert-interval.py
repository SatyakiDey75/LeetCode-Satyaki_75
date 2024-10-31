class Solution:
    def insert(self, inte: List[List[int]], nint: List[int]) -> List[List[int]]:
        res = []
        for i in range (len(inte)):
            if nint[1] < inte[i][0]:
                res.append(nint)
                return res + inte[i:]
            elif nint[0] > inte[i][1]:
                res.append(inte[i])
            else:
                nint = [min(nint[0], inte[i][0]), max(nint[1], inte[i][1])]
        res.append(nint)
        return res