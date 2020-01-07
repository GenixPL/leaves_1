import cv2

file = open("results_color.txt", "w+")

lowest = 1
amount = 0
sum = 0

for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 10):
            for d in range(0, 6):
                file_name = '0' + str(a) + '_0' + str(b) + '_00' + str(c) + '_0' + str(d)

                my_img = cv2.imread('./colored/rgb_' + file_name + '.png')

                labelled_img = cv2.imread('./labeled_data/label_' + file_name + '.png')

                good_pixels = 0
                for x in range(0, my_img.shape[0]):
                    for y in range(0, my_img.shape[1]):
                        b1, g1, r1 = my_img[x, y]
                        b2, g2, r2 = labelled_img[x, y]

                        if b1 == b2 and g1 == g2 and r1 == r2:
                            good_pixels += 1

                score = float(good_pixels) / float(my_img.shape[0] * my_img.shape[1])

                file.write(file_name + '\tscore: ' + str(score) + '\n')

                sum += score
                amount += 1

                if score < lowest:
                    lowest = score

file.write('LOWEST: ' + str(lowest) + '\n')
file.write('MEAN: ' + str(sum / amount) + '\n')

file.close()