from time import sleep
from cv2 import cv2
from ImageProcessor import ImageProcessor
# from picamera import PiCamera



class Camera:
    # def __init__(self):
        # self.camera = PiCamera()


    # .h264
    # def recordVideoFor(self,seconds,videoPath,display):
    #     camera.start_preview()
    #     camera.start_recording(videoPath)
    #     sleep(seconds)
    #     camera.stop_recording()
    #     camera.stop_preview()
    

    # Args:
    #   String path = "./Video2Images/videoname.avi"
    @staticmethod
    def PCrecord(path):
        cap = cv2.VideoCapture(0)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(path,fourcc, 20.0, (640,480))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                frame= cv2.flip(frame,1)
                out.write(frame)

                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break   

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    