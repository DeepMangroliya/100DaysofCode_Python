from art import logo

# addition
def add(n1,n2):
    return n1+n2

# subtraction
def subtract(n1,n2):
    return n1-n2

# multiplication
def multiply(n1,n2):
    return n1*n2

# division
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

print(logo)

def calculator():
    num1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from line above: ")

        num2 = float(input("Enter Next number: "))

        function = operations[operation_symbol]
        answer = round(function(num1,num2),2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' continue calculation with {answer} and 'n' to exit : ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
        
        
    

calculator()