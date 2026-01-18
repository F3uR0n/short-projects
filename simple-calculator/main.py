try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    op = (input("Enter any One Operation + - * / : "))
    match op:
        case "+":
            print("Answer", a+b)
        case "-":
            print("Answer", a-b)
        case "*":
            print("Answer", a*b)
        case "/":
            print("Answer", a/b)
        case default:
            print("There was an Error")
except Exception as e:
    print("Enter a Valid Number")