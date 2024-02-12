# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 4: fusion de imagenes

# AUTOR1: Fernandez Moreno, Jose Luis
# AUTOR2: Ramasco Gorria, Pedro
# PAREJA/TURNO: Grupo 14

import numpy as np
import matplotlib.pyplot as plt
import math

from p1_tests import test_p1_tarea4
from p1_utils import *
from p1_tarea1 import *
from p1_tarea2 import *
from p1_tarea3 import *

def run_fusion(imgA, imgB, mask, niveles): 
    """ 
    # Esta funcion implementa la fusion de dos imagenes calculando las 
    # pirámides Laplacianas de las imagenes de entrada y la pirámide
    # Gausiana de una mascara.
    #  
    # Argumentos de entrada:
    #   imgA: numpy array de tamaño [imagen_height, imagen_width].
    #   imgB: numpy array de tamaño [imagen_height, imagen_width].
    #   mask: numpy array de tamaño [imagen_height, imagen_width].
    #
    # Devuelve:
    #   Gpyr_imgA: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la imagen A
    #   Gpyr_imgB: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la imagen B
    #   Gpyr_mask: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Gaussiana de la máscara
    #   Lpyr_imgA: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la imagen A
    #   Lpyr_imgB: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la imagen B
    #   Lpyr_fus: lista de numpy arrays con variable tamaño con "niveles+1" elementos 
    #               correspodientes a la piramide Laplaciana de la fusion imagen A & B
    #   Lpyr_fus_rec:  numpy array de tamaño [imagen_height, imagen_width] correspondiente
    #               a la reconstruccion de la pirámide Lpyr_fus
    """ 
    
    # iniciamos las variables de salida    
    Gpyr_imgA = []      # Pirámide Gaussiana imagen A
    Gpyr_imgB = []      # Pirámide Gaussiana imagen B
    Gpyr_mask = []      # Pirámide Gaussiana máscara    
    Lpyr_imgA = []      # Pirámide Laplaciana imagen A
    Lpyr_imgB = []      # Pirámide Laplaciana imagen B
    Lpyr_fus = []       # Pirámide Laplaciana fusionada
    Lpyr_fus_rec = []   # Imagen reconstruida de la pirámide Laplaciana fusionada

    if(len(imgA.shape)>2 or len(imgB.shape)>2):#comprobamos si alguna de las imagenes tiene 3 planos rgb, si lo tiene reportamos error
        raise ValueError("Alguna de las imagenes es RGB y la funcion run_fusion no las soporta.")
    
    #Pasamos las imagenes y mascara a float PREGUNTAR PROFE SI EL CAST ASI ES LEGAL O NO
    imgA=imgA.astype(float)
    imgB=imgB.astype(float)
    mask=mask.astype(float)

    #Normalizamos las imagenes dividiendo por el maximo de cada una
    imgA=imgA/imgA.max()
    imgB=imgB/imgB.max()
    mask=mask/mask.max()

    #Calcular las pirámides Gaussianas de las imágenes calculadas en el apartado anterior utilizando la función "gaus_piramide“
    Gpyr_imgA=gaus_piramide(imgA, niveles)# Pirámide Gaussiana imagen A
    Gpyr_imgB=gaus_piramide(imgB, niveles)# Pirámide Gaussiana imagen B
    Gpyr_mask=gaus_piramide(mask, niveles)# Pirámide Gaussiana máscara 

    #Calcular las pirámides Laplacianas de las imágenes utilizando la función "lapl_piramide“
    Lpyr_imgA=lapl_piramide(Gpyr_imgA)# Pirámide Laplaciana imagen A
    Lpyr_imgB=lapl_piramide(Gpyr_imgB)# Pirámide Laplaciana imagen B

    #Fusionar las pirámides Laplacianas de las imágenes y la Gaussiana de la máscara con la función "fusionar_lapl_pyr
    Lpyr_fus=fusionar_lapl_pyr(Lpyr_imgA, Lpyr_imgB, Gpyr_mask)# Pirámide Laplaciana fusionada

    #Reconstruir la pirámide resultante para obtener una imagen con la función "reconstruir_lapl_pyr“
    Lpyr_fus_rec=reconstruir_lapl_pyr(Lpyr_fus)# Imagen reconstruida de la pirámide Laplaciana fusionada

    #Tras la reconstrucción, algunos valores pueden estar fuera de rango (<0 o >1). En caso positivo, recortar a '0' o '1' según corresponda.

    Lpyr_fus_rec[Lpyr_fus_rec>1] = 1
    Lpyr_fus_rec[Lpyr_fus_rec<0] = 0
    
    return Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec


if __name__ == "__main__":    
    
    path_imagenes = "../practica/img"
    print("Practica 1 - Tarea 4 - Test autoevaluación\n")    
    result,imgAgray,imgBgray,maskgray,\
        Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec \
            = test_p1_tarea4(path_img=path_imagenes,precision=2)
    print("Tests completado = " + str(result)) 

    if result==True:
        #visualizar piramides de la fusion (puede consultar el codigo en el fichero p1_utils.py)
        visualizar_fusion(imgAgray,imgBgray,maskgray,Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, Lpyr_fus_rec)