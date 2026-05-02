# class cals:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def __eq__(self, value):
#         return self.a == value.a and self.b == value.b
    
# c1 = cals(10, 20)
# c2 = cals(10, 20)
# print(c1 == c2)
import re

email = "yahs@gmail.ocm"

k = re.match("^[a-z0-9_.]+@[a-z]+\\.[a-z]{2,4}$",email)
print(k)

password = input("enter your password")

k = re.match()