try:
    import cv2
    import sys
    import imutils
    from os import listdir
    from cod.extension import arrhythmia_signals, path_to_images
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def data_augmentation():
    for file in listdir(path_to_images):
        if str(file) in arrhythmia_signals and file != 'NOR':
            print('Creating Data From ' + file)
            for item in listdir(path_to_images + '/' + file):
                image_path = path_to_images + '/' + file + '/' + item
                image_path_save = path_to_images + '/' + file + '_aug' + '/' + item
                image = cv2.imread(image_path)

                cropped_image = image[:100, :100]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_lefttop' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[:100, 14:114]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_centertop' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[:100, 28:]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_righttop' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[16:112:, :96]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_leftcenter' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[16:112, 16:112]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_centercenter' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[16:112, 32:]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_centerright' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[32:, :96]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_leftbottom' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[32:, 16:112]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_centerbottom' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cropped_image = image[32:, 32:]
                cropped_image = imutils.resize(cropped_image, width=128)
                cv2.imwrite(str(image_path_save[:-4]) + '_rightbottom' + '.png', cropped_image)
                # cv2.imshow("edited_image", cropped_image)
                # cv2.waitKey(0)

                cv2.destroyAllWindows()
