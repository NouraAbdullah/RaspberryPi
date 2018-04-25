from PIL import Image, ImageStat
import picamera
import requests
import time
import os
from shutil import copyfile
#import cv2
colorFlag=False;
blackFlag=False;
#files = {'image':open('/home/pi/Pic.jpg')}                                
while True :
    while True :    
        with picamera.PiCamera() as camera:
                camera.resolution = (1280,720)
                camera.capture("/home/pi/Pic.jpg")
                print("Picture taken.")
                im = Image.open("/home/pi/Pic.jpg").convert("RGB")
                stat = ImageStat.Stat(im)
                if  sum(stat.sum)/3 != stat.sum[0] :
                    #img=cv2.imread("/home/pi/Pic.jpg",1)
                    #dirname=os.path.dirname(__file__)
                    #g=os.path.join(dirname,'/home/pi/Pic.jpg')
                    copyfile('/home/pi/Pic.jpg', '/home/pi/gg/light.jpg')
                    #cv2.waitkey(0)
                    #files = {'image':open('/home/pi/Pic.jpg')}
                    if colorFlag==False and blackFlag==False :
                        colorFlag=True
                    else:
                        if colorFlag==False and blackFlag==True :
                            colorFlag=True
                            blackFlag=False

                else :
                    if sum(stat.sum)/3 == stat.sum[0] :
                        if colorFlag==False and blackFlag==False:
                            blackFlag=True
                        else:
                             if colorFlag==True and blackFlag==False:
                                 URL = "http://192.168.1.3:5000/"
                                 files = {'image':open('/home/pi/gg/light.jpg')}
                                 r=requests.post(URL, files=files)
                                 print(r.text)
                                 colorFlag=False
                                 

        break                                 
    time.sleep(2)


