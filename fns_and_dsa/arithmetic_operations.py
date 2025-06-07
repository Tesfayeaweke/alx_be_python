# function to perform operation
def perform_operation(num1, num2, operation):

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
          return num1 * num2
    elif operation == 'divide':
         if num2 == 0:
              return "The second number can't be zero."
         else:
              return num1 / num2
    else:
         return "Error, check the values entered." 
    """
match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide' if num2 != 0:
            return num1 / num2
        case _:
            return "Error, check the values entered." 



    """
    
