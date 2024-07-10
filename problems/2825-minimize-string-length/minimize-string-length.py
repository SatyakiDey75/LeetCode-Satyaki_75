class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # l = []
        # for i in s:
        #     if i not in l:
        #         l.append(i)

        # return len(l)
        return len(set(s))