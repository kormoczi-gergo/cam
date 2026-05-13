import cv2      # image capturing
import tkinter  # ui
import time
import threading# for multi threading
from PIL import Image, ImageTk # for tasks with images
import server_host_recieve # script that runs the server , recieves images, 1.arg: imagelise( first elements is changed to recieved image)


frame_counter = 0



###########################
#     TKINTER UI          #
###########################


### DEFS FOR TKINTER
def update_main_image(image_list, root, canvas):
    global frame_counter

    latest_image = image_list[0]

    if latest_image is not None: # if image1 exists draw it on the canvas
        # 1. Convert BGR to RGB
        rgb_array = cv2.cvtColor(latest_image, cv2.COLOR_BGR2RGB)
        # 2. Convert to PhotoImage
        img = Image.fromarray(rgb_array)
        photo = ImageTk.PhotoImage(image=img)

        # 3. Update the canvas
        canvas.create_image(0, 0, image=photo, anchor="nw")
        canvas.image = photo # Essential reference to prevent garbage collection


        print(frame_counter)
        frame_counter += 1

    if root is not None:    # connect image updating to tkinter loop
        root.after(60, update_main_image, image_list, root, canvas) # 60 = 15fps


##### MAIN TKINTER FLOW #####

def tkinter_ui_flow(image_list):
    ### UI ###
    # 1. Initialize the main window
    root = tkinter.Tk()

    # 2. Set window properties
    root.title("UI")
    root.geometry("800x600")  # Width x Height


    # 3. Add a Canvas (where your NumPy frames will eventually go)
    # This keeps the UI structured for your specific goal
    canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(fill="both", expand=True)


    # 4. The Main Loop
    # This is a blocking call that keeps the window open and responsive
    update_main_image(image_list, root, canvas) # start update loop
    root.mainloop()








#################
#  SERVER FLOW  #
#################
#reciever hosts the server
def host_server(image_list):
    server_host_recieve.main(image_list)





    

def main():

    
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
    # server flow on a seperate thread
    thread1 = threading.Thread(target=host_server, args=(image_list), daemon=True) #daemon true, so if tkinter stops, it immediatly stops this thread
    thread1.start()


    ### THREAD main ###
    # run tkinter ui flow on main thread
    # passing the pointer to images, so it can access it
    tkinter_ui_flow(image_list)









if __name__ == "__main__":
    main()