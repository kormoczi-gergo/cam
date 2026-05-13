import cv2      # image capturing
import tkinter  # ui
import time
import threading# for multi threading
from PIL import Image, ImageTk # for tasks with images
import socket
import server_send




frame_counter = 0



###########################
#   IMAGE TAKING          #
###########################

### TAKE IMAGE ###
def take_image(cam):
        # shoot a photo
        # frame is a numpy array of bgr of each pixel
        ret, frame = cam.read()    
        return frame


##### MAIN IMAGE RECORDING FLOW #####
def record_flow(cam, recorded_image_pointer):
        # cam is the object that takes photos
        # image1 is inputted so it can be changed
        while True:
            recorded_image_pointer[0] = take_image(cam)



#################
#  SERVER FLOW  #
#################
# sender connects to server
def connect_to_server_flow():

    server_send.main()




def main():

    server_send.main()


    
    ### CAMERA OBJECT ###
    camera = cv2.VideoCapture(0)    # open default webcam (0)
    if not camera.isOpened():       #catch error
        raise Exception("Could not open webcam")
        return
    ##########

    ### STRONING IMAGE/S IN ARRAY ###
    recorded_image_pointer = [None]
    #array so it is a pointer, and dinamically changes no matter the scope, [0]: main image

    ### THREAD 1 ###
    # run image_recording flow on a seperate thread
    thread1 = threading.Thread(target=record_flow, args=(camera, recorded_image_pointer), daemon=True) #daemon true, so if tkinter stops, it immediatly stops this thread
    thread1.start()

    ### THREAD main ###
    # run image_taker flow on main thread
    # passing the pointer to images, so it can access it
    
    connect_to_server_flow(recorded_image_pointer)








if __name__ == "__main__":
    main()