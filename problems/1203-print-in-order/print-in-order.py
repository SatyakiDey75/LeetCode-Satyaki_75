class Foo:
    f,s=False,False
    def __init__(self):
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.f=True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.f: continue
        printSecond()
        self.s=True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.s: continue
        printThird()