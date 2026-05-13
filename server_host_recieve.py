import socket
import os
import struct
import numpy as np
import cv2

def main(recorded_image_pointer):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    os.system("hostname -I") # starting output

    #listen to any incoming connection
    server_socket.bind(('0.0.0.0', 5005)) 
    server_socket.listen(1)

    #start listening
    print(f"IP: {server_socket.getsockname()[0]}")
    print("Server is listening on port 5005...")

    # 4. Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")





    payload_size = struct.calcsize(">L")
    data = b""

    while True:






        # 1. Get the header
        while len(data) < payload_size:
            data += server_socket.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]


        # 2. Get the full image data
        while len(data) < msg_size:
            data += server_socket.recv(4096)



        frame_data = data[:msg_size]
        data = data[msg_size:]


        # 3. Convert back to NumPy array
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


        recorded_image_pointer[0] = frame





    # 6. Close
    conn.close()
    server_socket.close()


if __name__ == "__main__":
    main([])