import cv2
import numpy as np

# fájlnevek lekérdezése
print("Path of the desired picture?:")
img_name = input()
print("Txt file name?:")
txt_name = input()

# függvény a kattintott koordináták txt fájlba való írásához
def clickpos_txt(name, mouse_position):
	with open(name, "a") as f:
		f.write(mouse_position+"\n")

# kép méretarányos átméretezése
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
		cv2.imshow('image',img)

img = cv2.imread(img_name)    # kép beolvasása
img = resize_pic(img, 60)     # kép átméretezése (személy szerint túl nagy volt 
                              #a képernyőmön, lehet, ez csak egyéni probléma)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()