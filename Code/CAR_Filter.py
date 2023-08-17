import numpy as np
import pandas as pd


def car_filter(data):
    # !--------------------------------------- Check dimensional data ----------------------------------------
    if data.ndim < 3:
        if data.shape[0] < data.shape[1]:
            data = data.T
    # *---------------------------------- Calculating the Average Signal -------------------------------------
    data_car = np.zeros((data.shape))
    mean = np.mean(data, axis=1)                                                
    #  ---------------------------------- Subtracting the Average Signal -------------------------------------
    for ind in range(data.shape[1]):                      
        data_car[:, ind] = data.iloc[:, ind] - mean
    
    return pd.DataFrame(data_car)
