class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            j=str(sorted(i))
            if j not in d:
                d[j]=[i]
            else:
                d[j].append(i)
        return d.values()
