try:
    import sys
    import shutil
    import os
    import random
    from os import listdir
    from cod.extension import path_to_images, path_to_dataset_from_images
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def choose_random_pict():
    for x in range(12000):
        rnd = random.choice(listdir('../test_train_data/test/NOR'))
        shutil.move('../test_train_data/test/NOR/' + rnd, '../test_train_data/train/NOR')


def create_train_test_dataset():
    existing_folders = ['APC', 'LBB', 'NOR', 'PAB', 'PVC', 'RBB', 'VEB']

    for folder in sorted(listdir(path_to_images)):
        if str(folder) in existing_folders:
            print('Collecting Data From ' + folder)

            number_files = len(listdir(path_to_images + '/' + folder))

            train_size = int(number_files * 0.8)
            test_size = number_files - train_size

            for x in range(train_size):
                rnd = random.choice(listdir(path_to_images + '/' + folder))
                shutil.move(path_to_images + '/' + folder + '/' + rnd, '../test_train_data/train/' + folder)

            for y in range(test_size):
                rnd = random.choice(listdir(path_to_images + '/' + folder))
                shutil.move(path_to_images + '/' + folder + '/' + rnd, '../test_train_data/test/' + folder)
