import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    
    arr = np.array(list).reshape(3,3)

    axis1_mean = arr.mean(axis=0)
    axis2_mean = arr.mean(axis=1)
    lst_mean = np.mean(list)

    axis1_variance = arr.var(axis=0)
    axis2_variance = arr.var(axis=1)
    lst_variance = np.var(list)

    axis1_stddev =  arr.std(axis=0)
    axis2_stddev =  arr.std(axis=1)
    lst_standarddev = np.std(list)

    axis1_max = arr.max(axis=0)
    axis2_max = arr.max(axis=1)
    lst_max = np.max(list)

    axis1_min = arr.min(axis=0)
    axis2_min = arr.min(axis=1)
    lst_min = np.min(list)

    axis1_sum = arr.sum(axis=0)
    axis2_sum = arr.sum(axis=1)
    lst_sum = sum(list)

    results = {
        
        'mean': [axis1_mean, axis2_mean, lst_mean],
        'variance': [axis1_variance, axis2_variance, lst_variance],
        'standard_dev': [axis1_stddev, axis2_stddev, lst_standarddev],
        'max' : [axis1_max, axis1_max, lst_max],
        'min' : [axis1_min, axis2_min, lst_min],
        'sum' : [axis1_sum, axis2_sum, lst_sum,]
    }


    return results

calculate([0,1,2,3,4,5,6,7,8])

