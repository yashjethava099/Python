# f = open("text.txt",'w')
# data = f.write("thisis first file")
# print(data)

# f = open("text.txt",'r')
# data = f.read()
# print(data)

# f = open("text.txt",'a')
# data = f.write(" give me more about python")
# print(data)

# f = open("text.txt",'a')
# data = f.writelines(["maths", "ml", "c#"])
# print(data)

# f = open("text.txt",'r')
# while True:  
#     data = f.readline()
#     print(data)
#     if not data:
#         break

# with open("text.txt",'r+') as f:
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("home.txt",'+w') as f:
#     f.write("hello python")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("ima.jpeg", "rb") as f:
#     data = f.read()
#     print(data)

import json

d = {"name":"aysh","email":"yash@gmail.com"}
with open("data.json",'w') as f:
    json.dump(d,f)