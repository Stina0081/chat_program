import tkinter as tk
import threading
import socket

def send_message():
    message = input_field.get()

    chat_history.insert(tk.END, "You: " + message + "\n")

    input_field.delete(0, tk.END)

    connection.send(message.encode())

def receive_messages():
    while True:
        try:
            message = connection.recv(1024).decode()
           
            chat_history.insert(tk.END, "Other: " + message + "\n")
        except ConnectionAbortedError:
            break

def establish_connection():
    global connection
    host = host_entry.get()
    port = int(port_entry.get())

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((host, port))

    
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()


window = tk.Tk()
window.title("Chat Program")
window.geometry("400x500")


chat_history = tk.Text(window)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


input_field = tk.Entry(window)
input_field.pack(padx=10, pady=10, fill=tk.X)


send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=10)


host_label = tk.Label(window, text="Host:")
host_label.pack()
host_entry = tk.Entry(window)
host_entry.pack(padx=10, pady=5)

port_label = tk.Label(window, text="Port:")
port_label.pack()
port_entry = tk.Entry(window)
port_entry.pack(padx=10, pady=5)


connect_button = tk.Button(window, text="Connect", command=establish_connection)
connect_button.pack(pady=10)


window.mainloop()
