def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

def calculator():
    print("Simple Calculator: +, -, *, /")
    op = input("Choose operation: ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if op == '+': print(f"Result: {add(num1, num2)}")
    elif op == '-': print(f"Result: {subtract(num1, num2)}")
    elif op == '*': print(f"Result: {multiply(num1, num2)}")
    elif op == '/': print(f"Result: {divide(num1, num2)}")
    else: print("Invalid operator")

#Example
if __name__ == "__main__":
    calculator()