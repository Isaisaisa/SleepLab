import numpy as np
import csv
import config_dev as cfg
import os
# Function to read CSV data at the 'input' path
# Returns data object (numpy array)

def readCSVData(fileName, patientID):
    with open(cfg.LOADPATH+ patientID + fileName + ".csv", "rt") as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',')
            #row_count = sum(1 for row in dataReader)
            row_count = 4909651
            data = np.zeros((1, row_count))
            next(dataReader)
            for row in dataReader:
                #print(row)
                data[0,dataReader.line_num-1] = float(row[0])
            return data

def saveNumpyData(data, fileName, patientID):
    filepath = cfg.SAVEPATH + patientID +  fileName + '.npy'
    if not os.path.exists(filepath):
        if not os.path.exists(cfg.SAVEPATH):
            os.makedirs(cfg.SAVEPATH, exist_ok=True)
        print('numpy array does not exist yet')
        np.save(filepath, data)


def readCSVDataAndSaveAsNumpy(fileName, patientID):
    data = readCSVData(fileName, patientID)
    saveNumpyData(data, fileName, patientID)
    return data