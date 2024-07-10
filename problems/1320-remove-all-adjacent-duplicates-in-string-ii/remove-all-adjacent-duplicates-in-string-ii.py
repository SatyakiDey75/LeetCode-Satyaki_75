class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l = [["1",0]]
        for i in s:
            if i == l[-1][0]:
                l[-1][1] += 1
                if l[-1][1] == k:
                    l = l[:-1]
            else:
                l.append([i, 1])
        return ''.join(i * count for i, count in l)