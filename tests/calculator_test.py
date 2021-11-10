""" These are the tests for the Calculator """
from calculator.calculator import Calculator

def test_calculator_result():
    """ Tests that Calculator's reset variable's initial value is 0 """

    assert Calculator.result == 0

def test_calculator_add():
    """ Tests Addition of 2 numbers"""
    assert Calculator.add(5, 4) == 9

def test_calculator_subtract():
    """ Tests Subtraction of 2 numbers """
    assert Calculator.subtract(5, 4) == 1

def test_calculator_multiply():
    """ Tests Multiplication of two numbers """
    assert Calculator.multiply(5, 4) == 20

def test_calculator_divide():
    """ Tests Division of two numbers """
    assert Calculator.divide(12, 4) == 3

def test_calculator_divide_by0():
    """ Tests that Division by Zero catches the error and doesn't crash the program """
    assert Calculator.divide(5, 0) == "DivBy0"
