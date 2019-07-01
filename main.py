import DataHandler
import PreProcessing
import numpy as np
import config_dev as cfg
import matplotlib.pyplot as plt

#switches
LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY = False
LOAD_SAVED_NUMPY_DATA = True


# add the sensors that should be used
listOfSensors = []
#listOfSensors.append("REOGM1_150HZ")
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

# load the saved numpy arrays into a dictionary
patDict = {}
if LOAD_SAVED_NUMPY_DATA:
    for patient in listOfPatients:
        key = patient

        length = np.load(cfg.SAVEPATH + str(patient) + "\\" + listOfSensors[1] + ".npy").shape[1]
        data = np.zeros((len(listOfSensors), length))

        for idx, sensor in enumerate(listOfSensors):
            data[idx,:] = DataHandler.loadNumpySensorData(sensor, patient)

        patDict[key] = data

#print(patDict)
print(patDict[1].shape   )
patDictResampled  = {}
# downsample the signals from the different sample frequency to 30 HZ
# 10 hour of signal with 30 HZ --> 30 * 60 * 60 * 10 = 1080000
targetFrequency = 10


for key in patDict:
    data = patDict[key]
    dataTime = patDict[key].shape[1] / 200
    dataResampled = np.zeros((len(listOfSensors),targetFrequency * 60 * 60 * dataTime))
    for idx, sensor in enumerate(listOfSensors):
        dataResampled[idx,:] = PreProcessing.downsample(data[idx], targetFrequency)
        DataHandler.saveNumpyData(dataResampled[idx,:], sensor + "_resampled", key)
    patDictResampled[key] = dataResampled

print(patDict[1].shape)


