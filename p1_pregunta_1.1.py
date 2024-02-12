# Tratamiento de Señales Visuales/Tratamiento de Señales Multimedia I @ EPS-UAM
# Practica 1: Fusion de imagenes mediante piramides
# Memoria: codigo de la pregunta XX

# AUTOR1: Fernandez Moreno, Jose Luis
# AUTOR2: Ramasco Gorria, Pedro
# PAREJA/TURNO: Grupo 14

import numpy as np
from matplotlib.pyplot import imread
from p1_tarea4 import run_fusion
from p1_utils import *


def main():

    dir="../practica/img/"
    #imagenes
    apple1=imread(dir+"apple1.jpg")
    apple2=imread(dir+"apple2.jpg")
    orange1=imread(dir+"orange1.jpg")
    orange2=imread(dir+"orange2.jpg")
    orchid=imread(dir+"orchid.jpg")
    violet=imread(dir+"violet.jpg")

    # mascaras
    mask_apple1_orange1=imread(dir+"mask_apple1_orange1.jpg")
    mask_apple2_orange2=imread(dir+"mask_apple2_orange2.jpg")
    orchid_mask=imread(dir+"orchid_mask.jpg")

    niveles=99#tiene que salir en la representacion un nievl mas de lo que le indiquemos ya que son niveles reduce +1 de la imagen original

    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, apple1_orange1_RED)=run_fusion(apple1[:,:,0] , orange1[:,:,0] , mask_apple1_orange1[:,:,0], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,apple1_orange1_GREEN)=run_fusion(apple1[:,:,1] , orange1[:,:,1], mask_apple1_orange1[:,:,1], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,apple1_orange1_BLUE)=run_fusion(apple1[:,:,2], orange1[:,:,2], mask_apple1_orange1[:,:,2], niveles)
    apple1_orange1_fusion=np.stack((apple1_orange1_RED,apple1_orange1_GREEN,apple1_orange1_BLUE),axis=2)
    visualizar_fusion(apple1,orange1,mask_apple1_orange1,Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, apple1_orange1_fusion)

    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,apple2_orange2_RED)=run_fusion(apple2[:,:,0] , orange2[:,:,0] , mask_apple2_orange2[:,:,0], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,apple2_orange2_GREEN)=run_fusion(apple2[:,:,1], orange2[:,:,1], mask_apple2_orange2[:,:,1], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,apple2_orange2_BLUE)=run_fusion(apple2[:,:,2], orange2[:,:,2], mask_apple2_orange2[:,:,2], niveles)
    apple2_orange2_fusion=np.stack((apple2_orange2_RED,apple2_orange2_GREEN,apple2_orange2_BLUE),axis=2)
    visualizar_fusion(apple2,orange2,mask_apple2_orange2,Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, apple2_orange2_fusion)

    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,orchid_violet_RED)=run_fusion(orchid[:,:,0] , violet[:,:,0] , orchid_mask[:,:,0], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,orchid_violet_GREEN)=run_fusion(orchid[:,:,1], violet[:,:,1], orchid_mask[:,:,1], niveles)
    (Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus,orchid_violet_BLUE)=run_fusion(orchid[:,:,2], violet[:,:,2], orchid_mask[:,:,2], niveles)
    orchid_violet_fusion=np.stack((orchid_violet_RED,orchid_violet_GREEN,orchid_violet_BLUE),axis=2)
    visualizar_fusion(orchid,violet,orchid_mask,Gpyr_imgA, Gpyr_imgB, Gpyr_mask, Lpyr_imgA, Lpyr_imgB, Lpyr_fus, orchid_violet_fusion)

    
    

if __name__ == "__main__":
    main()   
    
