import cv2

from utils.my_image import MyImage


# ALL

for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 10):
            for d in range(0, 6):
                file_name = 'rgb_0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)
                img = MyImage(file_name)
                cv2.imwrite('./created/' + img.file_name + '.png', img.get_final_img())

# ALL END


# TESTING
# images = []
#
# # init images
# for x in range(0, 6):
#     file_name = 'rgb_00_00_000_0' + str(x)
#     images.append(MyImage(file_name))
#
# # save images with green mask
# for img in images:
#     cv2.imwrite('./created/' + img.file_name + '.png', img.get_final_img())

# display

# cv2.imshow('image', images[0].get_final_img())

# cv2.drawContours(images[0].img, [images[0].get_biggest_proper_contour()], -1, (255, 255, 255), -1)
# cv2.imshow('image', images[0].img)

# cv2.imshow('green mask', images[0].get_inverted_green_mask())

# cv2.imshow('contour mask', images[0].get_biggest_contour_mask())


cv2.waitKey(0)
cv2.destroyAllWindows()
