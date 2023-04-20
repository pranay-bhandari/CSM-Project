import tkinter as tk
import os

def run_file1():
    os.system("python main.py")

def run_file2():
    os.system("python msg.py")

root = tk.Tk()
root.title("Lets Encrypt and Decrypt CSM")

description_label = tk.Label(root, text="This app allows you to encrypt and decrypt messages and any file that you desire.")
description_label.pack()


button1 = tk.Button(root, text="Encrypt/Decrypt File", command=run_file1)
button2 = tk.Button(root, text="Encrypt/Decrypt Message", command=run_file2)


button1.pack()
button2.pack()

root.mainloop()