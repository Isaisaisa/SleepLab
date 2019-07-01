import numpy as np
import csv
import config_dev as cfg
import os
#This file implements some functions to handle data (save, load, ....)


# Function to read CSV data from the 'fileName'
# Returns data object (numpy array)
def readCSVData(fileName, patientID):
    with open(cfg.LOADPATH+ str(patientID) + "\\" +  fileName + ".csv", "rt") as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',')
            #get the number of rows of the csv file
            row_count = sum(1 for row in dataReader)
            data = np.zeros((1, row_count))
            #reset the reader to the first row
            csvfile.seek(0)
            dataReader = csv.reader(csvfile, delimiter=',')
            #skip the first row due to unimportant informations
            next(dataReader)
            #read the data
            for row in dataReader:
                #print(row)
                data[0,dataReader.line_num-1] = float(row[0])
            return data

# save the given data 'data' under the name 'fileName' in the directory with the patients ID
# if the directory under cfg.SAVEPATH doesnt exists it will be created
def saveNumpyData(data, fileName, patientID):
    filepath = os.path.join(cfg.SAVEPATH, str(patientID),  fileName + '.npy')
    if not os.path.exists(filepath):
        #if not os.path.exists(cfg.SAVEPATH):
        os.makedirs(cfg.SAVEPATH + str(patientID) + "\\", exist_ok=True)
        print('numpy array does not exist yet (',filepath, ')' )
        np.save(filepath, data)

# functions that reads the given file 'fileName' of the specified patient and saves the data as numpy array
def readCSVDataAndSaveAsNumpy(fileName, patientID):
    data = readCSVData(fileName, patientID)
    saveNumpyData(data, fileName, patientID)
    return data

# this function loads the numpy array of the sensor data
def loadNumpySensorData(sensorName, patientID):
    return np.load(cfg.SAVEPATH + "\\" + str(patientID) + "\\" + sensorName + ".npy")