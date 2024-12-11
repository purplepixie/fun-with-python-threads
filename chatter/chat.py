# python chat.py [local port] [remote IP] [remote port]

import socket
import sys
import threading


localIP     = "0.0.0.0"
localPort   = int(sys.argv[1])
remoteIP    = sys.argv[2]
remotePort  = int(sys.argv[3])

def ServerThread(IP, Port):
    bufferSize = 1024
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((IP, Port))
    print("UDP server up and listening on port "+str(Port))
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Received: "+message.decode('utf-8')
        print(clientMsg)

quit = False

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

rxThread = threading.Thread(target=ServerThread, args=(localIP,localPort,), daemon=True)
rxThread.start()

print("Welcome to CHAT - type /quit to exit")

while not quit:
    text = input("Message: ")
    if text == "/quit":
        quit = True
    else:
        bytesToSend = str.encode(text)
        UDPClientSocket.sendto(bytesToSend, (remoteIP, remotePort))
        print("Message Sent")