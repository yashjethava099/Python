from multipledispatch import dispatch

class Clac:

    @dispatch(int, int, int)
    def add(self,a,b,c):
        print(f"Addd is {a+b+c}")

    @dispatch(int, int)
    def add(self,a,b):
        print(f"Addd is {a+b}")

c = Clac()
c.add(100, 25, 36)
c.add(10, 20)