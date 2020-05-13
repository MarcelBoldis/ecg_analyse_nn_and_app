try:
    import sys
    import numpy as np
    from sklearn.model_selection import train_test_split
    import gc
    import tensorflow as tf
    import keras
    from keras.models import Sequential
    from keras.preprocessing.image import ImageDataGenerator
    from keras.layers import Conv2D, Dropout, Dense, Flatten, MaxPooling2D, Activation
    from keras.layers.normalization import BatchNormalization
    from keras.optimizers import Adam
    from keras.callbacks import ModelCheckpoint, EarlyStopping
    import matplotlib.pyplot as plt
    from keras.utils import plot_model
    from sklearn.metrics import classification_report, confusion_matrix

except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def neural_network_model():
    # Parameters
    epochs = 30
    batch_size = 64
    num_clases = 7
    img_size = [128, 128]

    generator = ImageDataGenerator(rescale=1. / 255)
    test_gen = ImageDataGenerator(rescale=1. / 255)

    checkpoint = ModelCheckpoint(
        '/content/drive/My Drive/Diplomovka/my_model.h5',
        monitor='val_accuracy',
        verbose=1,
        save_best_only=True,
        mode='max')

    early_stop = EarlyStopping(
        monitor='val_loss',
        mode='min',
        verbose=1,
        patience=10)

    callbacks_list = [checkpoint, early_stop]

    # Model
    model = Sequential()

    model.add(Conv2D(32, (3, 3), strides=(1, 1), input_shape=(128, 128, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())

    model.add(Conv2D(32, (3, 3), strides=(1, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Conv2D(64, (3, 3), strides=(1, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())

    model.add(Conv2D(64, (3, 3), strides=(1, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Conv2D(128, (3, 3), strides=(1, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())

    model.add(Conv2D(128, (3, 3), strides=(1, 1), kernel_initializer='glorot_uniform'))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(1024))
    model.add(keras.layers.ReLU())
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    adam = Adam(lr=0.0001)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

    print(model.summary())
    # plot_model(model, to_file='/content/drive/My Drive/Diplomovka/model.png')

    valid_data_path = '/content/test_train_data/valid'
    train_data_path = '/content/test_train_data/train'

    valid_generator = generator.flow_from_directory(
        valid_data_path,
        target_size=img_size,
        shuffle=False,
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical')

    train_generator = generator.flow_from_directory(
        train_data_path,
        target_size=img_size,
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical')

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=37703 // batch_size,
        epochs=epochs,
        validation_data=valid_generator,
        validation_steps=9433 // batch_size,
        callbacks=callbacks_list,
        verbose=1)

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.ylim([0, 1])
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.ylim([0, 2])
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
