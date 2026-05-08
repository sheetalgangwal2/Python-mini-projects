while True:
    print("MINI CALCULATOR")
    print()
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    print()
    print("Please choose operation : \nfor SUM press 1 \nfor DIFFERNCE press 2 \nfor PRODUCT press 3 \nfor DIVISION press 4")
    print()
    x = input("choose operations : ")

    if(x == "1"):
     print("SUM : ", a + b)
    elif(x =="2"):
     print("DIFFERENCE : ", a - b)
    elif(x == "3"):
     print("PRODUCT : ", a * b)
    elif(x == "4"):
     print("DIVISION : ", a / b)

    else:
     print("please choose number between 1 to 4 for suitable results.")

    print("THANK YOU!")
    print()
    