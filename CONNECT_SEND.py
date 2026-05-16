import cv2      # image capturing
import tkinter  # ui
import time
import threading# for multi threading
from PIL import Image, ImageTk # for tasks with images
import server_send


import record_frame




frame_counter = 0














#################
#  SERVER FLOW  #
#################
# sender connects to server
def connect_to_server_flow(recorded_image_pointer):

    server_send.main(recorded_image_pointer)









def main():


    ### CAMERA OBJECT ###
    camera = cv2.VideoCapture(0)    # open default webcam (0)
    if not camera.isOpened():       #catch error
        raise Exception("Could not open webcam")
        return
    ##########




    ### STRONING IMAGE/S IN ARRAY ###
    #                          image(np arr)   |connection establsihed
    recorded_image_pointer = [None,             False]
    #array so it is a pointer, and dinamically changes no matter the scope, [0]: main image





    ### THREAD 1 ###
    # run image_recording flow on a seperate thread
    thread1 = threading.Thread(target=record_frame.record_flow, args=(camera, recorded_image_pointer), daemon=True) #daemon true, so if tkinter stops, it immediatly stops this thread
    thread1.start()




    ### THREAD main ###
    # run server flow on main thread
    # passing the pointer to images, so it can access it
    
    connect_to_server_flow(recorded_image_pointer)








if __name__ == "__main__":
    main()