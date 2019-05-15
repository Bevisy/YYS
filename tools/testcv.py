import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# cv.circle(img, (447, 63), 63, (0, 0, 225), -1)
# cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
cv.imshow("img", img)
cv.waitKey(0)

# img = np.zeros((300, 300, 3), dtype="uint8")
# green = (0, 255, 0)
# cv.line(img, (0, 0), (300, 300), green)
# cv.imshow("img", img)
# cv.waitKey(0)
#
# red = (0, 0, 255)
# cv.line(img, (300, 0), (0, 300), red, 3)
# cv.imshow("img", img)
# cv.waitKey(0)

# for i in range(0, 25):
#     radius = np.random.randint(5, high=200)
#     color = np.random.randint(0, high=256, size=(3,))
#     pt = np.random.randint(0, high=300, size=(2,))
#     cv.circle(img, tuple(pt), radius, color, -1)
#
# cv.imshow("img", img)
# cv.waitKey(0)
