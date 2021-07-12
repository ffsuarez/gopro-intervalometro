import time
import datetime
fecha=0
hora=0
aux=0
aux=datetime.datetime.today().time()
print('Comenzado a la hora ' + str(aux))
while('TRUE'):
    tiempo=datetime.datetime.today().date()
    hora=datetime.datetime.today().time()
    if((hora.hour>aux.hour) ):
        aux=datetime.datetime.today().time()
        print("###  Paso 1 hora   ###")
    else:
        time.sleep(60*60)