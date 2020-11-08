import cv2
import os
import imutils

personName = 'Sebastian'
dataPath ='C:/Users/OneDrive/Sebastián Hernández/Documentos/Reconocimiento Facial/Data'
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada exitosamente :' ,personPath)
    os.makedirs(personPath)



