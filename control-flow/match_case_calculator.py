# Assign the two values and the desired result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

# Calculation using match case conditional

match operator:
    case "+":
        result = num1 + num2
    case "*":
        result = num1 * num2

    case "/" if num2 != 0:
        result = num1/num2
    case _ if num2 != 0:
        print("Cannot divide by zero.")
    
if operator in ["+","-","*","/"] and num2 != 0:
    print(f"The result is {result}.")
        
        

        
