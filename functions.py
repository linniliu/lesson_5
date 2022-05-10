# Subroutine

def greet(fname):
    print("Hello " + fname)

greet("Linda")

# Now make the subroutine a Function

def greet(fname):
    return "Hello " + fname

print(greet("Linda"))

#Tip: always try to to a function instead of a subroutine

#1 return per function, ie:

def calculate(method, num1, num2):
    if method == "add":
        return num1 + num2

    if method == "subtract":
        return num1 - num2

print(calculate("add", 1, 2))

#Note: as soon as we have 1 return, the function stops executing
#Note: if you want to keep executing the returns, you have to put it in a loop

#If you want to run more than 1 return, use dictionaries, ie:

def calculate_both(num1, num2):
    result = {}
    result['sum'] = num1 + num2
    result['difference'] = num1 - num2
    return result

print(calculate_both(2, 4))