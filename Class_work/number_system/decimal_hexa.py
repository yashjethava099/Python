num = 456
sum = ""
m = 1
l=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while num !=0:
    rem = num%16
    sum = l[rem]+sum
    num//=16
print(sum)