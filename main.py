import cv2

from utils.my_image import MyImage


images = []

# init images
for x in range(0, 6):
    file_name = 'rgb_00_00_000_0' + str(x)
    images.append(MyImage(file_name))

# save images with green mask
for img in images:
    cv2.imwrite('./created/' + img.file_name + '.png', img.get_with_green_mask())


