from goprocam import GoProCamera, constants
import time
import datetime
gpCam = GoProCamera.GoPro("HERO3+")
gpCam.downloadLastMedia("HERO3+",'http://10.5.5.9:8080/DCIM/100GOPRO/')
#gpCam.downloadLastMedia(gpCam.take_photo(2))

#downloadLastMedia(self, path='', custom_filename='')