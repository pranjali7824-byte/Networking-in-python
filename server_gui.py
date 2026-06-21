import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = "localhost"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client = None

def receive_messages():
    global client

    client, addr = server.accept()
    chat_box.insert(tk.END, f"Connected: {addr}\n")

    while True:
        try:
            msg = client.recv(1024).decode("utf-8")

            if not msg:
                break

            chat_box.insert(tk.END, f"Client: {msg}\n")
            chat_box.see(tk.END)

        except:
            break

def send_message():
    global client

    msg = message_entry.get()

    if client and msg:
        client.send(msg.encode("utf-8"))
        chat_box.insert(tk.END, f"You: {msg}\n")
        chat_box.see(tk.END)

    message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Server Chat")
root.geometry("500x500")

chat_box = scrolledtext.ScrolledText(root)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

message_entry = tk.Entry(root)
message_entry.pack(fill=tk.X, padx=10, pady=5)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()

server.close()