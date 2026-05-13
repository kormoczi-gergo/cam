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
def record_flow(cam, image_list):
        # cam is the object that takes photos
        # image1 is inputted so it can be changed
        while True:
            image_list[0] = take_image(cam)



#################
#  SERVER FLOW  #
#################
# sender connects to server
def connect_to_server_flow():

    server_send.main()


    # 1. Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect to the Server's IP
    # Replace '192.168.1.XX' with the actual IP of the Host laptop
    client_socket.connect(('192.168.1.XX', 5005))

    # 3. Send data (Must be bytes!)
    message = "Motion Detected!"
    client_socket.send(message.encode('utf-8'))

    # 4. Close
    client_socket.close()


def main():

    server_send.main()


    
    ### CAMERA OBJECT ###
    camera = cv2.VideoCapture(0)    # open default webcam (0)
    if not camera.isOpened():       #catch error
        raise Exception("Could not open webcam")
        return
    ##########

    ### STRONING IMAGE/S IN ARRAY ###
    image_list = [None]
    #array so it is a pointer, and dinamically changes no matter the scope, [0]: main image

    ### THREAD 1 ###
    # run image_recording flow on a seperate thread
    thread1 = threading.Thread(target=connect_to_server_flow, args=(camera, image_list), daemon=True) #daemon true, so if tkinter stops, it immediatly stops this thread
    thread1.start()

    ### THREAD main ###
    # run tkinter ui flow on main thread
    # passing the pointer to images, so it can access it
    








if __name__ == "__main__":
    main()