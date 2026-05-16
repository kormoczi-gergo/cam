import cv2
import threading# for multi threading

import server_host_recieve # script that runs the server , recieves images, 1.arg: imagelise( first elements is changed to recieved image)

import UI_of_reciever








#################
#  SERVER FLOW  #
#################
#reciever hosts the server
def host_server(recieved_image_pointer):
    server_host_recieve.main(recieved_image_pointer)

    

def main():

    ### CAMERA OBJECT ###
    camera = cv2.VideoCapture(0)    # open default webcam (0)
    if not camera.isOpened():       #catch error
        raise Exception("Could not open webcam")
        return
    ##########


    ### STRONING IMAGE/S IN ARRAY ###
    #                          image(np arr)   |frame counter
    recieved_image_pointer = [None,             0]
    #array so it is a pointer, and dinamically changes no matter the scope, [0]: main image


    ### THREAD 1 ###
    # server flow on a seperate thread
    thread1 = threading.Thread(target=host_server, args=(recieved_image_pointer, ), daemon=True) #daemon true, so if tkinter stops, it immediatly stops this thread
    thread1.start()


    ### THREAD main ###
    # run tkinter ui flow on main thread
    # passing the pointer to images, so it can access it
    UI_of_reciever.tkinter_ui_flow(recieved_image_pointer)







if __name__ == "__main__":
    main()