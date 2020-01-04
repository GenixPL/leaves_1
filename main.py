import cv2

from utils.my_image import MyImage


images = []

# init images
for x in range(0, 1):
    file_name = 'rgb_00_00_000_0' + str(x)
    images.append(MyImage(file_name))

# save images with green mask
# for img in images:
#     cv2.imwrite('./created/' + img.file_name + '.png', img.get_with_green_mask())


# display

cv2.imshow('image', images[0].get_final_img())

# cv2.drawContours(images[0].img, [images[0].get_biggest_proper_contour()], -1, (255, 255, 255), -1)
# cv2.imshow('image', images[0].img)

# cv2.imshow('green mask', images[0].get_inverted_green_mask())

# cv2.imshow('contour mask', images[0].get_biggest_contour_mask())


cv2.waitKey(0)
cv2.destroyAllWindows()

