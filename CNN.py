from keras import layers
from keras.models import Sequential


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
        # model = Sequential()
        w = 300  # must be redefined
        h = lengthOfSensors  # must be redefined
        c = 1
        chanDim = -1
        # add model layers
        self.model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(h, w, c)))
        self.model.add(layers.BatchNormalization(axis=-1))
        self.model.add(layers.Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(5, activation='softmax'))

        # compile model using accuracy to measure model performance
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    def train(self, trainDataExpanded, oneHotGT):
        self.model.fit(x=trainDataExpanded, y=oneHotGT, epochs=5)


    def predfict(self, testData):
        predicted_classes = self.model.predict(x=testData)
        return predicted_classes