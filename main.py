import tkinter as tk
from tkinter.filedialog import asksaveasfile, askopenfile

FILE_NAME = tk.NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete("1.0", tk.END)

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name

    data = inp.read()
    text.delete("1.0", tk.END)
    text.insert("1.0", data)

def save_file():
    data = text.get("1.0", tk.END)
    out = asksaveasfile(mode="w")
    out.write(data)
    out.close()

root = tk.Tk()
root.title("text_editor_DZ v0.1")
root.minsize(width=500, height=600)
root.maxsize(width=500, height=600)

text = tk.Text(root, width=500, height=600)
text.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()