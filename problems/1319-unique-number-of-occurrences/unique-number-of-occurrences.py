class Solution(object):
    def uniqueOccurrences(self, arr):
        l=[arr.count(i) for i in list(set(arr))]
        return sorted(list(set(l)))==sorted(l)
        