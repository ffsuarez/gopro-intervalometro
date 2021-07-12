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
url = 'http://10.5.5.9:8080/DCIM/100GOPRO/GOPR0737.JPG'
r = requests.get(url, allow_redirects=True)
open('GOPR0737.JPG', 'wb').write(r.content)