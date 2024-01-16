class Solution(object):
    def truncateSentence(self, s, k):
        x=""
        d=0
        for i in s.split(" "):
            d+=1
            if(d<k):
                x+=i+" "
            elif(d==k):
                x+=i
        return x
        