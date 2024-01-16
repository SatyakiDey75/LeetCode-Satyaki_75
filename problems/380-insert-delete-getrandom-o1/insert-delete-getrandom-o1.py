class RandomizedSet(object):

    def __init__(self):
        self.vals = []
        self.VtoI = collections.defaultdict(int)

    def insert(self, val):
        if val in self.VtoI:
            return False
        self.VtoI[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.VtoI:
            return False
        index = self.VtoI[val]
        self.VtoI[self.vals[-1]] = index
        del self.VtoI[val]
        self.vals[index] = self.vals[-1]
        self.vals.pop()
        return True

    def getRandom(self):
        index = random.randint(0, len(self.vals) - 1)
        return self.vals[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()