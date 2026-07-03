while True:
    try: 
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"The division is {a / b}")

    except ValueError:
        print("Please dont perform bad typecasts")
    