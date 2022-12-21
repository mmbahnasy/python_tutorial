
import socket # import socket lib
PORTNUM = 9001
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Socket (IP, Local)
# sd.connect((socket.gethostname(), PORTNUM)) # If client: Connect to server (Server name / Ip, port number)
# If Server:
sd.bind((socket.gethostname(), PORTNUM))#   Bind (IP, port)
#   Listen for connection
sd.listen()
#   Accept new connection,
while True:
    conn, addr = sd.accept()
    while True:
        # data transfer (send/receive)
        msg = conn.recv(1024)
        print("Recived message:", msg)
        msgToSnd = input(">>")
        conn.send(msgToSnd.encode('utf-8'))
        # close resoures
    conn.close()
sd.close
