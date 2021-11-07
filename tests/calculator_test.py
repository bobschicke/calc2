""" These are the tests for the Calculator """
from calculator.main import Calculator

def test_calculator_result():
    """ Tests that Calculator's reset variable's initial value is 0 """
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """ Tests Addition of 2 numbers"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.result = 5
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 9

def test_calculator_subtract():
    """ Tests Subtraction of 2 numbers """
    calc = Calculator()
    calc.result = 5
    calc.subtract_number(7)
    assert calc.get_result() == -2

def test_calculator_multiply():
    """ Tests Multiplication of two numbers """
    calc = Calculator()
    calc.result = 3
    result  = calc.multiply_numbers(2)
    assert result == 6

def test_calculator_divide():
    """ Tests Division of two numbers """
    calc = Calculator()
    calc.result = 6
    result  = calc.divide_numbers(3)
    assert result == 2

def test_calculator_divide_by0():
    """ Tests that Division by Zero catches the error and doesn't crash the program """
    calc = Calculator()
    calc.result = 6
    result  = calc.divide_numbers(0)
    assert result == "DivBy0"
