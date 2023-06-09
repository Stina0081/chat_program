import tkinter as tk
import threading

def send_message():
    message = input_field.get()

    chat_history.insert(tk.END, "You: " + message + "\n")

    input_field.delete(0, tk.END)

    print("Message sent:", message)


window = tk.Tk()
window.title("Chat Program")
window.geometry("400x500")


chat_history = tk.Text(window)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


input_field = tk.Entry(window)
input_field.pack(padx=10, pady=10, fill=tk.X)


window.bind("<Return>", lambda event: send_message())


send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=10)


window.mainloop()
