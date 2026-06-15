import socket

# Create and connect the TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))

while True:
    # 1. Send message to the server
    msg = input("Enter your msg:- ")
    s.send(msg.encode("utf-8"))
    if msg.lower() == "exit":
        break
        
    # 2. Wait and receive the reply from the server
    reply = s.recv(1024).decode("utf-8")
    if not reply or reply.lower() == "exit":
        print("Server disconnected")
        break
    print(f"Server says:- {reply}")

s.close()
