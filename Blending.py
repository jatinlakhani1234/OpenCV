import cv2
import numpy as np
import matplotlib.pyplot as plt

imgL = cv2.imread('Dual_Left.jpg')
imgR = cv2.imread('Dual_Right.jpg')
print(imgL.shape)
imgL = cv2.resize(imgL, (2048, 1024))
imgR = cv2.resize(imgR, (2048, 1024))

# Left
layer_L = imgL.copy()
gp_L = [layer_L]
lp_L = []
for i in range(5):
    down = cv2.pyrDown(layer_L)
    up = cv2.pyrUp(down)
    lap_lyr = cv2.subtract(layer_L, up)
    lp_L.append(lap_lyr)
    layer_L = down
    gp_L.append(layer_L)

# Right
layer_R = imgR.copy()
gp_R = [layer_R]
lp_R = []
for i in range(5):
    down = cv2.pyrDown(layer_R)
    up = cv2.pyrUp(down)
    lap_lyr = cv2.subtract(layer_R, up)
    lp_R.append(lap_lyr)
    layer_R = down
    gp_R.append(layer_R)

# Merge and add
lp_L.reverse()
lp_R.reverse()
blend = np.hstack((gp_L[-1], gp_R[-1]))
i=0
for l, r in zip(lp_L, lp_R):
    # row, col, _ = l.shape
    merge = np.hstack((l, r))
    cv2.imshow(str(i+1), blend)
    blend = cv2.add(merge, cv2.pyrUp(blend))
    print(merge.shape, "   ", blend.shape)
    i += 1

plt.imshow(cv2.cvtColor(blend, cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()