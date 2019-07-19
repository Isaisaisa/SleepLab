# SleepLab

    
### Configure config file

We have a config file in this project calling ```` config.py ````. This file should be copied and the copied file should 
be renamed to ``` config_dev.py ```. Then you can configure the paths to the origin recorded data.
The constant ``` SAVEPATH ``` defines where the processed data will be saved e.g. the recorded data as numpy array.
The respective folders are created when starting the process/program.
    
### Rename the patients

We renamed the patient folder names so simplify the process. 
Each patient folder got an identity from 1 to 5 according "patientIDs_README.txt"


### Run project

    python PATH\TO\PROJECT\SleepLab\main.py
    
### Project structure
For each Process step we have a separated class/file. The file main.py starts all the Process at once and includes some boolean variables as switches. When you start it for the first time, all swtiches should be set to "True". Some new folders will be created under the path you specified under ```SAVEPATH``` in the configuration file (see the heading [Configure config file](#marker-hHeader-configure-config-file)).
Make sure the recorded data files are stored under the path you specified under ````LOADPATH````
Additionally add the patients id´s and the names of the sensor you want to use to the list. Here is an example

    LOAD_RAW_DATA_AND_SAVE_IT_AS_NUMPY_ARRAY = True
    LOAD_SAVED_NUMPY_DATA_AND_DOWNSAMPLE = True

    # add the sensors that should be used
    listOfSensors = []
    listOfSensors.append("C4M1_10HZ")
    listOfSensors.append("C3M2_10HZ")
    listOfSensors.append("F3M2_10HZ")
    listOfSensors.append("O1M2_10HZ")
    listOfSensors.append("REOGM1_10HZ")

    # add the patient IDs that should be used
    listOfPatients = [1,2,3,4,5]
    
Further classes/files:

```CNN.py```:  Provides the CNN architecture and some functions to train the net

```DataHandler.py```:  Functions to read CSV data and handle data

```PreProcessing.py```: Provide functions to segment and downsample data

All process-specific settings can be read in the report. 
