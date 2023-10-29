class Solution:
    def angleClock(self, h: int, m: int) -> float:
        if h==12:
            h=0
        c=abs((6*m)-(30*(h+m/60)))
        if c>180:
            c=360-c
        return c
