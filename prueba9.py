from goprocam import GoProCamera, constants
import time
import datetime
gpCam = GoProCamera.GoPro("HERO3")
time.sleep(10)
#gpCam.power_off()
#time.sleep(10)
try:
    print(gpCam.take_photo(2))
except:
    pass

gpCam.downloadLastMedia("HERO3",'http://10.5.5.9:8080/DCIM/100GOPRO/')
#---
#gpCam.power_on()
#gpCam = GoProCamera.GoPro("HERO3")
#---