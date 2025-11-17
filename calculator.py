def calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("q : Quit")
    
    while True:
        try:
        
            num1 = float(input("\nEnter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
        
            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
                
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
                
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
                
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
                    
            else:
                print("Invalid operation! Please use +, -, *, or /")
                
        except ValueError:
            print("Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\nCalculator closed.")
            break


calculator()