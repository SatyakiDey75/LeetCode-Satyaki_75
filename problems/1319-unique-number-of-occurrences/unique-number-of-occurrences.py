class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[arr.count(i) for i in list(set(arr))]
        return sorted(list(set(l)))==sorted(l)