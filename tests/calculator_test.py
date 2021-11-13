""" These are the tests for the Calculator """
import pytest
from calculator.calculator import Calculator

@pytest.fixture
def clear_hist():
    """ Clears the history in calc_history list """
    Calculator.clear_calc_history()

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

def test_get_last_result(clear_hist):
    """ Tests that the function returns the last result in calc_history """
    #clear_hist()
    assert Calculator.add(5, 4) == 9
    assert Calculator.add(6, 4) == 10
    assert Calculator.get_last_result_in_history() == 10

def test_get_first_result(clear_hist):
    """ Tests that the function returns the first result in calc_history """
    #clear_hist()
    assert Calculator.add(5, 4) == 9
    assert Calculator.add(6, 4) == 10
    assert Calculator.get_first_result_in_history() == 9

def test_count_history(clear_hist):
    """ Tests that the number of calculations in calc_history is correct """
    #clear_hist()
    assert Calculator.count_history() == 0
    assert Calculator.add(5, 4) == 9
    assert Calculator.add(6, 4) == 10
    assert Calculator.count_history() == 2

def test_get_history(clear_hist):
    """ The return value of get_calc_history() is a list of the calculation results from history"""
    # This tests that the returned list has the calculation history results
    # in order from oldest to newest
    #clear_hist()
    #get_calc_history
    assert Calculator.count_history() == 0
    assert Calculator.add(5, 4) == 9
    assert Calculator.add(6, 4) == 10
    assert Calculator.count_history() == 2
    hist_list =  Calculator.get_calc_result_history()
    assert len(hist_list) == 2
    assert  hist_list[0] == 9
    assert hist_list[1] == 10

def test_clear_hist(clear_hist):
    """ Tests that calc_history list is cleared """
    #clear_hist()
    assert Calculator.add(5, 4) == 9
    assert Calculator.add(6, 4) == 10
    assert Calculator.count_history() == 2
    assert Calculator.clear_calc_history() is True
    assert Calculator.count_history() == 0
