class Solution(object):
    def vowelStrings(self, words, left, right):
        l=['a','e','i','o','u']
        c=0
        for i in range(left,right+1):
            if words[i][0] in l and words[i][-1] in l:
                c+=1
        return c