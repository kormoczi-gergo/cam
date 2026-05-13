import socket
import os


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

    while True:
        # 5. Receive data
        data = conn.recv(1024)
        print(f"Received message: {data.decode('utf-8')}")





    # 6. Close
    conn.close()
    server_socket.close()


if __name__ == "__main__":
    main([])