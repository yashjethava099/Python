for i in range(100,1000):
    num = i
    temp = num
    sum = 0
    while num !=0:
        rem = num%10
        sum+=pow(rem,3)
        num=num//10
    if temp==sum:
        print(f"{temp} is armstrong")
    # else:
    #     print(f"{temp} is not armstrong")