try:
    import sys
    import json
    import pandas as pd
    import pymongo
    import numpy as np
    import biosppy
    import cv2
    import os
    import imutils
    from flask_pymongo import PyMongo
    import matplotlib.pyplot as plt
    from .mongo_setup import setup
    from keras.models import load_model
    from keras.utils import CustomObjectScope
    from keras.initializers import glorot_uniform
    from keras.preprocessing.image import ImageDataGenerator
except ValueError:
    print("Modules loading failed in " + sys.argv[0])

model = load_model('my_model_97.h5')
print('Model loaded successfully!')


def allowed_file(filename, allowed_file_types):
    if not '.' in filename:
        return False
    temp = filename.rsplit(".", 1)[1]
    if temp.lower() in allowed_file_types:
        return True
    else:
        return False


def allowed_image_size(file_size, max_file_size):
    if int(file_size) <= max_file_size:
        return True
    else:
        return False


def save_file(file, mongo):
    try:
        num_coll = len(mongo.db.list_collection_names())
        coll_name = setup.get('COLLECTION_NAME') + str(num_coll)
        user_collection = mongo.db.get_collection(coll_name)
        store_file = file.to_dict('records')

        user_collection.insert_many(store_file)

        return True

    except ValueError:
        return False


def make_prediction(file, column_count):
    try:
        APC, LBB, NOR, PAB, PVC, RBB, VEB = [], [], [], [], [], [], []
        result = {"APC": APC, "LBB": LBB, "NOR": NOR, "PAB": PAB, "PVC": PVC, "RBB": RBB, "VEB": VEB}

        csv_data = file.iloc[:, column_count-1]
        data = np.array(csv_data)
        r_peaks = biosppy.signals.ecg.christov_segmenter(signal=csv_data, sampling_rate=360)[0]
        peak_data = data[r_peaks]

        coordinates = []
        indices = []
        bad_signal = []
        counter = 1

        for item in r_peaks[1:-1]:
            x = r_peaks[counter - 1]
            y = r_peaks[counter + 1]
            diff1 = abs(x - item) // 2
            diff2 = abs(y - item) // 2
            data_from = x + diff1
            data_to = y - diff2
            coordinates.append(data[data_from:data_to])
            indices.append((data_from, data_to))
            counter += 1

        for count, item in enumerate(coordinates):
            fig = plt.figure(figsize=(4, 4))
            plt.plot(item)
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            for spine in plt.gca().spines.values():
                spine.set_visible(False)
            filename = 'image_to_detect/test/images/pict_' + str(count) + '.png'
            fig.savefig(filename)
            plt.close(fig)

            image = cv2.imread(filename)
            edited_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edited_image = imutils.resize(edited_image, width=128)
            cv2.imwrite(filename, edited_image)

        generator = ImageDataGenerator(rescale=1. / 255)
        test_data_path = 'image_to_detect/test/'
        test_generator = generator.flow_from_directory(
            test_data_path,
            target_size=[128, 128],
            shuffle=False,
            color_mode='grayscale',
            batch_size=1,
            class_mode=None)

        test_generator.reset()
        pred = model.predict_generator(test_generator)
        predicted_classes = np.argmax(pred, axis=1)

        for c, pred_class in enumerate(predicted_classes):
            if pred_class == 0:
                APC.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))
            elif pred_class == 1:
                LBB.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))
            elif pred_class == 2:
                continue
            elif pred_class == 3:
                PAB.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))
            elif pred_class == 4:
                PVC.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))
            elif pred_class == 5:
                RBB.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))
            elif pred_class == 6:
                VEB.append(indices[c])
                bad_signal.append(int(r_peaks[c+1]))

        for file in os.listdir('image_to_detect/test/images'):
            filepath = 'image_to_detect/test/images/' + str(file)
            try:
                os.remove(filepath)
            except OSError as e:
                print("Error: %s : %s" % (filepath, e.strerror))

    except Exception as e:
        return False, e, None, None, None

    return True, 'ok', data.tolist(), result, bad_signal
