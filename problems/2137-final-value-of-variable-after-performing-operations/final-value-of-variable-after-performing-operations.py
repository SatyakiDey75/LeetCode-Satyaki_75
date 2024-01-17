class Solution(object):
    def finalValueAfterOperations(self, ops):
        x=0
        for i in ops:
            if i in ("++X","X++"):
                x+=1
            else:
                x-=1
        return x
        