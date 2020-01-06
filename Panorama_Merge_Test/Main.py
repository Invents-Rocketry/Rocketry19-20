from ImageProcessor import ImageProcessor
from Camera import Camera
# from picamera import PiCamera
from cv2 import cv2
import os


def getImageListInFolder(path, type):
    # get files name in Video2Images folder
    for d,r,f in os.walk(path):
            vidImagesList=f
    print(vidImagesList)
    
    #list of images
    vidImages=[]
    for image in vidImagesList:
        # take only jpg file
        if(image.endswith(type)):
            file = './Video2Images/'+image
            print(file)

            # Panorama.displayPano(resized)
            vidImages.append(cv2.imread(file,-1))

    return vidImages

def resizeImageList(imageList,ratio):
    # percent of original size
    resizedImageList=[]
    for image in imageList:
        height = int(image.shape[0] * ratio)
        width = int(image.shape[1] * ratio)
        resized = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
        resizedImageList.append(resized)
    return resizedImageList

# camera = PiCamera()
# camera.start_preview()
# camera.start_recording(videoPath)
# while(not peak): # or whatever it needs to be
#     # TODO: need getAltitude()
#     altitude = getAltitude()
#     camera.annotate_text = altitude
# camera.stop_recording()
# camera.stop_preview()


Camera.PCrecord("./Video2Images/test.avi")
# ImageProcessor.convertV2I("./Video2Images/test.avi","./TestImages",10)

# panorama = ImageProcessor.panoFolder("./TestImages",'jpg')
# if(panorama is not None):
#     ImageProcessor.displayImage(panorama)
#     cv2.imwrite("./TestImages/test_resullt.jpg",panorama)
