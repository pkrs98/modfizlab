import cv2
import numpy as np
debug = False

sharp_kernel = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]])
a = "oldat"
aa = []
lista = []

#függvény a képek világosítására
def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# lista a módosítandó képek neveivel
for i in range(1,4):
    aa = np.append(aa, a+str(i))
for j in range(len(aa)):
    for i in range(1,8):
        lista = np.append(lista, aa[j]+'-'+str(i))

if debug:
    print(lista)

# képmanipulációk a lista elemeire:
for i in lista:
    gauss = cv2.imread("diffuzio-fenykepek/"+i+".jpg")
    hsv = change_brightness(gauss, 10)
	# forgatás balra 90 fokot
    rot = cv2.rotate(hsv, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
	# ROI kivágása
    crop = rot[1000:2352, 600:3136]
	# élesítés (már amennyire lehet)
    sharp = cv2.filter2D(crop, -1, sharp_kernel)
	# képek mentése új néven
    cv2.imwrite("szerk/"+i+"_RC.jpg", sharp)
    if debug:
        print("kész lett: ", i)
