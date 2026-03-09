num = "10110"
power = 0
sum = 0
for i in num[::-1]:
    sum = sum + int(i) * (2 ** power)
    power += 1
print(sum)