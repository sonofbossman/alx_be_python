class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of a and b."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b