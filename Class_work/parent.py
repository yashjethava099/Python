class A:
    def __init__(self):
        print("A con")

    def display(self):
        print("class A display calling")

class B:
    def __init__(self):
        print("B con")

    def display(self):
        print("class B display calling")

class C(A, B):
    def __init__(self):
        B.__init__(self)

    def display(self):
        print("c is calling")
        A().display()
c = C()
c.display()