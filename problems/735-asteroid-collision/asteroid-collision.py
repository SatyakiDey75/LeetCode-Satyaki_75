class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stk = []
        for i in ast:
            if (not stk) or not (stk[-1]>=0 and i<0):
                stk.append(i)
            else:
                while stk and stk[-1]>0 and (stk[-1]<abs(i)):
                    s=stk.pop()
                if stk and stk[-1]==abs(i):
                    stk.pop()
                    continue
                if (not stk) or stk[-1]<abs(i):
                    stk.append(i)
        return stk