class Foo:
    f=False
    s=False
    def __init__(self):
        pass

    def first(self, printFirst):
        printFirst()
        self.f=True

    def second(self, printSecond):
        while not self.f: continue
        printSecond()
        self.s=True

    def third(self, printThird):
        while not self.s: continue
        printThird()