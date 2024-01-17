class Solution(object):
    def finalValueAfterOperations(self, ops):
        x=0
        for i in ops:
            if i=="X++" or i=="++X":
                x+=1
            else:
                x-=1
        return x
        