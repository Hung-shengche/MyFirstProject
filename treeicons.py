import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Treeview with Icons")

# Create Treeview
tree = ttk.Treeview(root)
tree.pack()

# Add columns
tree["columns"] = ("名字", "圖標")

# Define column headings
tree.heading("名字", text="名字")
tree.heading("圖標", text="圖標")


img = PhotoImage(file="D:\images.png")
img = img.subsample(4)
tree.insert("","end",text="123",open=True,image=img,values=(1,2))


root.mainloop()
