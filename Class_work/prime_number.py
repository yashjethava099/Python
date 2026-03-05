total = 0
for i in range(3,101):
    flag = 0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(f"{i} is prime")

        total +=i
print(total)
        
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)