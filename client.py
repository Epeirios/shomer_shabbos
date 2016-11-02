import socket

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
videofile = "lebowski.mp4"

bytes = open(videofile).read()

print (len(bytes))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(bytes)

client.close()
