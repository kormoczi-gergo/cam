









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
            recorded_image_pointer[1] += 1 #inc frame counter with every shot