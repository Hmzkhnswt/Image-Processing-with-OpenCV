import cv2 as cv
import numpy as np

img_path = "D:\#DATA Science\Image Processing openCV2\Practice\BabarAzam.jpg"
img = cv.imread(img_path)
print(img.shape)

flag = False
x_initial = 0
y_initial = 0

def draw(event, x,y,flags,params):
    global x_initial,y_initial,flag
    if event == 1:          # when we just press the mouse
        flag = True
        x_initial = x
        y_initial = y

    if event == 0:          # when we move or drag the pointer
        if flag == True:
            cv.rectangle(img, pt1=(x_initial,y_initial), pt2=(x,y), color=(255,0,0), thickness=3)

    if event == 4:              # when we relase the mouse button
        flag = False
        cv.rectangle(img, pt1=(x_initial,y_initial), pt2=(x,y), color=(255,0,0), thickness=-1)


cv.namedWindow(winname="showing_image")
cv.setMouseCallback("showing_image", draw)

### Loop
while True:
    cv.imshow("showing_image", img)
    if cv.waitKey(1) & 0xFF == ord('x'):  # by pressing x we will wuit the window
        break

cv.destroyAllWindows()
