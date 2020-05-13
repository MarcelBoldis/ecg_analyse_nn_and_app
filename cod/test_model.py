try:
    import sys
    import cv2
    from sklearn.metrics import classification_report, confusion_matrix
    from keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt
    from keras.models import load_model
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def test_model():
    model = load_model('my_model_97.h5')

    generator = ImageDataGenerator(rescale=1./255)
    test_data_path = '../test_train_data/test'
    test_generator = generator.flow_from_directory(
            test_data_path,
            target_size=[128,128],
            shuffle=False,
            color_mode='grayscale',
            batch_size=64,
            class_mode='categorical')

    Y_pred = model.predict_generator(test_generator, workers=0)
    y_pred = np.argmax(Y_pred, axis=1)
    print(Y_pred)
    print(y_pred)
    print('Confusion Matrix')
    cm = confusion_matrix(test_generator.classes, y_pred)
    print(confusion_matrix(test_generator.classes, y_pred))
    print('Classification Report')
    target_names = ['APC', 'LBB', 'NOR', 'PAB', 'PVC', 'RBB', 'VEB']
    print(classification_report(test_generator.classes, y_pred, target_names=target_names))

    df_cm = pd.DataFrame(cm, range(7), range(7))
    sn.set(font_scale=1.4)
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}, xticklabels=target_names, yticklabels=target_names)
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix')
    plt.show()
