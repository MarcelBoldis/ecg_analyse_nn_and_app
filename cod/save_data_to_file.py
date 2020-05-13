try:
    import cv2
    import sys
    import numpy as np
    from os import listdir
    from random import shuffle
    from cod.extension import path_to_images, path_to_dataset_from_images
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def save_data_to_file():
    existing_folders = ['APC', 'LBB', 'NOR', 'PAB', 'PVC', 'RBB', 'VEB']
    counter = 0
    for folder in sorted(listdir(path_to_images)):
        training_dataset = []
        if str(folder) in existing_folders:
            label = np.zeros(7)
            label[counter] = 1
            counter += 1
            print('Creating Data From ' + folder)
            for item in listdir(path_to_images + '/' + folder):
                if item is not None:
                    image = cv2.imread(path_to_images + '/' + folder + '/' + item, 0)
                    if image is not None:
                        image = cv2.resize(image, (128, 128))
                        training_dataset.append([np.array(image), label])
                    else:
                        print('Image Not Found!')
                else:
                    print('Folder Is Empty!')
            shuffle(training_dataset)
            np.save(path_to_dataset_from_images + '/' + folder + '.npy', training_dataset)
            print('Data From ' + folder + ' Are Ready!')


def create_dataset_from_files():
    dataset = []
    for image_file in sorted(listdir(path_to_dataset_from_images)):
        print('Collecting Data From ' + image_file)
        data = np.load(path_to_dataset_from_images + '/' + image_file, allow_pickle=True)
        for item in data:
            dataset.append(item)

    np.random.shuffle(dataset)
    np.save('../dataset_128.npy', dataset)

    print('Dataset Created!')

