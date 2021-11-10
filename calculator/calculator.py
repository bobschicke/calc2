""" This is Main.py """

# These import the namespaces
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division


class Calculator:
    """ This is the Calculator class"""

    # calc history will save calculation objects
    calc_history = []

    # The input function will will put the first value in the object's result variable
    # This allows the program to only have to pass one value
    # (see commented main function below)

    # result is a class variable
    result = 0

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Adds a calculation object to the history list"""
        Calculator.calc_history.append(calculation)
        return True

    @staticmethod
    def get_last_result_in_history():
        """ Returns the last calculation (-1 signifies the last value in the list) """
        return Calculator.calc_history[-1].get_result()

    @staticmethod
    def add(value_a, value_b):
        """ adds 2 numbers and save them to calc_history list """
        # This instantiates an addition object which passes value_a and value_b to the constructor
        add = Addition.instantiate(value_a,value_b)
        # This adds the calculation to calc_history list
        Calculator.add_calculation_to_history(add)
        # This uses the base class method to get the result from the object
        return add.get_result()

    @staticmethod
    def subtract(value_a, value_b):
        """ adds 2 numbers and save them to calc_history list """
        # This instantiates a Subtraction object which passes value_a and value_b to the constructor
        sub = Subtraction.instantiate(value_a,value_b)
        # This adds the calculation to calc_history list
        Calculator.add_calculation_to_history(sub)
        # This uses the base class method to get the result from the object
        return sub.get_result()

    @staticmethod
    def multiply(value_a, value_b):
        """ adds 2 numbers and save them to calc_history list """
        # This instantiates a Multiplication object which passes value_a and value_b
        # to the constructor
        mult = Multiplication.instantiate(value_a,value_b)
        # This adds the calculation to calc_history list
        Calculator.add_calculation_to_history(mult)
        # This uses the base class method to get the result from the object
        return mult.get_result()

    @staticmethod
    def divide(value_a, value_b):
        """ adds 2 numbers and save them to calc_history list """
        if value_b == 0:
            return "DivBy0"
        # This instantiates a Division object which passes value_a and value_b to the constructor
        div = Division.instantiate(value_a,value_b)
        # This adds the calculation to calc_history list
        Calculator.add_calculation_to_history(div)
        # This uses the base class method to get the result from the object
        return div.get_result()

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
