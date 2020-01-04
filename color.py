import cv2

from utils.single_plant import SinglePlant

for i in range(0, 5):
    SinglePlant(i)


cv2.waitKey(0)
cv2.destroyAllWindows()


