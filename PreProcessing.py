# This file implements some functions to preprocess data
import scipy.signal as signal

#This function downsample data from
def downsample(data, frequency):
    data = signal.resample(data, frequency)
    return data