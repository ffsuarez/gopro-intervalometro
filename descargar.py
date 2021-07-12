from goprocam import GoProCamera
from goprocam import constants
import time
import datetime
import requests
gpCam = GoProCamera.GoPro("HERO3+")

tiempo=0
hora=0
tiempo=datetime.datetime.today().date()
hora=datetime.datetime.today().time()

filename='GOPR0736'
num=int(filename[4:8])
num=num+2
filename='GOPR0'+str(num)
url = 'http://10.5.5.9:8080/DCIM/100GOPRO/'+filename+'.JPG'
r = requests.get(url, allow_redirects=True)
open(filename +'.JPG', 'wb').write(r.content)