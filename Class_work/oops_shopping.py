class Shopping:
    def __init__(self, pr_name, pr_price, pr_quantity, pr_des):
        self.pr_name = pr_name
        self.pr_price = pr_price
        self.pr_quantity = pr_quantity
        self.pr_des = pr_des

    def display(self):
        print("Name:", self.pr_name)
        print("Price:", self.pr_price)
        print("Quantity:", self.pr_quantity)
        print("Description:", self.pr_des)

p1 = Shopping("parle", 10, 15, "biscuit")
p1.display()