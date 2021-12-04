import os
from csv_util.file_utils import Filehandler
from calculator.calculator import Calculator

def get_root_path():
    """This method gets the filename from path/filename"""
    absolute_path = os.path.abspath(__file__)
    end = absolute_path.find("tests")  # find current directory
    root_path = absolute_path[:end]
    print("root_path = " + root_path)
    return root_path


def test_read_csv():
    root_path = get_root_path()
    nump_array = Filehandler.read_csv(root_path + "/tests/test.csv")
    assert len(nump_array) == 4  #4 rows of data

def test_do_calcs():
    # do_calcs (rec_num, row_array, func, calc_type, filename)
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.add, "Addition", "test") == 209
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.subtract, "Subtraction", "test") == 191
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.multiply, "Addition", "test") == 3200
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.divide, "Addition", "test") == 12.5

