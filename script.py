import os
import socket
import json
import datetime
import msvcrt

HOST = '192.168.0.52'
PORT = 2000
#isActivated=False

socket.setdefaulttimeout(5)

cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect((HOST, PORT))
cl.sendall(b"11")


data = b""  # Initialize empty byte string to accumulate data
while True:
    try:
        chunk = cl.recv(1000)  # Receive data in 1000-byte chunks
        data += chunk  # Append to accumulated data
        print(len(data))
        if len(data) >= 5740:  # Process when 5740 bytes are reached
            bits_stream = []
            for byte in data:
                for i in range(8):
                    bit = (byte >> i) & 1
                    bits_stream.append(bit)
             
            now = datetime.datetime.now()
            json_data = {"timestamp": now.strftime("%m-%H:%M:S"), "data": bits_stream}
            with open('config.json', "a") as f:
                json.dump(json_data, f)
                f.write("\n")

            data = b""  # Reset data buffer
            '''
            if(isActivated==False):
               toSend=bytearray(600)
               toSend[0]|=0b11000000
               cl.sendall(toSend)
               isActivated=True
            else:
            '''
            isAlive=int(bits_stream[0])&1
            print(isAlive)
            toSend=bytearray(600)
            toSend[0]=int(toSend[0])^isAlive
            toSend[0]|=0b01000000
            toSend[30]&=0b11000000
            cl.sendall(toSend)
            #isActivated=False
            print("DATA SEND")

        if msvcrt.kbhit():  # Check for keyboard input
            key = msvcrt.getch()
            break  # Break the loop on key press

    except socket.timeout:
        print("Timeout occurred")
        break

cl.close()  # Close the socket
     