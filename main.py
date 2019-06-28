import DataHandler
import numpy as np

#switches
LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY = False
LOAD_SAVED_NUMPY_DATA = True


# add the sensors that should be used
listOfSensors = []
listOfSensors.append("REOGM1_150HZ")
listOfSensors.append("C4M1")
listOfSensors.append("C3M2")
listOfSensors.append("F3M2")
listOfSensors.append("O1M2")

# add the patient IDs that should be used
listOfPatients = [1,2,3,4,5]

# this loop only needs to run if the program is executed for the first time --> This can take a few minutes
if LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY:
    for sensor in listOfSensors:
        for patient in listOfPatients:
            DataHandler.readCSVDataAndSaveAsNumpy(sensor, patient)

# load the saved numpy arrays
if LOAD_SAVED_NUMPY_DATA:
    dataEOG = np.zeros((len(listOfPatients),len(listOfSensors)))




# downsample the signals from the different sample frequency to 30 HZ
# 10 hour of signal with 30 HZ --> 30 * 60 * 60 * 10 = 1080000

