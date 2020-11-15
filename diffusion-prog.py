import cv2
import numpy as np


def resize_pic(scale_percent):
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


print("Path of the desired picture?:\n")
img_name = input()
print("Txt file name?:\n")
txt_name = input()


# függvény a kattintott koordináták txt fájlba való írásához
def clickpos_txt(name, mouse_position):
	with open(name, "a") as f:
		f.write("\n"+mouse_position)

def resize_pic(img, scale_percent):
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resized

#kattintás koordinátái
def click_pos(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		str_MP = str(x)+'\t'+str(y)
		clickpos_txt(txt_name,str_MP)
		# kék pont rajzolása a kattintás helyére:
		#img = cv2.circle(img, (x,y), radius=0, color=(255, 0, 0), thickness=-1)
		cv2.imshow('image',img)


img = cv2.imread(img_name)
img = resize_pic(img, 60)

#cv2.resizeWindow("image", img.shape[1], img.shape[0])
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
print(img.shape)

cv2.setMouseCallback('image',click_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()
