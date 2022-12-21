
import socket # import socket lib
PORTNUM = 9001
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Socket (IP, Local)
sd.connect((socket.gethostname(), PORTNUM)) # If client: Connect to server (Server name / Ip, port number)
# If Server:
#   Bind (IP, port)
#   Listen for connection
#   Accept new connection,
while True:
    # data transfer (send/receive)
    msgToSnd = input("Chat>>")
    sd.send(msgToSnd.encode('utf-8'))
    msg = sd.recv(1024)
    print("Recived message:", msg)
# close resoures
sd.close
