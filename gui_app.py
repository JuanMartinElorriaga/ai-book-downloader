import tkinter as tk
import tkinter.ttk as ttk
import sys
from gui_main import *

def execute_command():
    author = author_entry.get()
    directory_path = path_entry.get()
    # Call your CLI function here with the provided command
    sys.stdout = StdoutRedirector(text_area)

    # Display initial message
    text_area.insert(tk.END, ".........LOADING.........\n")
    text_area.see(tk.END)  # Scroll to the end

    # Run main command
    main(author, directory_path)

    # Display final message
    text_area.insert(tk.END, "\nFINISHED!\n")
    text_area.see(tk.END)  # Scroll to the end


# Initialize GUI
root = tk.Tk()
root.title("Libgen Parser Downloader")

# GUI params
author_label = tk.Label(root, text="Author:")
author_label.pack()

author_entry = tk.Entry(root)
author_entry.pack()

path_label = tk.Label(root, text="Directory Path:")
path_label.pack()

default_path = "./downloads/"  # Your default directory path
path_entry = tk.Entry(root)
path_entry.insert(0, default_path)  # Set the default value
path_entry.pack()

# Button
button = tk.Button(root, text="Execute", command=execute_command)
button.pack()

# Text area
text_area = tk.Text(root)
text_area.pack()

# Run
root.mainloop()
