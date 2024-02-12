# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 3: fusion de piramides y reconstruccion

# AUTOR1: Fernandez Moreno, Jose Luis
# AUTOR2: Ramasco Gorria, Pedro
# PAREJA/TURNO: Grupo 14

import numpy as np
from p1_tests import test_p1_tarea3
from p1_tarea1 import expand

def fusionar_lapl_pyr(lapl_pyr_imgA, lapl_pyr_imgB, gaus_pyr_mask):
    """ 
    # Esta funcion realiza la fusion entre dos piramides laplacianas de distintas imagenes.
    #   La fusion esta determinada por una mascara de la cual se utiliza su correspondiente
    #   piramide Gaussiana para combinar las dos piramides laplacianas.
    #
    # Argumentos de entrada:
    #   lapl_pyr_imgA: lista de numpy arrays obtenida con la funcion 'lapl_piramide' sobre una imagen img2
    #   lapl_pyr_imgB: lista de numpy arrays obtenida con la funcion 'lapl_piramide' sobre otra imagen img1
    #   gaus_pyr_mask: lista de numpy arrays obtenida con la funcion 'gaus_piramide' 
    #                  sobre una mascara para combinar ambas imagenes. 
    #                  Esta mascara y la piramide tiene valores en el rango [0,1]
    #                  Para los pixeles donde gaus_pyr_mask==1, se coge la piramide de img1
    #                  Para los pixeles donde gaus_pyr_mask==0, se coge la piramide de img2
    #    
    # Devuelve:
    #   fusion_pyr: piramide fusionada
    #       lista de numpy arrays con variable tamaño con "niveles+1" elementos.    
    #       fusion_pyr[i] es el nivel i de la piramide que contiene bordes
    #       fusion_pyr[niveles] es una imagen (RGB o escala de grises)
    """ 
    fusion_pyr = [] # iniciamos la variable

    if(len(lapl_pyr_imgA)!=len(lapl_pyr_imgB)):#las piramides han de tener el mismo numero de nivels, error en caso contrario
        raise ValueError("Las dos pirámides no tienen el mismo numero de niveles")
    
    for i in range(len(lapl_pyr_imgA)):
        fusion_pyr.append(lapl_pyr_imgA[i]*gaus_pyr_mask[i]+lapl_pyr_imgB[i]*(1-gaus_pyr_mask[i]))
        
    return fusion_pyr

def reconstruir_lapl_pyr(lapl_pyr):
    """ 
    # Esta funcion reconstruye la imagen dada una piramide laplaciana.
    #
    # Argumentos de entrada:
    #   lapl_pyr: lista de numpy arrays obtenida con la funcion 'lapl_piramide' sobre una imagen img
    #    
    # Devuelve:
    #   output: numpy array con dimensiones iguales al primer nivel de la piramide lapl_pyr[0]
    #
    # NOTA: algunas veces, la operacion 'expand' devuelve una imagen de tamaño mayor 
    # que el esperado. Entonces no coinciden las dimensiones de la imagen expandida 
    #   del nivel k+1 y las dimensiones del nivel k. Verifique si ocurre esta 
    #   situacion y en caso afirmativo, elimine los ultimos elementos de la 
    #   imagen expandida hasta coincidir las dimensiones del nivel k
    #   Por ejemplo, si el nivel tiene tamaño 5x7, tras aplicar 'reduce' y 'expand' 
    #   obtendremos una imagen de tamaño 6x8. En este caso, elimine la 6 fila y 8 
    #   columna para obtener una imagen de tamaño 5x7 donde pueda aplicar la resta
    """ 
    output = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)
    output=expand(lapl_pyr[-1])
    for i in range(len(lapl_pyr)-1,0,-1):#for que empieza en el nivel final y baja hasta en nivel base 0 argumentos de la funcion, donde empiezo, saltos de -1 y acabo en -1 no inclusive, entonces hasta i=0
        if(output.shape[0]!=lapl_pyr[i-1].shape[0]): #si no coincide el nuemero de filas entre el nivel gaussiano expandido y reducido pues elimino esa fila
            output=np.delete(output,output.shape[0]-1,axis=0)
        if(output.shape[1]!=lapl_pyr[i-1].shape[1]): #si no coincide el nuemero de columnas entre el nivel gaussiano expandido y reducido pues elimino esa columna 
            output=np.delete(output,output.shape[1]-1,axis=1)
        if(i>1):
            output=expand(output+lapl_pyr[i-1])#si no es el ultimo nivel expandimos
        else:
            output=(output+lapl_pyr[i-1])#si es el ultimo nivel solo sumamos y no expandimos
   
    return output

if __name__ == "__main__":    
    print("Practica 1 - Tarea 3 - Test autoevaluación\n")                
    print("Tests completados = " + str(test_p1_tarea3(precision=2))) 