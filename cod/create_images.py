try:
    import sys
    import cv2
    import imutils
    import numpy as np
    import matplotlib.pyplot as plt
    from cod.extension import path_to_database, dataset, arrhythmia_signals, all_beats, image_size
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def create_images(ant_symbol, ant_sample, rec_signal, person, arrhythmia_signal, numb, pict_order):
    lists = {
        arrhythmia_signal: [],
    }

    print('creating images from person ' + person + ' with arrhythmia_signal: ' + arrhythmia_signal)

    ids = np.in1d(ant_symbol, all_beats[numb])
    imp_beats = ant_sample[ids]
    beats = list(ant_sample)

    for i_b in imp_beats:
        j = beats.index(i_b)
        if j != 0 and j != (len(beats)-1):
            x = beats[j-1]
            y = beats[j+1]
            diff1 = abs(x - beats[j])//2
            diff2 = abs(y - beats[j])//2
            lists[arrhythmia_signals[numb]].append(rec_signal[beats[j] - diff1: beats[j] + diff2])

    for count, item in enumerate(lists[arrhythmia_signals[numb]]):
        fig = plt.figure(figsize=(4, 4))
        plt.plot(item)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        for spine in plt.gca().spines.values():
            spine.set_visible(False)
        filename = '../image_data/' + str(arrhythmia_signals[numb])\
                   + '/' + str(pict_order) + '_' + \
                   arrhythmia_signal + '.png'
        pict_order += 1
        fig.savefig(filename)
        plt.close(fig)

        # for loading image with one channel: image = cv2.imread(filename, 0)
        image = cv2.imread(filename)
        edited_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edited_image = imutils.resize(edited_image, width=128)
        cv2.imwrite(filename, edited_image)

        # cv2.imshow("edited_image", edited_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    return pict_order
