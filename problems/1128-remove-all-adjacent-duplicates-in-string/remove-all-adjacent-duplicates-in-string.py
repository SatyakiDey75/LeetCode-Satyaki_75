class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in s:
            if l==[] or i != l[-1]:
                l.append(i)
            else:
                l.pop()
        return "".join(l)