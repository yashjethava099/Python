num = "154"
power = 0
sum = 0
for i in num[::-1]:
    sum = sum + int(i) * (8 ** power)
    power += 1
print(sum)