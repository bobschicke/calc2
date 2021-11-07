""" This is Main.py """
class Calculator:
    """ This is the Calculator class"""

    # The input function will will put the first value in the object's result variable
    # This allows the program to only have to pass one value
    # (see commented main function below)

    # result is a class variable
    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_b):
        """ adds number to result """
        self.result = self.result + value_b
        return self.result

    def subtract_number(self, value_b):
        """ subtracts number from result"""
        self.result = self.result - value_b
        return self.result

    def multiply_numbers(self, value_b):
        """ multiplies two numbers and saves to result """
        self.result = self.result * value_b
        return self.result

    def divide_numbers(self, value_b):
        """ divides two numbers and stores the result"""
        # This catches a divide by 0 error
        if value_b == 0:
            return "DivBy0"
        self.result = self.result / value_b
        return self.result

#def main():
# """ This is the Main function """
# calc = Calculator()
# leave = "a"
# while leave not in ("x", "X"):
#     calc.result = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))
#     operator = input("Enter an Operator: ")
#     if operator == '+':
#         answ = calc.add_number(num2)
#     if operator == '-':
#         answ = calc.subtract_number(num2)
#     if operator == '*':
#         answ = calc.multiply_numbers(num2)
#     if operator == '/':
#         answ = calc.divide_numbers(num2)
#
#     print(answ)
#
#     leave = input("c to continue: x to exit: ")
