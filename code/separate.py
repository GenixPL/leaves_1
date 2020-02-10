import cv2

from utils.my_image import MyImage


for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 10):
            for d in range(0, 6):
                file_name = 'rgb_0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)
                img = MyImage(file_name)
                cv2.imwrite('./separated/' + img.file_name + '.png', img.get_final_img())
                cv2.imwrite('./masks/' + img.file_name + '.png', img.get_biggest_contour_mask())
                cv2.imwrite('./boundaries/' + img.file_name + '.png', img.get_img_with_boundary())

