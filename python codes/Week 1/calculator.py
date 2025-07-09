num1=float(input("Enter the number: "))
num2=float(input("Enter the number"))
while True:
    print("-------------Simple calculator-----------")
    print("1.addition of numbers")
    print("2.muliplication of number")
    print("3.subtraction of number")
    print("4.division of number")
    print("5.exit")
    choice=input("Enter the choice(1-5):")
    if choice=="5":
        print("exit,goodbye")
    elif choice=="4":
        result=num1/num2
        print("result:",result)
    elif choice=="3":
        result=num1-num2
        print("result:",result)
    elif choice=="2":
        result=num1*num2
        print("result:",result)
    elif choice=="1":
        result=num1+num2
        print("result:",result)
    else:
        print("wrong choice")
        