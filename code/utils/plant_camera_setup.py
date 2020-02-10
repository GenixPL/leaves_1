import cv2


class PlantCameraSetup:
    __colors = [
        [255, 0, 0],
        [0, 255, 0],
        [255, 255, 0],
        [0, 0, 255],
        [255, 0, 255],
        [0, 255, 255],
        [128, 128, 128],
        [128, 0, 0],
    ]

    def __init__(self, a, b):
        for c in range(0, 10):
            for d in range(0, 6):
                if c == 0 and d == 0:
                    self.__handle_first_img(a, b, c, d)
                else:
                    self.__handle_other(a, b, c, d)

    def __handle_first_img(self, a, b, c, d):
        file_name = '0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)

        img = cv2.imread('./separated/rgb_' + file_name + '.png')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh, img_black_white = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        # first conts
        conts, hierarchy = cv2.findContours(img_black_white, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # getting center
        M = cv2.moments(conts[0])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        self.center = (cX, cY)

        cv2.circle(img_black_white, self.center, 7, (0, 0, 0), -1)

        # another conts
        conts2, hierarchy = cv2.findContours(img_black_white, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        cv2.circle(img, self.center, 7, self.__colors[0], -1)

        for i in range(0, len(conts2)):
            cv2.drawContours(img, [conts2[i]], -1, self.__colors[i], -1)

        self.previous = img.copy()
        cv2.imwrite('./colored/rgb_' + file_name + '.png', img)

    def __handle_other(self, a, b, c, d):
        file_name = '0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)
        img = cv2.imread('./separated/rgb_' + file_name + '.png')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh, img_black_white = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        cv2.circle(img_black_white, self.center, 7, (0, 0, 0), -1)

        # conts
        conts2, hierarchy = cv2.findContours(img_black_white, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        cv2.circle(img, self.center, 7, self.__colors[0], -1)

        for i in range(0, len(conts2)):
            cv2.drawContours(img, [conts2[i]], -1, self.__colors[i % 8], -1)

        self.previous = img.copy()
        cv2.imwrite('./colored/rgb_' + file_name + '.png', img)
