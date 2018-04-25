from PIL import Image, ImageStat
import picamera
import requests
import time
colorFlag=False;
blackFlag=False;
while True :
    with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/Pic.jpg")
            im = Image.open("Pic.jpg").convert("RGB")
            stat = ImageStat.Stat(im)
            if  sum(stat.sum)/3 != stat.sum[0] :
                if colorFlag==False and blackFlag==False :
                    colorFlag=True
                else:
                    if colorFlag==False and blackFlag==True :
                        colorFlag==True
                        blackFlag==True

            else :
                if sum(stat.sum)/3 == stat.sum[0] :
                    if colorFlag==False and blackFlag==False:
                        blackFlag==True
                    else:
                         if colorFlag==True and blackFlag==False:
                             URL = "http://192.168.1.3:5000/"
                             files = {'image':open('/home/pi/light.jpg')}
                             r=requests.post(URL, files=files)
                             print(r.text)
     time.sleep(2)








