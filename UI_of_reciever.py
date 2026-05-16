import cv2      # image capturing
import tkinter  # ui
from PIL import Image, ImageTk # for tasks with images



###########################
#     TKINTER UI          #
###########################


### DEFS FOR TKINTER
def update_main_image(recieved_image_pointer, root, canvas):
    global frame_counter

    latest_image = recieved_image_pointer[0]
    frame_counter = recieved_image_pointer[1]

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

    if root is not None:    # connect image updating to tkinter loop
        root.after(60, update_main_image, recieved_image_pointer, root, canvas) # 60 = 15fps


##### MAIN TKINTER FLOW #####

def tkinter_ui_flow(recieved_image_pointer):
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
    update_main_image(recieved_image_pointer, root, canvas) # start update loop
    root.mainloop()
