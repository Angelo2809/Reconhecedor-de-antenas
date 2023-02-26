import cv2 as cv
import numpy as np

def testeImagens(file, number):
    img = cv.imread(file)
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    _, img_process = cv.threshold(img_gray, 215, 255, cv.THRESH_BINARY)
    kernel = np.ones((3,3), np.uint8)
    img_process = cv.dilate(img_process, kernel, iterations=2)

    contornos, _ = cv.findContours(img_process, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(img, contornos, -1 , (0,255,0), 3)
    for c in contornos:
        perimeter = cv.arcLength(c, True)
        if perimeter > 100:
                (x, y, alt, lar) = cv.boundingRect(c)
                deltax = x - alt
                deltay = lar - y
                print(f'x -> {x}\ny -> {y}\naltura -> {alt}\nlargura -> {lar}')
                print(f'delta x = {deltax}')
                print(f'Delta Y = {deltay}')
                print (f'Deltay / deltaX = {deltay / deltax}')
                print('---------------------------')
                cv.putText(
                    img,
                    text = "Antena",
                    org = (x , y-5),
                    fontFace = cv.FONT_HERSHEY_PLAIN,
                    fontScale = 0.7,
                    color = (255, 0, 0),
                    thickness = 1
                    )
                cv.rectangle(img, (x,y), (x+alt, y+lar), (0,255,0), 2)
                


    cv.imshow("Original", img)
    cv.imshow("process", img_process)
    cv.imwrite(f"../results/antenas-{number}.png", img)
    cv.waitKey(0)

webcam = cv.VideoCapture(0)
def testeVideo():
    while True:
        _, img = webcam.read()
        img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        _, img_process = cv.threshold(img_gray, 215, 255, cv.THRESH_BINARY)
        kernel = np.ones((3,3), np.uint8)
        img_process = cv.dilate(img_process, kernel, iterations=2)

        contornos, hier = cv.findContours(img_process, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #cv.drawContours(img, contornos, -1 , (0,255,0), 3)

        for c in contornos:
            perimeter = cv.arcLength(c, True)
            if perimeter > 100:
                (x, y, alt, lar) = cv.boundingRect(c)
                deltax = x - alt
                deltay = lar - y
                print(f'x -> {x}\ny -> {y}\naltura -> {alt}\nlargura -> {lar}')
                print(f'delta x = {deltax}')
                print(f'Delta Y = {deltay}')
                print('---------------------------')
                cv.putText(
                    img,
                    text = "Antena",
                    org = (x , y-5),
                    fontFace = cv.FONT_HERSHEY_PLAIN,
                    fontScale = 0.7,
                    color = (255, 0, 0),
                    thickness = 1
                    )
                cv.rectangle(img, (x,y), (x+alt, y+lar), (0,255,0), 2)
            

        cv.imshow("Original", img)
        cv.imshow("process", img_process)

        if cv.waitKey(2) == 27:
            break

#testeVideo()
testeImagens("antena.png", 1)    
testeImagens("antena4.png", 2)
cv.destroyAllWindows()