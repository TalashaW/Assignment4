# TaLasha Winston
# Python for Web API Development
# Module 4: Command-Line Application with 100% Test Coverage
# Thomas Licciardello
# 9/30/2025

# Import the 'calculator' function from the 'app.calculator' module
from app.calculator import calculator

# If the script is run directly (i.e., not imported), the condition is True, and the calculator will start.
if __name__ == "__main__":
    # Call the 'calculator' function to start the calculator program.
    # This will allow the user to interact with the calculator.
    calculator()
