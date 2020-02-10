import cv2

from utils.plant_camera_setup import PlantCameraSetup

for a in range(0, 3):
    for b in range(0, 5):
        PlantCameraSetup(a, b)


cv2.waitKey(0)
cv2.destroyAllWindows()


