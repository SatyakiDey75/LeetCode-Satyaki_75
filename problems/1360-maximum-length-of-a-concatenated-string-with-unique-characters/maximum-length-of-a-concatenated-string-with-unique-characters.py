class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ml=0
        ms=[0]
        for i in arr:
            m=0
            for ch in i:
                ch_index=ord(ch) - ord('a')
                if m >> ch_index & 1:
                    m=0
                    break
                m |= 1 << ch_index
            if m != 0:
                for e_m in ms.copy():
                    if e_m & m == 0:
                        n_m=e_m | m
                        ms.append(n_m)
                        ml=max(ml, bin(n_m).count('1'))
        return ml