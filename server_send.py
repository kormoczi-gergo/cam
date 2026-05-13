import socket
import struct
import cv2


def main(recieved_image_pointer):
    # 1. Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect to the Server's IP
    # Replace '192.168.1.XX' with the actual IP of the Host laptop
    ip_address = input("address of computer:")
    client_socket.connect((ip_address, 5005))

    # 3. Send data 
    while True:
        frame = recieved_image_pointer[0] #get most recent photo done by camera

        if frame is not None:



            # 1. Encode the frame
            # '.jpg' is the format, 90 is the quality (1-100)
            result, encoded_img = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            data = encoded_img.tobytes()

            # 2. Pack the length of data into 4 bytes (L = unsigned long)
            size_header = struct.pack(">L", len(data))


            # 3. Send everything
            client_socket.sendall(size_header + data)





    # 4. Close
    client_socket.close()





    

if __name__ == "__main__":
    main()