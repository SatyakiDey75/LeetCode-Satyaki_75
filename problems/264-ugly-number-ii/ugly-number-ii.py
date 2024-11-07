class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]

        i2 = 0
        i3 = 0
        i5 = 0

        while len(l) < n:
            n2 = l[i2] * 2
            n3 = l[i3] * 3
            n5 = l[i5] * 5
            ne = min(n2, n3, n5)
            if ne == n2:
                i2 += 1
            if ne == n3:
                i3 += 1
            if ne == n5:
                i5 += 1
            l.append(ne)

        return l[-1]
