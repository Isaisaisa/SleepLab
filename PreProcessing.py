# This file implements some functions to preprocess data
import scipy.signal as signal

#This function downsample data from
def downsample(data, frequency):
    return signal.resample(data, frequency * 60 * 60 * 10)