import pandas as pd
import numpy as np

class Filehandler:

    def test_pandas(self, eventsrcpath: str):
        print("***pandas_csv.py***")
        df = pd.read_csv(eventsrcpath)
        print(df.columns)
        nump_arr = df.to_numpy()
        print("***Numpy array:***")
        print(nump_arr)

        rows, columns = nump_arr.shape

        for row in range(rows):
            sum1 = nump_arr[row,1]
            print("result = " + str(nump_arr[row,0]))
            print("pre-sum = " + str(sum1))
            for col in range(1, columns):
                sum1 /= nump_arr[row,col]
                print("pre-sum = " + str(sum1))
                #print("value = " + str(value))
            print("sum = " + str(sum1))

    #if __name__ == "__main__":
    #test_pandas()