# This file implements some functions to preprocess data
import scipy.signal as signal
import numpy as np

#This function downsample data 'data' with the given 'frequency'
def downsample(data, frequency):
    data = signal.resample(data, frequency)
    return data

#This function segments the data in 30 seconds window and returns it as 3d numpy array
#input data is a list of 2d numpy arrays
#   list dimension -> number of patient
#   np array first dimension --> XX sensors
#   np array second dimension --> ~10 hours of data
#output data is a 3d numpy array
#   first dimension --> number of sample
#   second dimension --> number of sensors
#   third dimension --> 30 second of the origin input data at 10 Hz = 300 data points
def segmentData(data):
    #number of datapoints, 30 seconds with 10 Hz --> 300 datapoints
    numberOfDataPoints = 30 * 10
    # calculate the total number of 30 seconds windows
    # only full 30 second windows will be used --> remaining parts are discarded
    numberOfWindows  = 0
    for dataSet in data:
        numberOfWindows += dataSet.shape[1] // numberOfDataPoints
    #create empty array for segmented data
    dataSegmented = np.zeros((numberOfWindows , data[0].shape[0], numberOfDataPoints))

    #save the windows into 3d numpy array, specified as given above
    counter = 0
    for dataSet in data:
        for i in range(0, dataSet.shape[1], numberOfDataPoints):
            if i+numberOfDataPoints <= dataSet.shape[1]:
                dataSegmented[counter, :,:] = dataSet[:,i : i+numberOfDataPoints]
                counter = counter + 1

    return dataSegmented

