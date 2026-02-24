import tkinter as tk
from tkinter import scrolledtext
from jarvis_command_center import process_command
from jarvis_base import speak, take_command

def start_listening():
    command = take_command()
    output_text.insert(tk.END, f"You: {command}\n")
    result = process_command(command)
    output_text.insert(tk.END, f"JARVIS: {result}\n")
    speak(result)

def send_command():
    command = input_entry.get()
    output_text.insert(tk.END, f"You: {command}\n")
    result = process_command(command)
    output_text.insert(tk.END, f"JARVIS: {result}\n")
    speak(result)
    input_entry.delete(0, tk.END)

app = tk.Tk()
app.title("JARVIS Assistant")
app.geometry("500x500")

output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD)
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_entry = tk.Entry(app, width=50)
input_entry.pack(padx=10, pady=5)

send_button = tk.Button(app, text="Send", command=send_command)
send_button.pack(pady=5)

listen_button = tk.Button(app, text="Start Listening", command=start_listening)
listen_button.pack(pady=5)

app.mainloop()