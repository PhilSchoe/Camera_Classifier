from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL

# Rewrite with CNN


class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters, image_size):
        image_list = np.arrry([])
        class_list = np.array([])

        for i in range(1, counters[0]):
            image = cv.imread(f'1/frame{i}.jpg')[:, :, 0]
            image = image.reshape(image_size)
            image_list = np.append(image_list, [image])
            class_list = np.append(class_list, 1)

        for i in range(1, counters[1]):
            image = cv.imread(f'2/frame{i}.jpg')[:, :, 0]
            image = image.reshape(image_size)
            image_list = np.append(image_list, [image])
            class_list = np.append(class_list, 2)

        image_list = image_list.reshape(counters[0] - 1 + counters[1] - 1, image_size)
        self.model.fit(image_list, class_list)

        print("Model successfully trained!")