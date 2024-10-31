class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = 0
        for i in apple:
            s += i
        if s < 2:
            return s
        capacity.sort(reverse = True)
        c = 0
        for i in capacity:
            s -= i
            c += 1
            if s <= 0:
                return c