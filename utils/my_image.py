import cv2
import numpy as np


class MyImage:
    __low_green = np.array([32, 40, 35])
    __high_green = np.array([90, 255, 255])

    def __init__(self, file_name):
        self.file_name = file_name

        path = './raw_data/' + str(file_name) + '.png'

        # import img
        try:
            self.img = cv2.imread(path)
            self.img_w = self.img.shape[0]
            self.img_h = self.img.shape[1]
        except:
            print path

        # create hsv
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def get_final_img(self):
        # apply contour mask
        final = cv2.bitwise_and(self.img, self.img, mask=self.get_biggest_contour_mask())

        return final

    def get_img_with_green_mask(self):
        # apply green mask
        green = cv2.bitwise_and(self.img, self.img, mask=self.get_green_mask())

        return green

    # GREEN

    def get_green_mask(self):
        # create green mask
        green_mask = cv2.inRange(self.hsv, self.__low_green, self.__high_green)

        return green_mask

    def get_inverted_green_mask(self):
        # create green mask
        green_mask = cv2.inRange(self.hsv, self.__low_green, self.__high_green)

        return 255 - green_mask

    # CONTOURS

    def get_contours(self):
        conts, hierarchy = cv2.findContours(self.get_green_mask(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        return conts

    def get_proper_contours(self):
        proper_conts = []

        for cont in self.get_contours():
            x, y, w, h = cv2.boundingRect(cont)

            if x < 5 or (x + w) > self.img_w:
                continue

            if y < 5 or (y + h) > self.img_h:
                continue

            proper_conts.append(cont)

        return proper_conts

    def get_biggest_proper_contour(self):
        proper_conts = self.get_proper_contours()
        biggest_area = 0
        biggest_contour = proper_conts[0]

        for cont in self.get_contours():
            x, y, w, h = cv2.boundingRect(cont)
            area = w * h

            if area > biggest_area:
                biggest_area = area
                biggest_contour = cont

        return biggest_contour

    def get_biggest_contour_mask(self):
        mask = np.zeros(self.img.shape[:2], np.uint8)

        cv2.drawContours(mask, [self.get_biggest_proper_contour()], -1, (255, 255, 255), -1)

        return mask
