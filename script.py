from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution = (1280, 720))

camera.iso = 100

sleep(3)

camera.shutter_speed = camera.exposure_speed

camera.exposure_mode = 'off'

g = camera.awb_gains

camera.awb_mode = 'off'
camera.awb_gains = g

camera.start_preview()

for fn in camera.capture_continuous('images/img{counter:03d}.jpg'):
    print('Captured %s' % fn)
    # take pic every 2 secs
    sleep(2)
