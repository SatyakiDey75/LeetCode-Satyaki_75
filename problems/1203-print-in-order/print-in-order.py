class Foo:
    a1=False
    a2=False
    def __init__(self):
        pass

    def first(self, printFirst):
        printFirst()
        self.a1=True

    def second(self, printSecond):
        while not self.a1: continue     
        printSecond()
        self.a2=True
                      
    def third(self, printThird):
        while not self.a2: continue
        printThird()