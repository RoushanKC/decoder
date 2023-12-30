import os
import socket
import json
import time
import datetime

HOST='192.168.0.52'
PORT=2000
json_data={}
socket.setdefaulttimeout(20)
cl=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
cl.connect((HOST,PORT))
cl.sendall(b"11")
ctr=5
while ctr:
    data=cl.recv(4999)
    bits_stream=[]
    for byte in data:
        for i in range(8):
            bit=(byte>>i) &1
            bits_stream.append(bit)
    now=datetime.datetime.now()
    json_data["timestamp"]=now.strftime("%m-%H:%M:S")
    json_data["data"]=bits_stream
    f=open('config.json' ,"a")
    json.dump(json_data ,f)
    f.write("\n")
    print(len(data))
    ctr-=1
