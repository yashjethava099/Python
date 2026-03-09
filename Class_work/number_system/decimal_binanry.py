num = 45
sum = 0
m = 1
while num !=0:
    rem = num%2
    sum = sum+(rem*m)
    num//=2
    m*=10
print(sum)