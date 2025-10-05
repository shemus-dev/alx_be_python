# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division safely, handling errors."""
    try:
        # Convert inputs to floats (this may raise ValueError)
        num = float(numerator)
        denom = float(denominator)

        # Attempt the division (this may raise ZeroDivisionError)
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric input (like 'ten')
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."
