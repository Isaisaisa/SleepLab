import DataHandler
import PreProcessing
import numpy as np
import config_dev as cfg
import os
import matplotlib.pyplot as plt

#switches
LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY = False
LOAD_SAVED_NUMPY_DATA_AND_DOWNSAMPLE = False
SEGMENT_WINDOW_AND_SAVE_AS_NUMPY_ARRAY = True
LOAD_LABELS_AND_SAVE_IT_AS_NUMPY_ARRAY = True

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

#Segmentation
if SEGMENT_WINDOW_AND_SAVE_AS_NUMPY_ARRAY:
    #load the data from numpy arrays and save in dataList as 3d numpy array
    #   first dimension -> number of patient
    #   second dimension --> XX sensors
    #   third dimension --> ~10 hours of data

    sensorData = []
    for patient in listOfPatients:
        dataLength = DataHandler.loadNumpySensorData(listOfSensors[0], patient).shape[1]
        tempData = np.zeros((len(listOfSensors), dataLength))
        for idxSensor, sensor in enumerate(listOfSensors):
            tempData[idxSensor,:] = DataHandler.loadNumpySensorData(sensor,patient)
        sensorData.append(tempData)

    #segmentedData contains the segmented 30 sec windows as discussed in a 3d numpy array
    #   first dimension --> number of samples
    #   second dimension --> number of sensors
    #   third dimension --> 30 second of the origin input data at 10 Hz = 300 data points
    segmentedData = PreProcessing.segmentData(sensorData)
    filepath = os.path.join(cfg.SAVEPATH, 'segmentedData' + '.npy')
    np.save(filepath, segmentedData)
    print(segmentedData.shape)



if LOAD_LABELS_AND_SAVE_IT_AS_NUMPY_ARRAY:
    #extract labels from csv file
    labels = np.zeros(0)
    for patient in listOfPatients:
        label_pat = PreProcessing.extract_labels(patient)
        labels = np.append(labels, label_pat[0])
    filepath = os.path.join(cfg.SAVEPATH, 'SleepStaging' + '.npy')
    np.save(filepath, labels)
