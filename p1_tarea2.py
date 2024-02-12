# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Tarea 2: piramide Gaussiana y piramide laplaciana

# AUTOR1: Fernandez Moreno, Jose Luis
# AUTOR2: Ramasco Gorria, Pedro
# PAREJA/TURNO: Grupo 14
import numpy as np
from p1_tests import test_p1_tarea2
from p1_tarea1 import reduce, expand

def gaus_piramide(imagen, niveles):
    """ 
    # Esta funcion crea una piramide Gaussiana a partir de una imagen
    #
    # Argumentos de entrada:
    #   imagen: numpy array de tamaño [imagen_height, imagen_width].
    #   niveles: entero positivo que especifica el numero de veces que se aplica la operacion 'reduce'.
    #           Si niveles=0 entonces se debe devolver una lista con la imagen de entrada
    #           Si niveles=1 entonces se debe realizar una operacion de reduccion               
    #
    # Devuelve:
    #   gauss_pyr: lista de numpy arrays con variable tamaño con "niveles+1" elementos.
    #       output[0] es la imagen de entrada
    #       output[i] es el nivel i de la piramide
    #  
    """ 
    gaus_pyr = []  # iniciamos la variable de salida (lista)

    gaus_pyr.append(imagen)#metemos en la lista el primer nivel que es la imagen original

    aux=imagen
    #en este for vamos a aplicar la funcion reduce que hemos implementado antes para crear la piramide
    for i in range(niveles):
        imagen=reduce(imagen)
        gaus_pyr.append(imagen)


    return gaus_pyr

def lapl_piramide(gaus_pyr):
    """ 
    # Esta funcion crea una piramide Laplaciana a partir de una piramide Gaussiana    
    #  
    # Argumentos de entrada:
    #   gauss_pyr: lista de numpy arrays creada con la funcion 'gauss_piramide'.               
    #
    # Devuelve:
    #   lapla_pyr: lista de numpy arrays con variable tamaño con "niveles+1" elementos.    
    #       lapla_pyr[0] es el primera nivel de la piramide que contiene bordes
    #       lapla_pyr[i] es el nivel i de la piramide que contiene bordes
    #       lapla_pyr[niveles-1] es una imagen (escala de grises)    
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
    lapl_pyr = [] # iniciamos la variable de salida (lista) 

    for i in range(len(gaus_pyr)):
        if(i!=(len(gaus_pyr)-1)):#si no estamos en el ultimo nivel de la gaussiana calculamos laplaciana
            G=expand(reduce(gaus_pyr[i]))#hago operacion reduce y expand y la guardo en una variable G
            if(G.shape[0]!=gaus_pyr[i].shape[0]): #si no coincide el nuemero de filas entre el nivel gaussiano expandido y reducido pues elimino esa fila
                G=np.delete(G,G.shape[0]-1,axis=0)
            if(G.shape[1]!=gaus_pyr[i].shape[1]): #si no coincide el nuemero de columnas entre el nivel gaussiano expandido y reducido pues elimino esa columna 
                G=np.delete(G,G.shape[1]-1,axis=1)
            L=gaus_pyr[i]-G           
            lapl_pyr.append(L)
        else:#ojo el ultimo nivel de la laplaciana es el de la gausiana sin restar
            lapl_pyr.append(gaus_pyr[i])


    return lapl_pyr
   
if __name__ == "__main__":    
    print("Practica 1 - Tarea 2 - Test autoevaluación\n")                
    print("Tests completados = " + str(test_p1_tarea2())) 