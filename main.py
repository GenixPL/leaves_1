import cv2
import numpy as np

for x in range(0, 5):
    # import img
    img = cv2.imread('./data/rgb_00_00_000_0' + str(x) + '.png')

    # convert it to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # use green mask
    low_green = np.array([35, 40, 40])
    high_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(hsv, low_green, high_green)
    green = cv2.bitwise_and(img, img, mask=green_mask)

    # save img
    cv2.imwrite('./created/rgb_00_00_000_0' + str(x) + '.png', green)

# # display
# cv2.imshow('image', green)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
