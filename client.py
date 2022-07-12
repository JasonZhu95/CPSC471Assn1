from socket import *
import sys

if len(sys.argv) < 4:
    print("Invalid Parameters: client.py server_host server_port filename")
    sys.exit(-1)
    
# Command Line Parameters
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

#TCP client
serverSocket = socket(AF_INET, SOCK_STREAM)

#Connect client socket to target
serverSocket.connect((server_host, server_port))

#HTTP GET
serverSocket.sendall(('GET /' + filename + ' HTTP/1.1 ').encode())

#Print server response
message = serverSocket.recv(1024)
print('Server Response: ', message)

sys.exit()