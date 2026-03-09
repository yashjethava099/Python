num = 1634
var = len(str(num))
temp = num
sum = 0
while num !=0:
    rem = num%10
    sum+=pow(rem,var)
    num=num//10   
if temp==sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")