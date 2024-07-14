# def func(stk):
    
#     return stk
        

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stk = []
        for i in ast:
            if not stk:
                stk.append(i)
            else:
                if stk[-1]>=0 and i<0:
                    if abs(i)<stk[-1]:
                        continue
                    elif abs(i)==stk[-1]:
                        stk.pop()
                        continue
                    else:
                        while stk and stk[-1]>0 and (stk[-1]<abs(i)):
                            s=stk.pop()
                        if stk and stk[-1]==abs(i):
                            stk.pop()
                            continue
                        if (not stk) or stk[-1]<abs(i):
                            stk.append(i)
                else:
                    stk.append(i)
            # print(stk)
        return stk