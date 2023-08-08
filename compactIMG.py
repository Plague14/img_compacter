import cv2, numpy as np

file = "671281.jpg"
form = file.split(".")[1]
file = file.split(".")[0]

im = cv2.imread(file+"."+form)
imC = np.array(im)

cFile = file+" [compact]."+form
cv2.imwrite(cFile,imC)
