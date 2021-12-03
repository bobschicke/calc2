"""This is a class to handle CSV files"""
import time
import os
import pandas as pd
import numpy as np
from calculator.calculator import Calculator

class Filehandler:
    """This is the Filehandler Class"""

    calc_log = np.array([])

    @staticmethod
    def get_root_path():
        """This method gets the filename from path/filename"""
        absolute_path = os.path.abspath(__file__)
        end = absolute_path.find("csv_util")  # find current directory
        root_path = absolute_path[:end]
        print("root_path = " + root_path)
        return root_path

    @staticmethod
    def write_to_csv(numpy_array):
        """Method to Write a Numpy array to a CSV file"""
        # np.savetxt("calc_log.csv", numpy_array, delimiter=",")
        dataframe = pd.DataFrame(numpy_array, columns= ['Rec_Num', 'Unix Time',
                                                 'Filename', 'Operation', 'Result'])
        # noinspection PyTypeChecker
        dataframe.to_csv(Filehandler.get_root_path() + 'logs/calc_log.csv', index= False)


    @staticmethod
    def create_calc_log(rec_num, utime, filename, operation, result):
        """This is a method to collect log info in a numpy array"""
        temp_array = np.array([rec_num, utime, filename, operation, result])
        if len(Filehandler.calc_log) == 0:
            Filehandler.calc_log = np.append(Filehandler.calc_log, temp_array)
        else:
            Filehandler.calc_log = np.vstack([Filehandler.calc_log, temp_array])

    @staticmethod
    def do_calcs (rec_num, row_array, func, calc_type, filename):
        """This method gets passed the function and an array and calls the calc function"""
        result = func(row_array)
        if isinstance(result, str):
            print("error = " + result)
        Filehandler.create_calc_log(rec_num, time.time(), filename, calc_type, result)

    @staticmethod
    def process_csv(nump_arr, filename : str):
        """This method iterates through the array and calls the calc functions"""
        rows, columns = nump_arr.shape

        for row in range(rows):
            Filehandler.do_calcs((row * 4)+0, nump_arr[row][1:columns],
                                 Calculator.add, "Addition", filename)
            Filehandler.do_calcs((row * 4)+1, nump_arr[row][1:columns],
                                 Calculator.subtract, "Subtraction", filename)
            Filehandler.do_calcs((row * 4)+2, nump_arr[row][1:columns],
                                 Calculator.multiply, "Multiplication", filename)
            Filehandler.do_calcs((row * 4)+3, nump_arr[row][1:columns],
                                 Calculator.divide, "Division", filename)
        print("calc_log:")
        print(Filehandler.calc_log)
        print("Writing to CSV")
        Filehandler.write_to_csv(Filehandler.calc_log)
        print('done')

    @staticmethod
    def read_csv(eventsrcpath: str):
        """This method reads a CSV file and returns a numpy array"""
        print("***pandas_csv.py***")
        dataframe = pd.read_csv(eventsrcpath)
        print(dataframe.columns)
        # pylint: disable=no-member
        nump_arr = dataframe.values
        print("***Numpy array:***")
        print(nump_arr)
        return nump_arr
