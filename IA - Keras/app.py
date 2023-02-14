import cv2
from os import listdir
import numpy as np
from keras.models import load_model
import tensorflow

#------------------------------------------------------------------------------------
# DEFS
def predict(file):          
        
        imagemVerificar = tensorflow.keras.utils.load_img('analise/'+ file, target_size=(img_x, img_y))
        imagemVerificar = tensorflow.keras.utils.img_to_array(imagemVerificar)
        imagemVerificar = np.expand_dims(imagemVerificar, axis = 0)
        result = classifier.predict(imagemVerificar)
        #print(result)
        maior, class_index = -1, -1
        for x in range(classes):      
            
            if result[0][x] > maior:
                maior = result[0][x]
                class_index = x
        
        return [result, letters[str(class_index)], maior]

#------------------------------------------------------------------------------------
#Variables

img_x, img_y = 32,32
classifier = load_model('models/model_TeP_20230207_1722.h5', compile=False) # MELHOR MODELO
#classifier = load_model('models/model_TeP_20221229_1016.h5', compile=False) #MODELO TESTE

print(classifier)
classes = 3
letters = {'0' : 'antena', '1' : 'bateria', '2' : 'disjuntor'}
total = success = 0
#--------------------------------------------------------------------------------- ---
# Main


for file in listdir('analise'):
    img_text = predict(file)
    result = str(round(float(img_text[2]) * 100, 2))
    #print(file, "Result:", img_text[1], "com", result ,'% de certeza')
    print(f'{file} --> Result: {img_text[1]} with {result}% accuracy')
    if img_text[1] in file:
         success += 1
    total += 1
print(f'success: {success} Total: {total} \nAcurracy {round(float(success/total) *100, 2)}%')


