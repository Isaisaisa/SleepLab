from keras import layers

def forward():
    #
    # data_format: Any = None, "channels_last":(batch, height, width, channels), "channels_first": (batch, channels, height, width)
    b = 1 # must be redefined
    w = 1 # must be redefined
    h = 1 # must be redefined
    c = 1
    layers.Conv2D(filters=50, kernel_size=(2,2), strides=(1, 1), padding='valid', use_bias=True, input_shape=(b, w, h, c))
    layers.BatchNormalization(axis=1)
    layers.ReLU()
    # output shape 1, 3617
    # ...
