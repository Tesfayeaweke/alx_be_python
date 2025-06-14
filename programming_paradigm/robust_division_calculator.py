def safe_divide(numerator,denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        division = numerator/denominator
    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of the division is {division}"
    


if __name__ == "__main__":
    safe_divide(10,5)
