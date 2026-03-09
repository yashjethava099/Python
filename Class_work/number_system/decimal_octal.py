num = 45
sum = 0
m = 1
while num !=0:
    rem = num%8
    sum = sum+(rem*m)
    num//=8
    m*=10
print(sum)