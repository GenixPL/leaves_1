import cv2
import numpy as np


class MyImage:
    __low_green = np.array([35, 40, 40])
    __high_green = np.array([90, 255, 255])

    def __init__(self, file_name):
        self.file_name = file_name

        path = './data/' + str(file_name) + '.png'

        # import img
        self.img = cv2.imread(path)

        # create hsv
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def get_with_green_mask(self):
        # create green mask
        green_mask = cv2.inRange(self.hsv, self.__low_green, self.__high_green)

        # apply green mask
        green = cv2.bitwise_and(self.img, self.img, mask=green_mask)

        return green

