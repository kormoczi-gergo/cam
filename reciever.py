import cv2      # image capturing
import tkinter  # ui
import time
import threading# for multi threading
from PIL import Image, ImageTk # for tasks with images
import socket  



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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    server_socket.bind(('0.0.0.0', 5005)) #listen to any incoming connection
    server_socket.listen(1)
    #start listening
    print(f"IP: {server_socket.getsockname()[0]}")
    print("Server is listening on port 5005...")

    # 4. Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # 5. Receive data
    data = conn.recv(1024)
    print(f"Received message: {data.decode('utf-8')}")



    # 6. Close
    conn.close()
    server_socket.close()







    

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