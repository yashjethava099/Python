class Students:

    def __init__(self, id, age, name):
        self.id = id
        self.age = age
        self.name = name

    def display(self):
        print(self.id, self.age, self.name)

s1 = Students(10,16,"yash")
s1.display()

s2 = Students(11, 18, "krish")
s2.display()