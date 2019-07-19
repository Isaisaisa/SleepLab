from keras import layers
from keras.models import Sequential
import sklearn.metrics as metrics


class CNN():

    def __init__(self):
        self.model = Sequential()

    def create_model(self, lengthOfSensors):
        #
        # data_format: Any = None, "channels_last":(batch, height, width, channels), "channels_first": (batch, channels, height, width)
        # output shape 1, 3617
        # ...
        # first try to build a CNN model

        # create model
        w = 300
        h = lengthOfSensors
        c = 1
        chanDim = -1
        # add model layers
        self.model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='same', input_shape=(h, w, c) ))
        self.model.add(layers.BatchNormalization(axis=-1))
        self.model.add(layers.ReLU())
        self.model.add(layers.MaxPool2D(pool_size=(1,2)))
        self.model.add(layers.Conv2D(32, kernel_size=3, padding='same'))
        self.model.add(layers.BatchNormalization(axis=-1))
        self.model.add(layers.ReLU())
        self.model.add(layers.Conv2D(16, kernel_size=3,padding='same'))
        self.model.add(layers.BatchNormalization(axis=-1))
        self.model.add(layers.ReLU())
        #self.model.add(layers.MaxPool2D(pool_size=(2,2)))
        #self.model.add(layers.BatchNormalization(axis=-1))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(300, activation='relu'))
        self.model.add(layers.Dropout(0.3))
        self.model.add(layers.Dense(100, activation='relu'))
        self.model.add(layers.Dropout(0.3))
        self.model.add(layers.Dense(5,activation='softmax'))

        # compile model using accuracy to measure model performance
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    #function to train the model
    def train(self, trainDataExpanded, oneHotGT):
        self.model.fit(x=trainDataExpanded, y=oneHotGT, epochs=5, batch_size=32, shuffle = True)

    #function to predict class labels
    def predfict(self, testData):
        predicted_classes = self.model.predict_proba(x=testData)
        return predicted_classes

    #function to calculate the f1 score
    def evaluate(self,y_true, y_pred):
        score = metrics.f1_score(y_true= y_true, y_pred = y_pred, average='macro')
        return score