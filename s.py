import socket

# Create and bind the TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen()

client, add = s.accept()
print("Connected with client", add)

while True:
    # 1. Receive message from the client
    msg = client.recv(1024).decode("utf-8")
    if not msg or msg.lower() == "exit":
        print("Client disconnected")
        break
    print(f"Client says:- {msg}")
    
    # 2. Reply back to the client
    server_msg = input("Enter reply to client:- ")
    client.send(server_msg.encode("utf-8"))
    if server_msg.lower() == "exit":
        print("Closing server...")
        break
client.close()
s.close()
