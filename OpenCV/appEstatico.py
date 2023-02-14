import cv2
import numpy as np

def preProcess(img):

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,12)
    kernel = np.ones((3,3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=2)
    return img

img  = cv2.imread("antena.png")
img_process = preProcess(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

contornos, hier = cv2.findContours(img_process, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#img_contorno = cv2.drawContours(img_contorno, contornos, -1 , (0,255,0), 3)

for c in contornos:
    perimeter = cv2.arcLength(c, True)

    if perimeter > 150:
        aprox = cv2.approxPolyDP(c, 0.03 * perimeter, True)
        (x, y, alt, lar) = cv2.boundingRect(c)
        deltax = x - alt
        deltay = lar - y
        print(f'delta x = {deltax}')
        print(f'Delta Y = {deltay}')
        print (f'{y} <- y, {lar} <- lar')
        
        if deltay / deltax > 0:
            recorte = img_process[y:y+lar, x:x+alt]
            white_level = cv2.countNonZero(recorte)
            print(f'nivel de branco {white_level}')
            if white_level < 1500:
                cv2.rectangle(img, (x,y), (x+alt, y+lar), (0,255,0), 2)

        print('---------------------------')

cv2.imshow("original", img)
cv2.imshow("TH", img_process) 
#cv2.imshow("contorno", img_contorno) 

cv2.waitKey(0)

cv2.destroyAllWindows()