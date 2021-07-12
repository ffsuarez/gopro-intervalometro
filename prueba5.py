from goprocam import GoProCamera
from goprocam import constants
## Test 1: Dump all info
gpCam = GoProCamera.GoPro("HERO3")
print(gpCam.getStatus(constants.Status.Status,constants.Status.STATUS.Mode))
