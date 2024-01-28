class Solution(object):
    def countKeyChanges(self, s):
        l,c=list(s.lower()),0
        for i in range (len(l)-1):
            if l[i]!=l[i+1]:
                c+=1
        return c
