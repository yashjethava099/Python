class test:
    a = 10
    _b = 20
    __c = 30

    def test(self):
        print(self.a,self.b)

class test1(test):
    def test1(self):
        print(self.a,self._b)

t1 = test()
print(t1.a)
print(t1._b)