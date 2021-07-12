from goprocam import GoProCamera, constants
import time
import datetime
#gpCam = GoProCamera.GoPro("HERO3")

#-----------------------
def subrutina():
    #encender la camara
    #gpCam.power_on()
    gpCam = GoProCamera.GoPro("HERO3")
    #esperar un tiempo
    time.sleep(10)
    #tomar la foto
    try:
        print(gpCam.take_photo(2))
    except:
        pass
    #esperar un tiempo
    time.sleep(10)
    #apagar la camara
    gpCam.power_off()
    return(0)
#-----------------------

#-----------------------
#subir la foto al drive (ver)

#-----------------------

#ejecutar las acciones de arriba cada 1 hora
#print("Camara encendida---se apagara en 10 seg y comenzara rutina ---")
#time.sleep(10)
#gpCam.power_off()
fecha=0
hora=0
aux=0
aux=datetime.datetime.today().time()
print('Comenzado a la hora ' + str(aux))
while('TRUE'):
    tiempo=datetime.datetime.today().date()
    hora=datetime.datetime.today().time()
    if((hora.minute>aux.minute) ):
        subrutina()
        aux=datetime.datetime.today().time()
        print("###  Paso 1 minuto   ###")
    else:
        time.sleep(10)
