#function for calculation
def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
#listing valid operators
operators = ["+", "-", "*", "/"]
print("=== Simple Calculator ===")
print("Available operations:", operators)
#loop for continuous calculation
while True:
    #user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    #calling funcion
    result = calculator(num1, num2, op)
    print("Result:", result)
    #ask to keep calculationg 
    choice = input("Do you want to calculate again? (y/n): ").lower()
    if choice != "y":
        print("Exiting calculator. Goodbye!")
        break