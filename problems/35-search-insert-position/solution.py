class Solution:
    def searchInsert(self, l: List[int], n: int) -> int:
        c=0
        if n>l[-1]:
            c=len(l)
        else:
            for i in range(len(l)):
                c=0
                if l[i]==n:
                    c=i
                    break
                if l[i]>n:
                    c=i
                    break
        return c