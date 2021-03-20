from tensorflow.keras.layers import (Activation, Conv2D, Input, MaxPooling2D,
                                     UpSampling2D)
from tensorflow.keras.models import Model


def basic_autoencoder():
    # Defining our Image denoising autoencoder
    Input_img = Input(shape=(960, 1280, 3))

    # Encoding architecture
    x1 = Conv2D(16, (3, 3), activation='relu', padding='same')(Input_img)
    x1 = MaxPooling2D((2, 2), padding='same')(x1)
    x2 = Conv2D(32, (3, 3), activation='relu', padding='same')(x1)
    x2 = MaxPooling2D((2, 2), padding='same')(x2)
    x3 = Conv2D(64, (3, 3), activation='relu', padding='same')(x2)
    encoded = MaxPooling2D((2, 2), padding='same')(x3)

    # Decoding architecture
    x3 = Conv2D(64, (3, 3), activation='relu', padding='same')(encoded)
    x3 = UpSampling2D((2, 2))(x3)
    x2 = Conv2D(32, (3, 3), activation='relu', padding='same')(x3)
    x2 = UpSampling2D((2, 2))(x2)
    x1 = Conv2D(16, (3, 3), activation='relu', padding='same')(x2)
    x1 = UpSampling2D((2, 2))(x1)
    decoded = Conv2D(1, (3, 3), activation='tanh', padding='same')(x1)

    model = Model(Input_img, decoded)
    return model
