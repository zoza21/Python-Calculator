'''
Simple calculator using Python
Author: zoarno
10082022
'''

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2


while True: 
    print("What operator would you like?")
    operator = input("Please enter the operator")
    if operator not in ['+', '-', '*', '/']:
        print("Invalid entry. Please select +, -, * or /")
    else: 
        break

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))


if operator == "+":
    print("The result is: + ", addition(num1, num2))

elif operator == "-":
    print("The result is: + ", subtraction(num1, num2))

elif operator == "*":
    print("The result is: + ", multiplication(num1, num2))

elif operator == "/":
    print("The result is: + ", subtraction(num1, num2))

else:
    print("Whoops. Invalid entry")

