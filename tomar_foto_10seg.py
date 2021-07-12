from goprocam import GoProCamera
from goprocam import constants
import time
gpCam = GoProCamera.GoPro("HERO9 Black")

print(gpCam.take_photo(2))