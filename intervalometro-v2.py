from goprocam import GoProCamera, constants
import time
import datetime
import sys
import requests
#import pdb
#gpCam = GoProCamera.GoPro("HERO3")

#-----------------------
def subrutina(NUM):
    #encender la camara
    #gpCam.power_on()
    gpCam = GoProCamera.GoPro("HERO3+")
    #esperar un tiempo
    time.sleep(10)
    #tomar la foto
    try:
        print(gpCam.take_photo(2))
    except:
        pass
    #esperar un tiempo
    time.sleep(10)
    #gpCam.downloadLastRawPhoto(new_filename)
    if (num<999):
        filename='GOPR0'+str(num)
    else:
        filename='GOPRO'+str(num)
    download_picture(filename)
    time.sleep(10)
    #apagar la camara
    gpCam.power_off()
    return(0)
#-----------------------

#-----------------------
#descargar foto
def download_picture(filename):
    url = 'http://10.5.5.9:8080/DCIM/100GOPRO/'+filename+'.JPG'
    r = requests.get(url, allow_redirects=True)
    archivo=filename+'.JPG'
    #pdb.set_trace()
    open(archivo, 'wb').write(r.content)

#-----------------------

#ejecutar las acciones de arriba cada 1 hora

fecha=0
momento_0=0
presente=0
momento_0=datetime.datetime.today().time()
marcador=datetime.datetime.today().time()
filename='GOPR0757'
num=int(filename[4:8])
print('Comenzado a la hora ' + str(marcador))
f=open('Informacion.txt','w')
while('TRUE'):
    presente=datetime.datetime.today().time()  #toma la hora
    if((presente.minute>marcador.minute) ):   #si quisiera esperar mas tiempo seria (marcador + x)
        subrutina(num)    #saca foto y la descarga al directorio donde se ejecuta el script
        num=num+1       #contador para poner el nombre de la foto
        #download_picture(filename)
        marcador=datetime.datetime.today().time()
        string=['La foto '+ filename , 'fue tomada el ' + str(marcador)]
        f.write(string[0])
        f.write(string[1])
        f.write('\n')
        if(num==(7*86400)):
            f.close()
            sys.exit("7 dias seguidos")
        print("###  Saco una foto   ###")
    else:
        time.sleep(5)
    if(num==86400):
        #f.close()
        print("Se tomaron 86400 fotos, son aproximadamente 1 dia")
        