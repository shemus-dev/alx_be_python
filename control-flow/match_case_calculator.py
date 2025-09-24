num1 = int(input("Enter the first number: "))
num2  = int(input("Enter the second number:"))
perform = input("Choose the operation (+, -, *, /):")

match perform:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2 
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            result = None
        else:
            result = num1/num2
            print(f"The result is {result}")

    case _:
          print("Invalid operation! Please choose from +, -, *, /")
          result = None

