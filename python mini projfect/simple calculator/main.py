try: 
    a = int(input("Enter the number a:  "))
    b = int(input("Enter the number b:  "))

    print("what kind of operation you want to do? + , -, *, /")
    

    o = input("Enter the operation: ")
    match o:
        case "+":
            print(f"The value of a + B is: {a+b}")
        case "-":
            print(f"the value of a - B is: {a-b}")
        case "*":
            print(f"the value of a * B is: {a*b}")
        case "/":
            print(f"the value of a / B is: {a/b}")
        case default:
            print("Enter a valid input")

except Exception as e: 
    print("Enter a valid input of \"a\" and \"b\"")