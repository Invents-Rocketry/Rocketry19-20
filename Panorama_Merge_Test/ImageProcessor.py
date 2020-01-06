from cv2 import cv2
import os
stitcher = cv2.createStitcher()

class ImageProcessor:
    
    # Converting a video to frame images. saving (for example) 1/40 frames
    # Args: 
    #   String videoPath = "./Video2Images/video.avi"
    #   String resultPath = "./Video2Images/"
    # Return: None
    # Result:
    #   frame00000.jpg, frame00040.jpg, etc.
    @staticmethod
    def convertV2I(videoPath,resultPath,frameRate):
        cap= cv2.VideoCapture(videoPath)
        i=0
        if(not os.path.isdir(resultPath)):
            os.mkdir(resultPath)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            if(i%frameRate==0):
                cv2.imwrite(resultPath+'/frame{0:05d}.jpg'.format(i),frame)
            i+=1
        
        cap.release()
        cv2.destroyAllWindows()

    # Take all files with specific type and pano them
    # Args: 
    #   String path = './Video2Images/'
    #   String type = 'jpg'
    # return:
    #   Image panoImg
    @staticmethod
    def panoFolder(path, type):

        vidImagesList = [file for file in os.listdir(path) if file.endswith(type)]
        print(vidImagesList)
        

        # list of images
        vidImages=[]
        for image in vidImagesList:
            # take only specifc type file
            file = path +"/"+ image
            print(file)
            img = cv2.imread(file,cv2.IMREAD_UNCHANGED)
            ratio = 0.7 # percent of original size
            height = int(img.shape[0] * ratio)
            width = int(img.shape[1] * ratio)
            resized = cv2.resize(img,(width,height),interpolation=cv2.INTER_AREA)
            # Panorama.displayPano(resized)
            vidImages.append(resized)


        panoImg = ImageProcessor.panoImageList(vidImages)
        return panoImg

    @staticmethod
    def pano2Images(left, right):
        images=[left,right]
        
        return ImageProcessor.panoImageList(images)

    @staticmethod
    def panoImageList(images):
        ret,pano = stitcher.stitch(images)
        
        if ret == cv2.Stitcher_OK:
            return pano
        print('These images cannot be stitched')
        return None
    
    @staticmethod
    def displayImage(mergedImage):
        if mergedImage is not None:
            cv2.imshow("Panorama", mergedImage)
            cv2.waitKey()