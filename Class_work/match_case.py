check = "y"
while check == "y":
    num1 = int(input("enter num 1 "))
    num2 = int(input("enter num 2 "))

    print("1: add \n2: substraction \n3: multiplty \n4:divide")

    choice = int(input("enter your choice "))

    match choice:
        case 1 : print(num1+num2)
        case 2 : print(num1-num2)
        case 3 : print(num1*num2)
        case 4 : print(num1/num2)
        case _:print("enter valid value")
    check = input("enter y or n")
