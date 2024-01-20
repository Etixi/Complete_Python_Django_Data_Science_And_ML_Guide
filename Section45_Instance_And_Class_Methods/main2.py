print()
print("Practice - Utilizing Static Methods in Classes" + "\n" +
      "===============================================")
print()

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        raise ValueError("can't divide by zero")


print(Calculator.add(20, 10))
print(Calculator.subtract(50, 28))
print(Calculator.mult(25, 25))
print(Calculator.divide(52, 13))