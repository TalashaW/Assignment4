#calculator_calculations.py

# Import ABC (Abstract Base Class) and abstractmethod from Python's abc module.
from abc import ABC, abstractmethod

# Import the Operation class from the app.operation module. 
from app.operation import Operation

# -----------------------------------------------------------------------------------
# Abstract Base Class: Calculation
# -----------------------------------------------------------------------------------
"""(ABC) Stands for abstract base class.
This class is set up as a base for any type of calculator involving two numbers"""
class Calculation(ABC):

    def __init__(self, a: float, b: float) -> None:
        """
        Initializes a Calculation instance with two operands (numbers involved in the calculation).
       Float is used instead of int so that the calculator can accept decimals and integers.
        """
        self.a: float = a  # Stores the first operand as a floating-point number.
        self.b: float = b  # Stores the second operand as a floating-point number.

    @abstractmethod
    def execute(self) -> float:
        
        pass  # The actual implementation will be provided by the subclass. # pragma: no cover

    def __str__(self) -> str:
        """
      defines a base class for a calculator operation 
      that requires subclasses to implement their own calculation 
      logic through the execute() method.
        """
        result = self.execute()  # Run the calculation to get the result.
        operation_name = self.__class__.__name__.replace('Calculation', '')  # Gets the operation name.
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}" #returns the math operation being performed.

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

# -----------------------------------------------------------------------------------
# Factory Class: CalculationFactory
# -----------------------------------------------------------------------------------
class CalculationFactory:
    """
    The CalculationFactory is a **Factory Class** responsible for creating instances 
    of Calculation subclasses. This design pattern allows us to encapsulate the 
    logic of object creation and make it flexible.

    **Why Use a Factory Class?**
    - **Single Responsibility Principle (SRP)**: The factory only deals with object creation. 
      This keeps our code organized, as the logic for creating different calculations is 
      separated from the calculations themselves.
    - **Open/Closed Principle (OCP)**: We can add new calculation types without changing 
      the existing codebase. We simply register new calculation classes, making our 
      code extensible and flexible to future modifications.
    """

    # _calculations is an empty dictionary to store the calculation types 
    # (like "add" or "subtract") to their respective classes.
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            # Convert calculation_type to lowercase to ensure consistency.
            calculation_type_lower = calculation_type.lower()
            # Check if the calculation type has already been registered to avoid duplication.
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            # Register the subclass in the _calculations dictionary.
            cls._calculations[calculation_type_lower] = subclass
            return subclass  # Return the subclass for chaining or additional use.
        return decorator  # Return the decorator function.

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        # If an invalid operator is selected, an error will display with supported operations
        if not calculation_class:
          raise ValueError(f"Unsupported calculation type: '{calculation_type}'")
      
        # Create and return an instance of the requested calculation class with the provided operands.
        return calculation_class(a, b)

# -----------------------------------------------------------------------------------
# Concrete Calculation Classes
# -----------------------------------------------------------------------------------

# Each of these classes defines a specific calculation type (addition, subtraction, 
# multiplication, or division). These classes inherit from Calculation, implementing 
# the `execute` method to perform the specific arithmetic operation. 

# Calculation Type Decorators

# Addition Definition 
@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    def execute(self) -> float:
        # Calls the addition method from the Operation module to perform the addition.
        return Operation.addition(self.a, self.b)

# Subtraction Definition
@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        # Calls the subtraction method from the Operation module to perform the subtraction.
        return Operation.subtraction(self.a, self.b)

#Multiplication Definition
@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
   

    def execute(self) -> float:
        # Calls the multiplication method from the Operation module to perform the multiplication.
        return Operation.multiplication(self.a, self.b)

#Division Definition
@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
  

    def execute(self) -> float:
        # Before performing division, check if `b` is zero to avoid ZeroDivisionError.
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        # Calls the division method from the Operation module to perform the division.
        return Operation.division(self.a, self.b)
