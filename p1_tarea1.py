# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 1: metodos reduce y expand

# AUTOR1: Fernandez Moreno, Jose Luis
# AUTOR2: Ramasco Gorria, Pedro
# PAREJA/TURNO: Grupo 14
import numpy as np
import scipy.signal

from p1_tests import test_p1_tarea1
from p1_utils import generar_kernel_suavizado

def reduce(imagen):
    """  
    # Esta funcion implementa la operacion "reduce" sobre una imagen
    # 
    # Argumentos de entrada:
    #    imagen: numpy array de tamaño [imagen_height, imagen_width].
    # 
    # Devuelve:
    #    output: numpy array de tamaño [imagen_height/2, imagen_width/2] (output).
    #
    # NOTA: si imagen_height/2 o imagen_width/2 no son numeros enteros, 
    #        entonces se redondea al entero mas cercano por arriba 
    #        Por ejemplo, si la imagen es 5x7, la salida sera 3x4  
    """   
    output = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)
    
    kernel=generar_kernel_suavizado(0.4)
    imagen_conv=scipy.signal.convolve2d(imagen,kernel,'same')

    #output=np.zeros((round(np.size(imagen_conv,0)/2),round(np.size(imagen_conv,1)/2)))
    output=imagen_conv[::2,::2]#nos quedamos con las posiciones impares
    
   
    return output  

def expand(imagen):
    """  
    # Esta funcion implementa la operacion "expand" sobre una imagen
    # 
    # Argumentos de entrada:
    #    imagen: numpy array de tamaño [imagen_height, imagen_width].
    #     
    # Devuelve:
    #    output: numpy array de tamaño [imagen_height*2, imagen_width*2].
    """ 
    output = np.empty(shape=[0,0]) # iniciamos la variable de salida (numpy array)

    output=np.zeros((round(np.size(imagen,0)*2),round(np.size(imagen,1)*2)))
    output[::2,::2]=imagen#las posiciones con índices pares (0,0 y 0,1) se han establecido en 255, mientras que las posiciones impares (1,0 y 1,1) permanecen en 0.
    kernel=generar_kernel_suavizado(0.4)
    output=scipy.signal.convolve2d(output,kernel,'same')
    output=4*output#multiplicamos por 4 para mantener el rango de la imagen de salida

    return output

if __name__ == "__main__":    
    print("Practica 1 - Tarea 1 - Test autoevaluación\n")                
    print("Tests completados = " + str(test_p1_tarea1())) 