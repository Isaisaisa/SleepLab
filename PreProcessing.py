# This file implements some functions to preprocess data
import scipy.signal as signal
import numpy as np
import csv
import config_dev as cfg

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
    numberOfWindows  = 0
    for dataSet in data:
        #numberOfWindows += dataSet.shape[1] // numberOfDataPoints
        numberOfWindows += np.ceil(dataSet.shape[1] / numberOfDataPoints)
    #create empty array for segmented data
    dataSegmented = np.zeros((int(numberOfWindows) , data[0].shape[0], numberOfDataPoints))

    #save the windows into 3d numpy array, specified as given above
    counter = 0
    for dataSet in data:
        for i in range(0, dataSet.shape[1], numberOfDataPoints):
            #full 30 second windows
            if i+numberOfDataPoints <= dataSet.shape[1]:
                dataSegmented[counter, :,:] = dataSet[:,i : i+numberOfDataPoints]
                counter = counter + 1
            #remaining elements, not full 30 second windows, fill up with zeros
            else:
                remainingElements = dataSet.shape[1] - i
                tempArray = np.zeros((dataSet.shape[0],dataSet.shape[1] +1))
                tempArray = dataSet[:, i : i + remainingElements]
                concatenatedArray = np.concatenate((tempArray, np.zeros((5, numberOfDataPoints - remainingElements))),1)
                dataSegmented[counter, :,:] = concatenatedArray
                counter = counter + 1

    return dataSegmented

# this function extract the labels from the csv files and changes the strings to numbers
#this function extract the labels from the csv files and changes the strings to numbers
def extract_labels(patNr):
    path = cfg.LOADPATH + str(patNr) + "\\SleepStaging.csv"
    with open(path, 'rt') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        # get the number of rows of the csv file
        row_count = sum(1 for row in dataReader)
        # reset the reader to the first row
        csvfile.seek(0)
        dataReader = csv.reader(csvfile, delimiter=',')
        # skip the first row due to unimportant informations
        next(dataReader)

        label = np.zeros((1, row_count-1))
        #change the string label to numbers
        label_dict = {"WK": 1, "REM": 2, "N1": 3, "N2": 4, "N3": 5}
        # read the data
        for row in dataReader:
            row[2] = label_dict[row[2]]
            #print(row[2])
            label[0, dataReader.line_num - 2] = row[2]
        return label