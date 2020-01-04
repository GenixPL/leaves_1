import cv2
from skimage.measure import compare_ssim

from utils.my_image import MyImage

file = open("results.txt", "w+")

lowest = 1
amount = 0
sum = 0

for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 10):
            for d in range(0, 6):
                file_name = '0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)

                my_img = cv2.imread('./created/rgb_' + file_name + '.png', cv2.COLOR_BGR2GRAY)
                greyscale_my = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
                thresh, black_white_my = cv2.threshold(greyscale_my, 10, 255, cv2.THRESH_BINARY)

                labelled_img = cv2.imread('./labeled_data/label_' + file_name + '.png', cv2.COLOR_BGR2GRAY)
                greyscale_label = cv2.cvtColor(labelled_img, cv2.COLOR_BGR2GRAY)
                thresh, black_white_label = cv2.threshold(greyscale_label, 10, 255, cv2.THRESH_BINARY)

                (score, diff) = compare_ssim(black_white_my, black_white_label, full=True)

                file.write(file_name + '\tscore: ' + str(score) + '\n')

                sum += score
                amount += 1

                if score < lowest:
                    lowest = score

file.write('LOWEST: ' + str(lowest) + '\n')
file.write('MEAN: ' + str(sum / amount) + '\n')

file.close()
