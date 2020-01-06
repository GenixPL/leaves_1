import cv2

from utils.single_plant import SinglePlantCamera

for a in range(0, 3):
    for b in range(0, 5):
        SinglePlantCamera(a, b)


cv2.waitKey(0)
cv2.destroyAllWindows()


