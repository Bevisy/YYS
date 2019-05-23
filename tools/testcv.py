import cv2
import aircv as ac
import numpy as np

# img = cv2.imread("images/background.png", 0)
# cv2.imshow('image', img)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('images/backgroundgray.png', img)
#     cv2.destroyAllWindows()


img_src = ac.imread("images/background.png")
img_obj = ac.imread("images/1.png")

pos = ac.find_template(img_src, img_obj)
print(pos)

