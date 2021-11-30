import pandas as pd
import numpy as np
def test_pandas():
    print("pandas_csv.py")
    df = pd.read_csv('events/temp.csv')
    #print(df.to_string())
    for i, row in df.iterrows():
        while i < 3:
            print(f'i = {i}')
            print('')
            print(row)