import cv2 as cv
import numpy as np

img_path = "D:\#DATA Science\Image Processing openCV2\Practice\BabarAzam.jpg"
img = cv.imread(img_path)
print(img.shape)

def draw(event, x,y,flags,params):
    if event == 1:    ################## when event ==1 then on mouse click if event == 0 then moving mouse if event == 4 then mouse reales
        cv.circle(img,center=(x,y), radius=30, color=(0,255,0), thickness=5) 

cv.namedWindow(winname="showing_image")
cv.setMouseCallback("showing_image", draw)

### Loop
while True:
    cv.imshow("showing_image", img)
    if cv.waitKey(1) & 0xFF == ord('x'):  # by pressing x we will wuit the window
        break

cv.destroyAllWindows()
