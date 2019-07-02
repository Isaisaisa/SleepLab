import DataHandler
import PreProcessing
import numpy as np
import config_dev as cfg
import matplotlib.pyplot as plt

#switches
LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY = True
LOAD_SAVED_NUMPY_DATA_AND_DOWNSAMPLE = False


# add the sensors that should be used
listOfSensors = []
listOfSensors.append("C4M1_10HZ")
listOfSensors.append("C3M2_10HZ")
listOfSensors.append("F3M2_10HZ")
listOfSensors.append("O1M2_10HZ")
listOfSensors.append("REOGM1_10HZ")

# add the patient IDs that should be used
listOfPatients = [1,2,3,4,5]

# this loop only needs to run if the program is executed for the first time --> This can take a few minutes
if LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY:
    #for all sensors
    for sensor in listOfSensors:
        #for all patient
        for patient in listOfPatients:
            DataHandler.readCSVDataAndSaveAsNumpy(sensor, patient)

#load the saved numpy array and downsample it to 10 Hz --> This can take few minutes to hours...
if LOAD_SAVED_NUMPY_DATA_AND_DOWNSAMPLE:
    #frequency of the output data
    targetFrequency = 10

    #for all patients
    for patient in listOfPatients:
        #for all sensors
        for idx, sensor in enumerate(listOfSensors):
            #load the data of the current sensor and the current patient
            data = DataHandler.loadNumpySensorData(sensor, patient)
            if sensor == "REOGM1_150HZ":
                recordFrequency = 150
            else:
                recordFrequency = 200
            signalLength = data.shape[1] / recordFrequency
            #downsample the data --> output frequency: 10 HZ * number of seconds
            dataResampled = PreProcessing.downsample(data[0,:], targetFrequency * int(signalLength))
            #save the resampled data
            DataHandler.saveNumpyData(dataResampled, sensor + "_resampled", patient)

