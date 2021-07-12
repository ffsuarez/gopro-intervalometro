from goprocam import GoProCamera, constants

goproCamera = GoProCamera.GoPro("HERO3")

goproCamera.shoot_video(10)